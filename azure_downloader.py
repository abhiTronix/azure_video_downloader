"""
    azure_video_downloader - Downloads videos from Azure Media Services.
    Copyright (C) 2020  Abhishek Thakur @abhiTronix <abhi.una12@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""


# import libs
import os, re
import platform
import argparse

try:
    # import Youtube-DL Binaries
    import youtube_dl
except ImportError:
    raise ImportError(
        "Failed to detect correct youtube_dl executables, install it with `python -m pip install -U youtube_dl` command."
    )


def return_ffmpeg_foldername():
    """
    returns system specific FFmpeg foldername
    """
    if platform.system() == "Windows":
        return "win64" if platform.machine().endswith("64") else "win32"
    elif platform.system() == "Darwin":
        return "macos64"
    else:
        return "amd64" if "64" in platform.machine() else "i686"


def split(string, maxsplit=0):
    delimiters = ",", "+"
    regexPattern = "|".join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)


def clean_extracted(extracted):
    if not extracted:
        return []
    cleaned = []
    for ext in extracted:
        if ext.strip().endswith(".ism"):
            cleaned.append(ext.strip())
        elif ".ism" in ext.strip():
            splitted = ext.strip().split(".ism")
            if len(splitted) != 2:
                print("Invalid value skipped: " + ext)
                continue
            cleaned.append(splitted[0] + ".ism")
        else:
            print("Invalid Value: " + ext)
    return cleaned


def parse_options(string, clean=True):
    splitted = split(string)
    return clean_extracted(splitted) if clean else splitted


def parse_options_file(path, clean=True):
    contents = []
    with open(path) as f:
        contents = f.read().splitlines()
    contents = [x for x in contents if x.strip()]
    return clean_extracted(contents) if clean else contents


def parse_output(out_path, inp_path):
    output = ""
    abs_path = os.path.abspath(out_path)
    if (os_windows or os.access in os.supports_effective_ids) and os.access(
        os.path.dirname(abs_path), os.W_OK
    ):
        if os.path.isdir(abs_path):
            extracted = (
                os.path.basename(inp_path).replace("%20", "_").replace(".ism", "")
            )
            output += os.path.join(abs_path, extracted)
        else:
            f_name = os.path.basename(abs_path).replace(".", "_")
            output += os.path.join(os.path.dirname(abs_path), f_name)
    return output


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Azure Media Services Video-Downloader.")
    ap.add_argument(
        "-i",
        "--input",
        required=True,
        type=str,
        help="URL(s) of valid ISM stream(s) or File containing multiple ISM URLs.",
    )
    ap.add_argument(
        "-o",
        "--output",
        type=str,
        default="output",
        help="Output Video filename (with/without path).",
    )
    ap.add_argument(
        "-f",
        "--ffmpeg",
        type=str,
        default="ffmpeg",
        help="Location of FFmpeg static binary (Required to merge Audio/Video Streams).",
    )
    ap.add_argument(
        "-q",
        "--quality",
        type=str,
        default="medium",
        choices=["low", "medium", "high"],
        help="Select Video-Stream Quality.",
    )
    args = vars(ap.parse_args())

    inputs = args["input"]
    Inputisfile = False
    if set(",+").intersection(inputs):
        inputs = parse_options(inputs)
        assert inputs, "Invalid Input `-i/--input` URL provided!"
    elif os.path.isfile(inputs):
        inputs = parse_options_file(inputs)
        assert inputs, "Invalid Input `-i/--input` URL provided!"
        Inputisfile = True
    else:
        assert str(inputs).endswith(".ism"), "Invalid Input `-i/--input` URL provided!"

    output = [] if isinstance(inputs, list) else ""
    os_windows = True if os.name == "nt" else False
    varout = args["output"]
    if varout == "":
        if isinstance(inputs, list):
            for inp in inputs:
                output.append(
                    os.path.basename(inp).replace("%20", "_").replace(".ism", "")
                )
        else:
            output += os.path.basename(inputs).replace("%20", "_").replace(".ism", "")
    else:
        if set(",+").intersection(varout):
            outputs = parse_options(varout, clean=False)
            assert isinstance(
                inputs, list
            ), "Invalid Multiple Output `-o/--output` paths provided for a single ISM input!"
            assert len(inputs) == len(
                outputs
            ), "Invalid Multiple Output `-o/--output` paths provided for {} ISM Inputs!".format(
                len(inputs)
            )
            for out, inp in zip(outputs, inputs):
                output.append(parse_output(out, inp))
        elif os.path.isfile(varout):
            outputs = parse_options_file(varout, clean=False)
            assert isinstance(
                inputs, list
            ), "Invalid Multiple Output `-o/--output` paths provided for a single ISM input!"
            assert len(inputs) == len(
                outputs
            ), "Invalid Multiple Output `-o/--output` paths provided for {} ISM Inputs!".format(
                len(inputs)
            )
            for out, inp in zip(outputs, inputs):
                output.append(parse_output(out, inp))
        else:
            if isinstance(inputs, list):
                for inp in inputs:
                    output.append(parse_output(out, inp))
            else:
                output += parse_output(out, inputs)

    assert output, "Invalid Output `-o/--output` path provided!"

    ffmpeg_location = os.path.abspath(args["ffmpeg"])
    if os.path.isdir(os.path.join(ffmpeg_location, "ffmpeg")):
        ffmpeg_location = os.path.join(
            *[
                os.path.join(ffmpeg_location, "ffmpeg"),
                return_ffmpeg_foldername(),
                "ffmpeg.exe" if os_windows else "ffmpeg",
            ]
        )
    elif os.path.isdir(ffmpeg_location):
        ffmpeg_location = os.path.join(
            *[
                ffmpeg_location,
                return_ffmpeg_foldername(),
                "ffmpeg.exe" if os_windows else "ffmpeg",
            ]
        )
    else:
        ffmpeg_location = ""

    if (
        ffmpeg_location
        and platform.system() == "Linux"
        and not os.access(ffmpeg_location, os.X_OK)
    ):
        os.chmod(ffmpeg_location, 509)

    ydl_opts = {}

    qualities = {"high": ">=720", "medium": "<720", "low": "<=480"}
    ydl_opts["format"] = "bestvideo[height{}]+bestaudio/best[height{}]".format(
        qualities[args["quality"]], qualities[args["quality"]]
    )

    if ffmpeg_location:
        ydl_opts["ffmpeg_location"] = ffmpeg_location
    else:
        print(
            "WARNING: FFmpeg not available, thereby Audio/Video streams will not be merged!"
        )

    if isinstance(inputs, list):
        for inp, out in zip(inputs, output):
            print(
                "Downloading Video: `{}.mp4` from playlist".format(
                    os.path.basename(out)
                )
            )
            ydl_opts["outtmpl"] = out + ".%(ext)s"
            inp += "/manifest(format=mpd-time-csf)"
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([inp])
        if Inputisfile:
            with open(args["input"], "r+") as raw:
                raw.seek(0)
                raw.truncate()
                raw.write("# Paste your URLs line-by-line below:\n")
    else:
        inputs += "/manifest(format=mpd-time-csf)"
        ydl_opts["outtmpl"] = output + ".%(ext)s"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([inputs])

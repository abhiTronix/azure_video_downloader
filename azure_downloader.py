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
import os
import platform
import argparse

try:
    # import OpenCV Binaries
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


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Azure Media Services Video-Downloader.")
    ap.add_argument(
        "-i",
        "--input",
        required=True,
        type=str,
        help="URL of valid ISM Videostream.",
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
    args = vars(ap.parse_args())

    inputs = args["input"]
    assert str(inputs).endswith(".ism"), "Invalid Input `-i/--input` URL provided!"

    output = ""
    os_windows = True if os.name == "nt" else False
    if args["output"] == "":
        output = os.path.basename(inputs).replace("%20", "_").replace(".ism", "")
    else:
        abs_path = os.path.abspath(args["output"])
        if (os_windows or os.access in os.supports_effective_ids) and os.access(
            os.path.dirname(abs_path), os.W_OK
        ):
            if os.path.isdir(abs_path):
                extracted = (
                    os.path.basename(inputs).replace("%20", "_").replace(".ism", "")
                )
                output += os.path.join(abs_path, extracted)
            else:
                f_name = os.path.basename(abspath).replace(".", "_")
                output += os.path.join(os.path.dirname(abspath), f_name)
        else:
            raise ValueError("Invalid Output `-o/--output` path provided!")

    inputs += "/manifest(format=mpd-time-csf)"

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

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": output + ".%(ext)s",
    }
    if ffmpeg_location:
        ydl_opts["ffmpeg_location"] = ffmpeg_location
    else:
        print(
            "WARNING: FFmpeg not available, thereby Audio/Video streams will not be merged!"
        )

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([inputs])

# Azure Video-Downloader Python Script

Azure Media Services Video-Downloader Script written in Python that enables us to download videos from any online Azure Media Services on-the-go through our commandline.  


&nbsp;

### Disclaimer

IT MAY BE ILLEGAL TO USE AZURE VIDEO-DOWNLOADER PYTHON SCRIPT FOR APPLICATIONS YOU DON'T HAVE PERMISSION TO ACCESS. YOU MUST USE IT FOR RESEARCH & EDUCATIONAL PURPOSES ONLY, AT YOUR OWN DISCRETION & WITHOUT REPRESENTATION OR WARRANTY OF ANY KIND. WE ARE NOT RESPONSIBLE FOR WHERE/HOW YOU USE THIS SCRIPT AND ANY DAMAGES YOU MAY CAUSE!

:warning: CONSIDER YOURSELF WARNED!

&nbsp;

### Prerequisites (one-time only)

Remember: You just have to perform these following 5-steps only one time! 

1.	Download and install Latest Python-3 along with pip: [Tutorial video-link: https://youtu.be/oNLhg29aykc]

2.	Download AZURE Video-Downloader Script: 
You can watch this video https://youtu.be/X5e3xQBeqf8 to download the folder containing script from a browser OR from git software. You can download this script from our GitHub repository

3.	Extract the ZIP file: If you downloaded script from browser it will be in compressed format such as master.zip. Right-click on it and select “Extract” to extract the content of this zip file. For reference in this document, let's call the extracted folder as script_folder. 

	**Note :bulb::** You don’t need to perform above step if you downloaded script_folder using git software!
 
4.	Now go into the script folder and open the terminal. Thereby, install required python dependencies by running following command:

	```sh
	# run these commands in your terminal/command-prompt/powershell
	python -m pip install -U --user requirement.txt
	```
 
5.	Download and extract FFmpeg binaries: Remember you must require FFmpeg in order to merge audio and video files automatically. In order to setup FFmpeg on your computer easily you can download `ffmpeg.zip` file from our repository: 
 
	**Download ffmpeg.zip file from:** http://xyz.com/to_be_implemented

6. After downloading, just copy the zip file inside your script_folder, and just Right-click and select “Extract” to extract its content right away. The extracted folder name must be `ffmpeg`.

&nbsp;
 
### Extracting URL

For downloading video, a **ISM URL** _(URL with `.ism` extension)_ is required as input for our python script. There are three ways to do this:

####  A.	Use any Web-Browser: (Recommended for all platforms)

1.	Go the video page where video is being played.
2.	Double check video is in the state of being played and not paused.
3.	Right-click on the webpage and select "Inspect" or something similar (See below).
4.	On clicking Inspect, A menu will open, and on the menu click "Network" tab.
5.	In "Network" tab, write "Fragments" in "filter" search field (see below).
6.	Select the first filter option (if available, otherwise make sure the video is still playing in the background). Right-click on the selected option and click "copy", and then "Copy link address" in order to copy that URL.
7.	Now your copied URL will look something like this:
	```sh
	https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism/QualityLevels(551000)/Fragments(video=360000000,format=mpd-time-csf)
	```
8.	Just delete everything past `.ism` in that URL, and the final value is the required ISM URL:
	```sh
 	https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism
 	```
 

#### B.	Use Internet Download Manager (IDM): (For Windows Only)
 
1.	Download and install IDM with 11 days trial period or forever if you’ve the key: (Watch this video https://youtu.be/uGct61De_EU).
2.	After successful installation, it will install extension on your browser automatically.
3.	Now when video is played on website, a “Download this video” button will show up at upper-right corner of the video.
4.	Click any of the available option and a Dialog Box will show up as follows.
5.	In opened Dialog Box, copy the URL present adjacent to the "URL" text field, which will be something like: 
	```sh
	https://streamdiat-inct.streaming.media.azure.net/94e43e68-2592-4866-95d7-52b587e41a9f/Feature%20Engineering%20Dimensionali.ism/manifest(format=mpd-time-csf)&selected_id=1_V_video_4
	```
6.	You can safely close the Dialog Box after that.
7.	Just delete everything past `.ism` and the final value is the required ISM URL, as follows:
	```sh
	https://streamdiat-inct.streaming.media.azure.net/94e43e68-2592-4866-95d7-52b587e41a9f/Feature%20Engineering%20Dimensionali.ism
	```
 

#### C.	Use Xtreme Download Manager (XDM): (For all platforms)
 
1.	Download and install Xtreme Download Manager. (Watch this video tutorial https://youtu.be/uksktuNvKNc).
2.	You will be asked to install extension on your browser of your choice manually. Go ahead do that.
3.	When we are done, restart the browser. 
4.	Now when video is being played on website, a "DOWNLOAD VIDEO" button will show up at down-right corner of the browser.
5.	Click any of the available option if related to video being played in the background (for e.g "DIAT.mp4").
6.	After clicking the option, downloading will start. Hurry to cancel it asap, as we don't need this video.
7.	Now right-click on Cancelled video and Click "Copy URL" which will be something like:
	```sh
	https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism/QualityLevels(551000)/Fragments(video=360000000,format=mpd-time-csf)
	```
8.	Just delete everything past `.ism` in that URL, and the final value is the required ISM URL:
	```sh
 	https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism
 	```


&nbsp;


### Usage

1.	Open a terminal/command-prompt/powershell of your choice, in the script_folder where your script exists.

2.	To get started, you can view help by simply use "-h / --help" flag for getting familiar with all the available options:

	```sh
	$ python azure_downloader.py -h

	usage: azure_downloader.py [-h] -i INPUT [-o OUTPUT] [-f FFMPEG]

	Azure Media Services Video-Downloader.

	optional arguments:
	  -h, --help            show this help message and exit
	  -i INPUT, --input INPUT
	                        URL of valid ISM Videostream.
	  -o OUTPUT, --output OUTPUT
	                        Output Video filename (with/without path).
	  -f FFMPEG, --ffmpeg FFMPEG
	                        Location of FFmpeg static binary (Required to merge Audio/Video Streams).

	```

3.	**[Compulsory]** Now give extracted ISM URL to the input `-i/--input` of the python script as follows: 
	```sh
	$ python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism
	```
	and video start downloading.

4.	**[Optional]** By default, our python script automatically assign file name of the output video file using ISM URL and downloads it to `output` directory of script_folder. But, you can also specify the output filename/file-directory using `-out/--output` command as follows:

	```sh
	$ python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism -o Overview.mp4
	```

	**OR give full output path:**

	```sh
	$ python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism -o C:/Overview.mp4
	```

5.	**[Optional/Only for developers]** By default python script uses FFmpeg(used to merge audio and video) provided in the `ffmpeg` folder of script_folder, that we downloaded and extracted in page-1, but you can assign your own FFmpeg binaries too using `-f/--ffmpeg` option as follows:

	```sh
	$ python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism -o Overview.mp4 -f "C:/ffmpeg/bin/ffmpeg.exe"
	```

&nbsp;

### Copyright

```tex
AZURE VIDEO-DOWNLOADER - Downloads videos from Azure Media Services.
Copyright (C) 2020  Abhishek Thakur @abhiTronix <abhi.una12@gmail.com>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
# Azure Video-Downloader Python Script :inbox_tray:

_A Video-Downloader Python Script that enables us to download videos from any online Azure Media Services on-the-go directly through our commandline._  

&nbsp;

## Disclaimer


We are not responsible for any misuse, you must use it for research & educational purposes only, at your own discretion & without representation or warranty of any kind. It is your responsibility to obey laws!

:warning: _CONSIDER YOURSELF WARNED!_

&emsp;

## Usage:

**Info 🕵️:** _There's also a detailed PDF version of [Azure Video-Downloader Python Script Docs](https://github.com/abhiTronix/azure_video_downloader/releases/download/v1.0.0/Azure.Downloader.Guide.v2.pdf)._

### A. Pre-requisites (one-time steps only)

All following steps you have to perform only one time.

- **Step-1:** Download and install latest python-3 with pip: [Tutorial video link](https://youtu.be/oNLhg29aykc)
- **Step-2:** Download script from git hub repository using browser or clone using _git_ software.
  - Watch [this video](https://youtu.be/X5e3xQBeqf8%20) for downloading from browser and from _git_ software
  - Extract the zip at suitable place let's for this document call it _`script_folder`_.
- **Step-3:** Download and install python dependencies:

  Run these commands in your terminal/command-prompt/ power-shell
  
  ```sh
  cd script_folder
  python -m pip install -r -U --user requirement.txt
  ```
- **Step-4:** Download and extract _ffmpeg.zip_

  - Must requires FFmpeg to merge audio and video.
  - Download ffmpeg.zip from: https://github.com/abhiTronix/azure_video_downloader/releases/download/v1.0.0/ffmpeg.zip
  - Copy zip file inside our `script_folder`, and Extract it there.
  - Extracted folder name will be _ffmpeg_.

&emsp;

### B. Extracting URL

ISM URL _(`https` URL with `.ism` extension)_ is necessary for our python script as input. There are mainly three ways to extract it:

#### 1. Use web-browser: _(Recommended)_ (For all platforms)

- Go the video page where video is being played.
- Double check video is being played not paused.
- Right click on the page and select _Inspect_ or something similar.
- A menu will open, then on the menu, click _Network_ tab.
- In _Network_ tab, write _Fragments_ in _filter_ search field.
- Select that `Fragment` filter option (if available, otherwise make sure video is still playing in the background)
- Right click on the selected option and click _copy_ and then _Copy link address_.
- The copied URL will look something like this:
  ```sh
  https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism/QualityLevels(551000)/Fragments(video=360000000,format=mpd-time-csf)
  ```
- Just delete everything past `.ism` and the final value is the required ISM URL, as follows:
  ```sh
  https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism
  ```

#### 2. Use IDM: (Windows Only)

- Download and install IDM with 11 days trial period (Watch this video [https://youtu.be/uGct61De\_EU](https://youtu.be/uGct61De_EU)).
- It will install extension on your browser automatically.
- Now when video is played on website, a Download button will show up at upper-right corner of the video.
- Click any of the available option and a dialog box will show up.
- In dialog box, Copy the URL present in the _Address_ text field which will be something like:
  ```sh
  https://streamdiat-inct.streaming.media.azure.net/94e43e68-2592-4866-95d7-52b587e41a9f/Feature%20Engineering%20Dimensionali.ism/manifest(format=mpd-time-csf)&selected_id=1_V_video_4
  ```
- Just delete everything past `.ism` and the final value is the required ISM URL, as follows:
  ```sh
  https://streamdiat-inct.streaming.media.azure.net/94e43e68-2592-4866-95d7-52b587e41a9f/Feature%20Engineering%20Dimensionali.ism
  ```

#### 3. Use XDM (Xtreme Download Manager): (For all platforms)

- Download and install IDM with 11 days trial period (Watch this video https://youtu.be/uksktuNvKNc).
- You will be asked to install extension on your browser manually, go ahead do it. When done restart browser.
- Now when video is being played on website, a _DOWNLOAD VIDEO_ button will show up at down-right corner of the browser.
- Click any of the available with _DIAT.mp4_.
- After clicking downloading will start, Hurry and Go head to cancel it as we don&#39;t need this video.
- Now right-click on Canceled video and Click _Copy URL_ which will be something like:
  ```sh
  https://streamdiat-inct.streaming.media.azure.net/25fcdac8-e577-4f59-acf9-8921887b4159/AI_W1_Bayesian%20Learning%20Part-1.ism/QualityLevels(1880000)/Fragments(video=60000000,format=mpd-time-csf)
  ```
- Just delete everything past `.ism` and the final value is the required ISM URL, as follows:
  ```sh
  https://streamdiat-inct.streaming.media.azure.net/25fcdac8-e577-4f59-acf9-8921887b4159/AI_W1_Bayesian%20Learning%20Part-1.ism
  ```

&emsp;

### C. Download Video with Script

**Tip:💡** _You can view help by running `python azure_downloader.py -h` command to get familiar with all the available options._

- Open a terminal/command-prompt/power-shell of your choice.
- Give extracted ISM URL _(explained [above](#b-extracting-url))_ to the input `-i/--input` of the python script as following and video start downloading:
  ```sh
  python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism
  ```
  
  ***OR give TXT file path containing multiple URLs(line-by-line):***
  
  ```sh 
  python azure_downloader.py -i URLs.txt
  ```
  
  ***OR give string of muliple URLs seperated by `,` or `+`***:
  
   ```sh 
   python azure_downloader.py -i "https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism,https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/DL1.ism,https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/DL2.ism"  
   ```

- **[Optional]** By default, our python script automatically assigns file name of the output video file using ISM URL and downloads it to `output` directory of script\_folder. But you can also specify the output filename/file-directory using _`-out/--output`_ command as follows:

  :warning: **Note:** This option does not works with input(`-i`) with multiple URLs.
  
  ```sh
  python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism -o Overview.mp4
  ```

  ***OR give full output path:***

  ```sh 
  python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism -o C:/Overview.mp4
  ```
  
- **[Optional/Only for developers]** By default python script uses FFmpeg(used to merge audio and video) provided in the `ffmpeg` folder of script\_folder, that we downloaded and extracted previously, but you can assign your own FFmpeg binaries too using _`-f/--ffmpeg`_ option as follows:
  ```sh
  python azure_downloader.py -i https://streamdiat-inct.streaming.media.azure.net/f12251d4-d8e8-43f1-8202-737f7a186b34/Overview%20of%20AI%20ML.ism -o Overview.mp4 -f C:/ffmpeg/bin/ffmpeg.exe
  ```

&nbsp;

## Copyright

AZURE VIDEO-DOWNLOADER - Downloads videos from Azure Media Services.

Copyright (C) 2020 Abhishek Thakur @abhiTronix abhi.una12@gmail.com

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses](https://www.gnu.org/licenses).

&nbsp;

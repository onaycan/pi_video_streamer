<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

The main purpose of this small project to achieve stepwise a final goal: ar race car. 
This repo is mainly based on [this article] (https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/). 
Since i had to perfoe slight changes to make it suitable for ar-race car project, this repo had to be generated. 
The main differeces include: 

* to increase the performance, threading is disabled
* CORS management is included to avoid problems to get streamer via android client
* fps counter is applied in order to further increase the performance

Additionally source of information you can get from [opencv documentation] (https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html) on this subject. 

### Built With
One major framewrk is used to achieve the goal is opencv. 

<!-- GETTING STARTED -->
## Getting Started

You need to fetch a local copy of these first. 
I would highly recommend to test your camera via motion or similar. 
Before starting all, you may need to add the right module into your modules list. 

```shell
can@canrasp1:~/workspace/.motion$ cat /etc/modules
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
snd-bcm2835

# camera with v4l2 driver
bcm2835-v4l2
can@canrasp1:~/workspace/.motion$
```

### Prerequisites

Use python3 for the project. The following modules are used and needs to be installed priorily: 

* flask
* flask_cors
* imutils
* cv2

Do not forget to create your own certificates.

### Installation
Instllation of flask, flask_cors and imutils is straightforward. 
If you face with problems installing opencv via pip3 utilities, try one or another: 

```shell
sudo apt install python3-opencv
```

if this does not work for you build opencv from the source. First install the dependencies:

```shell
sudo apt-get install cmake
sudo apt-get install gcc g++
sudo apt-get install python3-dev python3-numpy
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgtk-3-dev
```
Then clone the source code: 

```shell
git clone https://github.com/opencv/opencv.git
cd opencv
mkdir build
cd build
sudo make 
sudo make install
```

<!-- USAGE EXAMPLES -->
## Usage
Simply run a server using python3's http.server on an open port, and navigate into your browser. 

```shell
can@canrasp:~/workspace/pi_video_streamer$ sudo python3 video_streamer.py 
[sudo] password for can: 
[ WARN:0] global ../modules/videoio/src/cap_gstreamer.cpp (480) isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
 * Serving Flask app "video_streamer" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
Enter PEM pass phrase:
 * Running on https://10.42.0.1:5500/ (Press CTRL+C to quit)

..
.
```

![Image 1](./readme_pics/stream.png?raw=true "stream")

If the routes GET the url's video_socket and generate_frame are called and you will see above or similar. 
For this example a stereo camera is used, with single lense you will see only one-eye perspective of this. 

<!-- LICENSE -->
## License

Distributed under the MIT License as the major dependencies like opencv, imutils and flask. 

<!-- CONTACT -->
## Contact

Oenay Can - onaycan@gmail.com

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Adrian Rosebrocks articla on pyimagesearch](https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)
* [opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)
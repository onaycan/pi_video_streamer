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


### Installation

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
you@yourmachine$ python3 -m http.server 5000
Serving HTTP on 0.0.0.0 port 5000 (http://0.0.0.0:5000/) ...
127.0.0.1 - - [03/Aug/2020 01:51:30] "GET / HTTP/1.1" 200 -
..
.
```

![Image 1](./readme_pics/folder_structure.png?raw=true "Folder Structure")

The first example will show a single camera mode without background image.
All pages have mouse control options. 

![Image 2](./readme_pics/interior_single_eye.png?raw=true "First example")

The second example will show the same of above with the stereo effect. 

![Image 3](./readme_pics/interior_stereo_eyes.png?raw=true "First example")

The second example will show the same of above with the background [cat image](https://www.enewser.com/science/interesting-facts-about-cats/)

![Image 4](./readme_pics/interior_stereo_eyes_background.png?raw=true "Third example")

<!-- LICENSE -->
## License

Distributed under the MIT License as the major dependencies like three.js. 

<!-- CONTACT -->
## Contact

Oenay Can - onaycan@gmail.com

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [threejs](https://threejs.org/)
* [Sketchfab](https://sketchfab.com/3d-models/cockpit-model-vr-33acf5be400740aa85d7738871231962)
# Face_pkg

## Introduction********************************************************************

### face_pkg is the core ROS package for face recognition and face detection. It initiates through initiate_facial.launch
### It uses "deep_face" library to detect faces and recognize their emotions categorizing them into 7 categories:
#### happy|sad|angry|neutral|fear|disgust|surprise

### It listens on "/web_exp_publisher" Topic for "Exp.msg" messages and waits for a message with a true "auto" value.
### Then calls to the face_imitation module for emotion recognition and publishes the results on the /py_exp_publisher Topic as the "face_pub" Node. This is then recieved by rosbridge websocket and passed on to web-interface for furthur actions (e.g. Changing the video|audio respectively) : 
#### (script.js --> Django: Views.py --> script.js --> index.html)

## *NOTE*
### *There are no direct connections between the ROS nodes and the Android client. The Android client only recieves the data from the web-interface. The web-interface is the only module that is connected to both the ROS nodes and the Android client and is responsible for passing the data between them.*

## Nodes********************************************************************
### face_pub:
#### Subscribed Topics:
##### /web_exp_publisher
#### Published Topics:
##### /py_exp_publisher

## Launch Files********************************************************************
### initiate_facial.launch:
#### Nodes:
##### face_pkg/face_pub
##### rosbridge_websocket
##### web-video-server

## Messages********************************************************************
### Exp.msg:
#### Fields:
##### bool auto
##### string exp

## Services********************************************************************
### None

## Parameters********************************************************************
### None

## Dependencies********************************************************************
### deep_face
### rosbridge_suite
### web_video_server

# *NOTE* *If requirements.txt does not exist, run "pipreqs [path/to/ project]" to generate requirements.txt file for your project and install the requirements with pip install -r requirements.txt*


## Installation********************************************************************
### Install the package in the src folder of your catkin workspace and build it using catkin_make.

## Usage********************************************************************
### Run the launch file using roslaunch face_pkg initiate_facial.launch

## Bugs & Feature Requests********************************************************************
### Please report bugs and request features using the Issue Tracker

## Maintainers********************************************************************
### Mahta Akhyani (mahta.akhyani@gmail.com)

## License********************************************************************
### MIT License




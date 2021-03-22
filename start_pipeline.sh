#!/bin/bash
#
# This script 

gst-launch-1.0 v4l2src ! nvvidconv ! 'video/x-raw(memory:NVMM), width=1024, height=768, framerate=120/1' ! nvv4l2h264enc insert-sps-pps=true ! h264parse ! rtph264pay pt=96 ! multiudpsink clients=192.168.1.195:8000,127.0.0.0:5000 sync=false -e
#!/bin/bash
cd anime
/home/bsb/Downloads/ffmpeg -framerate 20 -i test%04d.png -c:v libx264 -profile:v high -r 30 -pix_fmt yuv420p output.mp4

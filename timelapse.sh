#!/bin/bash

$DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -F 30 -r 1920x1080 path_to_saved_pictures/$DATE.jpg
# split-video
A simple python program that uses ffmpeg to split video into chunks, given timing.

## Usage
python3 split_videos.py [-h] [-i INPUTFILE] [-o OUTPUTMASK] [-t TIMES] [-l LOGFILE]

optional arguments:

-h, --help show help

-i INPUTFILE, --inputfile INPUTFILE input file

-o OUTPUTMASK, --outputmask OUTPUTMASK name mask for the output file

-t TIMES, --times TIMES times in HH:MM:SS.S format separated by commas

-l LOGFILE, --logfile LOGFILE where to store log file

## Example
python3 split_videos.py -i inputvideo.mp4 -t 00:28:33,01:06:26,02:38:29 -o output -l splitvideo.log

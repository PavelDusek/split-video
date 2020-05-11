# split-video
A simple python program that uses ffmpeg to split video into chunks, given timing.

== Usage ==
python3 split_videos.py [-h] [-i INPUTFILE] [-o OUTPUTMASK] [-t TIMES]
                       [-l LOGFILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        input file
  -o OUTPUTMASK, --outputmask OUTPUTMASK
                        name mask for the output file
  -t TIMES, --times TIMES
                        times in HH:MM:SS.S format separated by commas
  -l LOGFILE, --logfile LOGFILE
                        where to store log file

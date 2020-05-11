# coding: utf-8
import math
import argparse
from subprocess import Popen, PIPE

def toSeconds( h, m, s ):
    return 3600*h + 60*m + s
    
def fromSeconds( t ):
    h = int(math.floor(t /3600))
    t -= h * 3600
    m = int(math.floor(t/60))
    t -= m * 60
    s = t
    return h, m, s

parser = argparse.ArgumentParser(description="Split video into smaller chunks")
parser.add_argument('-i', '--inputfile', help='input file', action='store')
parser.add_argument('-o', '--outputmask', help='name mask for the output file', action='store')
parser.add_argument('-t', '--times', help='times in HH:MM:SS.S format separated by commas', action='store')
parser.add_argument('-l', '--logfile', help='where to store log file', action='store')
args = parser.parse_args()

times = args.times.split(",")
time_tuples = [ t.split(":") for t in times ]
time_tuples = [ ( int(h), int(m), float(s) ) for h, m, s in time_tuples ]

previous = (0, 0, 0)
for i, (h, m, s) in enumerate(time_tuples):
    h_prev, m_prev, s_prev = previous
    h_dif, m_dif, s_dif = fromSeconds( toSeconds( h, m, s ) - toSeconds( h_prev, m_prev, s_prev ) ) 
    command_parts = [
            "ffmpeg",
            "-i", args.inputfile,
            "-ss", f"{h_prev:02d}:{m_prev:02d}:{s_prev}",
            "-t", f"{h_dif:02d}:{m_dif:02d}:{s_dif}", 
            f"{args.outputmask}{i}.mp4"
            ]
    print(" ".join(command_parts))
    p = Popen(command_parts, stdin=PIPE, stdout=PIPE, stderr=PIPE )
    output, err = p.communicate()
    if args.logfile:
        with open(args.logfile, "a") as log:
            log.write( "******************************" )
            log.write( " ".join(command_parts) )
            log.write( str(output) )
            log.write( "********************" )
            log.write( str(err) )
            log.write( "******************************" )
    previous = (h, m, s)

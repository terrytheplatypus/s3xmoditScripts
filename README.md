# s3xmoditScripts
Convenience scripts for openmpt.

Currently the only script in this repo is randITOffset.py, which is a utility for generating granular-style sample playback, where samples are chosen at a random offset from the playhead. This script is currently only compatible with the .it and .mptm formats. 

This script takes 6 arguments:
    rowLen: the number of rows in the tracker you want,
    offsetEnd: the last offset in the last frame  (in hex) ,
    frameLen: 0 if there is only one frame, increment for additional frames
    direction: 0 for forwards, 1 for backwards, 2 for totally random
    offset randomness: 0 through 10, picks offsets randomly distributed around the playhead (0 is no randomness, and 10 is chaotic)
    pan randomness: 0 through 10, increasing the value increases the probability of random pan
    
 Some ideas which i may implement: random pitch with e0x/f0x in the volume column
 stutter, where there's a probability that sample offsets will be repeated
 ability  to change step size of playhead (currently hardcoded at 1)


To use, run python randITOffset.py,followed by the 6 required parameters.
For example:

python randITOffset.py 256 8e 4 1 3 3

Then copy the text beginning with ModPlug Tracker MPT .

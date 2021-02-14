#first a | before each line, then three spaces for note
#, 2 spaces for instrument, 3 for vol column, then 3 for fx column
#what i want: something similar to saltbearer's sunvox thing, where
#i can control randomness.
#different desirable patterns:
#going forward or backward with random fluctuations normally distributed
#around the "play head"
#total randomness
#need parameters for sample length and frame number(frame size could be optional)
#and another parameter for how many rows you want it to "granulate" over
#also add option for random panning
#random panning shifts should be irregular, and also jump back to the center
#there could be interpolated panning
#also exx/fxx commands could be randomly inserted in vol column
#but first implement only random offset and random panning
#could also make it output to a file

#additionally yet another parameter could be added to control speed of granulation
#and another for stutter (repeating lines)

#input offsetlen as hex string to make it easier for user (me), so 
#script has to convert back and forth between hex and int

#for now, direction will be 0, 1, or 2
#0 is forward, 1 is backward, 2 is total randomness
#frame len is 0 if there's only one frame
#randomness could be 0 to 10
#randomPan is 0 for no random pan and 1 for random pan
#another possible param is step size but STOP FEATURE CREEPING

#leave instrument value blank for now

import random
import sys
import math

def intToHex(n):
    return hex(n)[2:]
def hexToInt(n):
    return int(n, 16)


#offsetEnd is the largest offset value on the ending frame


def randOffsetGenerate(rowLen,
                       offsetEnd,
                       frameLen,
                       direction,
                       offsetRandomness,
                       panRandomness):
    #if (frameLen+1)*256+offsetEnd is less than currRow then wrap around
    genString= "ModPlug Tracker MPT\n"
    sampleLen = (frameLen+1)*256+offsetEnd
    playHead= 0 if direction==0 else sampleLen
    iterVal = 0

    lastRowRandPan = False
    
    for currRow in range(1,rowLen):
        if(direction==0):
            playHead += 1
        if(direction==1):
            playHead -= 1
        if(direction==2):
            playHead = random.randrange(0, sampleLength)
            
        offset= playHead
        scalingFactor = 10
        
        #could try normal distribution but for now don't
        if(direction < 2 and offsetRandomness > 0):
            
            offset = random.randrange(math.floor(offsetRandomness/10*(sampleLen/2 - sampleLen)/scalingFactor),1)+playHead
            #random.randrange(0, 10)+playHead
                   
                    
        offset = intToHex(offset%256).upper()

        if(len(offset)<2):
            offset = "0"+offset

        panner="..." if not lastRowRandPan else "p32"
        
        if(panRandomness > 0):
            if (random.random() < panRandomness/10):
                panner = "p" + str(random.randrange(10,50))
                lastRowRandPan = True

        #if ((playHead-1)%256 == 0 or playHead==0):
        #    print("sdfhsdfkjh")
        #write line

        print("sfdsh "+str(iterVal))
        fx = "O"+offset if ( ((playHead-1)%256) != 0 and iterVal != 0  ) else "SA"+ str(math.floor(playHead/256))
        genString +="|C-5.."+panner+fx+"\n"
        iterVal+=1

    return genString


if(len(sys.argv)<7):
    print("""Not enough arguments. This script takes 6 arguments:
    rowLen: the number of rows in the tracker you want,
    offsetEnd: the last offset in the last frame,
    frameLen: 0 if there is only one frame, increment for additional frames
    direction: 0 for forwards, 1 for backwards, 2 for totally random
    offset randomness: 0 through 10, picks offsets randomly distributed around the playhead
    \10 randomness should be swarming around like half the sample
    pan randomness: 0 through 10, increasing the value increases the probability of random pan""")



print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
print(sys.argv[5])
print(randOffsetGenerate(int(sys.argv[1]),\
                   hexToInt("0x"+sys.argv[2]),\
                  int(sys.argv[3]),\
                  int(sys.argv[4]),\
                   int(sys.argv[5]),\
                  int(sys.argv[6])))

# CS5 Gold, Lab 3
# Filename: hw3pr1.py
# Name: Florence Lin
# Problem description: Lab 3 problem, "Sounds Good!"

import time
import random
import math
import csaudio
from csaudio import *
import wave
wave.big_endian = 0  # if you are having trouble, try commenting out this line...



# a function to get started with a reminder
# about list comprehensions...
def three_ize(L):
    """three_ize is the motto of the green CS 5 alien.
       It's also a function that accepts a list and
       returns a list of elements each three times as large.
    """
    # this is an example of a list comprehension
    LC = [3 * x for x in L]
    return LC



# Function to write #1:  scale
def scale(L, scale_factor):
    """scale is a function that accepts a list and a scale_factor and 
       returns a list of elements, each multiplied by the scale_factor
       Arugments: L is a list and scale_factor can be any int or float
    """

    return [scale_factor*x for x in L]





# here is an example of a different method
# for writing the three_ize function:
def three_ize_by_index(L):
    """three_ize_by_index has the same behavior as three_ize
       but it uses the INDEX of each element, instead of
       using the elements themselves -- this is much more flexible!
    """
    # we get the length of L first, in order to use it in range:
    N = len(L)
    LC = [3 * L[i] for i in range(N)]
    return LC



# Function to write #2:  add_2
def add_2(L, M):
    """returns a list from two lists that is the element by element sum of the two arguments
       if the lists are different lengths, don't add the extra elements from the longer list
       arugments: L and M are list with integers 
    """
    N = min(len(L), len(M))
    return [L[i] + M[i] for i in range(N)]






# Function to write #3:  add_3
def add_3(L, M, P):
    """returns a list from two lists that is the element by element sum of the two arguments
       if the lists are different lengths, don't add the extra elements from the longer list
       arugments: L and M are list with integers 
    """
    N = min(len(L), len(M), len(P))
    return [L[i] + M[i] +P[i] for i in range(N)]





# Function to write #4:  add_scale_2
def add_scale_2(L, M, L_scale, M_scale):
    """ Returns a single list that is the element by element sum of L and M scaled by L_scale and M_scale
       Arguments: L and M are two lists and L_scale and M_scale are two floating point numbers which stand for the scale of L and M
    """
    N = min(len(L), len(M))
    return [L_scale*L[i] + M_scale*M[i] for i in range(N)]









# Helper function:  randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    else:
        return x



# Function to write #5:  replace_some
def replace_some(L, chance_of_replacing):
    """ independently replaces each element in L using helper function randomize
        Argument: L is a list of numbers, chance_of_replacing is a floating point value
    """
    r = random.uniform(0,1)
    return [randomize(x, chance_of_replacing) for x in L]










#
# below are functions that relate to sound-processing ...
#


# a function to make sure everything is working
def test():
    """A test function that plays swfaith.wav
       You'll need swfaith.wav in this folder.
    """
    play('swfaith.wav')


# The example changeSpeed function
def changeSpeed(filename, newsr):
    """changeSpeed allows the user to change an audio file's speed.
       Arguments: filename, the name of the original file
                  newsr, the new sampling rate in samples per second
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    # we don't really need this line, but for consistency...
    newsr = newsr             # from the input! (not needed, a reminder!) 
    newsamps = samps          # same samples as before
    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'



def flipflop(filename):
    """flipflop swaps the halves of an audio file
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    x = len(samps)//2
    newsamps = samps[x:] + samps[:x]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'




# Sound function to write #1:  reverse
def reverse(filename):
    """creates a reversed set of sound samples
       Argument: filename, the name of the original file
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")
    # this gets the midpoint and calls it x
    newsamps = samps[::-1]
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'






# Sound function to write #2:  volume
def volume(filename, scale_factor):
    """uses filename and scale_factor and plays a the filename amplified by the scale factor (each sample multiplied by scale_factor)
       Argument: filename: the name of the original file, scale_factor: int or float value
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")

    newsamps = scale(samps, scale_factor)
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'







# Sound function to write #3:  static
def static(filename, probability_of_static):
    """uses a sound file and a floating-point value to handle sound in a way that outputs part of the sound as static/randomness
       Arguments: filename: the name of the original file, probability_of_static: float between 0 and 1
       Result: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """

    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")

    newsamps = replace_some(samps, probability_of_static)
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'





# Sound function to write #4:  overlay
def overlay(filename1, filename2):
    """ Takes two filenames and combines the two, creates a sound file that is the length of the shortest file
        Argument: accepts two filenames (filename1 and filename2)
        Results: no return value, but
               this creates the sound file 'out.wav'
               and plays it
    """
    print("Playing the original sounds...")
    play(filename1)
    play(filename2)

    samps, sr = readwav(filename1)   # get samps and sr from the file!
    samps2, sr2 = readwav(filename2)

    print("The first 10 sound-pressure samples in" + filename1 + "are\n", samps[:10])
    print("The number of samples per second in" + filename1 + "is", sr)
    print("The first 10 sound-pressure samples in" + filename2 + "are\n", samps2[:10])
    print("The number of samples per second in" + filename2 + "is", sr2)

    print("Computing new sound...")

    newsamps = add_scale_2(samps, samps2, 0.5, 0.5)
    newsr = sr               # same sr as before

    write_wav([newsamps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'
    

# Sound function to write #5:  
def echo(filename, time_delay):
    """Takes a sound file (filename) and float (time_delay) and runs echo which overlays the original sound by time_delay
        Argument: accepts filename: a sound file, and time_delay: a float
        Results: no return value, but
        this creates the sound file 'out.wav'
        and plays it
    """
    print("Playing the original sound...")
    play(filename)

    samps, sr = readwav(filename)   # get samps and sr from the file!

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Computing new sound...")

    delay = time_delay*len(samps)
    delay = int(delay)
    sampsecho = [0]*delay + samps
    sampsans = add_scale_2(samps, sampsecho, 0.5, 0.5)
    newsr = sr               # same sr as before

    write_wav([sampsans, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'






# Helper function for generating pure tones
def gen_pure_tone(freq, seconds):
    """pure_tone returns the y-values of a cosine wave
       whose frequency is freq Hertz.
       It returns nsamples values, taken once every 1/44100 of a second.
       Thus, the sampling rate is 44100 hertz.
       0.5 second (22050 samples) is probably enough.
    """
    # we get to pick our own sampling rate, sr
    sr = 22050
    # how many data samples to create
    nsamples = int(seconds*sr) # rounds down
    # our frequency-scaling coefficient, f
    f = 2*math.pi/sr   # converts from samples to Hz
    # our amplitude-scaling coefficient, a
    a = 32767.0
    
    # now, create the sound!
    samps = [a*math.sin(f*n*freq) for n in range(nsamples)]
    sr = sr   # not needed, but a reminder
    return [samps,sr]


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Generating tone...")
    samps, sr = gen_pure_tone(freq, time_in_seconds)

    print("The first 10 sound-pressure samples are\n", samps[:10])
    print("The number of samples per second is", sr)

    print("Writing out the sound data...")
    write_wav([samps, sr], "out.wav") # write data to out.wav

    print("Playing new sound...")
    play('out.wav')




# Sound function to write #6:  chord

def add_scale_3(L, M, P, L_scale, M_scale, P_scale):
    """ Returns a single list that is the element by element sum of L and M and P scaled by L_scale and M_scale and P_scale
       Arguments: L and M and P are three lists and L_scale and M_scale and P_scale are three floating point numbers which stand for the scale of L and M and P.
    """
    N = min(len(L), len(M), len(P))
    return [L_scale*L[i] + M_scale*M[i] + P_scale*P[i] for i in range(N)]

def chord(f1, f2, f3, time_in_seconds):
    """takes three float frequencies and another float and creates/plays a three note chord from those frequencies
       arguments: f1 f2 and f3 are all float values that represent frequencies, time_in_seconds is the amount of time the chord plays
       Results: no return value, but
       this creates the sound file 'out.wav'
       and plays it
    """


    samps1, sr1 = gen_pure_tone(f1, time_in_seconds)   # get samps and sr from the file!
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds) 
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds) 

    print("Computing new sound...")

    samps = add_scale_3(samps1, samps2, samps3, 0.33, 0.33, 0.33)
    newsr = sr1               # same sr as before

    write_wav([samps, newsr], "out.wav") # write data to out.wav
    print("\nPlaying new sound...")
    play('out.wav')   # play the new file, 'out.wav'
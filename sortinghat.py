#!/usr/bin/env python
# this program works like a Hogwarts sorting hat. It randomly picks a hogwarts house and speaks it out
import grovepi
import time
import os
from random import randint

def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    return words[num_picked]


# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4
while True:
        # Read distance value from Ultrasonic and check whether the hat is on someone's head (whether the vlaue is less than 30).
        if (grovepi.ultrasonicRead(ultrasonic_ranger) < 30):
                time.sleep(2)
                houses = ['Gryffyndor', 'Hufflepuff', 'Ravenclaw', 'Slitherin']
                # picks a house and speaks it
                os.system("espeak " + (pick(houses)))
                # Wait until the person takes off the hat(wait until the value is greater than 30).
                while True:
                        value = grovepi.ultrasonicRead(ultrasonic_ranger)
                        print(value)
                        if (value < 30):
                                time.sleep(1)
                        else:
                                break
        else:
                time.sleep(1)

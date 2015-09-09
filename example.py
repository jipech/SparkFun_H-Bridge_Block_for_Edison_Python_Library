#!/usr/bin/python
import mraa
import time
import sys

sys.path.append(r'~/programy/python/')

from robot import *

forward(1)
lrotate(1)
forward(1)
lrotate(1)
back(1)
rrotate(1)
back(1)
rrotate(1)

quit()

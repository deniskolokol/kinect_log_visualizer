# -*- coding: utf-8 -*-

import os
import time
import random
from utils import shoot, random, spinning_cursor, rand_string, weighted_choice

i = 0
curr = 0
while True:
    disp = (curr + random.uniform(1, 40)) / 2. # smooth it out
    curr = disp
    attrs = None if curr > 27 else ['dark']
    shoot(
        '{0: <35}'.format("|" * int(disp)) + ('%.3f' % disp),
        color='white',
        attrs=attrs
        )
    time.sleep(random.random()*0.05)
    i += 1

    # occasionally clear the screen and output rand string
    if i >= 100:
        if weighted_choice([(True, 1), (False, 9)]):
            os.system('clear')
            shoot("\n%s\n" % rand_string(random.randint(200, 800)),
                  color='blue')
            spinning_cursor(random.random()*0.5)
        i = 0

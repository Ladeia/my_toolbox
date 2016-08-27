#!/usr/bin/env python3

import time
import webbrowser

break_count = 0
max_breaks = 4

while(True):
    time.sleep(25 * 60)
    webbrowser.open("https://www.youtube.com/watch?v=igPBmG1mNf4")
    break_count = break_count + 1
    if break_count % 4 < max_breaks:
        time.sleep(5 * 60)
    else:
        time.sleep(20 * 60)



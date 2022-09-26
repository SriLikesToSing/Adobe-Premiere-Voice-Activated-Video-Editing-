
#Steps
#open when premiere pro starts
#Start running


'''
############CONTROLS##############

'''

import test
from pynput.keyboard  import Key, Controller

keyboard = Controller()

keyboard.press('k')
keyboard.release('k')
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)


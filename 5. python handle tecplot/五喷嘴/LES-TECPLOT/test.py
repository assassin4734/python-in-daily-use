from tecplot.exception import *
from tecplot.constant import *
import tecplot as tp
import pyautogui
import time


tp.session.connect()
tp.load_layout('E:\\0-PhD\\5 nozzle\\4-les\\untitled.lay')
time.sleep(0.5)
pyautogui.press('enter')
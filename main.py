import cv2
import numpy
import matplotlib
import matplotlib.pyplot
import PIL
import PIL.Image
import collections
img = PIL.Image.open("samples.png") # select png
img = img.convert("RGB") # 
pixels = img.getdata()
for color in pixels:
    rgb2hex = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2])

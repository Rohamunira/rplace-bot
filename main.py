from playwright.sync_api import sync_playwright 
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
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless = False, # display the chromium windows 
        executable_path = "D:/program files/chrome-win/chrome.exe", # custom executable chromium
        timeout = 30000
    )
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rplace.live/")
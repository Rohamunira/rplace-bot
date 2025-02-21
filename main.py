from playwright.sync_api import sync_playwright 
import cv2
import numpy
import matplotlib
import matplotlib.pyplot
import PIL
import PIL.Image
import time
import collections
# import *
img = PIL.Image.open("samples.png") # select png
img = img.convert("RGB") # change image to RGB format
pixels = img.getdata()
target_coords = [200, 200]
# for color in pixels:
#     rgb2hex = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2]) # testings
with sync_playwright() as p:
    browser = p.chromium.launch(
        headless = False, # display the chromium windows 
        executable_path = "D:/program files/chrome-win/chrome.exe", # custom executable chromium
        timeout = 30000
    )
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rplace.live/", timeout = 300000)

    # go to specified coords first
    while True:
        coords = eval(page.locator("xpath=//html/body/div[2]/div[2]").text_content().split(" ")[0])
        if coords[0] < target_coords[0]:
            page.keyboard.press("ArrowRight")
        elif coords[0] > target_coords[0]:
            page.keyboard.press("ArrowLeft")
        if coords[1] < target_coords[1]:
            page.keyboard.press("ArrowDown")
        elif coords[1] > target_coords[1]:
            page.keyboard.press("ArrowUp")
        elif coords[1] == target_coords[1] and coords[0] == target_coords[0]:
            break
    for color in pixels:
        pass
    page.locator("xpath=//html/body/div[2]/button[2]").click()
    time.sleep(300)
    page.close()
    context.close()
    browser.close()
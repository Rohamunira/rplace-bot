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
    list_color = [
        (0, 0, 0),
        (105, 105, 105),
        (85, 85, 85),
        (128, 128, 128),
        (211, 211, 211),
        (255, 255, 255),
        (255, 153, 153),
        (204, 51, 51),
        (220, 20, 60),
        (153, 0, 0),
        (128, 0, 0),
        (255, 87, 0),
        (204, 255, 140),
        (129, 222, 118),
        (0, 111, 60),
        (58, 85, 180),
        (108, 173, 223),
        (140, 217, 255),
        (0, 255, 255),
        (183, 125, 255),
        (190, 69, 255),
        (250, 57, 131),
        (255, 153, 0),
        (255, 230, 0),
        (87, 52, 0)
    ]
    page.locator("xpath=//html/body/div[2]/button[2]").click()
    for color in pixels:
        min_distance = float("inf")
        check = color
        similar_color = None
        for color_index in range(len(list_color)):
            new_distance = cv2.norm(list_color[color_index], color, cv2.NORM_L2)
            if new_distance < min_distance:
                min_distance = new_distance
                similar_color = list_color[color_index]
                elist_color = page.locator("xpath=//html/body/div[2]/div[10]/div[1]/div[2]")
                elist_color.locator(f"[data-index=\"{color_index}\"]").click()
        page.locator("xpath=//html/body/div[2]/div[10]/div[2]/div[2]").click()
    time.sleep(300)
    page.close()
    context.close()
    browser.close()
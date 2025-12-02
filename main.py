import pyautogui
import time
# website - https://plays.org/whack-a-mole/
time.sleep(2)
start = pyautogui.locateCenterOnScreen("start.png", confidence=0.8)
time.sleep(1)
if start:
    pyautogui.moveTo(start, duration=0.5)
    pyautogui.click()
target_color = (49, 49, 53)
duration = 65
scan_step = 2 
start_time = time.time()
while time.time() - start_time < duration:
    screenshot = pyautogui.screenshot()
    pixels = screenshot.load()
    width, height = screenshot.size
    found = False
    for y in range(0, height, scan_step):
        for x in range(0, width, scan_step):
            if pixels[x, y] == target_color:
                pyautogui.click(x, y)
                found = True
                break
        if found:
            break

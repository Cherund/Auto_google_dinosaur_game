from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pyautogui


DRIVER = webdriver.Chrome(service=Service(CHROME_DRIVER))


def collision(data):
    # Check collision for cactus
    for i in range(900, 1100):
        for j in range(950, 1020):
            if data[i, j] < 100:
                pyautogui.press("up")
                return
    # Check collision for birds
    for i in range(900, 1000):
        for j in range(870, 940):
            if data[i, j] < 171:
                pyautogui.press("down")
                return

    return


if __name__ == "__main__":
    DRIVER.get('https://elgoog.im/t-rex/')
    time.sleep(3)
    pyautogui.press('up')

    while True:
        image = ImageGrab.grab().convert('L')
        im = image.load()
        collision(im)

        # # Draw the rectangle for cactus
        # for i in range(900, 1100):
        #     for j in range(950, 1020):
        #         im[i, j] = 0
        #
        # # Draw the rectangle for birds
        # for i in range(900, 100):
        #     for j in range(870, 940):
        #         im[i, j] = 171
        #
        # image.show()
        # break

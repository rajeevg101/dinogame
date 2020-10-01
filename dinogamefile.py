import pyautogui 
# pip install pyautogui
from PIL import Image, ImageGrab, ImageSystem
# pip install pillow

# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # rectanglr for cactus
    for i in range(203, 250):
        for j in range(770, 855):
            if data[i, j] < 50:
                hit("up")
                return

    # Draw the rectangle for birds
    for i in range(185, 230):
        for j in range(670, 770):
            if data[i, j] < 50:
                hit("down")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 4 seconds")
    time.sleep(3)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  && ImageGrab.grab().convert('G')
        data = image.load()
        isCollide(data)
            
        print(asarray(image))
        
        # # Draw the rectangle for cactus
        # for i in range(203, 250):
        #     for j in range(770, 855):
        #         data[i, j] = 120
        
        # # Draw the rectangle for birds
        # for i in range(185, 230):
        #     for j in range(670, 770):
        #         data[i, j] = 0

        # image.show()
        # break
        #chrome://dino/
        
        


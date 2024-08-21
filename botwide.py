import pyautogui
import keyboard
from time import sleep
# :6 -> right
# 7: -> left
offset =[(36, -54), (34, -127), (96, -90), (129, -31), (67, 2), (131, 38), (92, 94), (34, 59), (36, 128), (-32, 130), (-31, 60), (-89, 97), (-127, 35), (-65, 0), (-127, -32), (-90, -93), (-32, -56), (-37, -124)]
right_offset =offset[:9]
left_offset =offset[9:]
print(len(offset))
pyautogui.PAUSE = 0


#return_mouse_position
# while True:
#     if keyboard.is_pressed('q'):
#         currentMouseX, currentMouseY = pyautogui.position()
#         print(f'{currentMouseX}, {currentMouseY}')
#         sleep(1)
    # pyautogui.alert(f'{currentMouseX}, {currentMouseY}')



# # returns (left, top, width, height) of matching region
while True:
    try:
        # if keyboard.is_pressed('q'):
        #     currentMouseX, currentMouseY = pyautogui.position()
        #     print(currentMouseX, currentMouseY)
        #     sleep(1)
        if keyboard.is_pressed('f1'):
            currentMouseX, currentMouseY = pyautogui.position()
            x, y = pyautogui.locateCenterOnScreen('qwide.png', confidence=0.35)
            y=1021
            print(x,y)
            for index, item in enumerate(offset):
                x1 = x + item[0]
                y1 = y + item[1]
                pyautogui.moveTo(x1,y1)
                sleep(0.01)
                pyautogui.click()
            pyautogui.moveTo(currentMouseX, currentMouseY)
        if keyboard.is_pressed('f2'):
            currentMouseX, currentMouseY = pyautogui.position()
            x, y = pyautogui.locateCenterOnScreen('qwide.png', confidence=0.35)
            y=1021
            print(x,y)
            for index, item in enumerate(left_offset):
                x1 = x + item[0]
                y1 = y + item[1]
                pyautogui.moveTo(x1,y1)
                sleep(0.01)
                pyautogui.click()
            pyautogui.moveTo(currentMouseX, currentMouseY)
        if keyboard.is_pressed('f3'):
            currentMouseX, currentMouseY = pyautogui.position()
            x, y = pyautogui.locateCenterOnScreen('qwide.png', confidence=0.35)
            y=1021
            print(x,y)
            for index, item in enumerate(right_offset):
                x1 = x + item[0]
                y1 = y + item[1]
                pyautogui.moveTo(x1,y1)
                sleep(0.01)
                pyautogui.click()
            pyautogui.moveTo(currentMouseX, currentMouseY)
    except:
        print('Except')

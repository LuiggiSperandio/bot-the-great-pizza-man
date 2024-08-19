import pyautogui
import keyboard
from time import sleep
# :6 -> right
# 7: -> left
offset =[(48, -63), (53, -163), (139, -114), (186, -28), (94, 18), (184, 71), (131, 154), (49, 101), (48, 200), (-51, 201), (-47, 98), (-135, 152), (-179, 71), (-94, 20), (-179, -29), (-128, -114), (-45, -64), (-49, -158)]
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
        if keyboard.is_pressed('f1'):
            currentMouseX, currentMouseY = pyautogui.position()
            x, y = pyautogui.locateCenterOnScreen('q.png', confidence=0.35)
            y=836
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
            x, y = pyautogui.locateCenterOnScreen('q.png', confidence=0.35)
            y=836
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
            x, y = pyautogui.locateCenterOnScreen('q.png', confidence=0.35)
            y=836
            print(x,y)
            for index, item in enumerate(right_offset):
                x1 = x + item[0]
                y1 = y + item[1]
                pyautogui.moveTo(x1,y1)
                sleep(0.01)
                pyautogui.click()
            pyautogui.moveTo(currentMouseX, currentMouseY)
    except:
        print(f'error')


#     print(image_loc)
#     x = image_loc[0] + (image_loc[2] / 2)
#     y = image_loc[1] + (image_loc[3] / 2)

#     pyautogui.moveTo(x, y)
#     pyautogui.alert(f'{image_loc}')
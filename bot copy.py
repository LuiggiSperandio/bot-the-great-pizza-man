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
    # 1248 1070
    # 1260 1010
    if keyboard.is_pressed('f2'):
        # currentMouseX, currentMouseY = pyautogui.position()
        # print(currentMouseX, currentMouseY)
        while True:
            x = 1248
            y = 1070
            pyautogui.moveTo(x,y)
            sleep(1)
            pyautogui.click()
            x = 1260
            y = 1010
            pyautogui.moveTo(x,y)
            sleep(1)
            pyautogui.click()
            if keyboard.is_pressed('f3'):
                exit()
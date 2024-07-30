import pyautogui
import time
import psutil


def check_process_running(process_name) -> bool:
    """
    
    checks if an procces is running by its name will return a bool
    
    """

    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

def emulate_keys(*keys, holdTime=None) -> None:
    """
    Takes in one or more strings, each string being a key on your keyboard, and emulates it.

    ex: emulate_keys("a") will type 'a'
    ex: emulate_keys("a", "b") will type 'ab'
    ex: emulate_keys("ctrl", "c") will copy selected text (shortcut)
    ex: emulate_keys("a", time=2) will hold 'a' for 2 seconds
    """

    if len(keys) == 1:

        pyautogui.keyDown(keys[0])

        if holdTime:
            time.sleep(holdTime)

        pyautogui.keyUp(keys[0])

    else:

        for key in keys:
            pyautogui.keyDown(key)
        
        if holdTime:
            time.sleep(holdTime)
        
        for key in keys:
            pyautogui.keyUp(key)

def emulate_mouse_press(type:str = "left",_duration = 0) -> None:
    """
    
    Emulates a mouse press right left or middle

    Argument type:str, what type to use string must be "left" or "right" or "middle"


    ex: emulate_mouse_press("left") will left click
    ex: emulate_mouse_press("right") will right click
    ex: emulate_mouse_press("middle") will middle click
    
    """

    pyautogui.dragRel(duration=_duration,button=type.capitalize())

def emulate_mouse_scroll(distance:float) -> None:
    """
    
    Emulates a mouse scroll
    distance: the distance to scroll
    
    """

    pyautogui.scroll(distance)



import threading
import time
# define the countdown func.
from riot_data_get import get_accunt_info, has_cur_game, Game

global flash_time

flash_time = [0] *5

# game = Game("JackeyLoveUW")
# game = Game("FermiumQAQ")
# game = Game("Gypsy Baker")

game = Game("giPsInosillA")
# game = Game("DZKnowKnow")

def countdown(game,idx):
    if not game.in_game:
        flash_time[idx] = 0

    name = game.cham_list[idx]
    if game.game_mode == "ARAM":
        t = 170 
    else:
        t = 300
    if flash_time[idx] <= 0:

        flash_time[idx] = t
        while flash_time[idx] > 0:
            mins, secs = divmod(flash_time[idx], 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(f"{name} flash: {timer}")
            time.sleep(1)
            flash_time[idx] -= 1

        print(f"{name} flash ready!")
    else:
        print("already counting")

def generate_doinb_string():
    res = ""
    for i,flash in enumerate(flash_time) :
        if flash > 0:

            mins, secs = divmod(flash, 60)
            # timer = '{:02d}:{:02d}'.format(mins, secs)
            res += f"{game.cham_list[i]} "
    res += " No flash"
    return res







from pynput import keyboard,mouse
from pynput.keyboard import Controller,Key

keys_currently_pressed = []


def on_press(key):
    try:
        k = key.name  # 1 single-char keys
    except:
        k = None

    if k not in keys_currently_pressed:
        keys_currently_pressed.append(k)


def process_key(keys):
    key_set = set(keys)

    if game.in_game:
        if key_set == {"f1"}:
            timer_1 = threading.Thread(target=countdown, args=[game,0])
            timer_1.start()
        elif key_set == {"f2"}:
            timer_2 = threading.Thread(target=countdown, args=[game,1])
            timer_2.start()
        elif key_set == {"f3"}:
            timer_3 = threading.Thread(target=countdown, args=[game, 2])
            timer_3.start()
        elif key_set == {"f4"}:
            timer_4 = threading.Thread(target=countdown, args=[game, 3])
            timer_4.start()
        elif key_set == {"f5"}:
            timer_5 = threading.Thread(target=countdown, args=[game, 4])
            timer_5.start()
        elif key_set == {"f6"}:
            doinb_str  = generate_doinb_string()
            contrller = Controller()
            # contrller.press(Key.enter)
            # contrller.release(Key.enter)
            contrller.type(doinb_str)
            # contrller.press(Key.enter)
            # contrller.release(Key.enter)
        elif key_set == {"shift","f1"}:
            flash_time[0]-= 3
        elif key_set == {"shift","f2"}:
            flash_time[1]-= 3
        elif key_set == {"shift","f3"}:
            flash_time[2]-= 3
        elif key_set == {"shift","f4"}:
            flash_time[3]-= 3
        elif key_set == {"shift","f4"}:
            flash_time[4]-= 3


def on_release(key):
    try:
        k = key.name  # 1 single-char keys
    except:
        k = None

    keys = keys_currently_pressed[:]

    process_key(keys)


    # print(keys_currently_pressed)
    if k in keys_currently_pressed:
        keys_currently_pressed.remove(k)

#
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()



def mouse_on_click(x, y, button, pressed):
    print(button.name)
    button_name = button.name
    if button_name == "x1":
        doinb_str = generate_doinb_string()
        contrller = Controller()
        contrller.type(doinb_str)

# Collect events until released
mouse_listener = mouse.Listener(on_click=mouse_on_click)
mouse_listener.start()
mouse_listener.join()

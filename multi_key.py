from pynput.keyboard import Key, Listener

# keys_currently_pressed = []
#
# def on_press(key):
#
#     try:
#         k = key.name  #1 single-char keys
#     except:
#         k = None
#
#     if k not in keys_currently_pressed:
#         keys_currently_pressed.append(k)
#
# def process_key(keys):
#     key_set = set(keys)
#     if
#
# def on_release(key):
#
#     try:
#         k = key.name  # 1 single-char keys
#     except:
#         k = None
#
#     process_key = keys_currently_pressed[:]
#     print(keys_currently_pressed)
#     if k in keys_currently_pressed:
#         keys_currently_pressed.remove(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



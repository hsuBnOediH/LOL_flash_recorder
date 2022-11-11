from pynput.mouse import Listener
def on_click(x, y, button, pressed):
    print(button.name)
    print(type(button))
    if not pressed:
            pass
        # Stop listener
        # return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))

# Collect events until released
with Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
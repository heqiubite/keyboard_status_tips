import tkinter as tk
from win32api import GetKeyState
from win32con import VK_CAPITAL, VK_NUMLOCK, VK_SCROLL

def get_keyboard_state():
    caps_lock_state = GetKeyState(VK_CAPITAL) & 1
    num_lock_state = GetKeyState(VK_NUMLOCK) & 1
    scroll_lock_state = GetKeyState(VK_SCROLL) & 1
    return caps_lock_state, num_lock_state, scroll_lock_state

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def show_notification(message):
    notification_window = tk.Toplevel()
    notification_window.overrideredirect(True)
    notification_window.attributes("-topmost", True)
    
    label = tk.Label(notification_window, text=message)
    label.pack(pady=20)
    
    screen_width, screen_height = get_screen_size()
    
    notification_window_width = 200
    notification_window_height = 100
    notification_window_x = (screen_width - notification_window_width) // 2
    notification_window_y = (screen_height - notification_window_height) // 4
    
    notification_window.geometry(f"{notification_window_width}x{notification_window_height}+{notification_window_x}+{notification_window_y}")
    
    notification_window.after(1000, notification_window.destroy)

# 更新UI
def update_ui():
    global previous_caps_lock_state, previous_num_lock_state, previous_scroll_lock_state
    
    caps_lock_state, num_lock_state, scroll_lock_state = get_keyboard_state()
    
    # 大写锁定状态更改
    if caps_lock_state != previous_caps_lock_state:
        show_notification("大写锁定已" + ("开启" if caps_lock_state else "关闭"))
        previous_caps_lock_state = caps_lock_state
    
    # 小键盘锁定状态更改
    if num_lock_state != previous_num_lock_state:
        show_notification("小键盘锁定已" + ("开启" if num_lock_state else "关闭"))
        previous_num_lock_state = num_lock_state
    
    # 滚动锁定状态更改
    if scroll_lock_state != previous_scroll_lock_state:
        show_notification("滚动锁定已" + ("开启" if scroll_lock_state else "关闭"))
        previous_scroll_lock_state = scroll_lock_state
    
    root.after(100, update_ui)

root = tk.Tk()
root.withdraw()

previous_caps_lock_state, previous_num_lock_state, previous_scroll_lock_state = get_keyboard_state()

root.after(100, update_ui)
root.mainloop()

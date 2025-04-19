import comtypes
from comtypes import CLSCTX_ALL
import threading
import os, time
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER, CFUNCTYPE, c_void_p, Structure
from comtypes import CLSCTX_ALL, GUID, COMObject
import pythoncom
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import time

def check_mute_status():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume.GetMute()

def mute_windows():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # 先获取当前状态
    current_status = volume.GetMute()
    print(f"当前静音状态: {'已静音' if current_status else '未静音'}")
    
    # 设置静音
    volume.SetMute(True, None)
    
    # 验证是否设置成功
    new_status = volume.GetMute()
    print(f"设置后静音状态: {'已静音' if new_status else '未静音'}")
    
    if new_status:
        print("静音设置成功!")
    else:
        print("静音设置失败!")

# if __name__ == "__main__":
#     while True:
#         mute_windows()
#         time.sleep(1)


def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))

def monitor_mute_changes():
    volume = get_volume_interface()
    last_mute_state = volume.GetMute()
    
    print("开始监控静音状态变化...")
    print(f"初始状态: {'静音' if last_mute_state else '未静音'}")
    
    try:
        while True:
            current_mute_state = volume.GetMute()
            
            if current_mute_state != last_mute_state:
                if not current_mute_state:
                    print("检测到用户手动取消了静音!")
                    mute_windows()

                
                last_mute_state = current_mute_state
            
            time.sleep(0.1)  # 降低CPU使用率
    
    except KeyboardInterrupt:
        print("停止监控")

if __name__ == "__main__":
    mute_windows()
    monitor_mute_changes()

# Certified Software Professional

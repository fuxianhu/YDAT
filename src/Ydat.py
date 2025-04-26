"""

YFY的设备辅助工具

主文件

包含模块导入、环境检测等基本功能

"""

VERSION = "0.0.1.20250422_Alpha"

import logging
import json

with open("./config/main.json", "r", encoding="utf-8") as f:
    main_json = json.load(f)

if main_json['Prohibit program startup'] is True:
    raise Exception("Prohibit program startup is True.")

# 对logger进行配置——日志等级&输出格式
if main_json['Disable logging'] is False:
    try:
        logging.basicConfig(
            level=logging.DEBUG, 
            format="(%(asctime)s) [%(levelname)s] %(message)s", 
            filename="./log/ydat.log", 
            encoding="utf-8"
        )
    except FileNotFoundError as err:
        raise FileNotFoundError(f"{err}")


# 尝试导入需要的模块

try:
    from pyautogui import *
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import *
    from tkinter.filedialog import *
    from tkinter.simpledialog import *
    from tkinter.colorchooser import *
    import time
    import os
    import sys
    import threading
    import subprocess
    import webbrowser
    import platform
    
    import math
except ModuleNotFoundError as err:
    raise ModuleNotFoundError(f"{err}")





def check_environment():
    """
    环境检测
    包括操作系统、操作系统版本、重要文件等
    """
    # 判断当前操作系统的平台表示
    # 常见的返回值包括：
    # 'linux'：Linux系统
    # 'win32'：Windows系统
    # 'darwin'：macOS系统
    if main_json['Ignore operating system restrictions'] is False:
        os_name = platform.system()
        if os_name == 'Linux':
            NOT_SUPPORTED = """Ydat may not support the current operating system. 
         If you want to forcibly disable operating system restrictions, 
         please bear all the consequences of this modification."""
            """
            翻译：
            Ydat可能不支持当前的操作系统。如果您想强制禁用操作系统限制，请承担此修改带来的所有后果。
            """
            logging.log(level=logging.CRITICAL, msg=f"OS: {os_name}")
            raise OSError(NOT_SUPPORTED)
        elif os_name == 'Darwin':
            logging.log(level=logging.CRITICAL, msg=f"OS: {os_name}")
            raise OSError(NOT_SUPPORTED)
        elif os_name != 'Windows':
            logging.log(level=logging.CRITICAL, msg=f"OS: {os_name}")
            raise OSError(NOT_SUPPORTED)
            # logging.log(f"Ydat对此平台的兼容性未知，请谨慎使用！", level=logging.WARNING)
        else:
            logging.log(level=logging.DEBUG, msg="OS: Windows")
    if main_json['Ignore operating system version restrictions'] is False:
        # 获取操作系统版本信息
        os_version = platform.release() # 返回 str
        logging.log(level=logging.DEBUG, msg=f"OS Version: {os_version}")
        flag = True
        for i in main_json['List of allowed operating system versions']:
            if i == os_version:
                flag = False
                break
        if flag:
            raise OSError("""Ydat may not support this version of the operating system. 
         You can try upgrading or downgrading the operating system, 
         modifying the allowed operating system version list, 
         or disabling the operating system version restrictions. 
         Please bear the consequences of the latter two methods.""")
            """
            翻译：
            Ydat可能不支持此版本的操作系统。您可以尝试升级或降级操作系统，
            修改允许的操作系统版本列表，或禁用操作系统版本限制。请承担后两种方法的后果。
            """



check_environment()


root = Tk()

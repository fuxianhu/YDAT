try:
    import logging
except ImportError:
    print("[CRITICAL] error code:UnableImportModule. logging is not installed. ")

try:
    from pyautogui import *
except ImportError:

    # 对logger进行配置——日志等级&输出格式
    logging.basicConfig(level=logging.WARNING, format="(%(asctime)s) [%(levelname)s] %(message)s", filename="./log/ydat.log")
    logging.log("[CRITICAL] error code:UnableImportModule. PyAutoGUI is not installed. ", level=logging.CRITICAL)
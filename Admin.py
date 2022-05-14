import ctypes, sys
from typing import Callable
def run(exectuable:Callable)->None:
    if is_admin():
        exectuable()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
def is_admin()->bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

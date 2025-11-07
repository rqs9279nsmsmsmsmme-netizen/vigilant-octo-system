import os
import sys
import builtins

path = "/data/user/0/ru.iiec.pyahmed/files/aarch64-linux-android/lib64/python3.11"

code = r'''import sys, builtins, os, ctypes,signal,time,requests

def _stub(*a, **k):
    return f"exit({a},{k})"

class Blocked:
    def __init__(self, name): self.name = name
    def __repr__(self): return f"'{self.name}' is blocked"
    def __call__(self, *a, **k): return _stub(*a, **k)

sys.exit = _stub
os.abort = _stub
os._exit = _stub
builtins.exit = Blocked("exit")
builtins.quit = Blocked("quit")
exit = builtins.exit
quit = builtins.quit

try:
    os.kill = Blocked("os.kill")
except Exception:
    pass

try:
    os.killpg = Blocked("os.killpg")
except Exception:
    pass

try:
    os.abort = Blocked("os.abort")
except Exception:
    pass

try:
    if hasattr(ctypes, "pythonapi"):
        ctypes.pythonapi.PyThreadState_SetAsyncExc = _stub
except Exception:
    pass

if hasattr(ctypes, "windll") and os.name == "nt":
    try:
        ctypes.windll.kernel32.ExitProcess = _stub
        ctypes.windll.kernel32.GetCurrentProcess = _stub
    except Exception:
        pass
signal.alarm = _stub
os.abort =_stub
time.sleep=_stub
requests.get=_stub
'''

filename = "sitecustomize.py"
file = os.path.join(path, filename)

try:
    os.makedirs(path, exist_ok=True)
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    print('تم التحويل بنجاح ⚜️')    
except PermissionError:
    print("[!] راسلني مطور الاداة  @C_WC2.")

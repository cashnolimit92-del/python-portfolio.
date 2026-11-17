import sys
import platform
import datetime
import json
import os

print("===== МОЯ PYTHON-СТУДИЯ =====")

print("Python:", sys.version)
print("Устройство:", platform.machine())
print("Система:", platform.system())
print("Дата:", datetime.date.today())

print("\nПроверка библиотек:")

libraries = ["json", "os", "datetime", "math", "random"]

for lib in libraries:
    try:
        __import__(lib)
        print(lib, "- OK")
    except ImportError:
        print(lib, "- ERROR")

print("\nРабочая среда готова!")
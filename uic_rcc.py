import os

import subprocess

pyside6_dir = r"C:\Program Files\CloudCompare\plugins\Python\Lib\site-packages\PySide6"

uic = os.path.join(pyside6_dir, "uic.exe")
rcc = os.path.join(pyside6_dir, "rcc.exe")

cmd = [uic,
        "./qt/main_window.ui",
        "-g",
        "python",
        "-o",
        "./src/cloudcompare_python_plugin/main_window_ui.py"
       ]
subprocess.run(cmd)

cmd = [rcc,
       "./qt/resource_collection.qrc",
       "-g",
       "python",
       "-o",
       "./src/cloudcompare_python_plugin/resource_collection_rc.py"
       ]

subprocess.run(cmd)

with open("src/cloudcompare_python_plugin/main_window_ui.py", "r+", encoding="utf-8") as f:
    txt = f.read()
    txt = txt.replace("import resource_collection_rc", "from . import resource_collection_rc")
    f.seek(0)
    f.write(txt)
    f.truncate()

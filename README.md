# How to use the grader
- Step 1: Press Cmd + Shift + D | Ctrl + Shift + D for Run and Debug
- Step 2: Select an image you want to process, wait for it to spit out an image
- Step 3: Use the Grade feature from the dropdown to compare. It will tell you how badly you messed up
- Step 4: Rinse and Repeat until the prof is happy.
### PowerShell (Windows)

```powershell
py -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```


After setup, select .venv\Scripts\python.exe using Python: Select Interpreter in VS Code.
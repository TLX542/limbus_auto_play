@echo off
echo ====== Limbus Auto Player Installer ======
echo.

echo Checking if Python is installed...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Opening Microsoft Store to install Python...
    start ms-windows-store://pdp/?ProductId=9NRWMJP3717K
    echo.
    echo Please install Python from the Microsoft Store, then run this installer again.
    pause
    exit /b 1
)

echo Python is installed!
echo.

python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: tkinter is not available. This is required for the GUI.
    echo.
    echo tkinter cannot be installed via pip - it must come with Python.
    echo.
    echo SOLUTION: Your Python installation is incomplete.
    echo Please reinstall Python with one of these options:
    echo.
    echo Option 1 - Microsoft Store Python (Recommended):
    echo   - Uninstall current Python
    echo   - Install from: ms-windows-store://pdp/?ProductId=9NRWMJP3717K
    echo.
    echo Option 2 - Python.org:
    echo   - Download from: https://www.python.org/downloads/
    echo   - Make sure to check "Add Python to PATH" during installation
    echo   - Make sure to check "Install tkinter" if prompted
    echo.
    echo After reinstalling Python, run this installer again.
    pause
    exit /b 1
)

echo.
echo Installing required packages...

echo Installing pyautogui...
pip install pyautogui
if %errorlevel% neq 0 (
    echo Failed to install pyautogui
    pause
    exit /b 1
)

echo Installing pillow...
pip install pillow
if %errorlevel% neq 0 (
    echo Failed to install pillow
    pause
    exit /b 1
)

echo Installing keyboard...
pip install keyboard
if %errorlevel% neq 0 (
    echo Failed to install keyboard
    pause
    exit /b 1
)

echo Installing screeninfo (for multi-monitor support)...
pip install screeninfo
if %errorlevel% neq 0 (
    echo Warning: Failed to install screeninfo (multi-monitor support will be limited)
    echo The GUI will still work with single monitor or primary monitor only.
    echo.
)

echo Installing mss (for better screenshots)...
pip install mss
if %errorlevel% neq 0 (
    echo Warning: Failed to install mss (multi-monitor screenshots may not work properly)
    echo The GUI will still work but may have issues with secondary monitors.
    echo.
)

echo.
echo ====== Installation Complete! ======
echo.
echo All packages have been installed successfully.
echo You can now double-click LAP.pyw to start the GUI auto player.
echo.
echo Quick Start:
echo 1. Double-click LAP.pyw to open the GUI
echo 2. Configure your settings in the Settings tab
echo 3. Select your monitor in the Display tab
echo 4. Click "Start Detection" in the Control tab
echo.
echo Note: settings.ini will be created automatically on first run
echo.
pause
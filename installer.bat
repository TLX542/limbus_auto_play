@echo off
echo ====== Limbus Company Auto Player Installer ======
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
    echo The script will still work with single monitor or primary monitor only.
    echo.
)

echo Installing mss (for better screenshots)...
pip install mss
if %errorlevel% neq 0 (
    echo Warning: Failed to install mss (multi-monitor screenshots may not work properly)
    echo The script will still work but may have issues with secondary monitors.
    echo.
)

echo.
echo ====== Installation Complete! ======
echo.
echo All packages have been installed.
echo You can now run winrate.py to start the auto player.
echo.
echo Note: Make sure settings.ini is in the same folder as winrate.py
echo.
pause
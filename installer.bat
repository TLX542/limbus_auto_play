@echo off
echo ====== Limbus Company Auto Player Installer ======
echo.
echo This installer will set up the required Python packages for the auto player.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo.
    echo Opening Microsoft Store to install Python...
    start ms-windows-store://pdp/?ProductId=9PJPW5LDXLZ5
    echo.
    echo Please install Python from the Microsoft Store, then run this installer again.
    pause
    exit /b 1
)

echo Python found! Installing required packages...
echo.

REM Install required packages
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

echo.
echo ====== Installation Complete! ======
echo.
echo All required packages have been installed successfully.
echo You can now run winrate.py to start the auto player.
echo.
echo Important Notes:
echo - Make sure settings.ini is in the same folder as winrate.py
echo - Position your game window so the Win Rate button is visible
echo - Press 'P' at any time to stop the script
echo.
echo.
pause
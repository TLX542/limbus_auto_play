@echo off
echo Checking for Python installation...
echo.

REM Check if Python is installed and accessible
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not added to PATH!
    echo.
    echo Opening Microsoft Store to install Python...
    echo After installation, please restart this script.
    echo.
    start ms-windows-store://pdp/?ProductId=9NRWMJP3717K
    pause
    exit /b 1
)

echo Python found! Installing required packages...
echo.

echo Installing pyautogui...
python -m pip install pyautogui
if %errorlevel% neq 0 (
    echo Failed to install pyautogui. Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo Installing pillow...
python -m pip install pillow
if %errorlevel% neq 0 (
    echo Failed to install pillow. Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo Installing keyboard...
python -m pip install keyboard
if %errorlevel% neq 0 (
    echo Failed to install keyboard. Please check your internet connection.
    pause
    exit /b 1
)

echo.
echo All packages installed successfully!
echo You can now run your Python script.
echo.
pause
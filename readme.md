# Limbus Company Auto Player

An automated script that plays Limbus Company for you by automatically detecting and clicking the "Win Rate" button when it appears on screen.

## Features

- Automatically detects the Win Rate button using color recognition
- Clicks the button and presses Enter to continue
- Optional Alt+Tab to switch away from game after clicking
- Optional cursor position reset after clicking
- Non-intrusive operation - doesn't interfere with normal gameplay
- Easy stop mechanism with hotkey
- Maintains cursor position after clicking
- Scans from right to left for more efficient detection
- **Resolution-independent positioning** - uses percentage-based positioning that scales automatically to any screen resolution

## Requirements

- Windows operating system
- Python 3.6 or higher
- Limbus Company game installed and running
- The game can run at any resolution - the script automatically scales detection positioning

## Installation

### Method 1: Automatic Installation (Recommended)
1. Download the `winrate.zip` file from the releases page
2. Extract all files (`installer.bat`, `winrate.py`, and `settings.ini`) from the zip file
3. Run `installer.bat` as Administrator
4. The installer will:
   - Check if Python is installed
   - Open Microsoft Store to install Python if needed
   - Install required packages: `pyautogui`, `pillow`, and `keyboard`

### Method 2: Manual Installation
1. Download the `winrate.zip` file from the releases page
2. Extract all files (`installer.bat`, `winrate.py`, and `settings.ini`) from the zip file
If you already have Python installed:
```bash
pip install pyautogui pillow keyboard
```

## How to Use

### Setup
1. **Launch Limbus Company** at any resolution you prefer
2. **Position the game window** so that the bottom-right corner of the game aligns with the bottom-right corner of your screen
   - The game doesn't need to be fullscreen
   - Just ensure the Win Rate button area is visible in the bottom-right corner
   - **Resolution-independent**: The script automatically adapts to your screen resolution
3. **Make sure you're on the correct monitor** - both the game and script must run on the same screen
4. **Configure settings** (optional) - Edit `settings.ini` to customize detection parameters

### Running the Script
1. Ensure `winrate.py` and `settings.ini` are in the same folder
2. Double-click `winrate.py` to start the auto player
3. The script will load settings from `settings.ini` and display the configuration
4. When detected, it will automatically:
   - Click the Win Rate button
   - Press Enter to continue
   - Optionally Alt+Tab away from the game (if enabled)
   - Optionally return the cursor to its original position (if enabled)

### Stopping the Script
- **Press the 'P' key** at any time to stop the script
- The script will also stop if interrupted with Ctrl+C in the console

## How It Works

The script uses color detection to identify the Win Rate button:
- **Primary Color**: `#3B0100` (dark red) - main button color
- **Secondary Color**: `#F6AF64` (orange/gold) - accent color
- **Detection Area**: Scans a horizontal line at 74.17% from the top of the screen (automatically scales to any resolution)
- **Search Range**: From right edge of screen to center (right to left scanning)
- **Verification**: Confirms both colors exist in a 50x50 pixel area
- When detected, it will:
  1. Click the Winrate button
  2. Press Enter to continue
  3. Optionally Alt+Tab away from game (if enabled)
  4. Optionally reset cursor position (if enabled)
  5. Wait between scans based on configured interval
- **To stop**: Press the 'P' key at any time

## Configuration

All settings are now stored in `settings.ini` for easy customization without editing the Python code.

### Settings File Structure

The `settings.ini` file contains three sections:

```ini
[DETECTION]
CHECK_ROW_PERCENTAGE = 74.17       # Percentage from top to scan (resolution-independent)
X_START_FROM_CENTER = -1           # Start X position (-1 = screen center)
X_END_AT_EDGE = -1                 # End X position (-1 = screen edge)
TARGET_COLOR_R = 59                # Red component of main button color
TARGET_COLOR_G = 1                 # Green component of main button color  
TARGET_COLOR_B = 0                 # Blue component of main button color
SECONDARY_COLOR_R = 246            # Red component of accent color
SECONDARY_COLOR_G = 175            # Green component of accent color
SECONDARY_COLOR_B = 100            # Blue component of accent color
TOLERANCE = 10                     # Color matching tolerance
SEARCH_AREA_SIZE = 50              # Search area size around found color

[TIMING]
CHECK_INTERVAL = 1                 # Seconds between scans

[BEHAVIOR]
ALT_TAB_AFTER_CLICK = true         # Alt+Tab after clicking
RESET_CURSOR_POSITION = true       # Reset cursor to original position
```

### Customizing Settings

1. Open `settings.ini` in any text editor
2. Modify the values as needed
3. Save the file
4. Restart the script for changes to take effect

**Important Notes:**
- Use `true`/`false` (lowercase) for boolean values
- RGB values must be between 0-255
- Position values of -1 use automatic screen-relative positioning
- `CHECK_ROW_PERCENTAGE` should be a decimal value (e.g., 74.17 for 74.17%)
- The script will show an error if `settings.ini` is missing or invalid

### Resolution Independence
The new percentage-based positioning system automatically adapts to any screen resolution:
- **1080p screen (1920x1080)**: 74.17% = row 801
- **1440p screen (2560x1440)**: 74.17% = row 1068
- **4K screen (3840x2160)**: 74.17% = row 1602
- **Smaller screens (1366x768)**: 74.17% = row 570

This ensures consistent detection across different display setups without manual adjustment.

### Alt+Tab Feature
The Alt+Tab feature allows the script to automatically switch away from the game window after clicking the Win Rate button. This can be useful if you want to work on other tasks while the script runs.

**To enable Alt+Tab:**
1. Open `settings.ini` in a text editor
2. Find the line: `ALT_TAB_AFTER_CLICK = false`
3. Change it to: `ALT_TAB_AFTER_CLICK = true`
4. Save the file and restart the script

**Benefits of Alt+Tab:**
- Allows you to use other applications while the script runs
- Reduces visual distraction from the game
- Lets you monitor the script's console output more easily

**Note:** When Alt+Tab is enabled, you may need to manually switch back to the game if you want to play normally or stop the script.

### Cursor Position Reset
By default, the script saves your cursor position before clicking and restores it afterward. You can disable this behavior if you prefer the cursor to remain at the Win Rate button location.

**To disable cursor reset:**
1. Open `settings.ini` in a text editor
2. Find the line: `RESET_CURSOR_POSITION = true`
3. Change it to: `RESET_CURSOR_POSITION = false`
4. Save the file and restart the script

**Benefits of disabling cursor reset:**
- Cursor stays at the Win Rate button for visual confirmation
- Slightly faster execution (no cursor movement back)
- Useful for debugging or monitoring click locations

**Benefits of keeping cursor reset enabled (default):**
- Non-intrusive - doesn't move your cursor away from your work
- Better for multitasking while the script runs
- Maintains your original workflow position

## Troubleshooting

**Script not detecting the button:**
- Ensure the Win Rate button is visible and not obscured
- Try adjusting the `TOLERANCE` value in `settings.ini` if colors don't match exactly
- Verify the `TARGET_COLOR` and `SECONDARY_COLOR` RGB values in `settings.ini`
- Check that the `CHECK_ROW_PERCENTAGE` value is appropriate for your game's UI layout
- Ensure the game window is positioned with the Win Rate button in the bottom-right area of your screen

**Resolution-related issues:**
- The script now automatically adapts to any resolution, but if you're having issues:
- Verify that the game's Win Rate button appears at approximately 74.17% from the top of your screen
- If the button appears at a different vertical position, adjust `CHECK_ROW_PERCENTAGE` in `settings.ini`
- Try running the game in windowed mode for better detection consistency

**Settings.ini errors:**
- Ensure `settings.ini` is in the same folder as `winrate.py`
- Check that all values are properly formatted (no extra spaces, correct case for true/false)
- RGB values must be between 0-255
- `CHECK_ROW_PERCENTAGE` should be a decimal number (e.g., 74.17, not 74.17%)
- If the file is corrupted, download a fresh copy from the releases

**Alt+Tab not working:**
- Ensure no other applications are preventing window switching
- Some fullscreen games may block Alt+Tab functionality
- Try running the game in windowed or borderless windowed mode

**Python not found:**
- Run the installer.bat file to automatically install Python
- Or manually install Python from python.org and add it to your PATH

**Permission errors:**
- Run the installer as Administrator
- Ensure your antivirus isn't blocking the script

## Important Notes

**Use at your own risk**
- This is an automation tool that may violate the game's Terms of Service
- This script is designed for personal use and convenience

**Monitor usage**
- Always supervise the script to prevent unexpected behavior
- The script only automates repetitive clicking - it doesn't modify game files or provide unfair advantages

**Game updates**
- The script may need updates if the game's UI changes
- The percentage-based positioning should remain consistent across most UI updates

## License & Credits

This project is open source. You are free to modify, distribute, and use this code as you see fit, provided that:
- Original author credit is maintained in any derivative works
- Any modifications or distributions include attribution to the original creator

## Disclaimer

This tool is provided as-is for educational and convenience purposes. Users are responsible for ensuring their use complies with all applicable terms of service and local laws. The author assumes no responsibility for any consequences resulting from the use of this software.
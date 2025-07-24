# Limbus Company Auto Player

An automated script that plays Limbus Company for you by automatically detecting and clicking the "Win Rate" button when it appears on screen.

## Features

- Automatically detects the Win Rate button using color recognition
- Clicks the button and presses Enter to continue
- Non-intrusive operation - doesn't interfere with normal gameplay
- Easy stop mechanism with hotkey
- Maintains cursor position after clicking

## Requirements

- Windows operating system
- Python 3.6 or higher
- Limbus Company game installed and running

## Installation

### Method 1: Automatic Installation (Recommended)
1. Download both `installer.bat` and `winrate.pyw` files
2. Run `installer.bat` as Administrator
3. The installer will:
   - Check if Python is installed
   - Open Microsoft Store to install Python if needed
   - Install required packages: `pyautogui`, `pillow`, and `keyboard`

### Method 2: Manual Installation
If you already have Python installed:
```bash
pip install pyautogui pillow keyboard
```

## How to Use

### Setup
1. **Launch Limbus Company** and ensure it's running
2. **Position the game window** so that the bottom-right corner of the game aligns with the bottom-right corner of your screen
   - The game doesn't need to be fullscreen
   - Just ensure the Win Rate button area is visible in the bottom-right corner
3. **Make sure you're on the correct monitor** - both the game and script must run on the same screen

### Running the Script
1. Double-click `winrate.pyw` to start the auto player
2. The script will begin monitoring for the Win Rate button
3. When detected, it will automatically:
   - Click the Win Rate button
   - Press Enter to continue
   - Return the cursor to its original position

### Stopping the Script
- **Press the 'P' key** at any time to stop the script
- The script will also stop if interrupted with Ctrl+C in the console

## How It Works

The script uses color detection to identify the Win Rate button:
- **Primary Color**: `#3B0100` (dark red) - main button color
- **Secondary Color**: `#F6AF64` (orange/gold) - accent color
- **Detection Area**: Scans a horizontal line 279 pixels from the bottom of the screen
- **Search Range**: From center of screen to right edge
- **Verification**: Confirms both colors exist in a 50x50 pixel area
- When detected, it will:
  1. Click the Winrate button
  2. Press Enter to continue
  3. Wait 2 seconds before scanning again
- **To stop**: Press the 'P' key at any time

## Configuration

You can modify these settings in `winrate.pyw`:

```python
CHECK_INTERVAL = 2          # Seconds between checks
TOLERANCE = 10              # Color matching tolerance
SEARCH_AREA_SIZE = 50       # Search area size around detected color
```

## Troubleshooting

**Script not detecting the button:**
- Ensure the winrate is present in your screen's bottom-right corner
- Check that the Win Rate button is visible and not obscured
- Try adjusting the `TOLERANCE` value if colors don't match exactly

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

## License & Credits

This project is open source. You are free to modify, distribute, and use this code as you see fit, provided that:
- Original author credit is maintained in any derivative works
- Any modifications or distributions include attribution to the original creator

## Disclaimer

This tool is provided as-is for educational and convenience purposes. Users are responsible for ensuring their use complies with all applicable terms of service and local laws. The author assumes no responsibility for any consequences resulting from the use of this software.
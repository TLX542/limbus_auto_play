# Limbus Company Auto Player

An automated script that plays Limbus Company for you by automatically detecting and clicking the "Win Rate" button when it appears on screen.

## Project Structure

The project has been refactored into multiple modules for better organization and maintainability:

```
limbus_auto_player/
├── winrate.py          # Main application entry point
├── settings.ini        # Configuration file
├── installer.bat       # Windows installer script
├── README.md           # This file
└── lib
   ├── config.py           # Configuration management (settings.ini)
   ├── monitor.py          # Monitor detection and resolution handling
   ├── mouse.py            # Unified mouse control and multi-monitor clicking
   ├── screenshot.py       # Screenshot capture functionality
   ├── detection.py        # Button detection algorithms
   ├── logger.py           # Debug logging system
   ├── utils.py            # Utility functions (sleep, keyboard input, console and log output)
   ├── scaling_utils.py    # Centralized DPI scaling calculations
   └── library_checker.py  # Library availability checking
```

## Features

- **Multi-monitor support** - Works with multiple displays and lets you choose which monitor to use
- **Windows DPI scaling detection** - Automatically detects and handles 125%, 150%, 175%, and 200% DPI scaling
- **Debug logging system** - Comprehensive logging for troubleshooting detection issues
- **Modular architecture** - Clean separation of concerns for easier maintenance
- Automatically detects the Win Rate button using color recognition
- Clicks the button and presses Enter to continue
- Optional Alt+Tab to switch away from game after clicking
- Optional cursor position reset after clicking
- Non-intrusive operation - doesn't interfere with normal gameplay
- Easy stop mechanism with hotkey
- Maintains cursor position after clicking
- Scans from right to left for more efficient detection
- **Centralized scaling utilities** - DPI scaling calculations in one place for consistency
- **Unified mouse control** - Smart mouse function handles all clicking scenarios automatically
- **Library availability checking** - Centralized detection of optional dependencies
- **Resolution-independent positioning** - uses percentage-based positioning that scales automatically to any screen resolution
- **Custom resolution support** - for non-primary monitors, you can specify exact resolutions
- **Enhanced multi-monitor mouse control** - uses Windows API for reliable clicking across different monitors

## Requirements

- Windows operating system
- Python 3.6 or higher
- Limbus Company game installed and running
- The game can run at any resolution - the script automatically scales detection positioning
- For multi-monitor support: `screeninfo` package (automatically installed by installer)
- For enhanced multi-monitor screenshots: `mss` package (recommended, automatically installed)

## Installation

### Method 1: Automatic Installation (Recommended)
1. Download the `winrate.zip` file from the releases page
2. Extract all files from the zip file to a folder
3. Run `installer.bat` as Administrator
4. The installer will:
   - Check if Python is installed
   - Open Microsoft Store to install Python if needed
   - Install required packages: `pyautogui`, `pillow`, `keyboard`, `screeninfo`, and `mss`

### Method 2: Manual Installation
1. Download the `winrate.zip` file from the releases page
2. Extract all files from the zip file to a folder
If you already have Python installed:
```bash
pip install pyautogui pillow keyboard screeninfo mss
```

## How to Use

### Setup
1. **Launch Limbus Company** on any monitor
2. **Position the game window** so that the bottom-right corner of the game aligns with the bottom-right corner of your chosen monitor
   - **Resolution-independent**: The script automatically adapts to your screen resolution
3. **Multi-monitor setup**: The script will detect all available monitors and let you choose which one to use
4. **Configure settings** (optional) - Edit `settings.ini` to customize detection parameters

### Running the Script
1. Ensure all Python files (`winrate.py`, `config.py`, etc.) and `settings.ini` are in the same folder
2. Double-click `winrate.py` to start the auto player
3. **Monitor Selection** (if multiple monitors detected):
   - The script will show all available monitors
   - Select the monitor where your game is running
   - For non-primary monitors, you can verify or customize the resolution
4. **DPI Scaling Detection** (automatic):
   - The script detects common Windows DPI scaling (125%, 150%, 175%, 200%)
   - Shows detected scaling and recommends the actual resolution
   - **Important**: If scaling detection fails, you may need to manually select the correct resolution
5. **Resolution Options** (for non-primary monitors):
   - Use detected resolution (may be incorrect with DPI scaling)
   - Use likely actual resolution (recommended when scaling is detected)
   - Choose from common resolutions (1920×1080, 2560×1440, 3840×2160)
   - Enter custom resolution (e.g., 1550x900)
6. The script will load settings from `settings.ini` and display the configuration
7. When detected, it will automatically:
   - Click the Win Rate button
   - Press Enter to continue
   - Optionally Alt+Tab away from the game (if enabled)
   - Optionally return the cursor to its original position (if enabled)

### Stopping the Script
- **Press the 'P' key** at any time to stop the script
- The script will also stop if interrupted with Ctrl+C in the console

## Module Overview

### winrate.py (Main Application)
The entry point that coordinates all other modules. Handles the main detection loop and user interaction.

### config.py (Configuration Management)
Loads and validates settings from `settings.ini`. Handles configuration errors gracefully.

### monitor.py (Monitor Management)
- Detects available monitors using centralized library checking
- Handles monitor selection interface
- **Uses centralized scaling utilities** for DPI detection and resolution correction
- Provides custom resolution input functionality


### mouse.py (Unified Mouse Control)
- **Unified smart clicking** - Single `smart_click()` function handles all scenarios
- Windows API integration with automatic fallback to pyautogui
- Intelligent cursor positioning and restoration
- Multi-monitor support with cursor force-movement
- Eliminates need for multiple mouse control functions

### screenshot.py (Screenshot Management)
- Uses `mss` library for efficient multi-monitor screenshots
- Falls back to pyautogui for single monitor setups
- Handles monitor region definitions and DPI scaling

### detection.py (Button Detection)
- Color matching algorithms with tolerance settings
- Secondary color verification in search areas
- **Uses centralized scaling utilities** for coordinate calculations
- Simplified coordinate transformation logic

### logger.py (Debug Logging)
- Configurable debug logging to `log.txt`
- Session separation and timestamped entries
- Supports both debug and info level logging

### utils.py (Utility Functions and Unified Output)
- Keyboard interrupt handling ('P' key to stop)
- Interruptible sleep function for responsive controls
- General utility functions used across modules
- Combined console and debug log output functions
- Eliminates duplicate configuration display code
- Supports selective output to console, log, or both
- Consistent formatting across all output

### scaling_utils.py (DPI Scaling)
- Centralized DPI scaling factor management
- Automatic scaling detection for common Windows scaling (125%, 150%, 175%, 200%)
- Coordinate transformation utilities
- Eliminates duplicate scaling calculations across modules

### library_checker.py (Library Management)
- Centralized checking for optional libraries (screeninfo, mss, Windows API)
- Unified error messages and installation instructions
- Prevents duplicate import attempts across modules
- Provides library status reporting

## Multi-Monitor Support

### Automatic Monitor Detection
- The script automatically detects all connected monitors
- Shows resolution and primary/secondary status for each monitor
- If only one monitor is detected, it's selected automatically

### Monitor Selection
When multiple monitors are detected, you'll see a menu like:
```
====== Monitor Selection ======
1. Monitor 1: 1920x1080 (Primary)
2. Monitor 2: 2560x1440
3. Monitor 3: 3840x2160

Select monitor (1-3): 
```

### DPI Scaling Handling
Windows DPI scaling can cause incorrect resolution detection. The script:
- **Automatically detects** common scaling factors (125%, 150%, 175%, 200%)
- **Shows warnings** when scaled resolutions are detected
- **Recommends actual resolution** based on detected scaling
- **Applies scaling compensation** during coordinate calculations

Example scaling detection:
```
====== Resolution Detection for Monitor 2 ======
Windows DPI scaling can cause incorrect resolution detection.
Detected resolution: 1536x864
⚠️  This looks like 1536x864 (125% scaling)
   Your actual monitor resolution is probably: 1920x1080
```

### Resolution Verification
For non-primary monitors, the script offers resolution options:
- **Use detected resolution** - May be incorrect due to DPI scaling
- **Use likely actual resolution** - Recommended when scaling is detected
- **Common resolutions** - 1920×1080, 2560×1440, 3840×2160
- **Custom resolution** - Enter manually (format: WIDTHxHEIGHT)

This ensures accurate positioning even if monitor detection or scaling compensation isn't perfect.

## Debug Logging System

The script includes a comprehensive debug logging system to help troubleshoot detection issues.

### Enabling Debug Logging
1. Open `settings.ini` in a text editor
2. Find the `[DEBUG]` section
3. Change `DEBUG_LOGGING = false` to `DEBUG_LOGGING = true`
4. Save the file and restart the script

### Debug Log Information
When enabled, the script logs detailed information to `log.txt`:
- **Configuration details** - Monitor settings, resolution, scaling factors
- **Detection attempts** - Each scan with coordinate information
- **Color matching** - Found colors vs target colors
- **Screenshot methods** - Whether MSS or pyautogui was used
- **Mouse operations** - Click coordinates, cursor movements
- **Errors and warnings** - Any issues during operation

### Using Debug Logs
Debug logs help identify issues like:
- **Color detection problems** - Check if target colors are being found
- **Coordinate issues** - Verify click positions are correct
- **Multi-monitor problems** - Confirm monitor positioning and scaling
- **Screenshot failures** - Identify if MSS or pyautogui is working properly

Example debug log entries:
```
2024-01-20 15:30:45 - INFO - Selected monitor: {'name': 'Monitor 2', 'width': 2560, 'height': 1440}
2024-01-20 15:30:45 - DEBUG - Scaling factor: 1.25
2024-01-20 15:30:46 - DEBUG - Scan #1...
2024-01-20 15:30:46 - DEBUG - Found target color at relative X1200, Y1068: (59, 1, 0)
2024-01-20 15:30:46 - DEBUG - Secondary color confirmed! Clicking...
```

## How It Works

The script uses color detection to identify the Win Rate button:
- **Primary Color**: `#3B0100` (dark red) - main button color
- **Secondary Color**: `#F6AF64` (orange/gold) - accent color
- **Detection Area**: Scans a horizontal line at 74.17% from the top of the selected monitor
- **Search Range**: From right edge to center of the selected monitor (right to left scanning)
- **Multi-Monitor Positioning**: Automatically adjusts coordinates based on monitor position and DPI scaling
- **Verification**: Confirms both colors exist in a 50x50 pixel area
- **Enhanced Mouse Control**: Uses Windows API for reliable multi-monitor clicking
- When detected, it will:
  1. Click the Winrate button on the selected monitor
  2. Press Enter to continue
  3. Optionally Alt+Tab away from game (if enabled)
  4. Optionally reset cursor position (if enabled)
  5. Wait between scans based on configured interval
- **To stop**: Press the 'P' key at any time

## Configuration

All settings are now stored in `settings.ini` for easy customization without editing the Python code.

### Settings File Structure

The `settings.ini` file contains four sections:

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
ALT_TAB_AFTER_CLICK = false        # Alt+Tab after clicking
RESET_CURSOR_POSITION = true       # Reset cursor to original position
FORCE_CURSOR_TO_MONITOR = false    # Force cursor to target monitor before clicking

[DEBUG]
DEBUG_LOGGING = false              # Enable debug logging to log.txt
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

### Multi-Monitor Positioning
The script automatically handles coordinate translation for different monitors:
- **Primary monitor**: Uses standard coordinates (0,0 at top-left)
- **Secondary monitors**: Adjusts coordinates based on monitor position
- **Virtual desktop**: Handles negative coordinates for monitors positioned left of primary
- **Resolution scaling**: Percentage-based positioning works across all monitor sizes
- **DPI scaling compensation**: Automatically adjusts for 125%, 150%, 175%, and 200% scaling

### Resolution Independence
The percentage-based positioning system automatically adapts to any screen resolution on any monitor:
- **1080p screen (1920x1080)**: 74.17% = row 801
- **1440p screen (2560x1440)**: 74.17% = row 1068
- **4K screen (3840x2160)**: 74.17% = row 1602
- **Custom resolution (1550x900)**: 74.17% = row 668

This ensures consistent detection across different display setups without manual adjustment.

### DPI Scaling Compensation
The script automatically compensates for Windows DPI scaling:
- **125% scaling**: Coordinates multiplied by 0.80
- **150% scaling**: Coordinates multiplied by 0.67
- **175% scaling**: Coordinates multiplied by 0.57
- **200% scaling**: Coordinates multiplied by 0.50
- **100% scaling**: No compensation applied

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

### Force Cursor to Monitor
This setting helps with multi-monitor setups where the cursor might get "stuck" on monitor borders.

**To enable force cursor movement:**
1. Open `settings.ini` in a text editor
2. Find the line: `FORCE_CURSOR_TO_MONITOR = false`
3. Change it to: `FORCE_CURSOR_TO_MONITOR = true`
4. Save the file and restart the script

**When to enable:**
- Multi-monitor setup with cursor movement issues
- Secondary monitors not responding to clicks
- Debugging coordinate problems

## Troubleshooting

**Script not detecting the button:**
- **Enable debug logging** in `settings.ini` and check `log.txt` for detailed information
- Ensure the Win Rate button is visible and not obscured on the selected monitor
- Try adjusting the `TOLERANCE` value in `settings.ini` if colors don't match exactly
- Verify the `TARGET_COLOR` and `SECONDARY_COLOR` RGB values in `settings.ini`
- Check that the `CHECK_ROW_PERCENTAGE` value is appropriate for your game's UI layout
- Ensure the game window is positioned with the Win Rate button in the bottom-right area of the selected monitor

**Multi-monitor issues:**
- If monitors aren't detected properly, install screeninfo: `pip install screeninfo`
- Ensure the game is running on the monitor you selected
- **Check for DPI scaling issues** - use the recommended actual resolution when scaling is detected
- For non-primary monitors, try using custom resolution if detection seems off
- Enable `FORCE_CURSOR_TO_MONITOR = true` in settings.ini
- Check Windows display settings to ensure monitors are configured correctly
- Try running the game in windowed mode for better detection consistency
- **Review debug logs** to see coordinate translations and scaling factors

**DPI Scaling Issues:**
- **Most common issue**: Script detects scaled resolution instead of actual resolution
- **Solution**: Select "Use likely actual resolution" when prompted during setup
- **Manual fix**: Use custom resolution option with your monitor's actual resolution
- **Debug**: Enable debug logging to see scaling factor and coordinate calculations
- **Symptoms**: Clicks appear in wrong location, usually offset from button
- **Prevention**: Run games in windowed mode to reduce scaling complications

**Resolution-related issues:**
- The script now automatically adapts to any resolution on any monitor
- **If DPI scaling is not detected properly**, manually select the correct actual resolution
- If you're having issues with non-primary monitors, use the custom resolution option
- Verify that the game's Win Rate button appears at approximately 74.17% from the top of the selected monitor
- If the button appears at a different vertical position, adjust `CHECK_ROW_PERCENTAGE` in `settings.ini`
- Try running the game in windowed mode for better detection consistency
- **Check debug logs** for coordinate calculations and scaling information

**Settings.ini errors:**
- Ensure `settings.ini` is in the same folder as all the Python files
- Check that all values are properly formatted (no extra spaces, correct case for true/false)
- RGB values must be between 0-255
- `CHECK_ROW_PERCENTAGE` should be a decimal number (e.g., 74.17, not 74.17%)
- If the file is corrupted, download a fresh copy from the releases

**Debug Logging Issues:**
- Ensure the script has write permissions in its directory
- Check that `DEBUG_LOGGING = true` (lowercase) in settings.ini
- Log file `log.txt` should appear in the same folder as the script
- If logging fails, run the script as Administrator

**Screeninfo/MSS installation issues:**
- If multi-monitor support fails, run: `pip install screeninfo mss`
- The script will work with single monitor even without these packages
- For manual installation: Download wheel files and install with pip
- If packages fail to install, try updating pip: `python -m pip install --upgrade pip`

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
- For debug logging, ensure the script can write to its directory

**Clicking in wrong location:**
- **Most likely cause**: DPI scaling not detected or compensated properly
- **Solution**: Use debug logging to verify coordinates and scaling factors
- **Check**: Monitor selection and resolution settings
- **Try**: Custom resolution with your monitor's actual specifications
- **Enable**: `FORCE_CURSOR_TO_MONITOR = true` for better cursor control

**Module import errors:**
- Ensure all Python files are in the same directory
- Check that no files are corrupted or missing
- Verify Python can find all modules by running: `python -c "import config, monitor, mouse, screenshot, detection, logger, utils, scaling_utils, library_checker"`
- If a specific module fails to import, re-download that file

## Development and Customization

### Adding New Features
The modular structure makes it easy to add new features:

1. **Detection algorithms**: Modify `detection.py` to add new color detection methods
2. **Mouse behavior**: Extend the `smart_click()` function in `mouse.py` for new clicking patterns
3. **Monitor support**: Enhance `monitor.py` for specialized display configurations
4. **Scaling support**: Add new scaling factors or algorithms to `scaling_utils.py`
5. **Configuration options**: Add new settings to `config.py` and `settings.ini`

### Code Structure Guidelines
- **Use centralized utilities**: Scaling calculations go in `scaling_utils.py`, library checks in `library_checker.py`
- **Single responsibility**: Each utility module handles one specific concern
- **Avoid duplication**: Check if functionality already exists in utility modules before adding new code
- Each module has a single responsibility
- Use the logging system for debugging rather than print statements
- Keep configuration in `settings.ini` rather than hardcoding values
- Import dependencies through `library_checker.py` to catch missing packages early

### Testing Changes
1. Enable debug logging to monitor behavior
2. Test with different monitor configurations
3. Verify DPI scaling compensation works correctly
4. Check that all configuration options function properly

## Important Notes

**Use at your own risk**
- This is an automation tool that may violate the game's Terms of Service
- This script is designed for personal use and convenience

**Monitor usage**
- Always supervise the script to prevent unexpected behavior
- The script only automates repetitive clicking - it doesn't modify game files or provide unfair advantages
- Multi-monitor support makes it easier to work on other tasks while the script runs

**DPI Scaling Awareness**
- Windows DPI scaling is the most common cause of detection issues
- The script attempts to detect and compensate for scaling automatically
- If detection fails, manually selecting the correct resolution usually resolves issues
- Debug logging provides detailed information about scaling calculations

**Game updates**
- The script may need updates if the game's UI changes
- The percentage-based positioning should remain consistent across most UI updates
- Multi-monitor support is independent of game version
- Color values may need adjustment if the game's button colors change

**System compatibility**
- Multi-monitor support requires Windows and the screeninfo package
- Virtual displays and unusual monitor configurations are supported
- Works with mixed resolution setups (e.g., 1080p + 4K monitors)
- DPI scaling compensation works with most common scaling factors

**Modular architecture benefits**
- Easier maintenance and debugging
- Individual components can be updated independently
- Clear separation of concerns
- Better code reusability and testing

## File Dependencies

Make sure all these files are present in the same directory:

### Required Files:
- `winrate.py` - Main application (run this file)
- `config.py` - Configuration management
- `monitor.py` - Monitor detection and management
- `mouse.py` - Unified mouse control and clicking
- `screenshot.py` - Screenshot capture
- `detection.py` - Button detection algorithms
- `logger.py` - Debug logging system
- `utils.py` - Utility functions and unified output functions
- `scaling_utils.py` - DPI scaling calculations
- `library_checker.py` - Library availability checking
- `settings.ini` - Configuration file

### Optional Files:
- `installer.bat` - Windows installation script
- `log.txt` - Debug log file (created when debug logging is enabled)

## License & Credits

This project is open source. You are free to modify, distribute, and use this code as you see fit, provided that:
- Original author credit is maintained in any derivative works
- Any modifications or distributions include attribution to the original creator

## Disclaimer

This tool is provided as-is for educational and convenience purposes. Users are responsible for ensuring their use complies with all applicable terms of service and local laws. The author assumes no responsibility for any consequences resulting from the use of this software.
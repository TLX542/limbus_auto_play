# Limbus Auto Player

> **⚠️ Important:** Use at your own risk. This automation tool may violate the game's Terms of Service. Designed for personal use and convenience only.

An automated script with a user-friendly GUI that plays Limbus Company for you by detecting and clicking the "Win Rate" button when it appears on screen.

## 📋 Table of Contents

- [Quick Start Guide](#-quick-start-guide)
- [What This Does](#-what-this-does)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Setup & Usage](#-setup--usage)
- [GUI Interface](#-gui-interface)
- [Theme & Appearance](#-theme--appearance)
- [Multi-Monitor Support](#-multi-monitor-support)
- [Settings & Customization](#-settings--customization)
- [Troubleshooting](#-troubleshooting)
- [Advanced Features](#-advanced-features)

---

## 🚀 Quick Start Guide

**New to this? Follow these 4 simple steps:**

1. **Download** the `limbus_auto_play.zip` file from the released tab
2. **Extract** all files to a folder
3. **Run** `installer.bat` as Administrator (it will install Python and required packages)
4. **Double-click** `LAP.pyw` to start the GUI auto player

That's it! The GUI will guide you through the rest.

---

## 🎯 What This Does

This script automatically:
- **Detects** the Win Rate button on your screen
- **Clicks** the button for you
- **Presses Enter** to continue
- **Tabs back to the previous window** if enabled
- **Repeats** until you stop it

**How to stop:** Press the **'P' key** anywhere or use the GUI controls.

### Key Features
- ✅ **Modern GUI Interface** - easy-to-use tabbed interface
- ✅ **Dark/Light Mode Support** - customizable theme that persists between sessions
- ✅ Works with **multiple monitors**
- ✅ Handles **different screen resolutions** automatically
- ✅ Works with **Windows display scaling** (125%, 150%, etc.)
- ✅ **Non-intrusive** - doesn't interfere with normal gameplay
- ✅ **Easy to stop/pause** with hotkey or GUI buttons
- ✅ **Real-time status updates** and configuration display
- ✅ **Debug logging** viewer built into the GUI
- ✅ **Live settings management** - change settings without restarting

---

## 💻 System Requirements

- **Windows** operating system
- **Python 3.6 or higher** (installer will handle this)
- **Limbus Company** game installed and running
- **Any screen resolution** - the script adapts automatically

---

## 📦 Installation

### Option 1: Automatic Installation (Recommended for Beginners)

1. **Download** `limbus_auto_play.zip` from releases
2. **Extract** all files to a folder of your choice
3. **Right-click** on `installer.bat` and select **"Run as administrator"**
4. **Follow the prompts** - the installer will:
   - Check if Python is installed
   - Install Python from Microsoft Store if needed
   - Install all required packages automatically

### Option 2: Manual Installation (For Advanced Users)

If you already have Python:
```bash
pip install pyautogui pillow keyboard screeninfo mss
```

---

## 🎮 Setup & Usage

### Initial Setup

1. **Launch Limbus Company** on any monitor
2. **Have the game in full screen** so the line checked is lined up for the program 
3. **Make sure** the Win Rate button is visible and not covered by other windows

### Running the Application

1. **Double-click** `LAP.pyw` to open the GUI
2. **Configure your settings** using the tabbed interface:
   - **Control Tab**: Start/stop detection and view real-time status
   - **Settings Tab**: Adjust detection parameters and behavior
   - **Display Tab**: Select monitor and resolution settings
   - **Log Tab**: View detailed debug information

### Using the GUI

#### Control Tab
- **Start/Stop Detection**: Main control button to begin or stop automation (also works with 'P' key)
- **Current Configuration**: View your current settings at a glance
- **Real-time Status**: See what the script is doing moment by moment

#### Settings Tab
- **Behavior Options**: Configure Alt+Tab, cursor behavior, and debug logging
- **Detection Timing**: Adjust scan interval and color tolerance
- **Color Configuration**: Fine-tune target and secondary colors with live previews

#### Display Tab
- **Monitor Selection**: Choose which monitor to scan (multi-monitor setups)
- **Resolution Settings**: Set correct resolution with scaling recommendations
- **Library Status**: Check if all optional libraries are available

#### Log Tab
- **Debug Log Viewer**: View detailed logs without opening external files
- **Real-time Updates**: See debug information as it happens
- **Log Management**: Clear or refresh log content

### Stopping the Application

- **Press 'P'** anywhere on your keyboard to pause/resume
- **Use GUI buttons** to stop or start
- **Close the window** to save settings and exit

---

## 🎨 Theme & Appearance

### Dark Mode Support
The GUI now features a comprehensive theming system:

**Theme Toggle:**
- **Settings Tab**: Use the "Dark Mode" checkbox to switch themes
- **Light Mode (Default)**: Clean white interface for daylight use
- **Dark Mode**: Easy-on-the-eyes dark theme for extended sessions

**Theme Features:**
- **Automatic persistence**: Your theme preference saves to `settings.ini`
- **Instant switching**: Toggle between themes without restarting
- **Complete theming**: All GUI elements adapt to the selected theme
- **Eye-friendly colors**: Carefully chosen colors for both themes

**Color Schemes:**
- **Light Theme**: White backgrounds, black text, blue accents
- **Dark Theme**: Dark gray backgrounds, white text, teal accents

### Theme Settings in Configuration

The dark mode setting is automatically saved in your `settings.ini` file:

```ini
[GUI]
SELECTED_MONITOR = Monitor 1
RESOLUTION = 1920x1080
# Set to true to enable dark mode (default is false for light mode)
DARK_MODE = false
```

**Default Behavior:**
- **First-time users**: Starts in light mode
- **Missing GUI section**: Automatically creates with light mode default
- **Invalid settings**: Falls back to light mode
- **Settings persistence**: Theme choice remembered between sessions

---

## 🖥️ GUI Interface

### Tabbed Interface
The application now features a modern tabbed interface with full theme support:

**Control Tab** - Main operations:
- Start/Stop detection with visual feedback
- Pause/Resume functionality 
- Real-time configuration display
- Live status updates

**Settings Tab** - Configuration:
- **Theme Selection**: Dark/Light mode toggle with instant preview
- Behavior settings (Alt+Tab, cursor control)
- Detection timing and tolerance
- Color settings with live previews
- All changes apply immediately

**Display Tab** - Monitor & resolution:
- Multi-monitor selection
- Resolution configuration with scaling detection
- DPI scaling recommendations
- Library status checking

**Log Tab** - Debug information:
- Real-time debug log viewing
- Log management tools
- No need to open external files

### Real-time Updates
- **Configuration Display**: Always shows current settings
- **Status Messages**: Live updates on what the script is doing
- **Visual Feedback**: Button states reflect current operation
- **Settings Persistence**: Changes save automatically
- **Theme Updates**: Instant theme switching without restart

---

## 🖥️ Multi-Monitor Support

### GUI Monitor Selection
The Display tab automatically detects all monitors and provides:
- **Drop-down selection** with monitor names and resolutions
- **Primary monitor indication** for easy identification
- **Automatic resolution suggestions** based on detected scaling

### Windows Display Scaling
The GUI automatically handles display scaling:
- **Detects** common scaling levels (125%, 150%, 175%, 200%)
- **Provides recommendations** in the resolution dropdown
- **Visual warnings** when scaling might cause issues

**Example in GUI:**
```
Resolution dropdown shows:
- 1920x1080 (Recommended - 125% scaling detected)
- 1536x864 (Detected resolution - may be scaled)
- 2560x1440
- Custom...
```

### Smart Resolution Detection
The Display tab provides multiple resolution options:
- **Recommended resolution** (accounts for scaling)
- **Detected resolution** (current monitor setting)
- **Common resolutions** (standard options)
- **Custom resolution** (manual entry dialog)

---

## ⚙️ Settings & Customization

### GUI Settings Management
All settings can now be managed through the **Settings Tab**:

**Appearance Settings:**
- ☑️ **Dark Mode**: Toggle between light and dark themes

**Behavior Settings:**
- ☑️ Alt+Tab after click (switch away from game)
- ☑️ Reset cursor position after click
- ☑️ Force cursor to monitor before click
- ☑️ Enable debug logging

**Detection Settings:**
- **Check interval**: Adjustable from 0.1 to 10.0 seconds
- **Color tolerance**: Fine-tune detection sensitivity (1-50)

**Color Configuration:**
- **Target Color**: Button background color with live preview
- **Secondary Color**: Text color with live preview
- **RGB sliders**: Precise color adjustment

### Settings File
Settings are stored in `settings.ini` and can be edited manually:

```ini
[DETECTION]
TARGET_COLOR_R = 59
TARGET_COLOR_G = 1
TARGET_COLOR_B = 0
SECONDARY_COLOR_R = 246
SECONDARY_COLOR_G = 175
SECONDARY_COLOR_B = 100
TOLERANCE = 10

[TIMING]
CHECK_INTERVAL = 1.0

[BEHAVIOR]
ALT_TAB_AFTER_CLICK = false
RESET_CURSOR_POSITION = true
FORCE_CURSOR_TO_MONITOR = false

[DEBUG]
DEBUG_LOGGING = false

[GUI]
SELECTED_MONITOR = Primary Monitor
RESOLUTION = 1920x1080
# Theme preference - saves automatically when changed
DARK_MODE = false
```

### Real-time Configuration
Changes made in the GUI:
- **Apply immediately** - no restart required for theme changes
- **Auto-save** when you close the application
- **Manual save** button available in Control tab
- **Theme persistence** - your preference is remembered

---

## 🔧 Troubleshooting

### GUI-Specific Issues

**Application won't start:**
- Ensure all files are in the same folder
- Check that `settings.ini` exists
- Run `installer.bat` as Administrator to reinstall dependencies

**Settings not saving:**
- Check file permissions in the application folder
- Ensure you have write access to the directory
- Use the "Save Settings" button in the Control tab

**Theme not persisting:**
- Verify the `[GUI]` section exists in `settings.ini`
- Check that `DARK_MODE` setting is being saved
- Try manually toggling dark mode in Settings tab

### Button Not Being Detected

**Use the GUI to troubleshoot:**
1. **Settings Tab**: Enable "Debug logging"
2. **Control Tab**: Start detection and watch status messages
3. **Log Tab**: View detailed debug information in real-time
4. **Settings Tab**: Adjust tolerance if needed (try 15-20)

**Color Detection Issues:**
- **Settings Tab**: Use color previews to verify target colors
- **Display Tab**: Ensure correct monitor and resolution are selected
- **Control Tab**: Watch real-time status for detection feedback

### Multi-Monitor Issues

**Monitor not showing in list:**
- **Display Tab**: Check library status section
- Install missing libraries if shown
- Restart the application

**Clicks in wrong location:**
- **Display Tab**: Use "Recommended" resolution option
- Check DPI scaling warnings in Display tab
- Try different resolution options from dropdown

**GUI Display Problems:**
- **Settings Tab**: Try switching themes to see if it helps
- **Settings Tab**: Disable "Force cursor to monitor" 
- **Display Tab**: Switch to primary monitor
- Try running in windowed mode instead of fullscreen

### Display Scaling Issues

**Symptoms:** Clicks appear offset from button location
**GUI Solution:**
1. **Display Tab**: Look for scaling warnings
2. **Select recommended resolution** from dropdown
3. **Control Tab**: Test detection and watch status messages
4. **Log Tab**: Check for coordinate calculation details

---

## 🔍 Advanced Features

### Theme System

**Comprehensive Dark Mode:**
- **Automatic UI adaptation**: All interface elements change color
- **Eye-friendly design**: Carefully chosen colors for comfortable viewing
- **Persistent preference**: Theme choice automatically saved to settings
- **Instant switching**: No restart required when changing themes

**Theme Colors:**
- **Light Mode**: White backgrounds, black text, blue info text
- **Dark Mode**: Dark gray backgrounds, white text, light blue accents

### Integrated Debug System

**Built-in Log Viewer:**
- **Log Tab**: View debug information without opening external files
- **Real-time updates**: See logs as they're generated
- **Log management**: Clear or refresh log content
- **No external file handling**: Everything in the GUI
- **Theme-aware**: Log viewer adapts to selected theme

**How to use:**
1. **Settings Tab**: Enable "Debug logging"
2. **Control Tab**: Start detection
3. **Log Tab**: Watch real-time debug information
4. Use log data to troubleshoot detection issues

### Project Structure
```
limbus_auto_player/
├── LAP.pyw                          # Main GUI application - double-click to start
├── settings.ini                     # Configuration file (auto-created)
├── installer.bat                    # Initial setup installer
├── README.md                        # This help file
├── gui/                             # GUI package
│   ├── __init__.py                  # GUI package initialization
│   ├── main_window.py               # Main window and application logic
│   ├── settings_manager.py          # Settings loading/saving logic
│   ├── theme_manager.py             # Dark/light theme management
│   ├── hotkey_manager.py            # Global hotkey functionality
│   ├── detection_worker.py          # Detection thread worker
│   └── tabs/                        # Tab implementations
│       ├── __init__.py              # Tabs package initialization
│       ├── control_tab.py           # Main control interface
│       ├── settings_tab.py          # Settings configuration
│       ├── display_tab.py           # Monitor/resolution settings
│       └── status_tab.py            # Debug log viewer
└── lib/                             # Core functionality (don't modify)
    ├── config.py
    ├── monitor.py
    ├── mouse.py
    ├── screenshot.py
    ├── detection.py
    ├── logger.py
    ├── utils.py
    ├── settings_handler.py           # Comment-preserving settings handler
    └── library_checker.py
```

### GUI Features

**Modern Interface:**
- **Tabbed design** for organized functionality
- **Dual theme support** with light and dark modes
- **Real-time status updates** in Control tab
- **Live configuration display** showing current settings
- **Visual feedback** for all operations

**Smart Defaults:**
- **Light mode default** for new installations
- **Auto-detects** optimal monitor and resolution
- **Suggests corrections** for common scaling issues
- **Preserves settings** between sessions including theme preference
- **Validates input** to prevent errors

**Advanced Controls:**
- **Global hotkey support** ('P' key works anywhere)
- **Thread-safe operation** with proper cleanup
- **Error handling** with user-friendly messages
- **Library checking** with installation guidance
- **Theme-aware components** that adapt to selected mode

### How Detection Works
The GUI shows this information in real-time:
- **Search area**: Horizontal scan at 74.17% from top of screen
- **Color matching**: RGB values with tolerance settings
- **Coordinate calculation**: Accounts for monitor offset and scaling
- **Success/failure feedback**: Immediate status updates

### GUI vs Command Line
The GUI provides all command-line functionality plus:
- **Visual configuration** instead of text prompts
- **Theme customization** with persistent preferences
- **Real-time monitoring** of detection status
- **Integrated debug viewing** without external files
- **Settings validation** with immediate feedback
- **Multi-monitor management** with visual selection

---

## 📝 Important Notes

### Safety & Terms of Service
- **Personal use only** - don't distribute or commercialize
- **Monitor the script** using the GUI status display
- **Game updates** may require script updates if UI changes
- **Be aware of the risks** before using automation tools

### GUI Performance Tips
- **Keep GUI open** while detection runs for best monitoring
- **Use Log tab** for detailed troubleshooting
- **Choose your preferred theme** for comfortable extended use
- **Single monitor setup** is more reliable than multi-monitor
- **Save settings** regularly using the GUI button

### Technical Limitations
- **Windows only** - doesn't work on Mac or Linux
- **GUI-based detection** - if button appearance changes, use Settings tab to adjust colors
- **No game modification** - only automates mouse clicks and keyboard input
- **No unfair advantage** - just automates repetitive clicking

---

## 🆘 Need More Help?

### Using the GUI for Troubleshooting:
1. ✅ **Settings Tab**: Enable debug logging and choose comfortable theme
2. ✅ **Control Tab**: Watch real-time status messages
3. ✅ **Log Tab**: View detailed debug information
4. ✅ **Display Tab**: Verify monitor and resolution settings
5. ✅ **Settings Tab**: Adjust detection parameters as needed

### Before Asking for Help:
1. ✅ Use the built-in Log tab to view debug information
2. ✅ Try different settings using the Settings tab
3. ✅ Check Display tab for scaling recommendations
4. ✅ Ensure all files are in the same folder
5. ✅ Note which theme you're using (shouldn't affect functionality but good to mention)

### When Reporting Issues:
- **Include your Windows version** and screen resolution
- **Use Log tab** to copy relevant debug information
- **Screenshot the GUI** showing your settings (either theme is fine)
- **Describe exactly what happens** vs what you expected
- **List any error messages** shown in the GUI
- **Mention theme preference** if visual issues occur

---

## 📄 License & Disclaimer

This project is open source for educational purposes. You're free to modify and use it, but:
- **Keep original author credit**
- **Use at your own risk**
- **Respect game Terms of Service**
- **Author not responsible for consequences**
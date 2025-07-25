# Limbus Company Auto Player

> **⚠️ Important:** Use at your own risk. This automation tool may violate the game's Terms of Service. Designed for personal use and convenience only.

An automated script that plays Limbus Company for you by detecting and clicking the "Win Rate" button when it appears on screen.

## 📋 Table of Contents

- [Quick Start Guide](#-quick-start-guide)
- [What This Does](#-what-this-does)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Setup & Usage](#-setup--usage)
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
4. **Double-click** `LAP.py` to start the auto player

That's it! The script will guide you through the rest.

---

## 🎯 What This Does

This script automatically:
- **Detects** the Win Rate button on your screen
- **Clicks** the button for you
- **Presses Enter** to continue
- **Tabs back to the previous window** if enabled
- **Repeats** until you stop it

**How to stop:** Press the **'P' key** at any time.

### Key Features
- ✅ Works with **multiple monitors**
- ✅ Handles **different screen resolutions** automatically
- ✅ Works with **Windows display scaling** (125%, 150%, etc.)
- ✅ **Non-intrusive** - doesn't interfere with normal gameplay
- ✅ **Easy to stop** with hotkey
- ✅ **Debug logging** for troubleshooting

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

### Running the Script

1. **Double-click** `LAP.py` 
2. **Choose your monitor** (if you have multiple screens)
3. **Verify resolution** settings when prompted (most usually take the recommended setting)
4. **Let it run** - the script will automatically detect and click the Win Rate button

### Stopping the Script

- **Press 'P'** on your keyboard to stop anytime
- Or use **Ctrl+C** in the console window

---

## 🖥️ Multi-Monitor Support

### Automatic Detection
The script automatically finds all your monitors and shows them like this:
```
====== Monitor Selection ======
1. Monitor 1: 1920x1080 (Primary)
2. Monitor 2: 2560x1440
3. Monitor 3: 3840x2160

Select monitor (1-3): 
```

### Windows Display Scaling
If you're using Windows display scaling (common on high-resolution monitors), the script will:
- **Detect** common scaling levels (125%, 150%, 175%, 200%)
- **Warn you** if scaling might cause issues
- **Recommend** the correct resolution to use

**Example:**
```
⚠️  This looks like 1536x864 (125% scaling)
   Your actual monitor resolution is probably: 1920x1080
```

### Resolution Options
For non-primary monitors, you can choose:
- **Use detected resolution** (might be wrong due to scaling)
- **Use recommended resolution** (usually correct)
- **Pick from common resolutions** (1920×1080, 2560×1440, 4K)
- **Enter custom resolution** (type it manually)

---

## ⚙️ Settings & Customization

All settings are in the `settings.ini` file. You can edit it with any text editor (like Notepad).

### Common Settings to Change

**Stop Alt+Tab after clicking:**
```ini
ALT_TAB_AFTER_CLICK = true    # Switches away from game after clicking
```

**Keep cursor in place:**
```ini
RESET_CURSOR_POSITION = false    # Cursor stays at button location
```

**Enable debug logging:**
```ini
DEBUG_LOGGING = true    # Creates detailed log.txt file for troubleshooting
```

**Adjust detection timing:**
```ini
CHECK_INTERVAL = 2    # Wait 2 seconds between scans (default is 1)
```

### Color Detection Settings
*Only change these if the button isn't being detected:*

```ini
[DETECTION]
TARGET_COLOR_R = 59        # Main button color (red part)
TARGET_COLOR_G = 1         # Main button color (green part)
TARGET_COLOR_B = 0         # Main button color (blue part)
TOLERANCE = 15             # How close colors need to match (higher = more lenient)
```

---

## 🔧 Troubleshooting

### Button Not Being Detected

**First, try this:**
1. Enable debug logging: Set `DEBUG_LOGGING = true` in `settings.ini`
2. Run the script again
3. Check the `log.txt` file for details

**Common fixes:**
- Make sure the Win Rate button is **fully visible** on screen
- Try increasing the **TOLERANCE** value in settings (try 15 or 20) (a tolerance too high might make it click something else)
- Ensure game window is positioned in the **bottom-right** of your monitor
- Check if you selected the **correct monitor**

### Multi-Monitor Issues

**Monitor not detected:**
- Install screeninfo: Open Command Prompt and type `pip install screeninfo`
- Restart the script

**Clicks in wrong location:**
- **Most common cause:** Windows display scaling
- **Solution:** Choose "Use recommended resolution" when prompted
- **Alternative:** Use custom resolution with your monitor's actual size

**Cursor gets stuck:**
- Enable `FORCE_CURSOR_TO_MONITOR = true` in settings
- Try running game in windowed mode instead of fullscreen

### Installation Problems

**Python not found:**
- Run `installer.bat` as Administrator
- If it still fails, download Python from python.org

**Permission errors:**
- Right-click `installer.bat` and select "Run as administrator"
- Check if antivirus is blocking the script

**Script won't start:**
- Make sure ALL files are in the same folder
- Ensure `settings.ini` file exists

### Display Scaling Issues

**Symptoms:** Clicks appear in wrong location, offset from button
**Cause:** Windows is using display scaling (125%, 150%, etc.)
**Solution:** 
1. When setting up, choose "Use likely actual resolution" 
2. Or use custom resolution with your monitor's real size
3. Enable debug logging to see coordinate calculations

---

## 🔍 Advanced Features

### Debug Logging System

**What it does:** Creates detailed `log.txt` file showing exactly what the script is doing

**When to use:**
- Button detection isn't working
- Clicks are in wrong location
- Multi-monitor setup issues

**How to enable:**
1. Open `settings.ini`
2. Change `DEBUG_LOGGING = false` to `DEBUG_LOGGING = true`
3. Save and restart script
4. Check `log.txt` file for detailed information

### Project File Structure
```
limbus_auto_player/
├── LAP.py          # Main file - double-click this to start
├── settings.ini        # Edit this to change settings
├── installer.bat       # Run this first to install everything
├── README.md           # This help file
└── lib/                # Supporting files (don't modify these)
   ├── config.py
   ├── monitor.py
   ├── mouse.py
   ├── screenshot.py
   ├── detection.py
   ├── logger.py
   ├── utils.py
   ├── scaling_utils.py
   └── library_checker.py
```

### How Detection Works
The script looks for specific colors on your screen:
- **Main color:** Dark red `#3B0100` (the button background)
- **Accent color:** Orange/gold `#F6AF64` (button highlights)
- **Search area:** Scans horizontally at 74.17% from the top of screen
- **Direction:** Searches right to left for faster detection

### Custom Resolution Format
When entering custom resolution, use format: `WIDTHxHEIGHT`
- **Examples:** `1920x1080`, `2560x1440`, `3840x2160`
- **Don't use spaces or other characters**

---

## 📝 Important Notes

### Safety & Terms of Service
- **Personal use only** - don't distribute or commercialize
- **Monitor the script** - don't leave it running unattended for hours
- **Game updates** may require script updates if UI changes
- **Be aware of the risks** before using automation tools

### Performance Tips
- **Single monitor setup** is more reliable than multi-monitor

### Technical Limitations
- **Windows only** - doesn't work on Mac or Linux
- **GUI-based detection** - if button appearance changes, script needs updates
- **No game modification** - only automates mouse clicks and keyboard input
- **No unfair advantage** - just automates repetitive clicking

---

## 🆘 Need More Help?

### Before Asking for Help:
1. ✅ Try the troubleshooting steps above
2. ✅ Enable debug logging and check `log.txt`
3. ✅ Make sure all files are in the same folder
4. ✅ Verify your settings.ini file is correct

### When Reporting Issues:
- **Include your Windows version** and screen resolution
- **Attach your log.txt file** (if debug logging is enabled)
- **Describe exactly what happens** vs what you expected
- **List any error messages** you see

---

## 📄 License & Disclaimer

This project is open source for educational purposes. You're free to modify and use it, but:
- **Keep original author credit**
- **Use at your own risk**
- **Respect game Terms of Service**
- **Author not responsible for consequences**
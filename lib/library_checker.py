"""
Centralized library availability checking to eliminate redundant import checks
"""

# Library availability flags
LIBRARIES = {
    'screeninfo': False,
    'mss': False,
    'windows_mouse': False
}

# Initialize library availability
def check_libraries():
    """Check availability of optional libraries"""
    
    # Check screeninfo
    try:
        from screeninfo import get_monitors
        LIBRARIES['screeninfo'] = True
    except ImportError:
        LIBRARIES['screeninfo'] = False
    
    # Check mss
    try:
        from mss import mss
        LIBRARIES['mss'] = True
    except ImportError:
        LIBRARIES['mss'] = False
    
    # Check Windows mouse control
    try:
        import ctypes
        from ctypes import wintypes
        ctypes.windll.user32  # Test access
        LIBRARIES['windows_mouse'] = True
    except (ImportError, AttributeError):
        LIBRARIES['windows_mouse'] = False

def is_available(library_name):
    """Check if a library is available"""
    return LIBRARIES.get(library_name, False)

def get_missing_libraries():
    """Get list of missing optional libraries with install instructions"""
    missing = []
    
    if not LIBRARIES['screeninfo']:
        missing.append(('screeninfo', 'pip install screeninfo', 'Multi-monitor support will be limited'))
    
    if not LIBRARIES['mss']:
        missing.append(('mss', 'pip install mss', 'Multi-monitor screenshots may not work properly'))
    
    if not LIBRARIES['windows_mouse']:
        missing.append(('Windows API', 'Built into Windows', 'Multi-monitor clicking may be unreliable'))
    
    return missing

def print_library_status():
    """Print status of all libraries"""
    print(f"Library Status:")
    print(f"  screeninfo: {'✓' if LIBRARIES['screeninfo'] else '✗'}")
    print(f"  mss: {'✓' if LIBRARIES['mss'] else '✗'}")
    print(f"  Windows mouse API: {'✓' if LIBRARIES['windows_mouse'] else '✗'}")
    
    missing = get_missing_libraries()
    if missing:
        print(f"\nMissing libraries (optional):")
        for name, install_cmd, impact in missing:
            print(f"  {name}: {install_cmd}")
            print(f"    Impact: {impact}")

# Initialize on import
check_libraries()
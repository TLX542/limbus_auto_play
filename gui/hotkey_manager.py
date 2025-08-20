"""
Limbus Auto Player - Hotkey Manager

Handles global hotkey functionality for start/stop detection.
"""
import threading

class HotkeyManager:
    def __init__(self, app):
        self.app = app
        self.setup_global_hotkey()
    
    def setup_global_hotkey(self):
        """Set up global hotkey listener for start/stop detection"""
        def hotkey_thread():
            try:
                import keyboard
                # Set up the 'P' key listener to toggle detection (start/stop)
                keyboard.add_hotkey('p', self.app.toggle_detection)
                # Keep the thread alive
                keyboard.wait()  # This will block until the program ends
            except ImportError:
                print("Warning: keyboard module not available. Hotkey functionality disabled.")
            except Exception as e:
                print(f"Warning: Could not set up hotkey listener: {e}")
        
        # Start hotkey listener in a daemon thread
        hotkey_listener = threading.Thread(target=hotkey_thread, daemon=True)
        hotkey_listener.start()
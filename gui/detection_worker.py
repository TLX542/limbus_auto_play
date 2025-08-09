"""
Limbus Auto Player - Detection Worker

Handles the main detection loop in a separate thread.
"""
import time
from lib.logger import setup_logging
from lib.screenshot import take_monitor_screenshot
from lib.detection import detect_button
from lib.mouse import smart_click

class DetectionWorker:
    def __init__(self, app):
        self.app = app
    
    def run(self):
        """Main detection worker thread"""
        try:
            # Setup logging
            setup_logging(self.app.debug_logging_var.get(), self.app.settings['script_dir'])
            
            # Calculate relative coordinates
            check_row_relative = int((self.app.settings['check_row_percentage'] / 100) * self.app.screen_height)
            
            x_start_relative = int(self.app.screen_width / 2) if self.app.settings['x_start_from_center'] == -1 else self.app.settings['x_start_from_center']
            x_end_relative = self.app.screen_width if self.app.settings['x_end_at_edge'] == -1 else self.app.settings['x_end_at_edge']
            
            # Prepare detection settings
            detection_settings = {
                'x_start_relative': x_start_relative,
                'x_end_relative': x_end_relative,
                'check_row_relative': check_row_relative,
                'target_color': self.app.get_current_colors()[0],
                'secondary_color': self.app.get_current_colors()[1],
                'tolerance': self.app.tolerance_var.get(),
                'search_area_size': self.app.settings['search_area_size']
            }
            
            monitor_settings = {
                'monitor_offset_x': self.app.selected_monitor['x'],
                'monitor_offset_y': self.app.selected_monitor['y']
            }
            
            # Prepare resolution info for scaling decisions
            resolution_info = {
                'monitor_width': self.app.selected_monitor['width'],
                'monitor_height': self.app.selected_monitor['height'],
                'screen_width': self.app.screen_width,
                'screen_height': self.app.screen_height
            }
            
            scan_count = 0
            
            while self.app.is_running and not self.app.stop_event.is_set():
                # Check if paused
                if self.app.pause_event.is_set():
                    # Update config display to show paused status
                    self.app.root.after(0, self.app.update_config_display)
                    # Wait while paused
                    while self.app.pause_event.is_set() and self.app.is_running and not self.app.stop_event.is_set():
                        time.sleep(0.1)
                    
                    # If we're no longer running, break out
                    if not self.app.is_running or self.app.stop_event.is_set():
                        break
                    
                    # Update display to show resumed status
                    self.app.root.after(0, self.app.update_config_display)
                
                scan_count += 1
                self.app.add_status(f"🔍 Scan #{scan_count}...")
                
                try:
                    # Take screenshot
                    screenshot, used_mss = take_monitor_screenshot(
                        self.app.selected_monitor, self.app.screen_width, self.app.screen_height
                    )
                    
                    # Detect button with resolution info for proper scaling
                    button_found, click_x, click_y = detect_button(
                        screenshot, used_mss, detection_settings, monitor_settings, resolution_info
                    )
                    
                    if button_found:
                        self.app.add_status("✅ Button detected! Clicking...")
                        
                        # Click the button
                        smart_click(
                            click_x, click_y,
                            target_monitor=self.app.selected_monitor,
                            force_cursor_to_monitor=self.app.force_cursor_var.get(),
                            restore_cursor=self.app.reset_cursor_var.get()
                        )
                        
                        # Press Enter
                        time.sleep(0.1)
                        import keyboard
                        keyboard.press_and_release('enter')
                        
                        # Optional Alt+Tab
                        if self.app.alt_tab_var.get():
                            time.sleep(0.2)
                            keyboard.press_and_release('alt+tab')
                            
                        self.app.add_status("🎯 Button clicked successfully!")
                        
                    else:
                        self.app.add_status("❌ Button not found in this scan")
                        
                except Exception as e:
                    self.app.add_status(f"⚠️ Error in scan #{scan_count}: {e}")
                    
                # Wait for next scan (check for pause/stop during wait)
                wait_time = self.app.check_interval_var.get()
                elapsed = 0
                while elapsed < wait_time and self.app.is_running and not self.app.stop_event.is_set():
                    if self.app.pause_event.is_set():
                        break  # Exit wait loop if paused
                    time.sleep(0.1)
                    elapsed += 0.1
                
        except Exception as e:
            self.app.add_status(f"💥 Detection error: {e}")
        finally:
            if self.app.is_running:
                self.app.root.after(0, self.app.stop_detection)
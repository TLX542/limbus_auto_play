"""
Centralized DPI scaling utilities to eliminate redundant scaling calculations
"""

# Global scaling factor for DPI compensation
scaling_factor = 1.0

def set_scaling_factor(factor):
    """Set the global scaling factor"""
    global scaling_factor
    scaling_factor = factor

def get_scaling_factor():
    """Get the current scaling factor"""
    return scaling_factor

def apply_scaling(x, y=None):
    """Apply scaling factor to coordinates"""
    if y is None:
        # Single value
        if scaling_factor == 1.25:
            return x * 0.80
        elif scaling_factor == 1.5:
            return x * 0.67
        elif scaling_factor == 1.75:
            return x * 0.57
        elif scaling_factor == 2.0:
            return x * 0.50
        else:
            return x
    else:
        # X, Y pair
        if scaling_factor == 1.25:
            return x * 0.80, y * 0.80
        elif scaling_factor == 1.5:
            return x * 0.67, y * 0.67
        elif scaling_factor == 1.75:
            return x * 0.57, y * 0.57
        elif scaling_factor == 2.0:
            return x * 0.50, y * 0.50
        else:
            return x, y

def detect_likely_scaling(detected_width, detected_height):
    """Detect likely DPI scaling based on detected resolution"""
    common_ratios = {
        (1920, 1080): [
            (1536, 864, 1.25, "125% scaling"),
            (1280, 720, 1.5, "150% scaling"),
            (1097, 617, 1.75, "175% scaling"),
            (960, 540, 2.0, "200% scaling")
        ],
        (2560, 1440): [
            (2048, 1152, 1.25, "125% scaling"),
            (1707, 960, 1.5, "150% scaling"),
            (1463, 819, 1.75, "175% scaling"),
            (1280, 720, 2.0, "200% scaling")
        ],
        (3840, 2160): [
            (3072, 1728, 1.25, "125% scaling"),
            (2176, 1224, 1.75, "175% scaling")
        ]
    }
    
    # Try to detect if current resolution matches a scaled version
    for actual_res, scaled_versions in common_ratios.items():
        for scaled_w, scaled_h, factor, desc in scaled_versions:
            if abs(detected_width - scaled_w) <= 5 and abs(detected_height - scaled_h) <= 5:
                return actual_res, factor, desc
    
    return None, 1.0, "No scaling detected"
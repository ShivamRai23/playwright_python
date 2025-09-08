import os
import time

# Ensure screenshots folder exists
os.makedirs("screenshots", exist_ok=True)

def screenshot_name(step: str) -> str:
    """Generate unique screenshot name with timestamp"""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    return f"screenshots/{step}_{timestamp}.png"

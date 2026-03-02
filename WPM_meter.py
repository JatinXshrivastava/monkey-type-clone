import time

class WPMMeter:
    def __init__(self):
        self.start_time = None

    def start(self):
        """Call this when the user types the first character."""
        if self.start_time is None:
            self.start_time = time.time()

    def get_wpm(self, typed_chars):
        """Calculate WPM based on typed characters and elapsed time."""
        if self.start_time is None:
            return 0
        
        elapsed = time.time() - self.start_time  # seconds
        minutes = elapsed / 60
        
        if minutes == 0:
            return 0
        
        # Standard WPM = characters / 5 per minute
        wpm = (typed_chars / 5) / minutes
        return wpm
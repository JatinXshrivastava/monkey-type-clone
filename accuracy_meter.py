class AccuracyMeter:
    def __init__(self, target_text):
        self.target = target_text
        self.total_keystrokes = 0
        self.incorrect_keystrokes = 0

    def register_keystroke(self, typed_char, index):
        """Called every time user types a key (NOT backspace)."""

        self.total_keystrokes += 1

        # Check if this keystroke was correct
        if index < len(self.target) and typed_char == self.target[index]:
            pass  # correct keystroke
        else:
            self.incorrect_keystrokes += 1  # count mistakes

    def get_raw_accuracy(self):
        """Raw accuracy = correct / total."""
        if self.total_keystrokes == 0:
            return 100.0

        correct = self.total_keystrokes - self.incorrect_keystrokes
        return (correct / self.total_keystrokes) * 100

    def get_error_count(self):
        return self.incorrect_keystrokes
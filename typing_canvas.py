import pygame
import time
from WPM_meter import WPMMeter
from accuracy_meter import AccuracyMeter

class TypingCanvas: 
    def __init__(self, target_text):
        pygame.init()
        self.screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Monkeytype Clone")

        self.font = pygame.font.SysFont("consolas", 28)
        
        self.target = target_text
        self.typed = ""

        self.wpm_meter = WPMMeter()
        self.accuracy_meter = AccuracyMeter(self.target)
        self.started = False
        self.test_finished = False

    def draw_text(self):
        self.screen.fill((20, 20, 20))

        # Target text (white)
        target_lines = self.wrap_text(self.target, 860)
        y_offset = 60

        for line in target_lines:
            target_surface = self.font.render(line, True, (200, 200, 200))
            self.screen.blit(target_surface, (20, y_offset))
            y_offset += 35

        # Render typed text with wrapping (SAFE method)
        typed_lines = self.wrap_text(self.typed, 860)

        y = 120 + (len(target_lines) * 35)
        typed_index = 0  # global position in self.typed

        for line in typed_lines:
            x = 20
            for ch in line:
                if typed_index < len(self.target) and ch == self.target[typed_index]:
                    color = (0, 255, 0)
                else:
                    color = (255, 50, 50)

                char_surface = self.font.render(ch, True, color)
                self.screen.blit(char_surface, (x, y))

                x += char_surface.get_width()
                typed_index += 1  # increase global position

            y += 35

            # Show final results AFTER test ends
        if self.test_finished:
            wpm = self.wpm_meter.get_wpm(len(self.typed), end_time=self.end_time)
            acc = self.accuracy_meter.get_raw_accuracy()
            errors = self.accuracy_meter.get_error_count()

            results = f"WPM: {wpm:.2f}   |   Accuracy: {acc:.2f}%   |   Errors: {errors}"
            result_surface = self.font.render(results, True, (255, 255, 0))
            self.screen.blit(result_surface, (20, 10))
        else:
            # show nothing while typing
            pass

        pygame.display.flip()

    def wrap_text(self, text, max_width):
        """Splits text into multiple lines based on window width."""
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            test_surface = self.font.render(test_line, True, (0, 0, 0))
            
            if test_surface.get_width() > max_width:
                lines.append(current_line)
                current_line = word + " "
            else:
                current_line = test_line

        lines.append(current_line)
        return lines

    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:

                    # Stop taking input after finish
                    if self.test_finished:
                        continue

                    # Start timer on first key
                    if not self.started:
                        self.wpm_meter.start()
                        self.started = True

                    # ESC exits
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        continue

                    # BACKSPACE
                    if event.key == pygame.K_BACKSPACE:
                        if len(self.typed) > 0:
                            self.typed = self.typed[:-1]
                        continue

                    # SPACE
                    if event.key == pygame.K_SPACE:
                        # Space is NOT a mistake — just add it
                        self.typed += " "
                        continue

                    # NORMAL CHARACTERS
                    if event.unicode and len(event.unicode) == 1:

                        # Register this as a raw keystroke BEFORE adding
                        self.accuracy_meter.register_keystroke(
                            event.unicode,
                            len(self.typed)       # index BEFORE character is added
                        )

                        # Add character
                        self.typed += event.unicode

                    # AUTO FINISH
                    if len(self.typed) >= len(self.target):
                        self.test_finished = True
                        self.end_time = time.time()
                        continue
            self.draw_text()
        pygame.quit()
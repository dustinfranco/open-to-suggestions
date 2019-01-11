import typewriter.suggestions_main as tw
import time

tw.gpio_setup()
tw.clear_pins()

class Game:

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        time.sleep(.15)
        print("something happened")
        print("button")

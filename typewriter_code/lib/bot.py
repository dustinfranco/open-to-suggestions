import time

from config.config import config
from lib.irc import Irc
from lib.game import Game
from lib.misc import pbutton

class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)
        self.game = Game()
        self.message_buffer = [{'username': '', 'button': ''}] * self.config['misc']['chat_height']

    def set_message_buffer(self, message):
        self.message_buffer.insert(self.config['misc']['chat_height'] - 1, message)
        self.message_buffer.pop(0)

    def run(self):
        throttle_timers = {button:0 for button in config['throttled_buttons'].keys()}

        while True:
            new_messages = self.irc.recv_messages(1024)
            
            if not new_messages:
                continue

            for message in new_messages: 
                button = message['message']
                username = message['username'] 
                self.set_message_buffer({'username': username, 'button': button})
                pbutton(self.message_buffer)
                self.game.push_button(button)

import sys
import RPi.GPIO as GPIO
from time import sleep

#Time settings
RELAY_SAFETY_TIME = 0.03
NEWLINE_TIME = 0.5
RETURN_TIME = 0.1

#tests
WHEEL_TEST = "wheel_test" in sys.argv
ALPHABET_TEST = "alphabet_test" in sys.argv
PREFACE_TEST = "preface_test" in sys.argv
#TODO: add pin test
test_alphabet = "\n\rAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz)0!1@2#3$4%5^6&7*8(9+=_-[].,?/\"'\n"


previous_tweets = []

upper_pin_dict = {
  17:40,
  18:38,
  19:35,
  20:37,
  21:36,
  22:33,
  23:31,
  24:29
}

lower_pin_dict = {
  9 : 7,
  10:16,
  11:15,
  12:22,
  13:11,
  14:13,
  15:12,
  16:18
}

letters = {
  "a" : (21, 10),
  "b" : (22, 12),
  "c" : (22, 11),
  "d" : (21, 11),
  "e" : (18, 11),
  "f" : (24, 11),
  "g" : (21, 12),
  "h" : (24, 12),
  "i" : (20, 13),
  "j" : (21, 13),
  "k" : (24, 13),
  "l" : (21, 14),
  "m" : (22, 13),
  "n" : (23, 12),
  "o" : (18, 14),
  "p" : (20, 14),
  "q" : (18, 10),
  "r" : (20, 11),
  "s" : (24, 10),
  "t" : (18, 12),
  "u" : (18, 13),
  "v" : (23, 11),
  "w" : (20, 10),
  "x" : (23, 10),
  "y" : (20, 12),
  "z" : (22, 10)
}

numbers = {
  "2" : (17, 10),
  # the number 1 is 19,10 but we can alias it as lowercase L since 1 doesn't work
  #"1" : (19, 10),
  "1" : (21, 14),
  "4" : (17, 11),
  "3" : (19, 11),
  "6" : (17, 12),
  "5" : (19, 12),
  "8" : (17, 13),
  "7" : (19, 13),
  "0" : (17, 14),
  "9" : (19, 14)
}

shifted_special_characters = {
  "!" : (19, 10),
  "@" : (17, 10),
  "$" : (19, 11),
  "#" : (17, 11),
  "CENTS SYMBOL NOT IN ASCII" : (19, 12),
  "%" : (17, 12),
  "*" : (19, 13),
  "&" : (17, 13),
  "(" : (17, 14),
  ")" : (19, 14),
  "?" : (23, 14),
  ":" : (24, 14),
  "QUARTER SYMBOL NOT IN ASCII" : (18, 15),
  "_" : (19, 15),
  "[" : (20, 15),
  '"' : (21, 15),
  "+" : (17, 15),
  "DEGREES SYMBOL NOT IN ASCII" : (24, 15)
}

special_characters = {
  " " : (21, 16),
  "," : ("IDK", 13),
  "." : (22, 14),
  "/" : (23, 14),
  ";" : (24, 14),
  "HALF SYMBOL NOT IN ASCII" : (18, 15),
  "-" : (19, 15),
  "]" : (20, 15),
  "'" : (21, 15),
  "PLUS MINUS SYMBOL NOT IN ASCII" : (24, 15),
  "=" : (17, 15)
}

movement_chars = {
  "\n" : (17, 16),
  "\r" : (18, 16)
}

Capslock_On = False
CAPS_PIN_UPPER = 21
CAPS_PIN_LOWER = 9

############
#GPIO setup#
############

def gpio_setup():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)

  for key,pin in lower_pin_dict.items():
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

  for key,pin in upper_pin_dict.items():
    GPIO.setup(pin,GPIO.OUT, initial=GPIO.HIGH)

############################################
#functions that interact with pins directly#
############################################

def clear_upper_pins(set_value = 1):
  for key,pin in upper_pin_dict.items():
    GPIO.output(pin, set_value)

def clear_lower_pins(set_value = 1):
  for key,pin in lower_pin_dict.items():
    GPIO.output(pin, set_value)

def clear_pins(set_value = 1):
  clear_upper_pins(set_value)
  clear_lower_pins(set_value)

#Set keyboard pin enforces always setting upper pin first

def set_keyboard_pin(input_pin):
  if input_pin in upper_pin_dict:
    clear_upper_pins()
    clear_lower_pins()
    sleep(RELAY_SAFETY_TIME)
    GPIO.output(upper_pin_dict[input_pin], 0)
  elif input_pin in lower_pin_dict:
    clear_lower_pins()
    sleep(RELAY_SAFETY_TIME)
    GPIO.output(lower_pin_dict[input_pin], 0)
  else:
    print(str(input_pin) + " not a valid pin")

def test_pin(pin_in):
  if(pin_in in lower_pin_dict):
    for pin_test in upper_pin_dict:
      set_keyboard_pin(pin_test)
      set_keyboard_pin(pin_in)
      sleep(RELAY_SAFETY_TIME)
  elif(pin_in in upper_pin_dict):
    for pin_test in lower_pin_dict:
      set_keyboard_pin(pin_in)
      set_keyboard_pin(pin_test)
      sleep(RELAY_SAFETY_TIME)
  clear_upper_pins()
  clear_lower_pins()

#################################
#print individual character code#
#################################

def caps_on():
  global Capslock_On
  Capslock_On = True
  clear_pins()
  sleep(RELAY_SAFETY_TIME)
  set_keyboard_pin(20)
  set_keyboard_pin(9)
  sleep(RELAY_SAFETY_TIME)
  clear_pins()
  sleep(RELAY_SAFETY_TIME)
 
def caps_off():
  global Capslock_On 
  Capslock_On = False
  clear_pins()
  sleep(RELAY_SAFETY_TIME)
  set_keyboard_pin(21)
  set_keyboard_pin(9)
  sleep(RELAY_SAFETY_TIME)
  clear_pins()
  sleep(RELAY_SAFETY_TIME)

def execute_movement_char(input_char):
  char_tuple = movement_chars[input_char]
  if(input_char == "\n"):
    set_keyboard_pin(char_tuple[0])
    set_keyboard_pin(char_tuple[1])
    sleep(NEWLINE_TIME)
  elif(input_char == "\r"):
    set_keyboard_pin(char_tuple[0])
    set_keyboard_pin(char_tuple[1])
    sleep(RETURN_TIME)
    clear_pins()
    sleep(RETURN_TIME)
    set_keyboard_pin(char_tuple[0])
    set_keyboard_pin(char_tuple[1])
    sleep(RETURN_TIME)
  clear_pins()
  sleep(RELAY_SAFETY_TIME)
  
def print_char_tuple(input_char_tuple):
  set_keyboard_pin(input_char_tuple[0])
  sleep(RELAY_SAFETY_TIME)
  set_keyboard_pin(input_char_tuple[1])
  sleep(RELAY_SAFETY_TIME)

def t_print_char(input_char, keep_caps_on = False):
  char_tuple = None
  if input_char in letters:
    char_tuple = letters[input_char]
  elif input_char in numbers:
    char_tuple = numbers[input_char]
  elif input_char in special_characters:
    char_tuple = special_characters[input_char]
  elif input_char in shifted_special_characters:
    caps_on()
    char_tuple = shifted_special_characters[input_char]
  elif input_char.lower() in letters:
    caps_on()
    print("caps char " +input_char) 
    char_tuple = letters[input_char.lower()]
  elif input_char in movement_chars:
    execute_movement_char(input_char)
    return
  else:
    print ("input char not supported: " + input_char)
    return
  print_char_tuple(char_tuple)
  turn_caps_off = Capslock_On and not keep_caps_on
  if turn_caps_off:
    caps_off()

###############
#print strings#
###############

def dist_to_char(current_index, input_string, input_char = " "):
  temp_string = input_string[current_index::]
  distance_to_char = input_string.find(input_char)
  return distance_to_char

def t_print_string(input_string):
  line_total = 0
  current_index = 0
  for character in input_string:
    if character == "\n":
      line_total = 0
    if line_total > CHARS_PER_LINE:
      line_total = 0
      t_print_char("\n")
    elif dist_to_char(line_total, input_string) > (CHARS_PER_LINE - line_total):
      line_total = 0
      t_print_char("\n") 
    line_total += 1
    t_print_char(character)
  clear_pins()
  sleep(RELAY_SAFETY_TIME)


########################
#code that runs on boot#
########################

def main():
  gpio_setup()
  clear_pins()
  while(1):
    last_tweet = ""
    if WHEEL_TEST:
      printed_text = "\n\r"
    elif ALPHABET_TEST:
      printed_text = test_alphabet
    elif PREFACE_TEST:
      preface_file = open("./the_preface", "r")
      printed_text = preface_file.read()
      preface_file.close()
    else:
      printed_text = "temporarily nothing"
      if printed_text == last_tweet:
        printed_text = ""
      else:
        last_tweet = printed_text
    if printed_text:   
      t_print_string(printed_text)
    sleep(60)

if __name__ == "__main__":
  main()

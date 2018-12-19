import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

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

for key,pin in lower_pin_dict.items():
  GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

for key,pin in upper_pin_dict.items():
  GPIO.setup(pin,GPIO.OUT, initial=GPIO.HIGH)


def clear_upper_pins(set_value = 1):
  for key,pin in upper_pin_dict.items():
    GPIO.output(pin, set_value)

def clear_lower_pins(set_value = 1):
  for key,pin in lower_pin_dict.items():
    GPIO.output(pin, set_value)

def clear_pins(set_value = 1):
  clear_upper_pins(set_value)
  clear_lower_pins(set_value)

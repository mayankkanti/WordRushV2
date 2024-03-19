
from time import sleep

def get_number():
    global no, add_mode
    if add_mode:no += 1
    else:no -= 1
    if no == 255:add_mode = False
    if no == 0:add_mode = True


no = 0
add_mode = True

while True:
    get_number()
    print(no)
    sleep(.1)
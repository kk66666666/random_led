def on_button_pressed_a():
    global list2, n, a, light_
    basic.clear_screen()
    list2 = []
    for index in range(25):
        list2.append(0)
    n = 0
    while n < light_:
        a = randint(0, 24)
        if list2[a] == 0:
            list2[a] = 1
        n += 1
        點燈(a + 1)
    if light_ > 25:
        light_ = 25
    if light_ < 0:
        light_ = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def dic(num: number):
    pass

def on_button_pressed_ab():
    global light_
    light_ += -1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global light_
    light_ += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def 點燈(num2: number):
    global x, y
    if num2 % 5 == 0:
        x = 4
        y = Math.floor(num2) / 5 - 1
    else:
        x = num2 % 5 - 1
        y = Math.floor(num2) / 5
    led.plot(x, y)
y = 0
x = 0
a = 0
n = 0
list2: List[number] = []
light_ = 0
light_ = 0

def on_forever():
    pass
basic.forever(on_forever)

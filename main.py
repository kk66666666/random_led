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

def num_(num: number):
    global i, _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15, _16, _17, _18, _19, _20, _21, _22, _23, _24, _25
    i = 0
    _1 = images.create_image("""
        . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
    """)
    _2 = images.create_image("""
        . # # # .
                . . . # .
                . # # # .
                . # . . .
                . # # # .
    """)
    _3 = images.create_image("""
        . # # # .
                . . . # .
                . # # # .
                . . . # .
                . # # # .
    """)
    _4 = images.create_image("""
        . # . # .
                . # . # .
                . # # # .
                . . . # .
                . . . # .
    """)
    _5 = images.create_image("""
        . # # # .
                . # . . .
                . # # # .
                . . . # .
                . # # # .
    """)
    _6 = images.create_image("""
        . # # # .
                . # . . .
                . # # # .
                . # . # .
                . # # # .
    """)
    _7 = images.create_image("""
        . # # # .
                . # . # .
                . . . # .
                . . . # .
                . . . # .
    """)
    _8 = images.create_image("""
        . # # # .
                . # . # .
                . # # # .
                . # . # .
                . # # # .
    """)
    _9 = images.create_image("""
        . # # # .
                . # . # .
                . # # # .
                . . . # .
                . # # # .
    """)
    _10 = images.create_image("""
        # . # # #
                # . # . #
                # . # . #
                # . # . #
                # . # # #
    """)
    _11 = images.create_image("""
        . # . . #
                . # . . #
                . # . . #
                . # . . #
                . # . . #
    """)
    _12 = images.create_image("""
        # . # # #
                # . . . #
                # . # # #
                # . # . .
                # . # # #
    """)
    _13 = images.create_image("""
        # . # # #
                # . . . #
                # . # # #
                # . . . #
                # . # # #
    """)
    _14 = images.create_image("""
        # . # . #
                # . # . #
                # . # # #
                # . . . #
                # . . . #
    """)
    _15 = images.create_image("""
        # . # # #
                # . # . .
                # . # # #
                # . . . #
                # . # # #
    """)
    _16 = images.create_image("""
        # . # # #
                # . # . .
                # . # # #
                # . # . #
                # . # # #
    """)
    _17 = images.create_image("""
        # . # # #
                # . # . #
                # . # . #
                # . . . #
                # . . . #
    """)
    _18 = images.create_image("""
        # . # # #
                # . # . #
                # . # # #
                # . # . #
                # . # # #
    """)
    _19 = images.create_image("""
        # . # # #
                # . # . #
                # . # # #
                # . . . #
                # . # # #
    """)
    _20 = images.create_big_image("""
        . . # # # . # # # .
                . . . . # . # . # .
                . . # # # . # . # .
                . . # . . . # . # .
                . . # # # . # # # .
    """)
    _21 = images.create_big_image("""
        . . # # # . . # . .
                . . . . # . . # . .
                . . # # # . . # . .
                . . # . . . . # . .
                . . # # # . . # . .
    """)
    _22 = images.create_big_image("""
        . . # # # . # # # .
                . . . . # . . . # .
                . . # # # . # # # .
                . . # . . . # . . .
                . . # # # . # # # .
    """)
    _23 = images.create_big_image("""
        . . # # # . # # # .
                . . . . # . . . # .
                . . # # # . # # # .
                . . # . . . . . # .
                . . # # # . # # # .
    """)
    _24 = images.create_big_image("""
        . . # # # . # . # .
                . . . . # . # . # .
                . . # # # . # # # .
                . . # . . . . . # .
                . . # # # . . . # .
    """)
    _25 = images.create_big_image("""
        . . # # # . # # # .
                . . . . # . # . . .
                . . # # # . # # # .
                . . # . . . . . # .
                . . # # # . # # # .
    """)
    while False:
        if True:
            pass
        i += 1

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
_25: Image = None
_24: Image = None
_23: Image = None
_22: Image = None
_21: Image = None
_20: Image = None
_19: Image = None
_18: Image = None
_17: Image = None
_16: Image = None
_15: Image = None
_14: Image = None
_13: Image = None
_12: Image = None
_11: Image = None
_10: Image = None
_9: Image = None
_8: Image = None
_7: Image = None
_6: Image = None
_5: Image = None
_4: Image = None
_3: Image = None
_2: Image = None
_1: Image = None
i = 0
a = 0
n = 0
list2: List[number] = []
light_ = 0
light_ = 0

def on_forever():
    pass
basic.forever(on_forever)

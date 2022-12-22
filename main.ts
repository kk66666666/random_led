input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    list2 = []
    for (let index = 0; index < 25; index++) {
        list2.push(0)
    }
    n = 0
    while (n < light_) {
        a = randint(0, 24)
        if (list2[a] == 0) {
            list2[a] = 1
        }
        n += 1
        點燈(a + 1)
    }
    if (light_ > 25) {
        light_ = 25
    }
    if (light_ < 0) {
        light_ = 0
    }
})
function num_ (num: number) {
    i = 0
    while (light_ == i) {
        if (true) {
            break;
        }
        i += 1
    }
}
input.onButtonPressed(Button.AB, function () {
    light_ += -1
    num_(i)
})
input.onButtonPressed(Button.B, function () {
    light_ += 1
    num_(i)
})
function 點燈 (num: number) {
    if (num % 5 == 0) {
        x = 4
        y = Math.floor(num) / 5 - 1
    } else {
        x = num % 5 - 1
        y = Math.floor(num) / 5
    }
    led.plot(x, y)
}
let y = 0
let x = 0
let i = 0
let a = 0
let n = 0
let list2: number[] = []
let light_ = 0
light_ = 0
let _1 = images.createImage(`
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    . . # . .
    `)
let _2 = images.createImage(`
    . # # # .
    . . . # .
    . # # # .
    . # . . .
    . # # # .
    `)
let _3 = images.createImage(`
    . # # # .
    . . . # .
    . # # # .
    . . . # .
    . # # # .
    `)
let _4 = images.createImage(`
    . # . # .
    . # . # .
    . # # # .
    . . . # .
    . . . # .
    `)
let _5 = images.createImage(`
    . # # # .
    . # . . .
    . # # # .
    . . . # .
    . # # # .
    `)
let _6 = images.createImage(`
    . # # # .
    . # . . .
    . # # # .
    . # . # .
    . # # # .
    `)
let _7 = images.createImage(`
    . # # # .
    . # . # .
    . . . # .
    . . . # .
    . . . # .
    `)
let _8 = images.createImage(`
    . # # # .
    . # . # .
    . # # # .
    . # . # .
    . # # # .
    `)
let _9 = images.createImage(`
    . # # # .
    . # . # .
    . # # # .
    . . . # .
    . # # # .
    `)
let _10 = images.createImage(`
    # . # # #
    # . # . #
    # . # . #
    # . # . #
    # . # # #
    `)
let _11 = images.createImage(`
    . # . . #
    . # . . #
    . # . . #
    . # . . #
    . # . . #
    `)
let _12 = images.createImage(`
    # . # # #
    # . . . #
    # . # # #
    # . # . .
    # . # # #
    `)
let _13 = images.createImage(`
    # . # # #
    # . . . #
    # . # # #
    # . . . #
    # . # # #
    `)
let _14 = images.createImage(`
    # . # . #
    # . # . #
    # . # # #
    # . . . #
    # . . . #
    `)
let _15 = images.createImage(`
    # . # # #
    # . # . .
    # . # # #
    # . . . #
    # . # # #
    `)
let _16 = images.createImage(`
    # . # # #
    # . # . .
    # . # # #
    # . # . #
    # . # # #
    `)
let _17 = images.createImage(`
    # . # # #
    # . # . #
    # . # . #
    # . . . #
    # . . . #
    `)
let _18 = images.createImage(`
    # . # # #
    # . # . #
    # . # # #
    # . # . #
    # . # # #
    `)
let _19 = images.createImage(`
    # . # # #
    # . # . #
    # . # # #
    # . . . #
    # . # # #
    `)
let _20 = images.createBigImage(`
    . . # # # . # # # .
    . . . . # . # . # .
    . . # # # . # . # .
    . . # . . . # . # .
    . . # # # . # # # .
    `)
let _21 = images.createBigImage(`
    . . # # # . . # . .
    . . . . # . . # . .
    . . # # # . . # . .
    . . # . . . . # . .
    . . # # # . . # . .
    `)
let _22 = images.createBigImage(`
    . . # # # . # # # .
    . . . . # . . . # .
    . . # # # . # # # .
    . . # . . . # . . .
    . . # # # . # # # .
    `)
let _23 = images.createBigImage(`
    . . # # # . # # # .
    . . . . # . . . # .
    . . # # # . # # # .
    . . # . . . . . # .
    . . # # # . # # # .
    `)
let _24 = images.createBigImage(`
    . . # # # . # . # .
    . . . . # . # . # .
    . . # # # . # # # .
    . . # . . . . . # .
    . . # # # . . . # .
    `)
let _25 = images.createBigImage(`
    . . # # # . # # # .
    . . . . # . # . . .
    . . # # # . # # # .
    . . # . . . . . # .
    . . # # # . # # # .
    `)
basic.forever(function () {
	
})

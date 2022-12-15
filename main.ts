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
function dic (num: number) {
	
}
input.onButtonPressed(Button.AB, function () {
    light_ += -1
})
input.onButtonPressed(Button.B, function () {
    light_ += 1
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
let a = 0
let n = 0
let list2: number[] = []
let light_ = 0
light_ = 0
basic.forever(function () {
	
})

let list: number[] = []
let n = 0
let a = 0
let x = 0
let y = 0
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    list = []
    for (let index = 0; index < 25; index++) {
        list.push(0)
    }
    n = 0
    while (n < 3) {
        a = randint(0, 24)
        if (list[a] == 0) {
            list[a] = 1
        }
        n += 1
        點燈(a + 1)
    }
})
function 點燈 (num: number) {
    if (num % 5 != 0) {
        x = num % 5 - 1
        y = Math.floor(num) / 5
    } else {
        x = 4
        y = num / 5 - 1
    }
    led.plot(x, y)
}
basic.forever(function () {
	
})

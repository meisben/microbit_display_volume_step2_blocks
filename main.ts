// The purpose of this code is to display a dynamic bar chart
// on the screen showing volume recorded with the microphone
// ---
// Lets define a variable 'state' that changes when buttons are pressed
input.onButtonPressed(Button.A, function () {
    state = 1
})
input.onButtonPressed(Button.B, function () {
    state = 0
})
let plot_value = 0
let state = 0
basic.showIcon(IconNames.Asleep)
basic.forever(function () {
    if (state == 1) {
        plot_value = input.soundLevel() / 131 * 180
        led.plotBarGraph(
        plot_value,
        180
        )
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})

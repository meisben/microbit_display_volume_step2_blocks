# The purpose of this code is to display a dynamic bar chart
# on the screen showing volume recorded with the microphone
# ---
# Lets define a variable 'state' that changes when buttons are pressed
def on_button_pressed_a():
    global state
    state = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global state
    state = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

# In our forever loop we will plot the value of the sound level using a bar chart
def on_forever():
    global plot_value
    if state == 1:
        plot_value = input.sound_level() / 131 * 180
        led.plot_bar_graph(plot_value, 180)
    else:
        basic.show_icon(IconNames.ASLEEP)

# Now lets start the program and run the forever loop!
plot_value = 0
state = 0
basic.show_icon(IconNames.ASLEEP)
basic.forever(on_forever)

import turtle, pandas

screen = turtle.Screen()
name = turtle.Turtle()

#Screen specifications
screen.title("U.S.A States Quiz Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Turtle specifications
name.penup()
name.hideturtle()

data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

#Variables
guessed_states = []
game_is_on = True
score = 0
ALIGNMENT = "center"
FONT = ('Courier', 9, 'normal')


while game_is_on:
    answer_state = screen.textinput(title = f"{score}/50 States Correct", prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in list_of_states:
            if state not in guessed_states:
                state_data = data[data.state == state]
                missing_states.append(state)
                name.goto(int(state_data.x), int(state_data.y))
                name.write(f"{state}", False, align=ALIGNMENT,font = FONT)
        new_data = pandas.DataFrame(missing_states)
        data.to_csv("new_data.csv")
        break

    if answer_state in list_of_states:
        if answer_state not in guessed_states:
            state_data = data[data.state == answer_state]
            guessed_states.append(answer_state)
            score += 1
            name.goto(int(state_data.x), int(state_data.y))
            name.write(f"{answer_state}", False, align=ALIGNMENT, font=FONT)




    if score == 50:
        name.goto(0, 0)
        name.write(f"You Win!", False, align=ALIGNMENT, font=FONT)
        game_is_on = False


screen.exitonclick()
import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tim = Turtle()

states = pandas.read_csv("50_states.csv")
correct_answers = 0
guessed_list = []
list_of_states = states["state"].to_list()
is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        missing_states = [state for state in list_of_states if state not in guessed_list]
        is_game_on = False
        conv_to_csv = pandas.DataFrame(missing_states)
        conv_to_csv.to_csv("missing_states.csv")
    elif answer_state in states.values:
        if answer_state in guessed_list:
            pass
        else:
            answer_data = states[states.state == answer_state]
            tim.hideturtle()
            tim.penup()
            tim.goto(answer_data.x.item(), answer_data.y.item())  # .item() retrieves the data as is
            tim.write(arg=answer_state, move=False, align="center", font=("Courier", 8, "normal"))
            guessed_list.append(answer_state)
            correct_answers += 1
            if correct_answers == 50:
                is_game_on = False

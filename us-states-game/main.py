import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    if answer_state in guessed_states:
        screen.textinput(title="Feedback", prompt="You've already guessed that state. "
                                                  "Press any key to continue guessing.")
    elif answer_state == "Exit":
        # States to learn
        states_to_learn = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        data_dict = {"State Name": states_to_learn}
        data_frame = pandas.DataFrame(data_dict)
        data_frame.to_csv("states_to_earn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        target = turtle.Turtle()
        target.penup()
        target.hideturtle()
        state_data = data[data.state == answer_state]
        target.goto(int(state_data.x), int(state_data.y))
        target.write(answer_state)

# To obtain the states coordinates off the image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# this "loop" keeps the turtle screen window open and its similar to exitonclick method.
# turtle.mainloop(get_mouse_click_coor)

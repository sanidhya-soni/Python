import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
# print(all_states)
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name?").title()
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_list = data.state.to_list()
        state_row = data[data.state == answer_state]
        state_x = state_row.x.item()
        state_y = state_row.y.item()

        # print(f'{state_x} + {state_y}')
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_x, state_y)
        t.write(state_row.state.item())

    elif answer_state == 'Exit':
        break

# states_not_guessed  = []
#
# for i in all_states:
#     if i not in guessed_states:
#         states_not_guessed.append(i)
#
# new_dict = {
#     'states': states_not_guessed
# }

new_data = pd.DataFrame([s for s in all_states if s not in guessed_states])

new_data.to_csv('states_to_learn.csv')

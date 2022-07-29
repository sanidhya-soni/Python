import turtle
import  pandas as pd
screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv('50_states.csv')
guessed_states = []

while len(guessed_states) < 50:
    

answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name?")
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


print(state_list)
print(state_x)
print(state_y)

screen.exitonclick()

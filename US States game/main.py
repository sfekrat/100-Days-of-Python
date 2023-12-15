import turtle
import pandas

# Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Extracting States coordinates from csv file
data = pandas.read_csv('50_states.csv')
states_names = data.state.to_list()
print(states_names)
guessed = {}
missed_states = []
score = 0

while True:
    user_input = screen.textinput(f"{score}/{50} Guess the state", "Type a state name: ").title()
    if user_input == 'Exit':
        for state in states_names:
            if state not in guessed.keys():
                missed_states.append(state)
        missed_states_dict = {"Missed States": missed_states}
        missing_states_data = pandas.DataFrame(missed_states_dict)
        missing_states_data.to_csv('missed_states.csv')
        break
    state_xy = ()
    if user_input in states_names:
        cur_state = data[data['state'] == user_input]
        if user_input not in guessed.keys():
            score += 1
            guessed[user_input] = False
            state_xy = (int(cur_state.x.iloc[0]), int(cur_state.y.iloc[0]))
    if user_input in guessed.keys() and guessed[user_input] is False:
        guessed[user_input] = True
        print(state_xy)
        t = turtle.Turtle()
        t.penup()
        t.goto(state_xy)
        t.write(user_input.title())
        t.hideturtle()
    if score == 50:
        break



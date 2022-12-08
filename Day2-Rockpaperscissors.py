# decode opponent choice
opp_choice = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}

# decode my choice
my_choice = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

# score received for playing that weapon
weapon_choice = {'rock': 1, 'paper': 2, 'scissors': 3}

# win possibilities
resolution = {'rock': 'scissors', 
                'scissors': 'paper',
                 'paper': 'rock'}
# score received for result 
scoring = {'lose': 0, 'draw': 3, 'win': 6}

# open text file containing scores and convert to list of strings 'B Z'
with open('Day2-puzzleinput.txt', 'r') as outfile:
    comp_string = outfile.read()
    comp_round_list = comp_string.split('\n')

# function to resolve a single round
def cruncher(round):
    opp_weapon = opp_choice[round.split(' ')[0]]
    my_weapon = my_choice[round.split(' ')[1]]

    if resolution[my_weapon] == opp_weapon:
        return scoring['win'] + weapon_choice[my_weapon]

    elif my_weapon == opp_weapon:
        return scoring['draw'] + weapon_choice[my_weapon]

    else: 
        return scoring['lose'] + weapon_choice[my_weapon]


# list of scores for each round
scores = [cruncher(round) for round in comp_round_list]

# tournament result based on sum of scores
total_score = sum(scores)

print(total_score)


## part two

desired_outcome = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

lose_resolution = {'scissors': 'rock', 
                'rock': 'paper',
                 'paper': 'scissors'}

def reverse_cruncher(round):
    opp_weapon = opp_choice[round.split(' ')[0]]
    result = desired_outcome[round.split(' ')[1]]

    if result == 'lose':
        my_weapon = resolution[opp_weapon]
        return scoring['lose'] + weapon_choice[my_weapon]

    if result == 'draw':
        my_weapon = opp_weapon
        return scoring['draw'] + weapon_choice[my_weapon]

    else:
        my_weapon = lose_resolution[opp_weapon]
        return scoring['win'] + weapon_choice[my_weapon]
        
parttwo_scores = [reverse_cruncher(round) for round in comp_round_list]

parttwo_total = sum(parttwo_scores)

print(parttwo_total)



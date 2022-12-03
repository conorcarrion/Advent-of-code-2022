A = 'rock'
B = 'paper'
C = 'scissors'

rock = 1
paper = 2
scissors = 3

lose = 0
draw = 3
win = 6

with open('Day2-Rockpaperscissors.txt', 'r') as outfile:
    rps_content = outfile.read()
    rps_lis = rps_content.split('\n')


from random import random

ogs = open('./train_output.csv', 'r').read().split("\n")
mods = open('./flipped_df.csv', 'r').read().split("\n")

op = open('./randomized_df.csv', 'w')

for row in range(0, len(ogs)):
    if random() > 0.5 and row < len(mods):
        op.write(mods[row] + "\n")
    else:
        op.write(ogs[row] + "\n")

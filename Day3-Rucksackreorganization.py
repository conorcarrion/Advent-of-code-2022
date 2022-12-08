import string

with open('Day3-puzzleinput.txt', 'r') as outfile:
    rucksack_string = outfile.read()
    rucksack_list = rucksack_string.split('\n')


def string_split(string):
    x = string[:(len(string)//2)]
    y = string[(len(string)//2):len(string)]
    return [x, y]

rs_compartements = [string_split(rucksack) for rucksack in rucksack_list]

def cruncher(rs):
    for letter in rs[0]:
        if letter in rs[1]:
            bad_item = letter
    return bad_item

rs_bad_items = [cruncher(rs) for rs in rs_compartements]


ascii_lower_prio = dict(zip(string.ascii_lowercase, range(1,27)))
ascii_upper_prio = dict(zip(string.ascii_uppercase, range(27,53)))

alphabet = {**ascii_lower_prio, **ascii_upper_prio}

def priority_cruncher(rs_bad):
    priority = alphabet[rs_bad]
    return priority

prio_list = [priority_cruncher(bad_item) for bad_item in rs_bad_items]

prio_sum = sum(prio_list)

print(prio_sum)

## part two

def group_cruncher(rs_full):
    elf_group_letters = []
    for n in range(0, len(rs_full), 3):
        rs = rs_full[n:n+3]
        for letter in rs[0]:
            if letter in rs[1] and letter in rs[2]:
                elf_group_letters.append(letter)
                break

    return elf_group_letters
    

elf_group_letters = group_cruncher(rucksack_list)

group_prio_list = [priority_cruncher(badge) for badge in elf_group_letters]
priorities_sum = sum(group_prio_list)

print(priorities_sum)


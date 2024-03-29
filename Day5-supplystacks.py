with open("Day5-puzzleinput.txt", "r") as outfile:
    x = outfile.read()
    stacks, instructions = x.split("\n\n")


# final line is the stacks and their relative position
stack_crates = stacks.splitlines()[:-1]
stack_numbers = stacks.splitlines()[-1]

# a list of spaces and the stack numbers
stack_numbers_ls = [*stack_numbers]

# calculate which indexes have a crate letter
def indexresolver(string):
    reso_ls = []
    x = [*string]
    for n in x:
        if n != " ":
            reso_ls.append(x.index(n))
    return reso_ls


# calculate the indexes which have a stack number
stack_str_nos = indexresolver(stack_numbers_ls)
# [1, 5, 9, 13, 17, 21, 25, 29, 33]


# create a dict to map the index number to the stack number
indexzip = dict(zip(stack_str_nos, range(1, 10)))
# {1: 1, 5: 2, 9: 3, 13: 4, 17: 5, 21: 6, 25: 7, 29: 8}

# function returns the stack number from the index number
def index_to_stack(index_no):
    x = indexzip[index_no]
    return x


# characters we are not interested in
neg_ls = ["[", "]", " "]

# works out which stack a crate_string has crates in and creates a dictionary with
# the stack number and the crate letter in that stack
# for example: {4: 'Q', 6: 'G', 8: 'M'}
def stack_locator(crate_string):
    crate_list = [*crate_string]
    i = {
        index_to_stack(crate_list.index(letter)): letter
        for letter in crate_list
        if not letter in neg_ls
    }
    return i


# a list with each crate line converted to dict as above
z = [stack_locator(x) for x in stack_crates]
# reverse the order so that the last line will be the 'bottom' of the pile
# by being the first crate in the list
z.reverse()

print(z)

# print(z)

# make a blank map:
# {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
master_plan = {i: [] for i in range(1, 10)}
# print(master_plan)


# update the master plan map with the list of crate positions
def value_updater(plan, list_of_dicts):
    for i in list_of_dicts:
        for key, value in i.items():
            plan[int(key)].append(value)


value_updater(master_plan, z)

# We now have a usable format
# 1  : ['R', 'S', 'L', 'F', 'Q']
# 2  : ['N', 'Z', 'Q', 'G', 'P', 'T']
# 3  : ['S', 'M', 'B']
# 4  : ['T', 'G', 'Z', 'J', 'H', 'C', 'B', 'Q']
# 5  : ['P', 'H', 'M', 'N', 'F', 'S']
# 6  : ['C', 'N', 'S', 'L', 'V', 'G']
# 7  : ['W', 'F']
# 8  : ['Q', 'G', 'Z', 'W', 'V', 'P', 'M']
# 9  : ['G', 'D', 'L', 'C', 'N', 'R']

master_procedure = instructions.split("\n")

# print(master_plan)

# print(master_procedure)


def crane(master_plan, from_key, to_key, num_items):
    from_list = master_plan[from_key]
    to_list = master_plan[to_key]

    for i in range(num_items):
        item = from_list.pop()
        to_list.append(item)

    new_from_pile = {from_key: from_list}
    new_to_pile = {to_key: to_list}

    print(new_from_pile)
    print(new_to_pile)

    master_plan.update(new_from_pile)
    master_plan.update(new_to_pile)
    return master_plan


def instruction_parser(instruction):
    parts = instruction.split(" ")
    num_items = int(parts[1])
    from_key = int(parts[3])
    to_key = int(parts[5])

    print(num_items)
    print(from_key)
    print(to_key)

    return num_items, from_key, to_key


def crane_operator(master_plan, master_procedure):
    for instruction in master_procedure:
        num_items, from_key, to_key = instruction_parser(instruction)
        crane(master_plan, from_key, to_key, num_items)
    return master_plan


# final_positions = crane_operator(master_plan, master_procedure)

test_plan = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

test_procedure = [
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]

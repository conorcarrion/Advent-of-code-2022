with open('Day4-puzzleinput.txt', 'r') as outfile:
    camp_clean_string = outfile.read()
    campclean_list = camp_clean_string.split('\n')


# split the elf pairs into ranges and convert to sets
def elf_pair_cruncher(x):
    a, b = x.split(',')
    m, n = a.split('-')
    r, s = b.split('-')

    set1 = set(range(int(m), int(n) +1))
    set2 = set(range(int(r), int(s)+1))
    return (set1, set2)

# whole list of sets
set_unpack = [elf_pair_cruncher(x) for x in campclean_list]

# are either sets subsumed by the other?
assignment_overlap = [set1.issubset(set2) or set2.issubset(set1) for set1, set2 in set_unpack]

# Use a list comprehension to create a new list with only the True values
true_values = [x for x in assignment_overlap if x]

# Count the number of True values
true_count = len(true_values)

# Print the result
print(true_count) 

# part two - any overlap at all

ass_any_overlap = [set1.intersection(set2) for set1, set2 in set_unpack]

true_values2 = [x for x in ass_any_overlap if x]

true_count2 = len(true_values2)

print(true_count2)
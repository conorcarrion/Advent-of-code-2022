with open('Day1-Calories.txt', 'r') as outfile:
    cal_content = outfile.read()
    cal_ls = cal_content.split('\n')
    cal_dash = '-'.join(cal_ls)
    elf_ls = cal_dash.split('--')

split_list = [x.split('-') for x in elf_ls]

combined_cals = [sum(int(x) for x in elf) for elf in split_list]

cc_sorted = sorted(combined_cals, reverse=True)

print('top elf is: ' + str(cc_sorted[0]))

print('top 3 elves are: ' + str(cc_sorted[:3]))

print('top 3 elf totals is: ' + str(sum(cc_sorted[:3])))
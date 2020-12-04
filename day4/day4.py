import re
with open('day4.txt') as f:
    l = list(map(str.split, f.read().split('\n\n')))

count = 0
for case in l:
    fields = {'byr': False, 'iyr': False, 'eyr': False,
              'hgt': False, 'hcl': False, 'ecl': False, 'pid': False}
    for f in case:
        fields[f[:3]] = True
    if False not in fields.values():
        count += 1
print(count)

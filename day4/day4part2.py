import re
with open('day4.txt') as f:
    l = list(map(str.split, f.read().split('\n\n')))

count = 0
for case in l:
    fields = {'byr': False, 'iyr': False, 'eyr': False,
              'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid': True}
    for f in case:
        x = f[:3]
        if x == 'byr':
            fields[x] = 1920 <= int(f[4:]) <= 2002
        elif x == 'iyr':
            fields[x] = 2010 <= int(f[4:]) <= 2020
        elif x == 'eyr':
            fields[x] = 2020 <= int(f[4:]) <= 2030
        elif x == 'hgt':
            if f[-2:] == 'cm':
                fields[x] = 150 <= int(f[4:-2]) <= 193
            elif f[-2:] == 'in':
                fields[x] = 59 <= int(f[4:-2]) <= 76
        elif x == 'hcl':
            fields[x] = re.fullmatch(r'#[0-9a-f]{6}', f[4:]) != None
        elif x == 'ecl':
            fields[x] = re.fullmatch(
                r'(amb|blu|brn|gry|grn|hzl|oth)', f[4:]) != None

        elif x == 'pid':
            fields[x] = re.fullmatch(r'\d{9}', f[4:]) != None
    if False not in fields.values():
        count += 1
print(count)

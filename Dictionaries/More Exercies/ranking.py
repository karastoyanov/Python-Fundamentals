data = input()
contests = {}

while not data == 'end of contests':
    contest = data.split(':')[0]
    password = data.split(':')[1]
    contests[contest] = password
    data = input()

more_data = input()
students = {}
while not more_data == 'end of submissions':
    contest_to_check = more_data.split('=>')[0]
    password_to_check = more_data.split('=>')[1]
    username = more_data.split('=>')[2]
    points = int(more_data.split('=>')[3])

    if contest_to_check in contests:
        if password_to_check == contests[contest_to_check]:
            if username not in students:
                students[username] = {contest_to_check: points}
            else:
                if contest_to_check not in students[username]:
                    students[username][contest_to_check] = points
                else:
                    if points > students[username][contest_to_check]:
                        students[username][contest_to_check] = points

    more_data = input()

best = {}

for k, v in students.items():
    best[k] = 0
    for kk, vv in v.items():
        best[k] += vv

max_points = max(best.items(), key=lambda k: k[1])

print(f'Best candidate is {max_points[0]} with total {max_points[1]} points.')
print('Ranking:')
for k, v in sorted(students.items(), key=lambda x: x[0]):
    print(f'{k}')
    for kk,vv in sorted(v.items(), key=lambda x: -x[1]):
        print(f'#  {kk} -> {vv}')
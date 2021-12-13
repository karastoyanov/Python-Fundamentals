import re

user_input = input()
pattern = r'(?P<day>\b[0-9]{2})(?P<symbol>.|/|-)(?P<month>[A-Z][a-z]{2,})\2(?P<year>[0-9]{4})'
matches = re.finditer(pattern, user_input)

for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
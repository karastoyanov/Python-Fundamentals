import re

user_input = input()

pattern = r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b"
matches = re.findall(pattern, user_input)

print("\n".join(matches))
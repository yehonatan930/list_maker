import re

string_without_parenthesis = re.sub(r"(\[[^]]+])", "", "a[v] nd")

print(string_without_parenthesis)

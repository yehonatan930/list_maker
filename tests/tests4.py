import re

string_without_parenthesis = re.sub(r"(\[[^]]+])", "", "oswalk[v] nd")

print(string_without_parenthesis)

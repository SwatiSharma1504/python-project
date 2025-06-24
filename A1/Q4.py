string1 = "hello"
string2 = " world"
combined_string = string1 + string2
print(f"Concatenated string using +: {combined_string}")
combined_string_join = "".join([string1, string2])
print(f"Concatenated string using join(): {combined_string_join}")
print(f"Uppercase: {combined_string.upper()}")
print(f"Lowercase: {combined_string.lower()}")
print(f"Capitalized: {combined_string.capitalize()}")
print(f"Replaced 'world' with 'python': {combined_string.replace('world', 'python')}")
print(f"Split into a list: {combined_string.split()}")
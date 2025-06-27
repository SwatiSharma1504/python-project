import re
text = "The quick brown fox jumps over the lazy dog."
match = re.search(r"quick (.*?) fox", text)
if match:
    print(f"Captured group: {match.group(1)}")
numbers = "123 abc 456 def 789"
all_digits = re.findall(r"\d+", numbers)
print(f"All digits found: {all_digits}")
sentence = "Hello world, hello Python!"
new_sentence = re.sub(r"hello", "hi", sentence, flags=re.IGNORECASE)
print(f"Modified sentence: {new_sentence}")
# Name: Ridham Mishra
# Question 3 – String Manipulator

# Asking user to enter a sentence
sentence = input("Enter a sentence: ")

print("\nOriginal:", sentence)

# Total characters with spaces
characters_with_spaces = len(sentence)
print("Characters (with spaces):", characters_with_spaces)

# Counting characters without spaces manually
characters_without_spaces = 0
for ch in sentence:
    if ch != " ":
        characters_without_spaces += 1

print("Characters (without spaces):", characters_without_spaces)

# Counting total words manually
word_count = 0
inside_word = False

for ch in sentence:
    if ch != " " and inside_word == False:
        word_count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False

print("Words:", word_count)

# Converting to uppercase
upper_case_sentence = sentence.upper()
print("UPPERCASE:", upper_case_sentence)

# Converting to lowercase
lower_case_sentence = sentence.lower()
print("lowercase:", lower_case_sentence)

# Title case
title_case_sentence = sentence.title()
print("Title Case:", title_case_sentence)

# Finding first word manually
first_word = ""
for ch in sentence:
    if ch == " ":
        break
    first_word += ch

print("First word:", first_word)

# Finding last word manually
last_word = ""
temp_word = ""

for ch in sentence:
    if ch != " ":
        temp_word += ch
    else:
        last_word = temp_word
        temp_word = ""

# Assign last collected word
if temp_word != "":
    last_word = temp_word

print("Last word:", last_word)

# Reversing sentence manually (no slicing)
reversed_sentence = ""
for ch in sentence:
    reversed_sentence = ch + reversed_sentence

print("Reversed:", reversed_sentence)
# Name: Ridham Mishra
# Question 19 – Text Analysis Functions


# 1. Count Words
def count_words(text):

    word_count = 0
    in_word = False

    for ch in text:
        if ch != " ":
            if in_word == False:
                word_count = word_count + 1
                in_word = True
        else:
            in_word = False

    return word_count


# 2. Count Vowels
def count_vowels(text):

    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count = count + 1

    return count


# 3. Count Consonants
def count_consonants(text):

    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch.isalpha():          # only letters
            if ch not in vowels:
                count = count + 1

    return count


# 4. Reverse Text
def reverse_text(text):

    reversed_text = ""

    for ch in text:
        reversed_text = ch + reversed_text

    return reversed_text


# 5. Check Palindrome
def is_palindrome(text):

    reversed_text = reverse_text(text)

    if text.lower() == reversed_text.lower():
        return True
    else:
        return False


# 6. Remove Vowels
def remove_vowels(text):

    vowels = "aeiouAEIOU"
    new_text = ""

    for ch in text:
        if ch not in vowels:
            new_text = new_text + ch

    return new_text


# 7. Word Frequency
def word_frequency(text):

    freq = {}
    word = ""

    for ch in text:

        if ch != " ":
            word = word + ch
        else:
            if word != "":
                word_lower = word.lower()

                if word_lower in freq:
                    freq[word_lower] = freq[word_lower] + 1
                else:
                    freq[word_lower] = 1

                word = ""

    # Last word handling
    if word != "":
        word_lower = word.lower()
        if word_lower in freq:
            freq[word_lower] = freq[word_lower] + 1
        else:
            freq[word_lower] = 1

    return freq


# 8. Longest Word
def longest_word(text):

    word = ""
    longest = ""

    for ch in text:

        if ch != " ":
            word = word + ch
        else:
            if len(word) > len(longest):
                longest = word
            word = ""

    # Last word check
    if len(word) > len(longest):
        longest = word

    return longest


# 9. Analyze Text (Main Function)
def analyze_text():

    text = input("Enter text: ")

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print("Longest word:", lw, "(", len(lw), "letters )")

    freq = word_frequency(text)
    print("Word Frequency:", freq)


# Call main function
analyze_text()
#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# Funtion 1:
def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. It must start with a capital letter, contain words, and end with '.', '!', or '?
                  .")
# Function 2: 
def calculate_frequencies(sentence):
    # Remove the punctuation and makes it lowercase
    sentence = sentence[:-1].lower()

    # Split it into words
    word_list = sentence.split()

    words = []
    frequencies = []

    for word in word_list:
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)

return words, frequencies

# Function 3: Print the word frequencies
def print_frequencies(words, frequencies):
    print("\nWord frequencies: ")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

# Main
def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

# Run program
if __name__ == "__main__":
    main()

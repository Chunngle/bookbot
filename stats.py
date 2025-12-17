def words(text):
    total_words = text.split()
    return total_words

def letters(text):
    total_letters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            total_letters[char] = total_letters.get(char, 0) + 1
    return total_letters

def sort(letter_counts):
    return dict(sorted(letter_counts.items()))
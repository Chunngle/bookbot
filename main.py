from stats import words, letters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = words(text)
    total_letters = letters(text)
    print(f"Found {len(total_words)} total words.")
    print(f"Found {total_letters} total letters.")
    #print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
from stats import (
    get_word_count,
    get_char_counts,
    sort_chars
)

import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_chars(char_counts)
    #print(f"{word_count} words found in the document")
    #print(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    return

main()

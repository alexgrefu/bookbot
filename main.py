from stats import get_words_count
from stats import get_chars_stat
from stats import get_char_report

import sys

def get_book_text(path):
    
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def main():

    book_path = None

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]


    book_text = get_book_text(book_path)
    words = get_words_count(book_text)
    chars = get_chars_stat(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    lst = get_char_report(chars)
    for item in lst:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    
     

if __name__ == "__main__":
    main()
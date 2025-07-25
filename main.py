import sys
from stats import get_num_words
from stats import get_letter_count
from stats import sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["num"]

def main():
    book_path=sys.argv[1] #"books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    letter_count = get_letter_count(book_text.lower())
    letter_count = sort_dict(letter_count)
    #print(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in letter_count:
        if letter["char"].isalpha():
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
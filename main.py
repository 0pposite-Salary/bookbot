import sys
from stats import num_words_book
from stats import get_char_occurance_num
from stats import sort_chars_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_path_to_file():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    return path_to_file

def main():
    
    path_to_file = get_path_to_file()

    book_contents = get_book_text(path_to_file)
    
    num_words, book_contents_word_list = num_words_book(book_contents)
    
    chars_dict = get_char_occurance_num(book_contents)
    
    chars_list = sort_chars_dict(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for one_char_dict in chars_list:
        if one_char_dict["char"].isalpha():
            print(f"{one_char_dict["char"]}: {one_char_dict["num"]}")
    print("============= END ===============")



main()
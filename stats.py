def num_words_book(book_contents):
    book_contents_word_list = book_contents.split()
    return len(book_contents_word_list), book_contents_word_list

def get_char_occurance_num(book_contents):
    chars_dict = {}
    for char in book_contents:
        char = char.lower()
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

def sort_on(items):
    return items["num"]

def sort_chars_dict(chars_dict):
    chars_list = []
    for key in chars_dict:
        chars_list.append({"char":key, "num":chars_dict[key]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
from stats import get_num_words, get_sorted_dict_char_count
import sys

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        list_words = file_contents.split()
        return  len(list_words)


def main():
    args = sys.argv
    if len(args) <=1 :
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print(f"============ BOOKBOT ============\n Analyzing book found at {filepath}... \n ----------- Word Count ---------- \n Found {get_num_words(filepath)} total words \n--------- Character Count ------- \n")
    dict_sorted_char = get_sorted_dict_char_count(filepath)
    for item in dict_sorted_char:
        print(f"'{item[0]}: {item[1]}'")


main()
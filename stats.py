def get_num_words(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        list_words = file_contents.split()
        return  len(list_words)
    
def get_char_count(filepath: str):
    with open(filepath) as f:
        file_as_string = f.read().lower()
        char_dict = {}
        for char in file_as_string:
            if char not in char_dict and char.isalpha():
                char_dict[char] =  file_as_string.count(char)
        return char_dict


def get_sorted_dict_char_count(filepath: str):
    dict = get_char_count(filepath)
    sorted_dict = sorted(dict.items(), key=lambda tuple: tuple[1], reverse=True)
    return sorted_dict


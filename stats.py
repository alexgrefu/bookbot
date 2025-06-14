def get_words_count(str):
    words = str.split()
    return len(words)

def get_chars_stat(str):
    chars = {}
    for char in str:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_char_report(chars_dict):
    char_count_lst = []
    for c in chars_dict:
        char_count_lst.append({"char": c, "num": chars_dict[c]})
    
    char_count_lst.sort(reverse=True, key=sort_on)

    return char_count_lst
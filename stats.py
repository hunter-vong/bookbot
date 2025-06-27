def get_num_words(text):
    return f"Found {len(text.split())} total words"

def character_count(text):
    text = text.lower()
    empty_dict = {}
    for i in text:
        if i not in empty_dict:
            empty_dict[i] = 1
        else:
            empty_dict[i] += 1
    return empty_dict

def sort_on(items):
    return list(items.values())[0]

def sort_text(char_dict):
    lst = []
    for key, value in char_dict.items():
    	small_dict = {"char": key, "num": value}
    	lst.append(small_dict)

    lst.sort(reverse=True, key=sort_on)
    return lst

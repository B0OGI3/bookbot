def count_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def character_count(text):
    characters = {}
    for char in text:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_dict(char_dict):
    list_of_dicts = []
    for ch, count in char_dict.items():
        list_of_dicts.append({"char": ch, "num": count})
    

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
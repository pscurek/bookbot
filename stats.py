def get_word_count(text):
    return len(text.split())

def get_char_counts(text):
    lower_text = text.lower()
    counts = {}
    for char in lower_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(items):
    return items["num"]

def sort_chars(chars):
    char_list = []
    for char in chars:
        char_list.append({"char":char, "num":chars[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

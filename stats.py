def check_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    file_contents = file_contents.lower()
    count = {}
    for char in file_contents:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(items):
    return items["num"]

def sort_dict(count):
    char_list = []
    for char in count:
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = count[char]
        char_list.append(temp_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
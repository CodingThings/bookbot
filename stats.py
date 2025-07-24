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

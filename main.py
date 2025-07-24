from stats import check_num_words
from stats import char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = check_num_words(file_contents)
    print(f"{num_words} words found in the document")
    count = char_count(file_contents)
    print(count)

main()

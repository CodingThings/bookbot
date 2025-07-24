from stats import check_num_words
from stats import char_count
from stats import sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = check_num_words(file_contents)
    count = char_count(file_contents)
    sorted_count = sort_dict(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_count:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
    

main()

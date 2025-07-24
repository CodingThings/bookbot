def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def check_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def main():
    num_words = check_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()

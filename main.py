from stats import count_words, character_count, sorted_dict
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print(f"Filename: {sys.argv[1]}")
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count_words(text)
    char_dict = character_count(text)

    sorted_list = sorted_dict(char_dict)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


main()
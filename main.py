from stats import get_num_words, get_character_count, get_dict_of_characters
import sys


def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as file:
        file_content = file.read()
    return file_content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_content)} total words")
    print("--------- Character Count -------")
    all_char_dicts = get_character_count(get_dict_of_characters(file_content))
    for char_dict in all_char_dicts:
        values = []
        for key, value in char_dict.items():
            values.append(value)
        print(f"{values[0]}: {values[1]}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

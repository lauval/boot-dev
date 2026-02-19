from stats import (
    get_book_text,
    count_words,
    count_unique_characters,
    convert_to_list_of_dicts,
    helper_sort,
)

import sys

def main(path):

    book_contents = get_book_text(path)
    word_count = count_words(book_contents)
    character_count = count_unique_characters(book_contents)
    dicts = convert_to_list_of_dicts(character_count)
    dicts.sort(reverse=True, key=helper_sort)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dictionary in dicts:
        print(f"{dictionary['char']}: {dictionary['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    # set placeholder path to resolve unbound error
    path = None

    # check if the user specified a path as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # exit code 1: failure, 0: success
    else:
        # user-defined path is then passed to main
        path = sys.argv[1]

    main(path)
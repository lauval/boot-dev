from stats import (
    get_book_text,
    count_words,
    count_unique_characters,
    convert_to_list_of_dicts,
    helper_sort,
)


def main():

    FILEPATH = "books/frankenstein.txt"

    book_contents = get_book_text(FILEPATH)
    word_count = count_words(book_contents)
    character_count = count_unique_characters(book_contents)
    dicts = convert_to_list_of_dicts(character_count)
    dicts.sort(reverse=True, key=helper_sort)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dictionary in dicts:
        print(f"{dictionary['char']}: {dictionary['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

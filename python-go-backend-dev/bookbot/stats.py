def get_book_text(book_path):
    """Read in and store the contents of a book

    Args:
        book_path (str): path to the txt file containing the book text

    Returns:
        contents (str): all of the words from the book, in order
    """
    with open(book_path) as f:
        contents = f.read()

    return contents


def count_words(entire_book_contents) -> int:
    """_summary_

    Args:
        entire_book_contents (str): string containing the full book text

    Returns:
        int: word count
    """
    word_count = len(entire_book_contents.split())
    return word_count


def make_lowercase(entire_book_contents):
    """Normalise the text to lowercase

    Args:
        entire_book_contents (str): the full book text in its original case

    Returns:
        str: the full text in lowercase
    """
    return entire_book_contents.lower()


def count_unique_characters(entire_book_contents):
    """_summary_

    Args:
        entire_book_contents (str): the full text as read in from file

    Returns:
        dict: dictionary containing the unique count by character
    """
    lowercase = make_lowercase(entire_book_contents)

    all_unique_characters = set(lowercase)

    dictionary = {}

    for character in all_unique_characters:
        count = lowercase.count(character)
        dictionary[character] = count

    return dictionary


def convert_to_list_of_dicts(dictionary):
    sorted_dictionaries = []
    for key, value in dictionary.items():
        if key.isalpha():
            sorted_dictionaries.append({"char": key, "num": value})

    return sorted_dictionaries


def helper_sort(list_of_dicts):
    return list_of_dicts["num"]

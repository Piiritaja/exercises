def read_file(file_path):
    """
    Read file contents.

    :param file_path:
    :return: file contents as a string
    """
    pass


def replace_word(file_path, word_to_replace, word_to_replace_with):
    """
    Replace all occurrences of a word with a new word.

    Save the old contents of the file to '[fileName]_old.txt'.
    :param file_path: file to write to.
    :param word_to_replace: words to replace.
    :param word_to_replace_with: word to replace with.
    :return:
    """
    pass


def roll_back(file_path):
    """
    Go back to the previous version of the file.

    Should look for '[file_path]_old.txt' and replace the newer file contents with the old ones.
    If no previous version of the file exists, file contents should be removed. results in an empty file.
    After contents are updated, '[file_path]_old.txt' should be deleted.
    :param file_path: file to roll back.
    :return:
    """
    pass


def count_occurrences(file_path, word):
    """
    Count the number of occurrences of a given word in the file.

    :param file_path: path to file
    :param word: word to search for
    :return: number of words in the input string
    """
    pass


def count_words(file_path):
    """
    Count the total number of words int the file.

    :param file_path:
    :return: number of words in input file
    """
    pass


def count_sentences(file_path):
    """
    Count the total number of sentences in the file.

    :param file_path:
    :return: number of sentences in the file
    """
    pass


def get_paragraphs(file_path):
    """
    Find and return all paragraphs of a file as a list.

    All paragraphs have a form of '[number]. [title]'.
    Every list item should be of the same form as well.
    :param file_path: file path of a book
    :return: list containing every paragraph as a string
    """
    pass


def readability(file_path):
    """
    Calculate the readability index.

    Formula to calculate with: 0.0588 * L - 0.296 * S - 15.8.
    Where L is the average number of letters per 100 words in the text and
    S is the average number of sentences per 100 words in the text.
    Titles and punctuations should not be counted.
    :param file_path: book contents as a string.
    :return: readability index
    """
    pass


def add_book(book_path, file_path):
    """
    Add a book and it's readability index to a given file.

    If the file does not exist, it should be created.
    The line should contain '[title of the book]: [readability index]. grade'.
    'title of the book' is the name of the file (note that from path 'books/My Book.txt', the title is 'My Book').
    If the file already contains a given book, it's readability index and title (if needed) should be updated
    and no new entry of the book is added.
    If the readability index is higher than 12, the book's entry should be '[title of the book]: not a children's book'.
    Every book entry should be on a new line.
    :param book_path: path of the book to add to file.
    :param file_path: file path of the books with readability indexes.
    :return:
    """
    pass


def add_books(book_folder_path, file_path):
    """
    Add all books from a specified folder to book readability index file.

    Only choose .txt files!
    :param book_folder_path: folder path containing books
    :param file_path: file path of the books with readability indexes.
    :return:
    """
    pass

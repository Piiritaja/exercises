import re
from string import ascii_letters
from shutil import copyfile
import os


def replace_word(file_path, word_to_replace, word_to_replace_with):
    """
    Replace all occurrences of a word with a new word.
    Save the old contents of the file to '[fileName]_old.txt'.
    :param file_path: file to write to.
    :param word_to_replace: words to replace.
    :param word_to_replace_with: word to replace with.
    :return:
    """
    create_backup(file_path)
    with open(file_path, "r") as f:
        content = f.read()
        content = content.replace(word_to_replace, word_to_replace_with)
    with open(file_path, "w") as f:
        f.write(content)


def create_backup(file_path):
    print("jah")
    r = re.search(r"(.+[/\\])(\w+\s*)+\.txt$", file_path)
    copy_path = f"{r.group(1)}{r.group(2)}_old.txt"
    print(copy_path)
    copyfile(file_path, copy_path)


def roll_back(file_path):
    """
    Go back to the previous version of the file.
    Should look for '[file_path]_old.txt' and replace the newer file contents with the old ones.
    If no previous version of the file exists, file contents should be removed. results in an empty file.
    After contents are updated, '[file_path]_old.txt' should be deleted.
    :param file_path: file to roll back.
    :return:
    """
    print(file_path)
    try:
        r = re.search(r"(.+[/\\])(\w+\s*)+\.txt$", file_path)
        copy_path = f"{r.group(1)}{r.group(2)}_old.txt"
        copyfile(copy_path, file_path)
        os.remove(copy_path)
        print(os.listdir("../books"))
    except FileNotFoundError:
        print("nope")
        with open(file_path, "w") as f:
            f.write("")


def read_file(file_path):
    """
    Read file contents.

    :param file_path:
    :return: file contents as a string
    """
    with open(file_path) as f:
        return f.read()


def count_occurrences(file_path, word):
    """
    Count the number of occurrences of a given word in the file.

    :param file_path: path to file
    :param word: word to search for
    :return: number of words in the input string
    """
    content = read_file(file_path)
    return content.count(word)


def calc_l(content):
    letter_count = 0
    for i in content:
        if i in ascii_letters:
            letter_count += 1
    return letter_count / get_words(content) * 100


def calc_s(content):
    return get_sentences(content) / get_words(content) * 100


def get_sentences(content):
    return len(re.findall(r".[\.!?]\s|\.\"\s", content))


def get_words(content):
    return len(re.findall(r"\S+", content))


def count_sentences(file_path):
    """
    Count the total number of sentences in the file.

    :param file_path:
    :return: number of sentences in the file
    """
    return get_sentences(read_file(file_path))


def count_words(file_path):
    """
    Count the total number of words in the file.

    :param file_path:
    :return: number of words in the file
    """
    return get_words(read_file(file_path))


def get_paragraphs(file_path):
    """
    Find and return all paragraphs of a file as a list.
    All paragraphs have a form of '[number]. [title]'.
    Every list item should be of the same form as well.
    :param file_path: file path of a book
    :return: list containing every paragraph as a string
    """
    contents = read_file(file_path)
    items = re.findall(r"\d+. [\w\s]+\n", contents)
    return [item.replace("\n", "") for item in items]


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
    re_compiler = re.compile(r"(/)*([\s\w]+)\.txt")
    book = re_compiler.search(book_path).group(2)
    contents = []
    if os.path.exists(file_path):
        with open(file_path, "r+") as f:
            contents = f.readlines()
    if any(book in content for content in contents):
        with open(file_path, "w") as f:
            index = readability(book_path)
            for n, i in enumerate(contents):
                if book in i:
                    if index <= 12:
                        contents[n] = f"{book}: {max(index, 0)}. grade\n"
                    else:
                        contents[n] = f"{book}: not a children's book\n"
            res = "".join(contents)
            f.write(res)
    else:
        with open(file_path, "a+") as f:
            index = readability(book_path)
            if index <= 12:
                res = f"{book}: {max(index, 0)}. grade\n"
            else:
                res = f"{book}: not a children's book\n"

            f.write(res)


def add_books(book_folder_path, file_path):
    """
    Add all books from a specified folder to book readability index file.

    :param book_folder_path:
    :param file_path:
    :return:
    """
    r = re.compile(r"(\w+\s*)+\.txt$")
    books = list(filter(r.match, os.listdir(book_folder_path)))
    for book in books:
        add_book(book_folder_path + book, file_path)


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
    content = read_file(file_path)
    return int(0.0588 * calc_l(content) - 0.296 * calc_s(content) - 15.8)


if __name__ == '__main__':
    add_books("../books/", "../grades.txt")

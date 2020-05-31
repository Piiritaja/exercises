import unittest
import solution.main as solution
import os
import re


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        res = solution.read_file("../books/sample.txt")
        self.assertEqual("tere", res)

    def test_get_paragraphs(self):
        res = solution.get_paragraphs("../books/Gemma.txt")
        expected = ['1. Golden', '2. Crooked', '3. Freed', '4. Serpentine', '5. Sandy', '6. Spiced', '7. Starry',
                    '8. Wooded', '9. Nervy', '10. Towering', '11. Salty', '12. Hidden', '13. Blurry', '14. Combative',
                    '15. Sneaky', '16. Illuminating', '17. Open']
        self.assertEqual(res, expected)

    def test_count_words(self):
        res = solution.count_words("../books/sentence_test.txt")
        self.assertEqual(17, res)

    def test_count_sentences(self):
        res = solution.count_sentences("../books/sentence_test.txt")
        self.assertEqual(4, res)

    def test_readability(self):
        readability = int(0.0588 * (82 / 17 * 100) - 0.296 * (4 / 17 * 100) - 15.8)
        self.assertEqual(readability, solution.readability("../books/sentence_test.txt"))

    def test_replace_word(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.replace_word(path, "kaugel", "far")
            with open(path) as f:
                new_contents = f.read()
            self.assertTrue(new_contents)
            self.assertFalse("kaugel" in new_contents)
            self.assertTrue("far" in new_contents)

        finally:
            self.restore_dir(path, contents)

    def test_replace_word_counts(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.replace_word(path, "kaugel", "far")
            with open(path) as f:
                new_contents = f.read()
            self.assertTrue(new_contents)
            self.assertEqual(0, new_contents.count("kaugel"))
            self.assertEqual(2, new_contents.count("far"))

        finally:
            self.restore_dir(path, contents)

    def test_replace_word_whole(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.replace_word(path, "kaugel", "far")
            with open(path) as f:
                new_contents = f.read()
            with open("../books/backups/sentence_test_mod.txt") as f:
                expected = f.read()
            self.assertEqual(expected, new_contents)

        finally:
            self.restore_dir(path, contents)

    def test_replace_word_creates_backup(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.replace_word(path, "kaugel", "far")
            files = os.listdir("../books/")
            self.assertTrue("sentence_test_old.txt" in files)
        finally:
            self.restore_dir(path, contents)

    def test_roll_back_contents(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.replace_word(path, "kaugel", "far")
            files = os.listdir("../books/")
            self.assertTrue("sentence_test_old.txt" in files)
            with open(path) as f:
                new_contents = f.read()
            self.assertFalse(new_contents == contents)
            solution.roll_back(path)
            with open(path) as f:
                new_contents = f.read()
            self.assertTrue(new_contents == contents)
        finally:
            self.restore_dir(path, contents)

    def test_roll_back_deletes_file(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.replace_word(path, "kaugel", "far")
            files = os.listdir("../books/")
            self.assertTrue("sentence_test_old.txt" in files)
            solution.roll_back(path)
            files = os.listdir("../books/")
            self.assertFalse("sentence_test_old.txt" in files)
        finally:
            self.restore_dir(path, contents)

    def test_roll_back_no_history(self):
        path = "../books/sentence_test.txt"
        try:
            with open(path) as f:
                contents = f.read()
            solution.roll_back(path)
            with open(path) as f:
                new_contents = f.read()
            self.assertFalse(new_contents)
        finally:
            self.restore_dir(path, contents)

    @staticmethod
    def restore_dir(path, contents):
        with open(path, "w") as f:
            f.write(contents)
            files = os.listdir("../books/")
            if "sentence_test_old.txt" in files:
                os.remove("../books/sentence_test_old.txt")

    def test_count_occurrences(self):
        path = "../books/sentence_test.txt"
        self.assertEqual(2, solution.count_occurrences(path, "kaugel"))
        self.assertEqual(0, solution.count_occurrences(path, "Kaugel"))

    def test_readability_large_book1(self):
        self.assertEquals(6, solution.readability("../books/Gemma.txt"))

    def test_readability_large_book2(self):
        self.assertEquals(5, solution.readability("../books/The Great Hill.txt"))

    def test_readability_large_book3(self):
        self.assertEquals(5, solution.readability("../books/The Guardians of Lore.txt"))

    def remove_grades(self):
        try:
            os.remove("grades.txt")
        except FileNotFoundError:
            pass

    def test_add_book_no_file_creates_file(self):
        self.remove_grades()
        solution.add_book("../books/Gemma.txt", "grades.txt")
        files = os.listdir()
        self.assertTrue("grades.txt" in files)

    def test_add_book_no_file_right_name(self):
        self.remove_grades()
        solution.add_book("../books/Gemma.txt", "grades.txt")
        re_compiler = re.compile("Gemma:")
        with open("grades.txt") as f:
            contents = f.read()
        self.assertTrue(re_compiler.match(contents))

    def test_add_book_no_file_right_grade(self):
        self.remove_grades()
        solution.add_book("../books/Gemma.txt", "grades.txt")
        re_compiler = re.compile(r".+ (\d)")
        with open("grades.txt") as f:
            contents = f.read()
        index = re_compiler.search(contents).group(1)
        self.assertIsNotNone(index)
        self.assertEqual('6', index)

    def test_add_book_no_file_right_entry(self):
        self.remove_grades()
        solution.add_book("../books/Gemma.txt", "grades.txt")
        expected = "Gemma: 6. grade\n"
        with open("grades.txt") as f:
            res = f.read()
        self.assertEqual(expected, res)

    def test_add_book_append_to_file_right_names(self):
        self.remove_grades()
        solution.add_book("../books/Gemma.txt", "grades.txt")
        solution.add_book("../books/The Guardians of Lore.txt", "grades.txt")
        with open("grades.txt") as f:
            res = f.read()
        self.assertTrue("Gemma:" in res)
        self.assertTrue("The Guardians of Lore" in res)

    def test_add_book_append_to_file_right_content(self):
        self.remove_grades()
        solution.add_book("../books/Gemma.txt", "grades.txt")
        solution.add_book("../books/The Guardians of Lore.txt", "grades.txt")
        with open("grades.txt") as f:
            res = f.read()
        expected = "Gemma: 6. grade\nThe Guardians of Lore: 5. grade\n"
        self.assertEqual(expected, res)

    def test_add_book_already_in_file_update_index(self):
        self.remove_grades()
        solution.add_book("../books/sentence_test.txt", "grades.txt")
        re_compiler = re.compile(r".+ (\d)")
        with open("grades.txt") as f:
            contents = f.read()
        sr = re_compiler.search(contents)
        self.assertIsNotNone(sr)
        index = sr.group(1)
        solution.add_book("../books/backups/edited/sentence_test.txt", "grades.txt")
        with open("grades.txt") as f:
            contents = f.read()
        self.assertEqual(1, contents.count("sentence_test"))
        print(contents)
        sr = re_compiler.search(contents)
        self.assertIsNotNone(sr)
        new_index = sr.group(1)
        self.assertTrue(new_index > index)

    def test_add_all_books(self):
        self.remove_grades()
        solution.add_books("../books/", "grades.txt")
        with open("grades_expected.txt") as f:
            expected = f.readlines()
        with open("grades.txt") as f:
            res = f.readlines()
        for line in res:
            self.assertTrue(line in expected)

    def test_not_a_children_book(self):
        self.remove_grades()
        solution.add_book("not_a_childrens_book.txt", "grades.txt")
        with open("grades.txt") as f:
            res = f.read()
        self.assertTrue("not a children's book" in res)

    def test_negative_index(self):
        self.remove_grades()
        solution.add_book("negative_grade.txt", "grades.txt")
        with open("grades.txt") as f:
            res = f.read()
        self.assertTrue("0. grade" in res)


if __name__ == '__main__':
    unittest.main()

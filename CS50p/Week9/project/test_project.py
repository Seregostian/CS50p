import unittest
from project import get_questions, get_options, get_answers, main

class TestProject(unittest.TestCase):

    def test_answers(self):
        # Test correctness of answers
        expected_answers = ["A", "A", "C", "B", "A", "A", "B", "A", "A", "A"]
        actual_answers = get_answers()
        self.assertEqual(actual_answers, expected_answers)

    def test_options(self):
        # Test correctness of options
        expected_options = [
            ("A. Gandalf", "B. Shelob", "C. Aragorn", "D. Wormtongue"),
            ("A. Gandalf", "B. Frodo Baggins", "C. Treebeard", "D. Legolas"),
            ("A. Gollum", "B. Frodo Baggins", "C. Aragorn", "D. Legolas"),
            ("A. Boromir", "B. Faramir", "C. Isildur", "D. Gimli"),
            ("A. Boromir", "B. Eowyn", "C. Isildur", "D. Aragorn"),
            ("A. Frodo Baggins", "B. Bilbo Baggins", "C. Gandalf", "D. Saruman"),
            ("A. Frodo Baggins", "B. Bilbo Baggins", "C. Gandalf", "D. Aragorn"),
            ("A. Legolas", "B. Gimli", "C. Boromir", "D. Merry"),
            ("A. Samwise Gamgee", "B. Merry Brandybuck", "C. Pippin Took", "D. Legolas"),
            ("A. Gandalf", "B. Dumbledore", "C. Elrond", "D. Saruman"),
        ]
        actual_options = get_options()
        self.assertEqual(actual_options, expected_options)

    def test_final_score(self):
        # Test correctness of final_score
        expected_final_score = 8  # You can adjust this based on your scenario
        # You may need to redirect stdout to capture the printed output
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
            main()
        actual_final_score = main.final_score
        self.assertEqual(actual_final_score, expected_final_score)


if __name__ == '__main__':
    unittest.main()

import unittest
from math_quiz import generate_random_number, generate_random_operator, generate_question_answer


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the operator returned in among the three specified operators or not 
        for _ in range(1000):  #will run the loop 1000 times to increase the data set for testing
            arithmeticOperator = generate_random_operator() # Test function call
            self.assertIn(arithmeticOperator, ['+', '-', '*']) # check if the operator returned is among the specified ones
            self.assertIsInstance(arithmeticOperator, str) # check if the datatype of returned operator is string or not

    def test_generate_question_answer(self):
            test_cases = [
                 # Normal Test Cases
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (7, 3, '+', '7 + 3', 10),
                (9, 4, '*', '9 * 4', 36),

                # Test cases with respect to zeros

                (0, 5, '+', '0 + 5', 5),
                (0, 3, '-', '0 - 3', -3),

                #Test cases with negative integers

                (-5, 2, '+', '-5 + 2', -3),
                (-10, -3, '-', '-10 - -3', -7),
                (-4, -6, '*', '-4 * -6', 24),

                #Test cases with large numbers
 
                (123456, 654321, '-', '123456 - 654321', -530865),
                (1234, 5678, '*', '1234 * 5678', 7006652)
            ]
            # To iterate through all the test cases mentioned above
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                question, answer = generate_question_answer(num1, num2, operator) # Generating question and answers for the above test cases

                # Check if the Question matches the expected question
                self.assertEqual(question, expected_problem , f"Failed for Question : {question}") 

                # Check if the answer matches the expected answer
                self.assertEqual(answer, expected_answer , f"Failed for Answer : {answer}")
                

if __name__ == "__main__":
    unittest.main()

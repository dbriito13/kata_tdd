import calculator as c
import unittest

class test_calculator(unittest.TestCase):

	#An empty string returns zero
	def test_empty(self):
		#Given
		input_number="";
		expected_result = 0

		#When
		result = c.calculator(input_number);
		wrong_result = 1;

		#Then
		self.assertEqual(expected_result, result);

	#A single number returns the value
	def test_single_number(self):
		#Given
		input_number = "5";
		expected_result = 5;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	def test_two_numbers_comma(self):
		#Given
		input_number = "5,3";
		expected_result = 8;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	def test_two_numbers_newline(self):
		#Given
		input_number = "4\n7";
		expected_result = 11;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);
	def test_three_numbers(self):
		#Given
		input_number = "3,2\n5"
		expected_result = 10;

		#When 
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	def test_negative_number(self):
		#Given
		input_number = "-1"
		#The expected result is an Exception
		
		#When and Then
		self.assertRaises(Exception, c.calculator, input_number)

	def test_twoneg_numbers(self):
		#Given
		input_number = "-1,2"
		#The expected result is an Exception
		
		#When and Then
		self.assertRaises(Exception, c.calculator, input_number)

		#Given
		input_number = "-1\n3"
		#The expected result is an Exception
		
		#When and Then
		self.assertRaises(Exception, c.calculator, input_number)

	def test_threeneg_numbers(self):
		#Given
		input_number = "-1,2,3"
		#The expected result is an Exception
		
		#When and Then
		self.assertRaises(Exception, c.calculator, input_number)

		#Given
		input_number = "-1\n3,4"
		#The expected result is an Exception
		
		#When and Then
		self.assertRaises(Exception, c.calculator, input_number)

	def test_overthousand(self):
		#Given
		input_number = "2,5,1110"
		expected_result = 7;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	def test_alloverthousand(self):
		#Given
		input_number = "1002\n1003"
		expected_result = 0

		#When 
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result,result)

	def test_chardelimiter(self):
		#Given
		input_number = "//#13#4"
		expected_result = 17

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	def test_strdelimiter(self):
		#Given
		input_number = "//###13###4,5"
		expected_result = 22

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

if __name__ == '__main__':
    unittest.main()
import calculator as c
import unittest

#Unittest class
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

	#Tests the sum of two numbers separated by a comma value
	def test_two_numbers_comma(self):
		#Given
		input_number = "5,3";
		expected_result = 8;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	#Tests the sum of two numbers separated by a line break
	def test_two_numbers_newline(self):
		#Given
		input_number = "4\n7";
		expected_result = 11;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	#Tests the sum of three numbers separated either by commas or new lines
	def test_three_numbers(self):
		#Given
		input_number = "3,2\n5"
		expected_result = 10;

		#When 
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	#Tests a negative number to see if it throws an exception
	def test_negative_number(self):
		#Given
		input_number = "-1"
		#The expected result is an Exception
		
		#When and Then
		self.assertRaises(Exception, c.calculator, input_number)

	#Tests the negative number with another number, separated either by comma or new line to see if it still throws an exception
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

	#Tests the negative number in a 3 number situation (delimiters are still comma and new line)
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

	#Test to see if numbers over 1000 are ignored
	def test_overthousand(self):
		#Given
		input_number = "2,5,1110"
		expected_result = 7;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	#Tests to see if in a situation of 2 or 3 numbers where all of them are over 1000 the result is == 0
	def test_alloverthousand(self):
		#Given
		input_number = "1002\n1003"
		expected_result = 0

		#When 
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result,result)

	#Tests the sum of two numbers separated by a user defined delimiter
	def test_chardelimiter(self):
		#Given
		input_number = "//#13#4"
		expected_result = 17

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	#Tests the sum of numbers separated by a user definied delimiter which can be longer than 1 char
	def test_strdelimiter(self):
		#Given
		input_number = "//###13###4,5"
		expected_result = 22

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result, result);

	
	def test_variousStrDelimiters(self):
		#Given
		input_number = "//[!][###]12!3,2###1";
		expected_result = 18;

		#When
		result = c.calculator(input_number);

		#Then
		self.assertEqual(expected_result,result);

if __name__ == '__main__':
    unittest.main()
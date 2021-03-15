import re


#Auxiliary function to check if a character is a number or not
def isnumber(char):
	return (char >= '0' and char <= '9');

def str_delimiter(input_number):
	input_number = input_number[2:]
	#Now let's extract the delimiter, which are all the characters until we find a number
	del_pos = 0;
	for i in range(0,len(input_number)-1):
		if isnumber(input_number[i]) == False:
			del_pos = del_pos+1;
		else:
			break;
	delimiter = input_number[:del_pos];
	input_number = input_number[del_pos:];
	##We have the number inputted and the newly defined delimiter
	delimiters = delimiter +'|,|\n';
	splitted = re.split(delimiters,input_number);
	if check_negative(splitted) == False:
		splitted = check_overthousand(splitted);
		return sum(splitted);

def onechar_delimiter(input_number):
	delimiter = input_number[2]
	splitted = input_number[3:].split(delimiter);
	if check_negative(splitted) == False:
		splitted = check_overthousand(splitted);
		return sum(splitted)

def normal_delimiter(input_number):
	splitted = re.split(',|\n', input_number);
	if check_negative(splitted) == False:
		splitted = check_overthousand(splitted);
		return sum(splitted)

def various_delimiters(input_number):
	input_number = input_number[3:];
	del_pos = 0;
	for i in range(0, len(input_number)-1):
		if isnumber(input_number[i]) == False:
			del_pos += 1;
		else:
			break;
	delimiter_list = input_number[:del_pos-1];
	input_number = input_number[del_pos:];

	#Now we separate using ][
	delimiter_list = delimiter_list.split('][');
	print(delimiter_list)

	#Now we build the concatenation of all our delimiters
	delimiters = ''
	for delimiter in delimiter_list:
		delimiters = delimiters + delimiter + '|'
	delimiters = delimiters + ',|\n'

	splitted = re.split(delimiters, input_number);
	if check_negative(splitted) == False:
		splitted = check_overthousand(splitted);
		return sum(splitted);


def check_negative(numbers):
	#Checks if the string of numbers has any negative numbers
	for number in numbers:
		if int(number) < 0:
			raise Exception("Negative numbers are not allowed")
	return False

#This function will examine the list of numbers that gets passed and remove from it any numbers over 1000
def check_overthousand(numbers):
	new_numbers = [];
	for number in numbers:
		if int(number) <= 1000:
			new_numbers.append(int(number));
	return new_numbers;
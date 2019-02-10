# Telemarketer or not?

#we have noted that telemarketers like to use
# seven-digit phone numbers where the last four digits have three properties. Looking 
# just at the last four digits, these properties are:
# • the first of these four digits is an 8 or 9;
# • the last digit is an 8 or 9;
# • the second and third digits are the same.

#Format: NNN - NNN - 8|9(SS)8|9

#Input Specification
# The input will be 4 lines where each line contains exactly one digit in the range from 0 to 9.

first = int(input("1st number in the last 4 digits of the phone number: "))
second = int(input("2nd number in the last 4 digits of the phone number: "))
third = int(input("3rd number in the last 4 digits of the phone number: "))
fourth = int(input("4th number in the last 4 digits of the phone number: "))

#isATelemarketer = False
#print("Last 4 digits: " + str(first) + str(second) + str(third) + str(fourth))

if (first == 8 or first == 9) and (second == third) and (fourth == 8 or fourth == 9):
    print("ignore")
else:
	print("answer call")

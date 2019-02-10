# Problem J2: Occupy parking

# How many of the parking spaces were occupied both yesterday and today?
# Input Specification
# The first line of input contains the integer N (1 ≤ N ≤ 100). The second and third lines of input
# contain N characters each. The second line of input records the information about yesterday’s
# parking spaces, and the third line of input records the information about today’s parking spaces.
# Each of these 2N characters will either be C to indicate an occupied space or . to indicate it was
# an empty parking space

firstInput = 0
while firstInput <= 1 or firstInput >= 100:
	firstInput = int(input("Input 1: "))
	
yesterday = ""
today = ""

occupied = "C"
vacant = "."

while len(yesterday) != firstInput:
	yesterday = input("YDAY: ") #information about yesterday’s parking spaces
	
while len(today) != firstInput:
	today = input("TDAY: ") #records the information about today’s parking spaces.

# print("yesterday " + yesterday)
# print("Today " + today)

i = 0
count = 0


while i < firstInput:
	# print(i)
	# print("today: " + today[i])
	# print("yday: " + yesterday[i])
	# print("count: " + str(count))
	if today[i] == occupied and yesterday[i] == today[i]:
		count += 1
	i += 1
 
print(count)



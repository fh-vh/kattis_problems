# quadrant.py
# 20 January 2020
# Python solution to "Quadrant Selection" problem on kattis.com (https://open.kattis.com/problems/quadrant)
# By Frederik Hoengaard - @frederikhoengaard - frph@itu.dk

# Is tested and works as of 20 Jan 2020 

#====================================================================================================
#====================================================================================================
#====================================================================================================

import sys

x = sys.stdin.readlines()

clean_input = [int(i.strip('\r\n')) for i in x]


def select_quadrant(sample_list):
	x = sample_list[0]
	y = sample_list[1]

	if x > 0:
		if y > 0:
			return 1
		else:
			return 4
	else:
		if y > 0:
			return 2
		else:
			return 3

#====================================================================================================

def main():
	print(select_quadrant(clean_input))

if __name__ == '__main__':
	main()

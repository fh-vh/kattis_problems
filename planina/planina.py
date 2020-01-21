# planina.py
# 21 January 2020
# Python solution to "Planina" problem on kattis.com (https://open.kattis.com/problems/planina)
# By Frederik Hoengaard - @frederikhoengaard - frph@itu.dk

# Is tested and works as of 21 Jan 2020

#====================================================================================================
#====================================================================================================
#====================================================================================================

import sys

x = int(sys.stdin.readline())

def find_unique_points(x):	
	points = ((2 ** x) + 1) ** 2
	return points

#====================================================================================================

def main():
	print(find_unique_points(x))

if __name__ == '__main__':
	main()

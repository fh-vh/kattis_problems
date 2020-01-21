# r2.py
# 20 January 2020
# Python solution to "R2" problem on kattis.com (https://open.kattis.com/problems/r2)
# By Frederik Hoengaard - @frederikhoengaard - frph@itu.dk

# Is tested and works as of 20 Jan 2020 

#====================================================================================================
#====================================================================================================
#====================================================================================================

import sys

x = sys.stdin.readline()

clean_input = [int(i) for i in x.split(' ')]

def find_R2(sample_input):
	r1 = sample_input[0]
	s = sample_input[1]
	r2 = 2*s - r1

	return r2	


#====================================================================================================

def main():
	print(find_R2(clean_input))

if __name__ == '__main__':
	main()

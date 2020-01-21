# bijele.py
# 21 January 2020
# Python solution to "Bijele" problem on kattis.com (https://open.kattis.com/problems/bijele)
# By Frederik Hoengaard - @frederikhoengaard - frph@itu.dk

# Is tested and works as of 21 Jan 2020

#====================================================================================================
#====================================================================================================
#====================================================================================================

import sys

input_data = sys.stdin.read()

int_list = [int(i) for i in input_data.split(' ')]
valid_list = [1,1,2,2,2,8] 

def check_valid(int_list,valid_list):
    if not int_list:
        return ''
    else:
        if len(int_list) == 1:
            return str(valid_list[0] - int_list[0])
        else:
            return str(valid_list[0] - int_list[0]) + ' ' + check_valid(int_list[1:],valid_list[1:]) 

#====================================================================================================

def main():
	print(check_valid(int_list,valid_list))

if __name__ == '__main__':
	main()

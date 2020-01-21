# carrots.py
# 20 January 2020
# Python solution to "Solving for Carrots" problem on kattis.com (https://open.kattis.com/problems/carrots)
# By Frederik Hoengaard - @frederikhoengaard - frph@itu.dk

# Tested and works as of 20 Jan 2020 

#====================================================================================================
#====================================================================================================
#====================================================================================================

import sys

x = sys.stdin.readlines()

clean_input = [i.strip('\r\n').split(' ') for i in x]

print(int(clean_input[0][1]))

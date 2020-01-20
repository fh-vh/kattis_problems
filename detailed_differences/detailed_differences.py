# detailed_differences.py
# 19 January 2020
# Python solution to "Detailed Differences" problem on kattis.com (https://open.kattis.com/problems/detaileddifferences)
# By Frederik Hoengaard - @frederikhoengaard - frph@itu.dk

# Is tested and works as of 19 Jan 2020

#====================================================================================================
#====================================================================================================
#====================================================================================================

import sys

x = sys.stdin.readlines()

def show_differences(sample):
	lb = '\n'
	tmp = []
	for i in sample:
		x = i.replace("\n","")
		tmp.append(x.replace("\r",""))
	tmp = tmp[1:]

	def comparer(string1,string2):
		tmp = ''
		for i in range(0,len(string1)):
			if string1[i] == string2[i]:
				tmp = tmp + '.'
			else:
				tmp = tmp + '*'
		return tmp

	def output_builder(input_list):
		if not input_list:
			return ''
		elif len(input_list) == 2:
			tmp = comparer(input_list[0],input_list[1])
			return input_list[0] + lb + input_list[1] + lb + tmp + lb
		else:
			tmp = comparer(input_list[0],input_list[1])
			return input_list[0] + lb + input_list[1] + lb + tmp + 2*lb + output_builder(input_list[2:])

	output = output_builder(tmp)
	return output

#====================================================================================================

def main():
	print(show_differences(x))

if __name__ == '__main__':
	main()

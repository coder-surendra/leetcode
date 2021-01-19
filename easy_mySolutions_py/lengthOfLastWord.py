# problem link : https://leetcode.com/problems/length-of-last-word/submissions/
def lengthOfLastWord(x):
	a = x.split()
	print(a)
	if(a):
		lastWord = a[-1]
		length = len(lastWord)
		print(length)
	else:
		print('empty')

lengthOfLastWord('  ')
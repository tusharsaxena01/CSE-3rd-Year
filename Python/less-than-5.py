'''Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for loop
for i in range(0,len(a)):
	if a[i]<5:
		print(a[i])
#while loop
'''
i=0
while i < len(a):
	if a[i] < 5:
		print(a[i])
	i+=1
'''
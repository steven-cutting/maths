from itertools import islice, count, izip
from math import sqrt

def P_Pie(base, amount, pies):
	# terst = 0
	for i in range(base, amount+1):
		pies = ((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))*pies
		# terst += 1
	# print "------"
	# print terst
	# print "------"
	return pies


def wallis(num):
	pie = 1.0
	for i in islice(count(1), int(num)):
		pie = ((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))*pie
	return 2*pie





def wallis2(num):
	s = 4
	# print s
	end = int(num/s)
	numo = int(num/s)
	numi = int(num/s)*(s-1)
	start = 1
	pie = 1.0
	# print [1, end, numo, numi, start, pie]
	
	for times in range(1, s):
		# print ['p', times, end, start]
		start = (end + 1) - numo
		
		if times == 1:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]
		
		else:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]
	
	# print [2, end, numo, numi, start, pie]	
	
	start = (end + 1) - numo
	
	while (numi + numo) != num:
		numo += 1

	# print [3, end, numo, numi, start, pie]
		
	pie = P_Pie(start, numo + numi, pie)
	
	# print [4, end, numo, numi, start, pie]
	
	return 2*pie




def wallis3(num):
	splits = (lambda x: (int(sqrt(sqrt(x))) if x>1000000 else 4))
	s = splits(num)
	# print s
	end = int(num/s)
	numo = int(num/s)
	numi = int(num/s)*(s-1)
	start = 1
	pie = 1.0
	# print [1, end, numo, numi, start, pie]
	
	for times in range(1, s):
		# print ['p', times, end, start]
		start = (end + 1) - numo
		
		if times == 1:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]
		
		else:
			# print ['m', times, end, start],
			pie = P_Pie(start, end, pie)
			end += numo
			# print ['a', times, end, start]
	
	# print [2, end, numo, numi, start, pie]	
	
	start = (end + 1) - numo
	
	while (numi + numo) != num:
		numo += 1

	# print [3, end, numo, numi, start, pie]
		
	pie = P_Pie(start, numo + numi, pie)
	
	# print [4, end, numo, numi, start, pie]
	
	return 2*pie
 
 
 
 

def wallis4(num):
    pies = []
    for i in islice(count(1), int(num)):
        pies.append((4.0*(i**2.0))/((4.0*(i**2.0))-1.0))
    
    pie = 1
    
    for seq in pies:
        pie *= seq
    
    return pie*2
         

def trip(a, b):
    return a/b



def wallis5(num):  
    i2 = []
    fouri2 = []
    btm = []
    pies = []
    pie = 1
    
    for i in islice(count(1), int(num)):
        i2.append(i**2.0)
    
    for seq in i2:
        fouri2.append(seq*4.0)
    
    for seq in fouri2:
        btm.append(seq-1.0)
    
    for seq,point in izip(btm,fouri2):
        pies.append(point/seq)
    
    for seq in pies:
        pie *= seq
    
    return pie*2
        






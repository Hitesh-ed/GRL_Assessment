import re

extract_numbers = r'\d+'                # to detect digits
pat = r'^\d{4}-\d{4}-\d{4}-\d{4}$'      # to detect specified pattern
cons_4 = r'(\d)\1{3}'			# to detect consecutive identical digits

n = int(input())
cd_num = []                             # to store all inputs to be validated

# this loop stores all the inputs to the list
for i in range(n):
	cd_num.append(input())

# this loop does the main job
for num in cd_num:

	if num[0] == '4' or num[0] == '5' or num[0] == '6':  # checks if begins with 4,5 or 6 

		nums = re.findall(extract_numbers,num)       # makes a list of all consecutive numbers
		nums_s = ''.join(nums)        		     # combines all elements in the list to a string
		
		if (bool(re.search(pat,num)) or len(nums)==1):  # checks for pattern dddd-dddd-dddd-dddd or consecutive 16 
		    
		    if not bool(re.search(cons_4,nums_s)):      # checks for 4 consecutive identical numbers
		        print('valid')
		    else:
		        print('invalid')
		else:
			print('invalid')
	else:
		print('invalid')

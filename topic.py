#NAME: Dylan Gonzalez
#Prog Purpose: This program finds a random number for our C.E. Project topic using a 
#Python LIST
# "A" means the topic is available
# "U" means the topic is unavailable

import random
topics = []			#empty list to hold topic codes
TOTAL_TOPICS = 5 #test with 5 topics

def main():
	num_used_topics = 0 
	for i in range(TOTAL_TOPICS): #Fill the list with items with an "A" in each one
		topics.append("A")

	generate_another_randnumber = True  #boolean variable to control the outer loop
	continue_search = True #boolean to control the inner loop

	while generate_another_randnumber: #OUTER LOOP
		continue_search = True

		while continue_search: #INNER LOOP
			randnumber = random.randint(0, TOTAL_TOPICS-1) #items in list start w 0
			if topics[randnumber] == "A";
				topics[randnumber] = "U"
				num_used_topics += 1
				 continue_search = False

		print("\nRandom Topic Number: " + str(randnumber+1)) #items in list start w 0 
		print("List of topic availablility by number:")
		for i in range(TOTAL_TOPICS):
		print("\t" + str(i+1) + ". " + topics[i])

		if num_used_topics == TOTAL_TOPICS:
			print("There are no more topics availble at this time.")
			return() #quit to main() function
		else:
			answer = input("Would you like another random number? Y/N: ")
			if answer.upper() == "n" or answer.upper() == "N":
				generate_another_randnumber = False
main()
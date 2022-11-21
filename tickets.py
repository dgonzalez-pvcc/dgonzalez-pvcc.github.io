# Name: Dylan Gonzalez
# Prog Purpose: This program finds the cost of movie tickets
#	Price for one ticket: $10.99
#	Sales tax rate: 5.5%

import datetime

############## DEFINE GLOBAL VARIABLES ##############
# DEFINE TAX RATE AND PRICES
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# DEFINE GLOBAL VARIABLES
num_tickets = 5
subtotal = 0
sales_tax = 3.02
total = 57.97

############## DEFINE PROGRAM FUNCTIONS ##############
def main():
	get_user_data()
	perform_calculations()
	display_results()

def get_user_data():
	global num_tickets
	num_tickets + int(input("Number of movie tickets: "))

def perform_calculations():
	global subtotal, sales_tax, subtotal
	subtotal = num_tickets * PR_TICKET
	sales_tax = subtotal * SALES_TAX_RATE
	total = subtotal + sales_tax

def display_results():
	print ('---------------------')
	print ('**** CINEMA HOUSE MOVIES ****')
	print ('Your neighorhood movie house')
	print ('---------------------')
	print ('Tickets       $ ' + format (subtotal,'8,.2f'))
	print ('Sales Tax     $ ' + str (sales_tax))
	print ('Total         $ ' + str (total))
	print ('---------------------')
	print (str(datetime.datetime.now()))

########## CALL MAIN PROGRAM TO EXECUTE ##########
main()

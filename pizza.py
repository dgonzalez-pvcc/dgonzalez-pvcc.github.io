# Name: Dylan Gonzalez
# Prog Purpose: This program finds the cost of a pizza
# Price for small pizza: $9.99
# Price for medium pizza: $12.99
# Price for large pizza: $14.99
# Price for extra large pizza: $17.99
# Sales tax rate: 5.5%

import datetime

###define global variables ###
# define tax rate and prices
SALES_TAX_RATE = .055
SPZA = 9.99
MPZA = 12.99
LPZA = 14.99
XLPZA = 17.99

# define global variables
num_pizzas = 0
pizza_price = 0
pizza_cost = 0
pizza_size = 0
sales_tax = 0
total = 0

###define program funcitons ###
def main():
	get_user_data()
	perform_calculations()
	display_results()

def get_user_data():
        global num_pizzas, pizza_size
        num_pizzas = int(input("number of pizzas: "))
        pizza_size = input("Size of pizza: \n S for Small \n M for Medium \n L for Large \n XL for Extra Large\n")
        
def perform_calculations():
        global num_pizzas, sales_tax, pizza_size, pizza_cost, pizza_price, total
        if pizza_size.upper()== 'S': 
                pizza_price = 9.99
        pizza_cost = num_pizzas * pizza_price
        sales_tax = pizza_cost * SALES_TAX_RATE
        total = pizza_cost + sales_tax
        print(total)
        
def display_results():
	print ('------------------------------')
	print ('**** PALERMO PIZZA ****')
	print ('------------------------------')
	print ('Pizzas        $ ' + format (pizza_cost,'8,.2f'))
	print ('Sales Tax     $ ' + format (sales_tax,'8,.2f'))
	print ('Total         $ ' + format(total,'8,.2f'))
	print ('------------------------------')
	print (str(datetime.datetime.now()))

########## call on main program to execute ##########
main()

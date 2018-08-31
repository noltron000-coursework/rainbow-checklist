# Lets make some noise :D
# We'll start with printing and functions.
print()

print("<=== Hello World ===>")
print("Welcome to THE CHECKLIST")

def my_fun_function(say_this):
	print(say_this)

my_fun_function('Hello World')

# Lets run through making a list.
print()

print("we are going to make some modifications to a list...")
checklist = []
print(checklist)
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)
checklist = ['Hello', 'World']
print(checklist)
checklist[1] = 'Cats'
print(checklist)
checklist = ['Hello', 'World']
print(checklist)
checklist.pop(1)
print(checklist)

# Now, lets sum it up within FUNCTIONS.
print()

def create(item):
	checklist.append(item)

def read(index):
	return checklist[index]

def update(index, item):
	checklist[index] = item

def destroy(index):
	checklist.pop(index)

def list_all_items():
	index = 0
	for list_item in checklist:
		print(str(index) + ': ' + list_item)
		index += 1

def test():
	create("purple sox")
	create("red cloak")

	print(read(0))
	print(read(1))

	update(0, "purple socks")
	destroy(1)

	print(read(0))

	list_all_items()

test()

# Time for Mark_Completed

def select(function_code):
	# Create item
	if function_code == "C":
		input_item = user_input("Input item:")
		create(input_item)

	# Read item
	elif function_code == "R":
		item_index = user_input("Index Number?")

		# Remember that item_index must actually exist or our program will crash.
		read(item_index)

	# Print all items
	elif function_code == "P":
		list_all_items()

	# Catch all
	else:
		print("Unknown Option")

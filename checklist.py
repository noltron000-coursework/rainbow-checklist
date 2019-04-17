# Create a list of items
checklist = []

# This is CRUD:
# - Create
# - Read
# - Update
# - Delete

# Define CRUD for our checklist
def create(item):
	'''adds an item to the list'''
	print('appending item...')
	checklist.append(str(item))

def read(index):
	'''prints an item on the list'''
	print('reading item...')
	print(str(index) + ': ' + checklist[index])

def update(index, item):
	'''changes an item on the list'''
	print('updating item...')
	checklist[index] = str(item)

def destroy(index):
	'''removes an item from the list'''
	print('destroying item...')
	checklist.pop(index)

def list_all_items():
	'''prints all items on the list'''
	print('printing all items...')
	index = 0
	for list_item in checklist:
		print(str(index) + ': ' + list_item)
		index += 1

# I created the 'mark completed' function here.
def mark_completed(completed_item):
	'''adds a nice checkmark to the list'''
	print('marking item as complete...\n')
	# Add code here that marks an item as completed
	checklist[completed_item] = '[x] '+str(checklist[completed_item])
	print()

# The select functoin can create, read one item, or read all items.
def select(function_code):
	# Create item
	if function_code == 'C':
		input_item = user_input('New Item Value: ')
		create(input_item)

	# Read item
	elif function_code == 'R':
		item_index = user_input('Index to Read: ')
		# Remember that item_index must actually exist or our program will crash.
		read(int(item_index))

	elif function_code == 'U':
		item_index = int(user_input('Index to Update: '))
		input_item = user_input('Update Item Value: ')
		update(item_index, input_item)


	elif function_code == 'D':
		item_index = int(user_input('Index to Delete: '))
		destroy(item_index)

	# Print all items
	elif function_code == 'P':
		list_all_items()

	# Mark as complete
	elif function_code == 'M':
		completed_item = int(user_input('Index to Mark: '))
		mark_completed(completed_item)

	# Print Tutorial
	elif function_code == 'T':
		tutorial()

	# QUIT
	elif function_code == 'Q':
		print('===QUITTING PROGRAM===')
		return False

	# Catch all
	else:
		print('Unknown Option. Please try again.')
	return True


def user_input(prompt):
	# the input function will display a message in the terminal
	# and wait for user input.
	user_input = input(prompt)
	return user_input

def tutorial():
	print('''===Listing Tutorial...===
C: Create
R: Read (single)
P: Print (all)
U: Update
M: Mark Item
D: Destroy
T: Tutorial
Q: Quit
===Tutorial Completed===
''')

def test_1():
	print('===Test 1 Starting===')
	print()
	create('purple sox')
	create('red cloak')

	read(0)
	read(1)

	list_all_items()
	update(0, 'purple socks')
	destroy(1)

	read(0)

	list_all_items()
	print('===Test 2 Complete===')
	print()


def test_2():
	# Your testing code here
	test_1()
	# Call your new function with the appropriate value
	print('===Test 2 Starting===')
	print()
	# Create a new value
	select('C')
	# View all results
	list_all_items()
	# Call function with new value
	select('R')
	# View single result
	select('M')
	# Mark items as completed
	select('P')
	# View all results
	# Continue until all code is run
	print('===Test 2 Complete===')
	# Continue to main program
	print('please continue to main program.\n')

test_2()

running = True
while running:
	selection = user_input('Input Command. (Type 'T' for Tutorial): ')
	running = select(selection)

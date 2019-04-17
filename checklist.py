'''
This file makes a terminal checklist.
You can add, remove, update, and read from this checklist.
An empty checkbox is added to every new item.
You can check or uncheck the item's checkbox.
'''
# here's the checklist
checklist = [] # Make the checklist a class

# This is CRUD:
# - Create
# - Read
# - Update
# - Delete

# Define CRUD for our checklist
def create(item):
	'''adds an item to the list'''
	print('appending item...\n')
	checklist.append('[ ] ' + str(item))

def read(index):
	'''prints an item on the list'''
	print('reading item...\n')
	print('{' + str(index) + '}: ' + checklist[index])

def update(index, item):
	'''changes an item on the list'''
	print('updating item...\n')
	checklist[index] = '[ ] ' + str(item)

def destroy(index):
	'''removes an item from the list'''
	print('destroying item...\n')
	checklist.pop(index)

def list_all_items():
	'''prints all items on the list'''
	print('printing all items...\n')
	index = 0
	for list_item in checklist:
		print('{' + str(index) + '}: ' + list_item)
		index += 1

# I created the 'mark completed' function here.
def mark_completed(index):
	'''adds a nice checkmark to indexed item'''
	print('toggling check on index...\n')
	# get string from checklist
	string = checklist[index]
	# mark unchecked string
	print(string[:4])
	if string[:4] == '[ ] ':
		string = string[:1] + 'x' + string[2:]
	# unmark checked string
	elif string[:4] == '[x] ':
		string = string[:1] + ' ' + string[2:]
	# there's no checkbox!
	else:
		raise ValueError('this string does not have a checkbox!')
	# update checklist with string
	checklist[index] = string

# The select functoin can create, read one item, or read all items.
def select(function_code):
	'''Tests for lowercase letters as well, 
		Swap the word index for number, so parents can understand
	'''
	# Create item
	if function_code == 'C':
		input_item = input_str('New Item Value: ')
		create(input_item)

	# Read item
	elif function_code == 'R':
		item_index = input_idx('Index to Read: ')
		# Remember that item_index must actually exist or our program will crash.
		read(int(item_index))

	elif function_code == 'U':
		item_index = int(input_idx('Index to Update: '))
		input_item = input_str('Update Item Value: ')
		update(item_index, input_item)


	elif function_code == 'D':
		item_index = int(input_idx('Index to Delete: '))
		destroy(item_index)

	# Print all items
	elif function_code == 'P':
		list_all_items()

	# Mark as complete
	elif function_code == 'M':
		completed_item = int(input_idx('Index to Mark: '))
		mark_completed(completed_item)

	# Print Tutorial
	elif function_code == '?':
		tutorial()

	# Run Test Suite
	elif function_code == 'T':
		test_1()
		test_2()

	# QUIT
	elif function_code == 'Q':
		print('===QUITTING PROGRAM===')
		return False

	# Catch all
	else:
		print('Unknown Option. Please try again.')
	return True

def input_str(prompt):
	# display a message in the terminal & await an input.
	output_str = str(input(prompt))
	return output_str
	
def input_idx(prompt):
	# Improve function names
	# display a message in the terminal & await an input.
	output_idx = int(input(prompt))
	if 0 <= output_idx < len(checklist):
		return output_idx
	else:
		print('Unknown Option. Please try again.')


def tutorial():
	# TODO: Keep semantics consistent, Explain UI of box
	print('''
┌────────────────────────────┐ 
│     ** INSTRUCTIONS **     │
╞════════════════════════════╡
│ C: create                  │
│ R: read one item           │
│ P: print all items         │
│ U: update                  │
│ M: (un)mark item           │
│ D: destroy                 │
│ ?: tutorial                │
│ T: run test suite          │
│ Q: quit                    │
└────────────────────────────┘
''')

def test_1():
	#TODO: Add asserts
	create('purple sox')
	create('red cloak')
	read(0)
	read(1)
	list_all_items()

	update(0, 'purple socks')
	destroy(1)
	read(0)
	destroy(0)
	list_all_items()

def test_2():
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
	# Delete it!
	select('D')
	# View all results
	list_all_items()
	# Continue to main program
	print('all tests successfully completed,\nplease continue to main program.\n')

def main():
	running = True
	print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ WELCOME TO CHECKLIST BUDDY ┃
┃                            ┃
┃ to access the instructions ┃
┃ enter `?` when prompted to ┃
┃   do so by the terminal.   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')
	while running:
		selection = input_str('Input Command: ')
		running = select(selection)

if __name__ == '__main__':
	main()

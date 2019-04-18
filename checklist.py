'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''
# here's the checklist
checklist = [] # Make the checklist a class

# This is CRUD:
# - Create
# - Read
# - Update
# - Delete

# Define CRUD for our checklist
def create(entry):
	'''
	adds one new entry to the end of the list
	'''
	checklist.append('[ ] ' + str(entry))

def read(index):
	'''
	prints one entry to the terminal from its index
	'''
	# set entry
	entry = checklist[index]

	# print starter box
	print('\n┌──┬─────────────────────────┐')

	if index < 10:
		index_str = ' ' + str(index)

	# do nothing to orient string
	else:
		index_str = str(index)

	# check length of entry to see if box fits
	if len(entry) <= 24:
		entry_str = entry + ' '*(24-len(entry)) + '│'

	# if it doesnt, break the boundries and keep going
	else:
		entry_str = entry

	print('│'+ index_str + '│ ' + entry_str)

	# print exiter box
	print('└──┴─────────────────────────┘\n')


def update(index, entry):
	'''
	changes the contents of one entry on the list
	note that this keeps the entry checked or unchecked
	'''
	checklist[index] = checklist[index][:4] + str(entry)


def destroy(index):
	'''
	removes one entry from the list
	'''
	checklist.pop(index)


def list_all_entries():
	'''
	prints all entries on the list
	'''
	index = 0
	chart = ''
	# print starter box
	print('\n┌──┬─────────────────────────┐')

	for entry in checklist:
		# add extra space to orient string
		if index < 10:
			index_str = ' ' + str(index)

		# do nothing to orient string
		else:
			index_str = str(index)

		# check length of entry to see if box fits
		if len(entry) <= 24:
			entry_str = entry + ' '*(24-len(entry)) + '│'

		# if it doesnt, break the boundries and keep going
		else:
			entry_str = entry

		# finally, print the entry to the terminal
		print('│'+ index_str + '│ ' + entry_str)

		# add one to iteration
		index += 1

	# print exiter box
	print('└──┴─────────────────────────┘\n')


def mark_completed(index):
	'''
	check an entry if it is unchecked
	uncheck an entry if it is checked
	---
	notice that the first four characters of an entry is:
	"[ ] " -OR- "[x] "
	this is useful to tell which entries have are checked.
	'''
	# get string from checklist
	string = checklist[index]

	# mark unchecked string
	if string[:4] == '[ ] ':
		string = string[:1] + 'x' + string[2:]

	# unmark checked string
	elif string[:4] == '[x] ':
		string = string[:1] + ' ' + string[2:]

	# there's no checkbox!
	else:
		raise ValueError('this entry does not have a checkbox')

	# update checklist with string
	checklist[index] = string


def select(function_code):
	'''
	Tests for lowercase letters as well, 
	Swap the word index for number, so parents can understand
	'''
	# Capitalize code before checking it
	function_code = function_code.upper()
	
	# Create entry
	if function_code == 'C':
		input_entry = input('Enter text for new entry: ')
		create(input_entry)

	# Print all entries
	elif function_code == 'P':
		if len(checklist) == 0:
			print('your checklist is empty!')
		else:
			list_all_entries()

	# Read entry
	elif function_code == 'R':
		if len(checklist) == 0:
			print('your checklist is empty!')
		else:
			entry_index = int(input_idx('Enter index of entry to read: '))
			read(int(entry_index))

	# Update entry
	elif function_code == 'U':
		if len(checklist) == 0:
			print('your checklist is empty!')
		else:
			entry_index = int(input_idx('Enter index of entry to update: '))
			input_entry = input('Enter new text for updated entry: ')
			update(entry_index, input_entry)

	# Delete entry
	elif function_code == 'D':
		if len(checklist) == 0:
			print('your checklist is empty!')
		else:
			entry_index = int(input_idx('Enter index of entry to delete: '))
			destroy(entry_index)

	# Mark as complete
	elif function_code == 'M':
		if len(checklist) == 0:
			print('your checklist is empty!')
		else:
			completed_entry = int(input_idx('Enter index of entry to mark: '))
			mark_completed(completed_entry)

	# Print Tutorial
	elif function_code == '?':
		tutorial()

	# Run Test Suite
	elif function_code == 'T':
		test_1()
		test_2()

	# QUIT
	elif function_code == 'Q':
		print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Goodbye!          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')
		return False

	# Catch all
	else:
		print('Unknown Option. Please try again.')

	return True

def input_idx(prompt):
	# Improve function names
	# display a message in the terminal & await an input.
	output_idx = input(prompt)
	if not output_idx.isdigit():
		print('INVALID! Please input a value below ' + str(len(checklist)) + '.\n')
		return input_idx(prompt)

	else:
		output_idx = int(output_idx)
		if 0 <= output_idx < len(checklist):
			return output_idx

		else:
			print('INVALID! Your index must be below ' + str(len(checklist)) + '.\n')
			return input_idx(prompt)


def tutorial():
	# TODO: Keep semantics consistent, Explain UI of box [ ]
	print('''
┌────────────────────────────┐ 
│     ** INSTRUCTIONS **     │
╞════════════════════════════╡
│ ?: view user manual        │
│ C: create a new entry      │
│ R: read one entry          │
│ P: print all entries       │
│ U: update one entry        │
│ M: mark or unmark an entry │
│ D: delete an entry         │
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
	list_all_entries()

	update(0, 'purple socks')
	destroy(1)
	read(0)
	destroy(0)
	list_all_entries()

def test_2():
	# Create a new value
	select('C')
	# View all results
	list_all_entries()
	# Call function with new value
	select('R')
	# View single result
	select('M')
	# Mark entries as completed
	select('P')
	# Delete it!
	select('D')
	# View all results
	list_all_entries()
	# Continue to main program
	print('all tests successfully completed,\nplease continue to main program.\n')

def main():
	running = True
	print('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ WELCOME TO CHECKLIST BUDDY ┃
┃     enter the ? symbol     ┃
┃  to view the user manual.  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
''')

	while running:
		selection = input('\nEnter Command: ')
		running = select(selection)

if __name__ == '__main__':
	main()

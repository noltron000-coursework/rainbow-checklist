# Lets make some noise :D
# We'll start with printing and functions.
print()

print("<=== Hello World ===>")
print("Welcome to THE CHECKLIST")

def my_fun_function(say_this):
	'''prints say_this to console'''
	print(say_this)

my_fun_function('Hello World')

# lets go through the motions of what an array can do
print("we are going to make some modifications to a list...")
checklist = [] # Create a "LIST" item
print(checklist)
checklist.append('Blue') # Add "BLUE" to  list
print(checklist)
checklist.append('Orange') # Add "ORANGE" to list
print(checklist)
checklist = ['Hello', 'World'] # Completely change list
print(checklist)
checklist[1] = 'Cats' # Change nature of one item
print(checklist)
checklist = ['Hello', 'World'] # change it back again
print(checklist)
checklist.pop(1) # remove final list item
print(checklist)

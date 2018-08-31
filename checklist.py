print("Hello World")

def my_fun_function(say_this):
	print(say_this)

my_fun_function('Hello World')

checklist = []
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
	checklist.append(item)

def read(index):
	return checklist[index]

checklist = ['Hello', 'World']
checklist[1] = 'Cats'
print(checklist)

def update(index, item):
	checklist[index] = item

checklist = ['Hello', 'World']
checklist.pop(1)
print(checklist)

def destroy(index):
	checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
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

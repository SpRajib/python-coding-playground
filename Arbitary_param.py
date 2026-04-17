def print_name(*args): # args is tuple
    print(args)
    print(args[2])

def print_name(*rajib):
    # print(rajib)
    # print(rajib[2])
    for a in rajib:
        print(a)

# print_name("Alice", "Bob", "Charlie", "David")

def get_sum_of_all_numbers(*numbers):
    print(sum(numbers))

def get_min_of_all_numbers(*numbers):
    print(min(numbers))

def get_max_of_all_numbers(*numbers):
    print(max(numbers))

get_sum_of_all_numbers(10, 20, 30, 40, 50)
get_min_of_all_numbers(10, 20, 5, 40, 50)
get_max_of_all_numbers(10, 200, 30, 40, 50)

def print_info(**kwargs): # Return value as dictionary
    print(kwargs)
    print(kwargs['age'])

print_info(name="Alice", age=30, city="New York")

def hello_world(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

def hello_world(fname,*args, **kwargs):
    print("First Name:", fname)
    print("Args:", args)
    print("Kwargs:", kwargs)

hello_world("Rajib",10, 20, name="Alice", age=30)
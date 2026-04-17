def hello(msg):
    def greet(*args,**kwargs):
        print("hello world")
        msg(*args,**kwargs)
        print("Hello python")
    return greet

@hello
def add(a,b):
    print(a+b)

add(1,2)
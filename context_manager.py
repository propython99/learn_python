# below example is written using the talk found here:
# https://www.youtube.com/watch?v=-tpn94V9vK4

# his github.com page has more details:
# https://github.com/banool/pycon-au-2019

# context managers manage the context, in the below example it is a file.
# the file is closed upon exiting the block
# i.e. read and write operations to that file will fail
# examples of resources that context managers can handle are:
# files, database connections, socket connections, manage threads and thread pools, etc.
# they also increase the readability of the code 
# Think of writing a file close every time. 
# Even worse think of closing a file every time after use.
# example of opening a file using a context manager below:
print("~~~~~~ Example 1 ~~~~~~")
with open("sample_file.txt") as f:
    content = f.read()
    print(content)

# suppressing errors without doing anything
print("~~~~~~ Example 2 ~~~~~~")
# without using a context manager 
def kill_process_without_context_manager(pid):
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError: #useful when the process doesn't exist
        pass

# using a context manager called suppress
from contextlib import suppress
def kill_process(pid):
    with suppress(ProcessLookupError):
        os.kill(pid, signal.SIGKILL)

print("~~~~~~ Example 3 ~~~~~~")
# context manager usecase with ThreadPool

# let's define some data
data = {
    "watermelon" : "delicious",
    "fruit" : "spectacular",
    "dairy" : "scary",
    "chicken" : "not cool"
}

# create a small function 
# that shows the nouns and the relevant adjectives
def myfunc(noun, adj):
    return f"{noun} is {adj}!"

from concurrent.futures import ThreadPoolExecutor

# Now bad version of using a ThreadPoolExecutor
pool = ThreadPoolExecutor()
for k,v in data.items():
    pool.submit(myfunc, k, v)
# wait on the results and do something with them.
# you would have to make sure the pool is shutdown to free up the computing resource
pool.shutdown()

# Good and safe version
# context managed!
with ThreadPoolExecutor() as pool:
    for k, v in data.items():
        pool.submit(myfunc, k, v)




print("~~~~~~ Example 4.1 ~~~~~~")
# you can create your own context manager
# In the custom context managers, you would have steps to 
# setup and tear down the resources you used.
class MyContextManager:
    def __enter__(self):
        print(f"Enter!")

    def __exit__(self, *exc):
        print("Exit!")

# this is how you call your context manager
with MyContextManager():
    print("Inside the block!")

print("~~~~~~ Example 4.2 ~~~~~~")
# Another example that shows a context manager that uses the as keyword
class FoodContextManager():
    def __init__(self, data):
        self.data = data
    
    def __enter__(self):
        print(f"Enter: {self.data}")
        return self.data
    
    def __exit__(self, *exc):
        print(f"Exit: {self.data}")

with FoodContextManager({"dairy": "yucky"}) as food:
    print(food)
    food["fruit"] = "delicious"


# usinga  contextmanager decorator
# this way you don't have to write a class and define enter and exit methods. Rather you can just do your entry(setup) logic and yield. At the end, you can use the exit (or the tear down) logic.
print("~~~~~~ Example 4.3 ~~~~~~")
from contextlib import contextmanager

@contextmanager
def food_context_manager(data):
    print(f"Enter! {data}")
    yield data
    print(f"Exit! {data}")

with food_context_manager({"dairy": "yucky"}) as food:
    food["veggies"] = "healthy"


####### Lets read about how scopes work when working with context managers.
# the variables defined inside the with block are still accessible outside of the block. The scope doesn't change. For variable defined after the "as" keyword, it will be inaccessible after the block because that resource will be closed by the context manager.
print("~~~~~~ Example 5.1 ~~~~~~")
with open("sample_file.txt") as f:
    msg = "hello context manager!"
print(msg) # this will print fine
content = f.read() # we will get a ValueError
print(content)
# ValueError: I/O operation on closed file.
# we will get a ValueError because f is closed by the context manager.
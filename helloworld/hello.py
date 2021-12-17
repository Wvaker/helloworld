# first python program
def hello(msg):
    # works only on Python 3.7+
    print(f"hello {msg}!")

    if __name__=="_main_":
        hello("world")
        hello("Alice")
        hello("Bob")
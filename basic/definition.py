def say_something():
    print("Hi!")

# say_something()

def say_something():
    s = 'hi'
    return s

result = say_something()
# print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif  color == 'green':
        return 'green pepper'
    else:
        return 'i don\'t know'
    
result = what_is_this('red')
print(result)
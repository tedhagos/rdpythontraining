
# simple solution to the switch statement

# simple val
def switch(val):
    foo = {
        'a': 1,
        'b': 2
    }
    return foo[val]

# switch with actions
def s2(val):
    return {
        'a': lambda x: print("lower case A"),
        'b': lambda x: print("lower case B")
    }[val](val)

print(switch('b'))
s2('b')
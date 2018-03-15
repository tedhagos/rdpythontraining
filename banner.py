

def display(message, border):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


if __name__ == "__main__":
    display("Hello World", "-")
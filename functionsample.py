
#display("Hello World", "*")

def display(message="Hi there", bannerchar="*"):
    # line = multiplybanner(bannerchar, len(message))
    line = bannerchar * len(message)
    print(line)
    print(message)
    print(line)

#display(bannerchar="-", message="Hello there",)
#display(message="Hi there", bannerchar="V")

display("Hello there world")
display(bannerchar="-")




# def multiplybanner(bannerchar, msglen):
#     retval = ""
#     for i in range(0,msglen):
#         retval = retval + bannerchar
#     return retval

# def sumTwoNumbers(a,b):
#     print(a + b)
#
# sumTwoNumbers(10)



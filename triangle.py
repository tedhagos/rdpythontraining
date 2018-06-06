
# solution for the simple case
# try:
#     layer = int(input("How many layer? "))
#     for i in range(1, layer + 1):
#         print(i * "*")
# except ValueError:
#     print("enter only integers")


# solution for the problem
def drawTriangle(layer=10, char="*"):
    for i in range(1, layer + 1):
        print(i * char)

numberOfLayers = input("How many layers? [ENTER] ")
whichCharToUse = input("Which character to use? [ENTER] ")

if len(numberOfLayers) > 0:
    numLay = int(numberOfLayers)
    drawTriangle(numLay, whichCharToUse)
else:
    drawTriangle()










import sys


def printstory():
    with open('story.tx', 'r') as s:
        storywords = []
        for i in s:
            words = i.split()
            for word in words:
                storywords.append(word)
    print(storywords)


if __name__ == "__main__":
    printstory()
    # for i in sys.argv:
    #     print(i)

    # if len(sys.argv) > 1:
    #     print(sys.argv[1])
    #     print(sys.argv[2])
    #     print(sys.argv[3])



'''
https://docs.python.org/ko/3/reference
'''


def main():
    sentence = "the early bird catches the worm."
    # sentence = "Actions Speak Louder Than Words."
    # sentence = "PRACTICE MAKES PERFECT."

    start = sentence[0]
    # print(start)

    remain = sentence[1:]
    # print(remain)

    upper = start.upper()
    # print(upper)

    lower = remain.lower()
    # print(lower)

    print("{}{}".format(upper, lower))

main()

stack = []


def push(item, top):
    top = top + 1
    stack.append(item)
    return top


def pop(top):
    item = None
    if stack[top] != None:
        item = stack[top]
        del stack[top]
        top = top - 1
        return item, top


def main():
    while 1:
        word1 = False
        while word1 is False:
            print("\nInput only alphabets.")

            word = input("\nInput Word: ").lower()
            word1 = word.isalpha()

        if word1 is True:

            reversed_str = ''
            top = -1

            for i in range(len(word)):
                push_top = push(word[i], top)
                top = push_top

            for i in range(len(stack)):
                word1, top1 = pop(top)
                reversed_str += word1
                top = top1

            if reversed_str == word:
                print("\nWord is a palindrome")
            else:
                print("\nWord not a palindrome")


main()

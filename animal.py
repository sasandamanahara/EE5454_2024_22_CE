import sys

def dog():
    print("Baw")

de cat():
    print("Meow")


def default():
    print('hello')

def main():
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()


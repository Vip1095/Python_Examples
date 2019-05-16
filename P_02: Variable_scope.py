x = 'Global x'


def test():
    # global x
    y = 'Local y'
    x = 'Local x'
    print(x + ',' + y)
    # prints 'Local x' and  'Local y'


if __name__ == '__main__':
    test()
    print(x)  # prints 'Global x'

# It means that if a variable is declared inside a function, we can use that variable inside function only.

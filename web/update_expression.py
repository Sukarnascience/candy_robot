def update_expression(new_expression):
    with open('expression.txt', 'w') as file:
        file.write(new_expression)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        update_expression(sys.argv[1])
    else:
        print("Usage: python update_expression.py [expression]")


# Use by : python update_expression.py happy

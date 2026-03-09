# This program prints a spruce made of stars (*). Added spruce tree function with centered whitespace logic. 
def spruce(size):
    """
    Prints a spruce of the given height using stars and spaces. The is always a single star centered at the base.
    """
    print("A spruce!")
    row = 1 
    while row <= size:
        spaces = " " * (size - row)
        stars = "*" * (2 * row - 1)
        print(spaces + stars)
        row += 1
    bottom_spaces = " " * (size - 1)
    print(bottom_spaces + "*")
if __name__ == "__main__":
    spruce(10)
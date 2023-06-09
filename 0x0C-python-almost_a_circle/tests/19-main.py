#!/usr/bin/python3
""" 19-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    # Save the list of rectangles to a file
    Rectangle.save_to_file(list_rectangles_input)

    # Load the list of rectangles from the file
    list_rectangles_output = Rectangle.load_from_file()

    # Print the original list of rectangles
    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    # Print the loaded list of rectangles
    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    # Save the list of squares to a file
    Square.save_to_file(list_squares_input)

    # Load the list of squares from the file
    list_squares_output = Square.load_from_file()

    # Print the original list of squares
    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    # Print the loaded list of squares
    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

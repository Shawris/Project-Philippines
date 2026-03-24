#This code prints out a square on letters depending on the user's input
#It then, according to the specific user's input, uses capitalised letters "A, B, C, D...." to create a box increasing its lettered layers by input
import string

def print_square(layers):
    # This gets the letters in the alphabet according to the specific numbered input (a-z)
    alphabet = string.ascii_uppercase
    
    # This then calculates the total width/height of the square
    size = 2 * layers - 1
    
    #Here it is iterated through each row and column according to the maximum distance and the corresponding line
    for row in range(size):
        line = ""
        for col in range(size):
            dist_row = abs(row - (layers - 1))
            dist_col = abs(col - (layers - 1))
            
            char_idx = max(dist_row, dist_col)
            line += alphabet[char_idx]
            
        print(line)

num_layers = int(input("Layers: "))
print_square(num_layers)

# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    if x % 2:
        return False
    elif x == 0:
        return False
    else:
        return True
    
    
print(is_even(12))
print(is_even(3))
print(is_even(0))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if is_even(num) is True:
    print("Even!")
else:
    print("Odd")

print(num)
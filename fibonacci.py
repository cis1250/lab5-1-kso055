#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_nums():
  while True:
    num = input("Enter how many terms of the Fibonacci sequence you wantL ")

    if num.isdigit():
        num = int(num)
        if num > 0:
          return num
        else:
          print("Please enter a positive number greater than zero.")
    else:
      print("Invalid input. Please enter a positive whole number.")

# Function 2: Generate Fibonacci sequence
def generate_fib(n):
  sequence = []
  a, b = 0, 1
  for i int range(n):
    sequence.append(a)
    a, b = b, a + b
return sequence

# Function 3: Print the Fibonacci sequence
def print_sequence(sequence):
  print("\nFibonacci sequence:")
  print(",".join(map(str, sequence)))

# Main
def main():
  num_terms = get_nums()
  fib_sequence = generate_fib(num_terms)
  print_sequence(fib_sequence)

# Run program
if __name__ == "__main__":
  main()

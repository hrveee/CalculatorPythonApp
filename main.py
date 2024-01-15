# creating add() function to add two numbers
def add(num1, num2):
  """This function is useful to add two numbers"""

  # save the sum in a variable
  totalSum = num1 + num2

  # return the totalSum value
  return totalSum


# creating subtract() function to subtract two numbers
def substract(num1, num2):
  """This function is useful to substract two numbers"""

  # save the difference in a variable
  totalDifference = num1 - num2

  # return the totalDifference value
  return totalDifference


# creating multiply() function to multiply
def multiply(num1, num2):
  """This function is useful to multiply two numbers"""

  # save the product in a variable
  totalProduct = num1 * num2

  # return the totalProduct value
  return totalProduct


# creating divide() function to divide
def divide(num1, num2):
  """This function is useful to divide two numbers"""

  # save the quotient in a variable
  totalQuotient = num1 / num2

  # return the totaQuotient value
  return totalQuotient


# creating main() function to call all functions
def main():
  """This function is useful to call all functions"""

  # print welcome message to user and give the user 5 options operation
  print("Hey user! Welcome to the calculator program\n")
  print("There are 4 math operations with one exit options (to the program)")
  print(
      "1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5. Exit")

  # looping the user input until user enter 5 as "5. Exit"
  while True:

    # try the program to catch any error
    try:
      choice = int(input("\nChoose between 1 - 5 options: "))

      # if user enter 1 as "1. Addition"
      if choice == 1:

        # ask user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # call add() function and save the result in a variable
        result = add(num1, num2)
        print("the result of {} + {} is {}".format(num1, num2, result))

      # if user enter 2 as "2. Substraction"
      elif choice == 2:

        # ask user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # call substract() function and save the result in a variable
        result = substract(num1, num2)
        print("the result of {} - {} is {}".format(num1, num2, result))

      # if user enter 3 as "3. Multiplication"
      elif choice == 3:
        # ask user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # call substract() function and save the result in a variable
        result = multiply(num1, num2)
        print("the result of {} * {} is {}".format(num1, num2, result))

      # if user enter 4 as "4. Division"
      elif choice == 4:
        # ask user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # call substract() function and save the result in a variable
        result = divide(num1, num2)
        print("the result of {} / {} is {}".format(num1, num2, result))

      # if user enter 5 as "5. Exit"
      elif choice == 5:
        exit()

      else:
        continue

    # print error message if user enter any other value than 1 - 5
    except ValueError:
      print(
          "\nSorry, your input is invalid. Please enter a valid input from the above of options, thank you!"
      )


# executing the main() function
if __name__ == "__main__":
  main()

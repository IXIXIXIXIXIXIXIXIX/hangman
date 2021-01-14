def fizz_buzz(input_number):

    try:
        char_convert = int(input_number)
    except:
        return "not a number" 

    if (input_number % 5 == 0) and (input_number % 3 == 0):
        return "FizzBuzz"

    elif input_number % 5 == 0:
        return "Buzz"

    elif input_number % 3 == 0:
        return "Fizz"

    return str(input_number)
def collatz (number):
    
    if (number % 2) == 0:
        val = (number // 2)
        print val
        return val
    else:
        val = (3 * number + 1)
        print val
        return val

# main function calls collatz to generate sequence 
if __name__ == "__main__":
    user_val = int(input("Enter integer: "))
    final_val = collatz (user_val)
    while (final_val != 1):
        final_val = collatz (final_val)
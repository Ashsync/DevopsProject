# Python3 program to add two numbers
num1 = 15
num2 = 12

# Adding two nos
sum = num1 + num2

# printing values
print("Sum of", num1, "and", num2 , "is", sum)

# Initialize a list Done By Tathya
my_list = [1, 2, 3, 4, 5]

# Interchange first and last elements  Done By Tathya
my_list[0], my_list[-1] = my_list[-1], my_list[0]

# Print the modified list  Done By Tathya
print("List after swapping first and last elements:", my_list)
#<<<<<<< ashishbranch
# this is me ashish  



# 21BEC037 - Rigal - Code to find prime numbers in a given range (SIEVE OF ERATOSTHENES)
def sieve_of_eratosthenes(n):
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries as true. A value in is_prime[i] will finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    p = 2  # Start with the first prime number

    while (p * p <= n):
        # If is_prime[p] is true, then it is a prime
        if is_prime[p]:
            # Updating all multiples of p to not prime
            for i in range(p*p, n+1, p):
                is_prime[i] = False
        p+=1

    # Collecting all prime numbers
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

# Example usage
if __name__ == "__main__":
    n = 30  # Find all primes up to 30
    prime_numbers = sieve_of_eratosthenes(n)
    print(f"Prime numbers up to {n}: {prime_numbers}")




# Odd and Even python program Done by Ayush Dubey
n1 = 3
if n1 % 2==0:
    print("This is Even number")
else:
    print("This is Odd number")
#>>>>>>> main

### RANDOM PASSWORD GENERATOR
import random
import string


# Generate a random password of the desired length
def gen_password(length):
    characters = (
        string.digits + string.punctuation + string.hexdigits + string.ascii_letters
    )
    password = "".join(random.choice(characters) for _ in range(length))
    return password


num_suffix = (
    lambda n: "th"
    if 10 <= n % 100 <= 20
    else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
)


def main():
    try:
        password_length = int(input("Enter the desired length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        if password_length <= 0:
            print("Please enter a valid password length.")
            return

        for _ in range(num_passwords):
            password = gen_password(password_length)
            print(f"{_ + 1}{num_suffix(_ + 1)}", "Password: ", password)

    except ValueError:
        print("Please enter a valid integer for the password length.")


if __name__ == "__main__":
    main()

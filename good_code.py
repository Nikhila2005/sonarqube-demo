import os
import secrets
import subprocess


def calculate_division(num1, num2):
    """
    Safely divide two numbers.
    """
    if num2 == 0:
        raise ValueError("Division by zero is not allowed.")

    return num1 / num2


def login(username, password_input):
    """
    Simulated secure login.
    """
    stored_password = os.getenv("APP_PASSWORD")

    if stored_password is None:
        raise EnvironmentError("Password environment variable not set.")

    return username == "admin" and password_input == stored_password


def secure_random_token():
    """
    Generate secure random token.
    """
    token = secrets.token_hex(16)
    return token


def safe_command_execution():
    """
    Safe subprocess execution without shell=True.
    """
    result = subprocess.run(
        ["echo", "Safe Execution"],
        check=True,
        capture_output=True,
        text=True
    )

    return result.stdout


def display_numbers():
    """
    Display numbers cleanly.
    """
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        print(number)


def main():
    """
    Main application flow.
    """
    try:
        result = calculate_division(10, 2)
        print(f"Division Result: {result}")

        token = secure_random_token()
        print(f"Generated Token: {token}")

        output = safe_command_execution()
        print(output)

        display_numbers()

    except ValueError as error:
        print(f"Application Error: {error}")

    except subprocess.SubprocessError as error:
        print(f"Subprocess Error: {error}")


if __name__ == "__main__":
    main()

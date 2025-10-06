import streamlit as st

def check_password(password):
    """
    This function displays true when the password is strong and false when the password is not strong with a list of comments or rules that were not met.
   
    Parameters:
    password 

    Returns:
    True (If the password is strong.)
    False (If the password is weak.)
    List of comments (If the password is not strong it returns a list of rules that were not met.)   
    """
    comments = []  # List to hold comments about password strength
    common_passwords = ["password", "123456", "qwerty", "letmein", "123456789", "12345678", "12345", "qwerty", "qwerty123",
    "111111", "123123", "abc123", "password1", "iloveyou", "000000", "letmein",
    "monkey", "dragon", "sunshine", "football", "admin", "welcome", "login",
    "princess", "solo", "starwars", "baseball", "hello", "freedom", "whatever",
    "trustno1", "654321", "superman", "asdfghjkl", "pokemon", "liverpool",
    "charlie", "computer", "michelle", "jordan", "tigger", "purple", "ginger",
    "summer", "ashley", "buster", "hannah", "michael", "daniel", "hunter",
    "shadow", "minecraft", "qwertyuiop", "qazwsx", "qwert", "qwe123", "qweasd",
    "1q2w3e4r", "1qaz2wsx", "12qwaszx", "q1w2e3r4", "zaq12wsx", "zaq12wsxc",
    "admin123", "welcome123", "password123", "letmein123", "pass123", "secret",
    "default", "root", "user", "guest", "oracle", "mysql", "postgres",
    "11111111", "aaaaaa", "abc12345", "abc123456", "qwerty1", "qwerty12", "qwerty1234",
    "qwerty!", "1234567", "987654321", "696969", "football1", "monkey1", "dragon1",
    "p@ssw0rd", "pa$$w0rd", "passw0rd", "password!", "password01", "welcome1",
    "admin1", "admin01", "login123", "letmein1"]

    if len(password) < 8 or len(password) > 64:
        comments.append("* The password should be at least 8 characters long and at most 64 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    special_characters = "!@#$%^&*()-_+={}[]:;,<.>?/\\|`"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        elif char.isspace():
            has_space = True

    if not has_upper:
        comments.append("* Please include at least one uppercase letter.")
    if not has_lower:
        comments.append("* Please include at least one lowercase letter.")
    if not has_digit:
        comments.append("* Please include at least one number.")
    if not has_special:
        comments.append("* Please include at least one special character.")
    if has_space:
        comments.append("* The password must not contain any spaces.")
    
    if password.isalpha():
        comments.append("* The password must not be entirely alphabetic.")
    if password.isdigit():
        comments.append("* The password must not be entirely numeric.")

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            comments.append("* The password must not contain 3 or more identical consecutive characters or numbers.")
            break  

    if password in common_passwords:
        comments.append("* The password must not be a common password.")

    is_good = len(comments) == 0
    return is_good, comments


st.title("Check password project by Group 2")

password = st.text_input("Enter a password:", type="password")

if password:
    comments = check_password(password)
    if not comments:
        st.success("Great job! Your password is secure and ready to use. Keep it safe!")
    else:
        st.error("Oops your password is weak. Please try again and follow these comments to make it strong.")
        for comment in comments:
            st.write(comment)
        st.info("Please enter a strong password.")

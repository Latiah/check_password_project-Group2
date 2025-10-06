import streamlit as st

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        color: #333333;
    }
    .password-title {
        color: #4B0082;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
    }
    .success {
        color: #2E8B57;
        font-weight: bold;
    }
    .error {
        color: #B22222;
        font-weight: bold;
    }
    .comment {
        margin-left: 20px;
        color: #555555;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

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

    # --- Length Check ---
    if len(password) < 8 or len(password) > 64:
        comments.append("* The password should be at least 8 characters long and at most 64 characters long.")

    # --- Character Types ---
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
    
    # --- Entirely Alphabetic or Numeric ---
    if password.isalpha():
        comments.append("* The password must not be entirely alphabetic.")
    if password.isdigit():
        comments.append("* The password must not be entirely numeric.")

    # --- Repeated Characters ---
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            comments.append("* The password must not contain 3 or more identical consecutive characters or numbers.")
            break  

    # --- Common Passwords Check ---
    if password in common_passwords:
        comments.append("* The password must not be a common password.")

    return comments


# --- Streamlit UI ---
st.markdown('<div class="password-title">🔒 Password Strength Checker</div>', unsafe_allow_html=True)

password = st.text_input("Enter your password here:", type="password")

if password:
    observations = check_password(password)
    if not observations:
        st.markdown('<p class="success">✅ Great job! Your password is strong and ready to use. Keep it safe!</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="error">⚠️ Oops! Your password is weak. Follow the tips below:</p>', unsafe_allow_html=True)
        for comment in observations:
            st.markdown(f'<p class="comment">• {comment}</p>', unsafe_allow_html=True)
        st.info("💡 Tip: Use a mix of letters, numbers, and symbols to create a stronger password.")

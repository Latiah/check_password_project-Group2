import streamlit as st
import time

# ---------- Page Setup ----------
st.set_page_config(page_title="Password Strength Checker — Group 2", page_icon="🔒", layout="centered")

# ---------- Custom Styling ----------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

        html, body {
            background: linear-gradient(120deg, #0f172a, #1e293b, #334155);
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .main {
            background: #1e293b;
            border-radius: 25px;
            padding: 40px;
            box-shadow: 0 0 25px rgba(255,255,255,0.1);
            animation: fadeIn 1.2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            text-align: center;
            color: #38bdf8;
            font-size: 2.4rem;
            margin-bottom: 0;
        }
        .subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 18px;
            margin-bottom: 40px;
        }
        .comment-box {
            background: #0f172a;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            color: #fca5a5;
            border-left: 4px solid #ef4444;
        }
        .success-box {
            background: #064e3b;
            padding: 15px;
            border-radius: 12px;
            color: #bbf7d0;
            border-left: 4px solid #22c55e;
        }
        .progress-container {
            background-color: #1e293b;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
        }
        .footer {
            text-align: center;
            color: #94a3b8;
            margin-top: 30px;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 160px;
            margin-bottom: 10px;
            animation: fadeIn 2s ease-in;
        }
        .qr-section {
            text-align: center;
            margin-top: 40px;
            animation: fadeIn 2s ease-in;
        }
        .fade-in {
            animation: fadeIn 1.5s ease-in;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Password Check Function ----------
def check_password(password):
    comments = []
    common_passwords = [
        "password", "123456", "qwerty", "letmein", "admin", "welcome", "root", "guest", "football", "dragon"
    ]

    if len(password) < 8 or len(password) > 64:
        comments.append("The password should be between 8 and 64 characters long.")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=<>?/\\|{}[]:;" for c in password)
    has_space = any(c.isspace() for c in password)

    if not has_upper:
        comments.append("Include at least one uppercase letter.")
    if not has_lower:
        comments.append("Include at least one lowercase letter.")
    if not has_digit:
        comments.append("Include at least one numeric character.")
    if not has_special:
        comments.append("Include at least one special character (e.g. !@#$%).")
    if has_space:
        comments.append("Remove spaces — they are not allowed.")

    if password in common_passwords:
        comments.append("Avoid using a common password for better security.")

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            comments.append("Avoid using 3 or more identical consecutive characters.")
            break

    return comments

# ---------- UI Layout ----------
st.markdown(f"""
    <img src="https://github.com/gracekitonyi-bit/gracekitonyi-bit-daily-reports/blob/main/AIMS_Logo.jpeg?raw=true" class="logo"/>
    <h1>Password Strength Checker</h1>
    <div class="subtitle">A Collaborative Project by <b>Group 2</b><br>Presented at AIMS 2025</div>
""", unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password", help="Enter a password to test its strength")

if password:
    with st.spinner("Analyzing password strength..."):
        time.sleep(1)

    observations = check_password(password)
    strength = 100 - (len(observations) * 15)
    strength = max(strength, 0)

    st.progress(strength / 100)

    if not observations:
        st.markdown("<div class='success-box fade-in'>Excellent! Your password is strong and well structured.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='comment-box fade-in'>Your password can be improved. Please review the following suggestions:</div>", unsafe_allow_html=True)
        for comment in observations:
            st.markdown(f"<div class='comment-box'>{comment}</div>", unsafe_allow_html=True)

    if strength < 50:
        st.warning("Password Strength: Weak")
    elif strength < 80:
        st.info("Password Strength: Moderate")
    else:
        st.success("Password Strength: Strong")

else:
    st.info("Please enter a password to begin analysis.")

# ---------- QR Section ----------
st.markdown("""
    <div class="qr-section">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=https://check-password-group2.streamlit.app" width="160">
        <p style="color:#cbd5e1;">Scan the QR code to access the Password Strength Checker online.</p>
    </div>
""", unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("""
    <div class="footer">
        © 2025 Group 2 | AIMS Project Presentation
    </div>
""", unsafe_allow_html=True)

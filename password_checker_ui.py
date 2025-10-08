import streamlit as st
import time

# ---------- Page Configuration ----------
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# ---------- Custom CSS Styling ----------
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #0f172a, #1e293b, #334155);
            color: white;
        }
        .main {
            background: #1e293b;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 0 20px rgba(255,255,255,0.1);
        }
        h1 {
            text-align: center;
            color: #38bdf8;
            font-family: 'Poppins', sans-serif;
        }
        .subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .comment-box {
            background: #0f172a;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: #fca5a5;
            border-left: 4px solid #ef4444;
        }
        .success-box {
            background: #064e3b;
            padding: 15px;
            border-radius: 10px;
            color: #bbf7d0;
            border-left: 4px solid #22c55e;
        }
        .progress-container {
            background-color: #1e293b;
            border-radius: 10px;
            padding: 10px;
            margin-top: 10px;
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
        comments.append("🔸 Must be between 8–64 characters.")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=<>?/\\|{}[]:;" for c in password)
    has_space = any(c.isspace() for c in password)

    if not has_upper:
        comments.append("🔸 Add at least one uppercase letter.")
    if not has_lower:
        comments.append("🔸 Add at least one lowercase letter.")
    if not has_digit:
        comments.append("🔸 Add at least one number.")
    if not has_special:
        comments.append("🔸 Add at least one special character (!@#$%^&*).")
    if has_space:
        comments.append("🔸 Remove spaces.")

    if password in common_passwords:
        comments.append("🔸 Avoid using common passwords.")

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            comments.append("🔸 Avoid 3 or more identical consecutive characters.")
            break

    return comments

# ---------- UI Section ----------
st.markdown("<h1>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>A Cybersecurity project by <b>Group 2</b><br>Securing Digital Identities with Strong Passwords</div>", unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password")

if password:
    with st.spinner("Analyzing password strength..."):
        time.sleep(1)

    observations = check_password(password)
    strength = 100 - (len(observations) * 15)
    strength = max(strength, 0)

    # Strength bar visualization
    st.progress(strength / 100)

    if not observations:
        st.markdown("<div class='success-box'>✅ Excellent! Your password is strong and secure. Keep it safe!</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='comment-box'>⚠️ Weak password! Please review the feedback below:</div>", unsafe_allow_html=True)
        for comment in observations:
            st.markdown(f"<div class='comment-box'>{comment}</div>", unsafe_allow_html=True)

    if strength < 50:
        st.warning("Password strength: Weak ⚠️")
    elif strength < 80:
        st.info("Password strength: Moderate 🟡")
    else:
        st.success("Password strength: Strong ✅")

else:
    st.info("👆 Please enter a password to analyze.")

# ---------- Footer ----------
st.markdown("""
    <hr>
    <div style="text-align:center; color:#94a3b8;">
        Made with ❤️ by <b>Group 2</b> | Cybersecurity Project 2025
    </div>
""", unsafe_allow_html=True)

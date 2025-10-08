import streamlit as st
import random
import time

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Password Strength Checker — Group 2", page_icon="🔐", layout="centered")

# ---------- CUSTOM STYLING ----------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        body {
            background: linear-gradient(-45deg, #0f172a, #1e293b, #334155, #1e3a8a);
            background-size: 400% 400%;
            animation: gradientMove 10s ease infinite;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        h1 { text-align: center; color: #38bdf8; font-size: 2.6rem; margin-bottom: 0; }
        .subtitle { text-align: center; color: #cbd5e1; font-size: 18px; margin-bottom: 25px; }
        .comment-box { background: #0f172a; padding: 12px 18px; border-radius: 12px; margin-bottom: 10px; color: #fca5a5; border-left: 4px solid #ef4444; animation: fadeIn 1s ease-in; }
        .success-box { background: #064e3b; padding: 15px; border-radius: 12px; color: #bbf7d0; border-left: 4px solid #22c55e; animation: fadeIn 1s ease-in; }
        .footer { text-align: center; color: #94a3b8; margin-top: 30px; }
        .logo { display: block; margin: 0 auto; width: 95%; max-width: 700px; border-radius: 10px; animation: fadeIn 2s ease-in; margin-bottom: 15px; }
        .qr-section { text-align: center; margin-top: 40px; animation: fadeIn 2s ease-in; }
        .fade-in { animation: fadeIn 1.5s ease-in; }
    </style>
""", unsafe_allow_html=True)

# ---------- PASSWORD CHECK FUNCTION ----------
def check_password(password):
    comments = []
    common_passwords = ["password", "123456", "qwerty", "letmein", "admin", "welcome", "root", "guest", "football", "dragon"]

    if len(password) < 8 or len(password) > 64:
        comments.append("🔸 Must be between 8–64 characters long.")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=<.>?/\\|{}[]:;~" for c in password)
    has_space = any(c.isspace() for c in password)

    if not has_upper:
        comments.append("🔸 Add at least one uppercase letter.")
    if not has_lower:
        comments.append("🔸 Add at least one lowercase letter.")
    if not has_digit:
        comments.append("🔸 Add at least one number.")
    if not has_special:
        comments.append("🔸 Add at least one special character such as ! @ # $ % ^ & * ( ) - _ + = [ ] { } ; : ' , < . > / ? | ~")
    if has_space:
        comments.append("🔸 Remove spaces — they weaken the password.")
    if password in common_passwords:
        comments.append("🔸 Avoid using common passwords.")

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            comments.append("🔸 Avoid 3 or more identical consecutive characters.")
            break

    return comments

# ---------- STRONG PASSWORD SUGGESTIONS ----------
def generate_strong_passwords():
    words = ["Sky", "River", "Quantum", "Matrix", "Secure", "Flame", "Orbit", "Pulse", "Vertex", "Nova"]
    symbols = ["@", "#", "$", "%", "&", "*"]
    suggestions = []
    for _ in range(3):
        password = random.choice(words) + str(random.randint(10, 99)) + random.choice(symbols) + random.choice(words)
        suggestions.append(password)
    return suggestions

# ---------- UI HEADER ----------
st.markdown("""
    <img src="https://github.com/Latiah/check_password_project-Group2/blob/main/aimslogo.jpg?raw=true" class="logo"/>
    <h1>🔐 Password Strength Checker</h1>
    <div class="subtitle">An Interactive Project by <b>Group 2</b> — AIMS 2025</div>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "password" not in st.session_state:
    st.session_state.password = ""

# ---------- USER INPUT ----------
password = st.text_input("Enter your password:", value=st.session_state.password, type="password", help="Try typing a password to see how strong it is")

if password:
    with st.spinner("Analyzing password strength... 🔍"):
        time.sleep(1)

    observations = check_password(password)
    strength = 100 - (len(observations) * 15)
    strength = max(strength, 0)

    # Determine color for progress bar
    if strength < 50:
        color = "red"
    elif strength < 80:
        color = "orange"
    else:
        color = "green"

    # Display progress bar
    st.markdown(f"""
        <div style="background-color:#1e293b; border-radius:10px; padding:5px;">
            <div style="width:{strength}%; background-color:{color}; height:15px; border-radius:8px;"></div>
        </div>
    """, unsafe_allow_html=True)

    # Password strength messages
    if len(observations) == 0:
        st.success("Password Strength: Strong ✅")
        st.markdown("<div class='success-box fade-in'>🎉 Excellent! Your password is strong, secure, and ready to use. Great job!</div>", unsafe_allow_html=True)
    else:
        if strength < 50:
            st.error("Password Strength: Weak ⚠️")
        elif strength < 80:
            st.info("Password Strength: Moderate 🟡")

        st.markdown("<div class='comment-box fade-in'>⚠️ Your password needs improvement. Here's what to fix:</div>", unsafe_allow_html=True)
        for comment in observations:
            st.markdown(f"<div class='comment-box'>{comment}</div>", unsafe_allow_html=True)

        st.warning("💡 Don’t worry — even experts refine their passwords! You’re learning to stay secure 💪")

        # Clickable Tab for Suggestions
        with st.expander("💡 View Strong Password Suggestions"):
            st.markdown("Click on a suggestion below to auto-fill 👇")
            for suggestion in generate_strong_passwords():
                if st.button(suggestion, key=suggestion, use_container_width=True):
                    st.session_state.password = suggestion
                    st.rerun()

else:
    st.info("👆 Enter a password or choose one from the suggestions below.")

# ---------- QR CODE ----------
st.markdown("""
    <div class="qr-section">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=https://check-password-group2.streamlit.app" width="180">
        <p style="color:#cbd5e1;">📱 Scan the QR code to access this tool online.</p>
    </div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
    <div class="footer">
        Made with ❤️ by <b>Group 2</b> | AIMS 2025 Presentation
    </div>
""", unsafe_allow_html=True)

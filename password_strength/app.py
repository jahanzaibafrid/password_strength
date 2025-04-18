import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# ---- UI Heading ----
st.title("🔐 Live Password Strength Analyzer")
st.write("Check how strong your password is in real-time!")

# ---- Password Input ----
password = st.text_input("Enter your password:", type="password")

# ---- Strength Check Logic ----
def analyze_password(pw):
    score = 0
    feedback = []

    if len(pw) >= 8:
        score += 1
    else:
        feedback.append("🔸 At least 8 characters required.")

    if re.search(r"[A-Z]", pw) and re.search(r"[a-z]", pw):
        score += 1
    else:
        feedback.append("🔸 Mix UPPER and lower case letters.")

    if re.search(r"\d", pw):
        score += 1
    else:
        feedback.append("🔸 Add at least one digit (0–9).")

    if re.search(r"[!@#$%^&*]", pw):
        score += 1
    else:
        feedback.append("🔸 Use a special character (!@#$%^&*).")

    return score, feedback

# ---- Output Section ----
if password:
    score, messages = analyze_password(password)

    st.subheader("Password Strength:")

    if score == 4:
        st.success("✅ Very Strong Password!")
    elif score == 3:
        st.info("💪 Good! But can be stronger.")
    elif score == 2:
        st.warning("⚠️ Weak password. Needs improvements.")
    else:
        st.error("❌ Very weak password!")

    # Progress Bar
    st.progress(score / 4)

    st.subheader("Suggestions:")
    for msg in messages:
        st.write("- " + msg)

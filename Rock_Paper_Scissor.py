import streamlit as st
import random

# ----------- Page Configuration -----------
st.set_page_config(
    page_title="Rock Paper Scissors",
    layout="centered",
    page_icon="🕹️"
)

# ----------- Title Section -----------
st.title("🪨 📄 ✂️ Rock, Paper, Scissors Game")
st.markdown("Test your luck against the computer! Choose your move and see who wins.")

# ----------- Game Options -----------
choices = ["Rock", "Paper", "Scissors"]
user_choice = st.radio("Choose your move:", choices, horizontal=True)

# ----------- Image Mapping -----------
image_urls = {
    "Rock": "https://raw.githubusercontent.com/Shyam-Singh-Bhargaw/rock-paper-scissor/main/rock.png",
    "Paper": "https://raw.githubusercontent.com/Shyam-Singh-Bhargaw/rock-paper-scissor/main/paper.png",
    "Scissors": "https://raw.githubusercontent.com/Shyam-Singh-Bhargaw/rock-paper-scissor/main/scissor.jpg"
}

# ----------- Game Logic Triggered on Button Click -----------
if st.button("Play 🎮"):
    computer_choice = random.choice(choices)

    st.divider()
    st.subheader("🎯 Game Snapshot")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🧍 You chose:**")
        st.image(image_urls[user_choice], caption=user_choice, width=180)

    with col2:
        st.markdown("**💻 Computer chose:**")
        st.image(image_urls[computer_choice], caption=computer_choice, width=180)

    # ----------- Outcome Calculation -----------
    outcomes = {
        ("Rock", "Scissors"): "🎉 You win!",
        ("Paper", "Rock"): "🎉 You win!",
        ("Scissors", "Paper"): "🎉 You win!",
        ("Rock", "Paper"): "😞 Computer wins!",
        ("Paper", "Scissors"): "😞 Computer wins!",
        ("Scissors", "Rock"): "😞 Computer wins!",
    }

    result = outcomes.get((user_choice, computer_choice), "🤝 It's a tie!")

    # ----------- Result Display -----------
    st.divider()
    st.subheader("🏆 Result")
    st.success(result)

    # ----------- Debug Information -----------
    with st.expander("🧠 See Debug Info"):
        st.write(f"User Choice ➜ `{user_choice}`")
        st.write(f"Computer Choice ➜ `{computer_choice}`")

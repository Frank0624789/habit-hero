import streamlit as st

#App title/app-looks config
st.set_page_config(page_title="Habit Hero", page_icon="🐱‍👓", layout="centered")
st.title("🐱‍👓 Habit Hero: Level Up Life 🎮")
st.subheader("Turn your daily routine into a series of engaging quests!")

#state memory vault init
if "xp" not in st.session_state:
    st.session_state.xp =0

import streamlit as st
from datetime import datetime, timedelta

#App title/app-looks config
st.set_page_config(page_title="Habit Hero", page_icon="🐱‍👓", layout="centered")
st.title("🐱‍👓 Habit Hero: Level Up Life 🎮")
st.subheader("Turn your daily routine into a series of engaging quests!")

#state memory vault init
if "xp" not in st.session_state:
    st.session_state.xp =0

if "habits" not in st.session_state:
    # A starting dictionary of habits and their completion status
    st.session_state.habits ={
        "Drink seven glasses of water": False,
        "Eat breakfast": False,
        "Spend an hour outside": False
    }


#Level up logic
player_level = (st.session_state.xp//100)+1
xp_remainder = st.session_state.xp % 100

#layout
col1, col2 = st.columns(2)
with col1:
   st.metric(label="Hero Level", value = player_level)
with col2:
    st.metric(label="Total XP", value = f"{st.session_state.xp}")

#Progress bar
st.progress(xp_remainder/100)
st.write(f"{xp_remainder}/100 XP to Level {player_level +1} ✨")
st.divider()

st.subheader("Today's Quests ⚔️")
for habit_name, is_done in list(st.session_state.habits.items()):
    
    #Rendering the checkbox
    check = st.checkbox(habit_name,value=is_done,key=habit_name, disabled = is_done)
    
    if check and not is_done:
        #If it gets checked and is false in the memory
        old_level = (st.session_state.xp//100)+1

        st.session_state.habits[habit_name] = True
        st.session_state.xp+=25
        new_level = (st.session_state.xp//100)+1

        if new_level>old_level:
            #Level up effect
            st.balloons()
            st.toast(f"🚀 LEVEL UP! You are now level {new_level}!")
        st.rerun()



st.divider()
st.subheader("➕ Craft a New Quest")

#Addin new habits
with st.form(key = "quest_crafter", clear_on_submit=True):
    new_habit = st.text_input("What habit do you want to track?", placeholder="e.g., Meditate for 10 mins")
    submit_button = st.form_submit_button("Add to Quest Log")

    if submit_button:
        if new_habit:
            if new_habit not in st.session_state.habits:
                st.session_state.habits[new_habit] = False
                st.toast(f"✅ Added quest: {new_habit}") # Clean pop-up message
                st.rerun()
            else:
                st.error("This habit already exists!")
        else:
            st.warning("Please type something first!")

st.divider()
#Daily reset timer
now = datetime.now()
midnight = datetime.combine(now.date()+timedelta(days=1),datetime.min.time())
time_remaining = midnight-now

hours, remainder = divmod(time_remaining.seconds,3600)
minutes, _ = divmod(remainder, 60)

st.metric(label="⏳ Time Remaining for Daily Quests", value=f"{hours}h {minutes}m")

# Milestone badges for levelling
st.subheader("🏆 Milestone Achievements")
badge_cols = st.columns(5)

# Milestones at Level 10, 20, 30, 40, 50
milestones = [10, 20, 30, 40, 50]
badge_images = [
    "https://img.icons8.com/isometric/50/bronze-medal.png",
    "https://img.icons8.com/isometric/50/silver-medal.png",
    "https://img.icons8.com/isometric/50/gold-medal.png",
    "https://img.icons8.com/isometric/50/diamond.png",
    "https://img.icons8.com/isometric/50/crown.png"
]

for i, milestone in enumerate(milestones):
    with badge_cols[i]:
        if player_level >= milestone:
            st.image(badge_images[i], width=50)
            st.caption(f"Lvl {milestone} Clear")
        else:
            st.image("https://img.icons8.com/isometric/50/lock.png", width=50)
            st.caption(f"Lvl {milestone}")
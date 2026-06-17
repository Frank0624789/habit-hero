import streamlit as st
from datetime import datetime, timedelta

#App title/app-looks config
st.set_page_config(page_title="Habit Hero", page_icon="🐱‍👓", layout="centered")
st.title("🐱‍👓 Habit Hero: Level Up Life 🎮")
st.subheader("Turn your daily routine into a series of engaging quests!")

#State memory vault init
if "xp" not in st.session_state:
    st.session_state.xp =0

if "habits" not in st.session_state:
    #List of dictionaries to track "type" and "completed" status cleanly
    st.session_state.habits = [
        {"name": "Drink seven glasses of water", "completed": False, "type": "default"},
        {"name": "Eat breakfast", "completed": False, "type": "default"},
        {"name": "Spend an hour outside", "completed": False, "type": "default"}
    ]
if "current_level" not in st.session_state:
    st.session_state.current_level = (st.session_state.xp // 100) + 1

if "last_reset_date" not in st.session_state:
    st.session_state.last_reset_date = datetime.now().date()

current_date = datetime.now().date()

#If the computer's current date is past our saved reset date, a new day has dawned!
if current_date > st.session_state.last_reset_date:
    #Filter out and delete all custom quests
    st.session_state.habits = [h for h in st.session_state.habits if h["type"] == "default"]
    #Reset completion statuses of the 3 default quests back to False
    for habit in st.session_state.habits:
        habit["completed"] = False
    #Save the new date to memory vault and refresh page
    st.session_state.last_reset_date = current_date
    st.toast("🌅 A new day dawns! Quests have reset.")
    st.rerun()

#Level up logic
player_level = (st.session_state.xp//100)+1
xp_remainder = st.session_state.xp % 100

if player_level > st.session_state.current_level:
    st.balloons()
    st.toast(f"🚀 LEVEL UP! Welcome to Level {player_level}!")
    #Update level tracking vault so it only fires once per level
    st.session_state.current_level = player_level

#Layout
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
for index, habit in enumerate(st.session_state.habits):
    habit_name = habit["name"]
    is_done = habit["completed"]
    quest_type = habit["type"]
    
    #Assign point values based on rules
    pts = 15 if (quest_type == "default") else (15000 if habit_name == "maxmilestonepython" else 25)
    label_text = f"{habit_name} (+{pts} XP)"
    #Render the checkbox
    check = st.checkbox(label_text, value=is_done, key=f"habit_{index}", disabled=is_done)
    if check and not is_done:
        st.session_state.habits[index]["completed"] = True
        st.session_state.xp += pts
        st.rerun()



st.divider()
st.subheader("➕ Craft a New Quest")

#Addin new habits
with st.form(key="quest_crafter", clear_on_submit=True):
    new_habit = st.text_input("What habit do you want to track?", placeholder="e.g., Meditate for 10 mins")
    submit_button = st.form_submit_button("Add to Quest Log")

    if submit_button:
        if new_habit:
            #Calculate total custom quests currently active
            custom_quest_count = sum(1 for h in st.session_state.habits if h["type"] == "custom")
            
            if custom_quest_count >= 7:
                st.error("🛡️ Quest log full! You can only maintain up to 7 custom habits at once.")
            elif any(h["name"].lower() == new_habit.lower() for h in st.session_state.habits):
                st.error("This habit already exists!")
            else:
                #Add with explicit custom type flag
                st.session_state.habits.append({"name": new_habit, "completed": False, "type": "custom"})
                st.toast(f"✅ Added custom quest: {new_habit}")
                st.rerun()
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

#Milestone badges for levelling
st.subheader("🏆 Milestone Achievements")
badge_cols = st.columns(5)

#Milestones at lvl 10, 20, 30, 40, 50
milestones = [10, 20, 30, 40, 50]
badge_images = [
    "images/Bronze.png",
    "images/Silver.png",
    "images/Gold.png",
    "images/Diamond.png",
    "images/Prestige.png"
]

for i, milestone in enumerate(milestones):
    with badge_cols[i]:
        if player_level >= milestone:
            st.image(badge_images[i], width=75)
            st.caption(f"Lvl {milestone} Clear")
        else:
            st.image("https://img.icons8.com/isometric/50/lock.png", width=50)
            st.caption(f"Lvl {milestone}")
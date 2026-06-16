import streamlit as st

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
    check = st.checkbox(habit_name,value=is_done,key=habit_name)
    
    if check and not is_done:
        st.session_state.habits[habit_name] = True
        st.session_state.xp+=25
        st.rerun()
        #If it gets checked and is false in the memory
    elif not check and is_done:
        st.session_state.habits[habit_name]=False
        st.session_state.xp -= 25
        st.rerun()
        #Reverse the points if unchecked but marked as done.

st.divider()
st.subheader("➕ Craft a New Quest")

#Addin new habits
new_habit = st.text_input("What habit do you want to track?", placeholder="e.g., Meditate for 10 mins")

if st.button("Add Habit to Quest Log"):
    if new_habit:
        if new_habit not in st.session_state.habits:
            #Add the habit to the memory w/ false value
            st.session_state.habits[new_habit] = False
            st.success(f"Added quest: {new_habit}")
            st.rerun()
        else:
            st.error("This habit already exists!")
    else:
        st.warning("Please type something first!")




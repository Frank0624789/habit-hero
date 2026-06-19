# 🐱‍👓 Habit Hero: Level Up Life 🎮

Turn your daily routine into an engaging fantasy RPG quest log! **Habit Hero** is a gamified habit tracker built with Python and Streamlit that helps you defeat procrastination, earn experience points (XP), and unlock milestone badges as you master your real-life daily goals.

Live Link: *https://habit-hero.streamlit.app/*

---

## 🚀 Features

* **Daily Quest Log:** Attack 3 default daily habits worth 15 XP each.
* **Custom Quest Crafting:** Add up to 7 custom daily habits worth 25 XP each.
* **Dynamic Leveling System:** Track your level progression and watch the screen erupt in balloons (`st.balloons`) every time you cross a 100 XP level boundary!
* **Live Midnight Reset Engine:** A real-time countdown timer locked to Eastern Time (EST) that automatically resets your quest checklist and clears custom habits at midnight.
* **Milestone Achievements:** Unlock profile badges (Bronze, Silver, Gold, Diamond, and Prestige medals) as your Hero Level climbs from 10 to 50.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Streamlit (UI & Stateful Session Storage)
* **Time Management:** `datetime`, `timedelta`, and `zoneinfo` (Timezone-aware EST alignment)

---

## 📦 Local Installation & Setup

Want to run Habit Hero locally on your computer? Follow these quick steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/habit-hero.git](https://github.com/YOUR_GITHUB_USERNAME/habit-hero.git)
    cd habit-hero
    ```

2.  **Set Up a Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install streamlit
    ```

4.  **Ensure Asset Folder Layout:**
    Make sure your local directory includes your custom badge icons in lowercase format:
    ```text
    habit-hero/
    ├── app.py
    └── images/
        ├── bronze.png
        ├── silver.png
        ├── gold.png
        ├── diamond.png
        ├── prestige.png
        └── lock.png
    ```

5.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

## 🎮 How to Play

1.  Launch the app to check your starting Hero Level.
2.  Complete your habits throughout the day and check them off to claim your XP rewards.
3.  Keep an eye on the **Daily Reset Timer**—make sure to cash in your quests before midnight cuts off your streak!

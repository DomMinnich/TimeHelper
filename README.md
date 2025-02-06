# Time Helper GUI
---
Sooo a clock in service I use does clock ins by minutes which can lead to some interesting hourly times like 8.21 or 9.03 which by the last work day could be hard to figure out how long your last day would be without going into overtime and going under your total. This app helps this!

A Python-based time management application developed by **Dominic Minnich**. This GUI tool lets you:
- Specify a **weekly target** of working hours.
- Track **hours worked** each day.
- Calculate **remaining hours** needed to meet your weekly goal.
- Visualize a **work period** via a pair of sliders (start/end time).

Enjoy a fade-in window effect, custom ttk theme styling, and real-time updates as you enter data.


![image](https://github.com/user-attachments/assets/f0c61e48-b8bc-4f33-9ee8-f2766a748f78)
![TimeApp](https://github.com/user-attachments/assets/2611e673-a62d-4f6e-804e-539a3e464370)

---

## Features

1. **Weekly Target Hours**  
   - Enter total weekly hours you aim to work.

2. **Hours Already Worked**  
   - Input hours worked for each weekday (Monday – Sunday).
   - Instantly see how many hours remain to hit your weekly target.

3. **Work Period Sliders**  
   - **Start Time** and **End Time** sliders.
   - Real-time display of the selected time range (12-hour format + duration).

4. **Automatic Adjustment**  
   - Press **Calculate Remaining Hours** to recalculate the leftover hours.
   - The End Time slider adjusts automatically based on your Start Time and the newly computed remaining hours.

5. **Fade-In Animation**  
   - Smoothly transition from transparent to fully visible on startup.

6. **Dark-Themed, Custom Styles**  
   - Dark background with green highlights.
   - Minimal, intuitive design.

---

## Getting Started

### Prerequisites
- **Python 3.8+** (older versions may still work, but this is recommended)
- **Tkinter** (commonly included by default with Python installations)

### Installation & Execution

1. **Clone or Download** the repository:
   ```bash
   git clone https://github.com/<YourUserName>/<RepoName>.git
   ```
   Or download the ZIP and extract it locally.

2. **Navigate to the Project Directory**:
   ```bash
   cd <RepoName>
   ```

3. **(Optional) Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

4. **Run the Application**:
   ```bash
   python time_helper_app.py
   ```
   The **Time Helper** GUI will open, fade in, and be ready for use.

---

## Usage

1. **Set Weekly Target**  
   - Default is 20 hours. Adjust as needed.

2. **Hours Already Worked**  
   - Enter your daily hours in the provided text fields.

3. **Calculate Remaining**  
   - Click the **Calculate Remaining Hours** button.
   - The label updates with how many hours you still need to work.
   - The end time slider shifts accordingly if you start at the chosen start time.

4. **Adjust Work Period**  
   - The sliders allow you to pick a start/end time.
   - The display updates in real time, showing a 12-hour format and a numeric duration (e.g., 8h 30m).

---
Enjoy your time management with **Time Helper**!

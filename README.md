# Website Time Tracker

## Overview
This is a **Python GUI application** that tracks the amount of time spent on different websites. It uses:
- **Tkinter** for the graphical user interface (GUI)
- **PyGetWindow** to detect the active browser window
- **Threading** to track time without freezing the UI

The program continuously monitors the active browser tab, logs the time spent on each website, and displays the results in a simple GUI.

---

## Features
✅ Tracks time spent on different websites in real-time  
✅ Displays results in a Tkinter GUI  
✅ Uses a background thread for tracking (prevents UI freezing)  
✅ Auto-updates every second  

---

## Installation
### **Step 1: Install Python (if not already installed)**
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### **Step 2: Install Required Libraries**
Run the following command in the terminal or command prompt:
```bash
pip install pygetwindow
```

---

## Usage
1. **Run the Script**
   ```bash
   python website_tracker.py
   ```
2. The application will open a **Tkinter window**.
3. It will track the **active browser window** and log the time spent on each website.
4. The data will automatically **refresh every second**.
5. Close the window to **stop tracking**.

---


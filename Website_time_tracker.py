import time
import pygetwindow as gw
import tkinter as tk
from threading import Thread

#Dictionary to store variables on website
website_times = {}
previous_site = None
start_time = time.time()

#function used to check the title name and then calculate current time on website
def track_websites():
    global previous_site, start_time

    while True:
        active_window = gw.getActiveWindow()
        if active_window:
            window_title = active_window.title

       
            if " - " in window_title:
                site = window_title.split(" - ")[-1]
            else:
                site = window_title  # Fallback case

            if site != previous_site:
                if previous_site:
                    elapsed = time.time() - start_time
                    website_times[previous_site] = website_times.get(previous_site, 0) + elapsed
                previous_site = site
                start_time = time.time()

        time.sleep(1)  

#constantly updates gui and refreshes with multithreading to stop gui crashing
def update_gui():
    text_widget.delete("1.0", tk.END) 
    for site, duration in website_times.items():
        text_widget.insert(tk.END, f"{site}: {duration:.2f} sec\n")
    root.after(1000, update_gui)  


tracking_thread = Thread(target=track_websites, daemon=True)
tracking_thread.start()

#sets up gui
root = tk.Tk()
root.title("Website Time Tracker")
root.geometry("400x300")

label = tk.Label(root, text="Time Spent on Websites", font=("Arial", 14))
label.pack()

text_widget = tk.Text(root, height=15, width=50)
text_widget.pack()


update_gui()


root.mainloop()

import subprocess
import customtkinter as ctk
from tkinter import messagebox

# Function to run commands without showing a console
def run_command(command):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.Popen(command, shell=True, startupinfo=si)

def shutdown():
    run_command("shutdown -s -t 0")

def cancel_shutdown():
    run_command("shutdown -a")

def reboot():
    run_command("shutdown -r -t 0")

def timed_shutdown():
    try:
        minutes = int(entry.get())
        seconds = minutes * 60
        run_command(f"shutdown -s -t {seconds}")
        messagebox.showinfo("Shutdown Scheduled", f"Shutdown scheduled in {minutes} minutes.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")

# GUI Setup
ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Blue theme

root = ctk.CTk()
root.title("Schedule Shutdown v1.0")
root.geometry("350x250")

# Buttons
ctk.CTkButton(root, text="Shutdown", command=shutdown, width=200, height=40).pack(pady=10)
ctk.CTkButton(root, text="Cancel Shutdown", command=cancel_shutdown, width=200, height=40).pack(pady=10)
ctk.CTkButton(root, text="Reboot", command=reboot, width=200, height=40).pack(pady=10)

# Timed Shutdown
frame = ctk.CTkFrame(root)
frame.pack(pady=10)

ctk.CTkLabel(frame, text="Shutdown in minutes:").pack(side="left", padx=5)
entry = ctk.CTkEntry(frame, width=50)
entry.pack(side="left", padx=5)
ctk.CTkButton(frame, text="Set", command=timed_shutdown, width=50).pack(side="left", padx=5)

root.mainloop()

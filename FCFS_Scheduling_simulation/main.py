import tkinter as tk
from tkinter import messagebox
from fcfs_algorithm import find_avg_time, plot_gantt_chart

# Create the tkinter window
root = tk.Tk()
root.title("FCFS Scheduling Algorithm")

# Input Frame
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=20, pady=20)

# Lists to store entry widgets for arrival and burst times
arrival_time_entries = []
burst_time_entries = []
processes = []  # This will hold the processes data

# Function to add a new process entry
def add_process_entry():
    row = len(arrival_time_entries) + 1

    tk.Label(input_frame, text=f"Process {row} Arrival Time:").grid(row=row, column=0, padx=5, pady=5)
    arrival_entry = tk.Entry(input_frame)
    arrival_entry.grid(row=row, column=1, padx=5, pady=5)
    arrival_time_entries.append(arrival_entry)

    tk.Label(input_frame, text=f"Process {row} Burst Time:").grid(row=row, column=2, padx=5, pady=5)
    burst_entry = tk.Entry(input_frame)
    burst_entry.grid(row=row, column=3, padx=5, pady=5)
    burst_time_entries.append(burst_entry)

# Output area for scheduling results and Gantt chart
output_frame = tk.Frame(root)
output_frame.grid(row=1, column=0, padx=20, pady=20)

# Function to get inputs, calculate scheduling, and update the Gantt chart
def add_process_and_update():
    try:
        process_id = len(processes) + 1
        arrival_time = int(arrival_time_entries[-1].get())
        burst_time = int(burst_time_entries[-1].get())
        processes.append([process_id, arrival_time, burst_time])

        # Sort processes by arrival time before scheduling
        processes.sort(key=lambda x: x[1])

        # Update the scheduling results and Gantt chart
        update_display()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for arrival and burst times.")

# Function to update display with scheduling results and Gantt chart
def update_display():
    # Clear previous output
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Find average time and update text
    find_avg_time(processes, len(processes), output_frame)

    # Plot Gantt chart
    plot_gantt_chart(processes, output_frame)

# Button to add new process entry
add_button = tk.Button(root, text="Add Process", command=add_process_entry)
add_button.grid(row=2, column=0, padx=20, pady=10)

# Button to add process and update scheduling
update_button = tk.Button(root, text="Add and Update", command=add_process_and_update)
update_button.grid(row=3, column=0, padx=20, pady=10)

# Add the first process input field on launch
add_process_entry()

# Main loop
root.mainloop()

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to calculate waiting time
def calculate_waiting_time(processes, n, waiting_time):
    service_time = [0] * n
    service_time[0] = processes[0][1]  # Service time for first process
    waiting_time[0] = 0  # First process has no waiting time

    for i in range(1, n):
        service_time[i] = service_time[i - 1] + processes[i - 1][2]
        waiting_time[i] = service_time[i] - processes[i][1]
        if waiting_time[i] < 0:
            waiting_time[i] = 0

# Function to calculate turnaround time
def calculate_turnaround_time(processes, n, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]

# Function to find average time for the processes
def find_avg_time(processes, n, output_frame):
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Find waiting and turnaround times
    calculate_waiting_time(processes, n, waiting_time)
    calculate_turnaround_time(processes, n, waiting_time, turnaround_time)

    # Create headers
    headers = ["Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time"]
    for idx, header in enumerate(headers):
        tk.Label(output_frame, text=header, relief="ridge", width=15).grid(row=0, column=idx)

    total_waiting_time = 0
    total_turnaround_time = 0

    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

        # Display each row of process data
        tk.Label(output_frame, text=f"P{processes[i][0]}", relief="ridge", width=15).grid(row=i+1, column=0)
        tk.Label(output_frame, text=f"{processes[i][1]}", relief="ridge", width=15).grid(row=i+1, column=1)
        tk.Label(output_frame, text=f"{processes[i][2]}", relief="ridge", width=15).grid(row=i+1, column=2)
        tk.Label(output_frame, text=f"{waiting_time[i]}", relief="ridge", width=15).grid(row=i+1, column=3)
        tk.Label(output_frame, text=f"{turnaround_time[i]}", relief="ridge", width=15).grid(row=i+1, column=4)

    # Display average waiting and turnaround times
    tk.Label(output_frame, text=f"Average Waiting Time: {total_waiting_time / n:.2f}", relief="ridge", width=30).grid(row=n+2, column=0, columnspan=2)
    tk.Label(output_frame, text=f"Average Turnaround Time: {total_turnaround_time / n:.2f}", relief="ridge", width=30).grid(row=n+2, column=2, columnspan=3)

# Function to plot Gantt chart
def plot_gantt_chart(processes, frame):
    fig, ax = plt.subplots(figsize=(8, 4))
    start_time = 0
    colors = ['red', 'blue', 'green', 'orange', 'purple']

    for i in range(len(processes)):
        ax.broken_barh([(start_time, processes[i][2])], (10, 9), facecolors=(colors[i % len(colors)]))
        ax.text(start_time + processes[i][2]/2, 15, f"P{processes[i][0]}", color='white', weight='bold', ha='center')
        start_time += processes[i][2]

    ax.set_xlabel('Time')
    ax.set_yticks([15])
    ax.set_yticklabels(['Processes'])
    ax.set_xticks(range(0, start_time + 1))
    ax.grid(True)

    # Clear previous Gantt chart
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    # Embed the chart in tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=0, columnspan=5)

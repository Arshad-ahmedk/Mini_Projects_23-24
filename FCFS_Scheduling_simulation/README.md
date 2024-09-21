# FCFS Scheduling Algorithm

## Overview

This project implements the First-Come, First-Served (FCFS) scheduling algorithm using Python. It provides a graphical user interface (GUI) for users to input process details, calculate scheduling metrics, and visualize the scheduling results in real-time.

The application uses `Tkinter` for the GUI and `Matplotlib` for generating the Gantt chart.

## Features

- **Add Processes**: Input arrival and burst times for multiple processes.
- **Real-Time Updates**: Update scheduling results and Gantt chart as processes are added.
- **Textual Output**: Displays waiting time, turnaround time, and averages for each process.
- **Gantt Chart Visualization**: Visual representation of process execution over time.

## Tech Stack

- **Python**: Programming language used for development.
- **Tkinter**: Library for creating the GUI.
- **Matplotlib**: Library for visualizing the Gantt chart.
- **FigureCanvasTkAgg**: Backend for embedding Matplotlib plots in Tkinter.

## Installation

To run this project, you need Python and the required libraries installed. Follow these steps to set up the environment:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/FCFS_Scheduling.git
   cd FCFS_Scheduling

2. **Install Dependencies**
   ```pip install matplotlib```

3. **Run the Application**
   Navigate to the project directory and run the ```main.py``` script:
   ```python main.py```

4. **Interact with the GUI**
- **Add Process**: Click the "Add Process" button to add input fields for arrival time and burst time.
- **Add and Update**: Fill in the arrival and burst times, then click the "Add and Update" button to add the process and refresh the results and Gantt chart.

5. **View Results**
- The textual output will display process details including arrival time, burst time, waiting time, and turnaround time.
- The Gantt chart will show a visual representation of process execution over time.

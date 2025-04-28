# Highest Response Ratio Next (HRRN) scheduling algorithm
from core.process import Process

def hrrn_schedule(processes):
    time = 0  # Current time in the simulation
    completed = 0  # Counter for completed processes
    n = len(processes)  # Number of processes
    processes = sorted(processes, key=lambda p: p.arrival_time)  # Sort by arrival time
    completed_processes = []  # List to store completed processes

    while completed < n:
        ready_queue = [p for p in processes if p.arrival_time <= time and p.completion_time is None]

        if not ready_queue:
            time += 1  # If no processes are ready, increment time
            continue

        # Calculate response ratios for each process in the ready queue
        for p in ready_queue:
            waiting_time = time - p.arrival_time
            p.response_ratio = (waiting_time + p.burst_time) / p.burst_time

        # Pick the process with the highest response ratio
        current_process = max(ready_queue, key=lambda p: p.response_ratio)

        # Set times
        current_process.start_time = time
        current_process.response_time = time - current_process.arrival_time
        time += current_process.burst_time
        current_process.completion_time = time
        current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time

        completed += 1
        completed_processes.append(current_process)

    return completed_processes

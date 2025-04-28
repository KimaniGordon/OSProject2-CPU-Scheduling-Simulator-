# Shortest Remaining Time First (SRTF) scheduling algorithm
from core.process import Process
import heapq

def srtf_schedule(processes):
    time = 0  # Current time in the simulation
    completed = 0  # Counter for completed processes
    n = len(processes)  # Number of processes
    processes = sorted(processes, key=lambda p: p.arrival_time)  # Sort by arrival time
    ready_queue = []  # Priority queue for ready processes
    current_process = None
    i = 0  # Index for tracking incoming processes

    while completed < n:
        # Add newly arrived processes to the ready queue
        while i < n and processes[i].arrival_time <= time:
            heapq.heappush(ready_queue, (processes[i].remaining_time, processes[i]))
            i += 1

        if ready_queue:
            _, current_process = heapq.heappop(ready_queue)

            # First time the process is being executed
            if current_process.start_time is None:
                current_process.start_time = time
                current_process.response_time = time - current_process.arrival_time

            # Simulate 1 unit of time for the current process
            current_process.remaining_time -= 1
            time += 1

            if current_process.remaining_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed += 1
            else:
                heapq.heappush(ready_queue, (current_process.remaining_time, current_process))
        else:
            # If no processes are ready, just increment time
            time += 1

    return processes

# core/main.py

from core.metrics import compute_metrics, print_metrics, to_dict
from core.process import Process
from core.schedulers.fcfs_scheduler import fcfs_schedule
from core.schedulers.hrrn_scheduler import hrrn_schedule
from core.schedulers.srtf_scheduler import srtf_schedule
from tabulate import tabulate 

# Example test processes
test_processes = [
    Process(pid=1, arrival_time=0, burst_time=5),
    Process(pid=2, arrival_time=1, burst_time=3),
    Process(pid=3, arrival_time=2, burst_time=8),
    Process(pid=4, arrival_time=3, burst_time=6),
]

# Run each algorithm
fcfs_completed = fcfs_schedule([p.copy() for p in test_processes])
fcfs_metrics = compute_metrics(fcfs_completed)
print_metrics("FCFS", fcfs_metrics)

hrrn_completed = hrrn_schedule([p.copy() for p in test_processes])
hrrn_metrics = compute_metrics(hrrn_completed)
print_metrics("HRRN", hrrn_metrics)

srtf_completed = srtf_schedule([p.copy() for p in test_processes])
srtf_metrics = compute_metrics(srtf_completed)
print_metrics("SRTF", srtf_metrics)

# Prepare data for comparison table
table_data = [
    ["FCFS", 
     fcfs_metrics["Average Waiting Time"],
     fcfs_metrics["Average Turnaround Time"],
     fcfs_metrics["Average Response Time"],
     fcfs_metrics["CPU Utilization (%)"],
     fcfs_metrics["Throughput (Processes per Second)"]],
     
    ["HRRN", 
     hrrn_metrics["Average Waiting Time"],
     hrrn_metrics["Average Turnaround Time"],
     hrrn_metrics["Average Response Time"],
     hrrn_metrics["CPU Utilization (%)"],
     hrrn_metrics["Throughput (Processes per Second)"]],
     
    ["SRTF", 
     srtf_metrics["Average Waiting Time"],
     srtf_metrics["Average Turnaround Time"],
     srtf_metrics["Average Response Time"],
     srtf_metrics["CPU Utilization (%)"],
     srtf_metrics["Throughput (Processes per Second)"]]
]

# Define headers
headers = ["Algorithm", "Avg Waiting Time", "Avg Turnaround Time", "Avg Response Time", "CPU Utilization (%)", "Throughput (proc/sec)"]

# Print table
print("\n=== Algorithm Comparison Table ===")
print(tabulate(table_data, headers=headers, floatfmt=".2f", tablefmt="grid"))

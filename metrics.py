# Function to compute various scheduling metrics for a list of processes
def compute_metrics(processes):
    n = len(processes)  # Number of processes
    if n == 0:
        return {}

    # Calculate the total waiting time, turnaround time, response time, and burst time
    total_waiting = sum(p.waiting_time for p in processes)
    total_turnaround = sum(p.turnaround_time for p in processes)
    total_response = sum(p.response_time for p in processes)
    total_burst = sum(p.burst_time for p in processes)

    # Calculate the start time and end time of the entire simulation
    start_time = min(p.arrival_time for p in processes)
    end_time = max(p.completion_time for p in processes)
    total_time = end_time - start_time

    # Return a dictionary of calculated metrics
    return {
        "Average Waiting Time": total_waiting / n,
        "Average Turnaround Time": total_turnaround / n,
        "Average Response Time": total_response / n,
        "CPU Utilization (%)": (total_burst / total_time) * 100 if total_time > 0 else 0,
        "Throughput (Processes per Second)": n / total_time if total_time > 0 else 0
    }

# Function to print the calculated metrics for a scheduling algorithm
def print_metrics(algorithm_name, metrics):
    print(f"\n--- {algorithm_name} Metrics ---")
    for k, v in metrics.items():
        print(f"{k}: {v:.2f}")

# Convert the metrics into a dictionary suitable for export or graphing
def to_dict(algorithm_name, metrics):
    return {
        "Algorithm": algorithm_name,
        **metrics
    }

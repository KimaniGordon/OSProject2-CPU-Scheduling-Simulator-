import json

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid  # Process ID
        self.arrival_time = arrival_time  # Arrival time of the process
        self.burst_time = burst_time  # Burst time (time needed for execution)
        self.remaining_time = burst_time  # Time remaining for the process to complete
        self.priority = priority  # Priority level (used in some scheduling algorithms)

        # For calculating process metrics after execution
        self.start_time = None  # When the process started
        self.completion_time = None  # When the process finished
        self.waiting_time = 0  # Time the process spends waiting in the ready queue
        self.turnaround_time = 0  # Total time the process spends from arrival to completion
        self.response_time = None  # Time from arrival to the first execution

    def __repr__(self):
        return (f"Process(pid={self.pid}, arrival={self.arrival_time}, "
                f"burst={self.burst_time}, priority={self.priority})")

    def reset(self):
        """Reset the process's runtime metrics so it can be reused in another simulation."""
        self.remaining_time = self.burst_time
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = None

    def copy(self):
        """Return a fresh copy of this process for independent scheduling runs."""
        # Creating a new Process ensures metrics start from clean state
        new_proc = Process(
            pid=self.pid,
            arrival_time=self.arrival_time,
            burst_time=self.burst_time,
            priority=self.priority
        )
        return new_proc

# Helper function to load process data from a JSON file

def load_processes_from_json(filepath):
    processes = []
    with open(filepath, 'r') as f:
        data = json.load(f)
        for item in data:
            p = Process(
                pid=item['pid'],
                arrival_time=item['arrival_time'],
                burst_time=item['burst_time'],
                priority=item.get('priority', 0)  # Default priority 0 if not specified
            )
            processes.append(p)
    return processes

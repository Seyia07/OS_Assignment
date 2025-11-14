"""
CPU Scheduling Algorithms Implementation
OS Assignment - https://github.com/Seyia07/OS_Assignment.git

Implements four scheduling algorithms:
1. First Come First Serve (FCFS)
2. Shortest Remaining Time First (SRTF)
3. Round Robin (RR)
4. Priority Scheduling (Preemptive)
"""

class Process:
    """Represents a process in the system"""
    def __init__(self, pid, arrival, burst, priority=0):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0
        self.remaining = burst

def fcfs(processes):
    """
    First Come First Serve (FCFS) - Non-preemptive
    Processes are executed in order of arrival time
    """
    processes.sort(key=lambda x: x.arrival)
    current_time = 0
    
    for p in processes:
        # If CPU is idle, jump to next process arrival
        if current_time < p.arrival:
            current_time = p.arrival
        
        # Execute process completely
        p.completion = current_time + p.burst
        p.turnaround = p.completion - p.arrival
        p.waiting = p.turnaround - p.burst
        current_time = p.completion
    
    return processes

def srtf(processes):
    """
    Shortest Remaining Time First (SRTF) - Preemptive
    Always execute the process with shortest remaining burst time
    """
    n = len(processes)
    remaining = [p.burst for p in processes]
    current_time = 0
    completed = 0
    
    while completed < n:
        # Find process with shortest remaining time
        shortest_idx = -1
        shortest_time = float('inf')
        
        for i in range(n):
            if (processes[i].arrival <= current_time and 
                remaining[i] > 0 and 
                remaining[i] < shortest_time):
                shortest_time = remaining[i]
                shortest_idx = i
        
        # No process available, CPU idle
        if shortest_idx == -1:
            current_time += 1
            continue
        
        # Execute process for 1 time unit
        remaining[shortest_idx] -= 1
        current_time += 1
        
        # Process completed
        if remaining[shortest_idx] == 0:
            completed += 1
            processes[shortest_idx].completion = current_time
            processes[shortest_idx].turnaround = current_time - processes[shortest_idx].arrival
            processes[shortest_idx].waiting = processes[shortest_idx].turnaround - processes[shortest_idx].burst
    
    return processes

def round_robin(processes, quantum):
    """
    Round Robin (RR) - Preemptive with time quantum
    Each process gets quantum time units in cyclic order
    """
    queue = []
    remaining = [p.burst for p in processes]
    current_time = 0
    completed = 0
    arrived = set()
    
    def add_arrived(time):
        """Add all processes that have arrived by given time to queue"""
        for i, p in enumerate(processes):
            if p.arrival <= time and i not in arrived and remaining[i] > 0:
                queue.append(i)
                arrived.add(i)
    
    # Add initial processes
    add_arrived(0)
    
    while completed < len(processes):
        # CPU idle
        if not queue:
            current_time += 1
            add_arrived(current_time)
            continue
        
        # Get next process from queue
        idx = queue.pop(0)
        execute_time = min(quantum, remaining[idx])
        remaining[idx] -= execute_time
        current_time += execute_time
        
        # Add newly arrived processes
        add_arrived(current_time)
        
        # Check if process completed
        if remaining[idx] == 0:
            completed += 1
            processes[idx].completion = current_time
            processes[idx].turnaround = current_time - processes[idx].arrival
            processes[idx].waiting = processes[idx].turnaround - processes[idx].burst
        else:
            # Process not finished, add back to queue
            queue.append(idx)
    
    return processes

def priority_preemptive(processes):
    """
    Priority Scheduling - Preemptive
    Higher number = Higher priority
    Always execute highest priority process
    """
    n = len(processes)
    remaining = [p.burst for p in processes]
    current_time = 0
    completed = 0
    
    while completed < n:
        # Find highest priority process
        highest_priority_idx = -1
        highest_priority = -1
        
        for i in range(n):
            if (processes[i].arrival <= current_time and 
                remaining[i] > 0 and 
                processes[i].priority > highest_priority):
                highest_priority = processes[i].priority
                highest_priority_idx = i
        
        # No process available, CPU idle
        if highest_priority_idx == -1:
            current_time += 1
            continue
        
        # Execute highest priority process for 1 time unit
        remaining[highest_priority_idx] -= 1
        current_time += 1
        
        # Process completed
        if remaining[highest_priority_idx] == 0:
            completed += 1
            processes[highest_priority_idx].completion = current_time
            processes[highest_priority_idx].turnaround = current_time - processes[highest_priority_idx].arrival
            processes[highest_priority_idx].waiting = processes[highest_priority_idx].turnaround - processes[highest_priority_idx].burst
    
    return processes

def print_results(algorithm_name, processes, show_priority=False):
    """Print formatted results table"""
    print(f"\n{'='*95}")
    print(f"Algorithm: {algorithm_name}")
    print(f"{'='*95}")
    
    # Header
    if show_priority:
        print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Completion':<13}{'Turnaround':<13}{'Waiting'}")
        print("-" * 95)
    else:
        print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}{'Completion':<13}{'Turnaround':<13}{'Waiting'}")
        print("-" * 85)
    
    # Process details
    for p in processes:
        if show_priority:
            print(f"{p.pid:<10}{p.arrival:<10}{p.burst:<10}{p.priority:<10}{p.completion:<13}{p.turnaround:<13}{p.waiting}")
        else:
            print(f"{p.pid:<10}{p.arrival:<10}{p.burst:<10}{p.completion:<13}{p.turnaround:<13}{p.waiting}")
    
    # Averages
    avg_waiting = sum(p.waiting for p in processes) / len(processes)
    avg_turnaround = sum(p.turnaround for p in processes) / len(processes)
    
    if show_priority:
        print("-" * 95)
    else:
        print("-" * 85)
    
    print(f"Average Waiting Time: {avg_waiting:.2f} units")
    print(f"Average Turnaround Time: {avg_turnaround:.2f} units")
    
    if show_priority:
        print(f"{'='*95}\n")
    else:
        print(f"{'='*85}\n")

def main():
    """Main function to run all scheduling algorithms"""
    
    print("\n" + "="*95)
    print(" "*25 + "CPU SCHEDULING ALGORITHMS")
    print(" "*20 + "Operating Systems Assignment")
    print(" "*15 + "Repository: https://github.com/Seyia07/OS_Assignment.git")
    print("="*95)
    
    # TASK 1: First Come First Serve (FCFS)
    print("\n" + ">"*3 + " TASK 1: First Come First Serve (FCFS)")
    fcfs_processes = [
        Process("P1", 0, 8),
        Process("P2", 1, 4),
        Process("P3", 2, 9),
        Process("P4", 3, 5)
    ]
    print_results("First Come First Serve (FCFS) - Non-preemptive", fcfs(fcfs_processes))
    
    # TASK 2: Shortest Remaining Time First (SRTF)
    print("\n" + ">"*3 + " TASK 2: Shortest Remaining Time First (SRTF)")
    srtf_processes = [
        Process("P1", 3, 1),
        Process("P2", 1, 4),
        Process("P3", 4, 2),
        Process("P4", 0, 6),
        Process("P5", 2, 3)
    ]
    print_results("Shortest Remaining Time First (SRTF) - Preemptive", srtf(srtf_processes))
    
    # TASK 3: Round Robin (RR)
    print("\n" + ">"*3 + " TASK 3: Round Robin (Time Quantum = 2)")
    rr_processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 1),
        Process("P4", 3, 2),
        Process("P5", 4, 3)
    ]
    print_results("Round Robin (RR) - Time Quantum = 2 units", round_robin(rr_processes, 2))
    
    # TASK 4: Priority Scheduling (Preemptive)
    print("\n" + ">"*3 + " TASK 4: Priority Scheduling (Preemptive)")
    print("Note: Higher number = Higher priority")
    priority_processes = [
        Process("P1", 0, 4, 2),
        Process("P2", 1, 3, 3),
        Process("P3", 2, 1, 4),
        Process("P4", 3, 5, 5),
        Process("P5", 4, 2, 5)
    ]
    print_results("Priority Scheduling - Preemptive (Higher number = Higher priority)", 
                  priority_preemptive(priority_processes), 
                  show_priority=True)

if __name__ == "__main__":
    main()
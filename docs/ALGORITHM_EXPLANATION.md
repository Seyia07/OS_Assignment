# CPU Scheduling Algorithms - Detailed Explanations

---

## Table of Contents

1. [First Come First Serve (FCFS)](#1-first-come-first-serve-fcfs)
2. [Shortest Remaining Time First (SRTF)](#2-shortest-remaining-time-first-srtf)
3. [Round Robin (RR)](#3-round-robin-rr)
4. [Priority Scheduling](#4-priority-scheduling-preemptive)

---

## 1. First Come First Serve (FCFS)

### Overview
FCFS is the simplest CPU scheduling algorithm where processes are executed in the order they arrive in the ready queue.

### How It Works
```
Step 1: Processes arrive and enter ready queue
Step 2: CPU assigned to first process in queue
Step 3: Process runs to completion (non-preemptive)
Step 4: Next process in queue gets CPU
Step 5: Repeat until all processes complete
```

### Example Walkthrough

**Given Processes:**
- P1: Arrival=0, Burst=8
- P2: Arrival=1, Burst=4
- P3: Arrival=2, Burst=9
- P4: Arrival=3, Burst=5

**Execution Timeline:**
```
Time 0-8:   P1 executes (arrived at 0)
Time 8-12:  P2 executes (arrived at 1, waited 7 units)
Time 12-21: P3 executes (arrived at 2, waited 10 units)
Time 21-26: P4 executes (arrived at 3, waited 18 units)
```

**Gantt Chart:**
```
|--- P1 ---|-- P2 --|--------- P3 ---------|---- P4 ----|
0          8       12                      21          26
```

### Advantages
✅ Simple to understand and implement  
✅ No starvation - every process eventually executes  
✅ Low overhead

### Disadvantages
❌ Convoy effect - short processes wait for long ones  
❌ High average waiting time  
❌ Not suitable for interactive systems

---

## 2. Shortest Remaining Time First (SRTF)

### Overview
SRTF is the preemptive version of Shortest Job First (SJF). The process with the smallest remaining burst time is executed next. A running process can be preempted if a new process arrives with shorter burst time.

### How It Works
```
Step 1: At each time unit, check all arrived processes
Step 2: Select process with shortest remaining time
Step 3: Execute selected process for 1 time unit
Step 4: Update remaining times
Step 5: Repeat until all processes complete
```

### Example Walkthrough

**Given Processes:**
- P1: Arrival=3, Burst=1
- P2: Arrival=1, Burst=4
- P3: Arrival=4, Burst=2
- P4: Arrival=0, Burst=6
- P5: Arrival=2, Burst=3

**Step-by-Step Execution:**

| Time | Available Processes | Remaining Times | Selected | Reason |
|------|-------------------|----------------|----------|---------|
| 0    | P4                | P4:6           | P4       | Only one available |
| 1    | P4, P2            | P4:5, P2:4     | P2       | P2 has shorter time |
| 2    | P4, P2, P5        | P4:5, P2:3, P5:3 | P2 | P2 running (tied with P5) |
| 3    | P4, P2, P5, P1    | P4:5, P2:2, P5:3, P1:1 | P1 | P1 shortest |
| 4    | P4, P2, P5, P3    | P4:5, P2:2, P5:3, P3:2 | P2 | P2 tied with P3 |

### Advantages
✅ Minimizes average waiting time  
✅ Optimal for batch systems  
✅ Good throughput

### Disadvantages
❌ Requires knowledge of burst times  
❌ Can cause starvation of long processes  
❌ High context switch overhead

---

## 3. Round Robin (RR)

### Overview
Round Robin assigns each process a fixed time quantum. Processes are executed in cyclic order, and if not completed within the quantum, they're moved to the back of the queue.

### How It Works
```
Step 1: Set time quantum (e.g., 2 units)
Step 2: Add arrived processes to ready queue
Step 3: Dequeue first process
Step 4: Execute for min(quantum, remaining_time)
Step 5: Add newly arrived processes to queue
Step 6: If process not finished, add back to queue
Step 7: Repeat until all processes complete
```

### Example Walkthrough

**Given Processes (Quantum = 2):**
- P1: Arrival=0, Burst=5
- P2: Arrival=1, Burst=3
- P3: Arrival=2, Burst=1
- P4: Arrival=3, Burst=2
- P5: Arrival=4, Burst=3

**Execution Timeline:**

| Time | Queue | Process Executed | Remaining After |
|------|-------|-----------------|-----------------|
| 0-2  | [P1] | P1 (2 units) | P1:3 |
| 2-4  | [P1, P2, P3] | P2 (2 units) | P2:1 |
| 4-5  | [P1, P3, P4] | P3 (1 unit) | P3:0 ✓ |
| 5-7  | [P1, P4, P5] | P1 (2 units) | P1:1 |
| 7-9  | [P4, P5, P1] | P4 (2 units) | P4:0 ✓ |
| 9-10 | [P5, P1] | P2 (1 unit) | P2:0 ✓ |
| 10-12| [P1, P5] | P5 (2 units) | P5:1 |
| 12-13| [P5, P1] | P1 (1 unit) | P1:0 ✓ |
| 13-14| [P5] | P5 (1 unit) | P5:0 ✓ |

**Gantt Chart:**
```
|-- P1 --|-- P2 --|P3|-- P1 --|-- P4 --|P2|-- P5 --|P1|P5|
0        2        4  5        7        9  10       12 13 14
```

### Choosing Time Quantum

**Too Small (e.g., 1 unit):**
- High context switch overhead
- More time spent switching than executing

**Too Large (e.g., 100 units):**
- Degenerates to FCFS
- Poor response time

**Optimal (e.g., 10-100ms in real systems):**
- Balance between overhead and response time
- Generally, quantum should be larger than context switch time

### Advantages
✅ Fair allocation of CPU  
✅ Good response time  
✅ No starvation  
✅ Suitable for time-sharing systems

### Disadvantages
❌ Higher average waiting time than SJF  
❌ Performance depends on quantum size  
❌ Higher context switch overhead

---

## 4. Priority Scheduling (Preemptive)

### Overview
Each process is assigned a priority. The CPU is allocated to the process with the highest priority. In preemptive mode, a running process can be interrupted if a higher priority process arrives.

**Note:** In our implementation, higher number = higher priority.

### How It Works
```
Step 1: Assign priorities to all processes
Step 2: At each time unit, check all arrived processes
Step 3: Select process with highest priority
Step 4: Execute selected process for 1 time unit
Step 5: If new higher priority process arrives, preempt current
Step 6: Repeat until all processes complete
```

### Example Walkthrough

**Given Processes:**
- P1: Arrival=0, Burst=4, Priority=2
- P2: Arrival=1, Burst=3, Priority=3
- P3: Arrival=2, Burst=1, Priority=4
- P4: Arrival=3, Burst=5, Priority=5
- P5: Arrival=4, Burst=2, Priority=5

**Step-by-Step Execution:**

| Time | Available | Priorities | Selected | Reason |
|------|-----------|-----------|----------|---------|
| 0    | P1        | P1:2      | P1       | Only process |
| 1    | P1, P2    | P1:2, P2:3 | P2      | Higher priority |
| 2    | P1, P2, P3 | P1:2, P2:3, P3:4 | P3 | Highest priority |
| 3    | P1, P2, P4 | P1:2, P2:3, P4:5 | P4 | Priority 5 |
| 4    | P1, P2, P4, P5 | P1:2, P2:3, P4:5, P5:5 | P4 | Running, same priority |

**Priority Levels:**
```
Priority 5: P4, P5 (highest)
Priority 4: P3
Priority 3: P2
Priority 2: P1 (lowest)
```

### Handling Priority Ties

When two processes have the same priority:
1. Continue executing the current process (if it's one of them)
2. If both are waiting, use FCFS (arrival time)

### Priority Assignment Strategies

**Static Priorities:**
- Assigned at process creation
- Don't change during execution
- Simpler to implement

**Dynamic Priorities:**
- Change based on behavior
- Aging: Increase priority of waiting processes
- Prevents starvation

### Advantages
✅ Important processes execute first  
✅ Flexible - can be adapted to needs  
✅ Good for real-time systems

### Disadvantages
❌ Can cause starvation of low-priority processes  
❌ Priority inversion problem  
❌ Difficult to assign appropriate priorities

### Solving Starvation: Aging

Gradually increase priority of waiting processes:
```python
def aging_priority_scheduling():
    for each time unit:
        for each waiting process:
            if waiting_time > threshold:
                increase_priority(process)
```

---

## Comparison Summary

| Feature | FCFS | SRTF | RR | Priority |
|---------|------|------|----|----|
| Preemptive | No | Yes | Yes | Yes |
| Starvation | No | Yes | No | Yes |
| Complexity | Low | Medium | Medium | Medium |
| Overhead | Low | Medium | High | Medium |
| Avg WT | High | Low | Medium | Low |
| Fairness | High | Low | High | Medium |
| Best For | Batch | Predictable loads | Interactive | Real-time |

---

## Key Takeaways

1. **No algorithm is perfect for all scenarios**
2. **FCFS:** Simple but inefficient
3. **SRTF:** Optimal for minimizing wait time but impractical
4. **Round Robin:** Best for fairness and interactive systems
5. **Priority:** Best when processes have different importance levels

---

**Repository:** https://github.com/Seyia07/OS_Assignment.git

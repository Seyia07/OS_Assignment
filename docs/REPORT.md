# CPU Scheduling Algorithms - Project Report

**Course:** Operating Systems  
**Date:** November 14, 2025  
**Repository:** https://github.com/Seyia07/OS_Assignment.git

---

## Executive Summary

This project implements four fundamental CPU scheduling algorithms used in operating systems to manage process execution. Each algorithm demonstrates different strategies for allocating CPU time to processes, with varying impacts on system performance metrics such as waiting time and turnaround time.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Algorithms Implemented](#algorithms-implemented)
3. [Implementation Details](#implementation-details)
4. [Results and Analysis](#results-and-analysis)
5. [Performance Comparison](#performance-comparison)
6. [Conclusions](#conclusions)
7. [References](#references)

---

## 1. Introduction

### 1.1 Background

CPU scheduling is a fundamental function of operating systems that determines which process runs at any given time. The scheduler's goal is to maximize CPU utilization, minimize waiting time, and ensure fair resource allocation among processes.

### 1.2 Objectives

- Implement four different CPU scheduling algorithms
- Calculate turnaround time and waiting time for each process
- Compare algorithm performance using average metrics
- Provide both command-line and web-based interfaces

### 1.3 Scope

This project covers:
- First Come First Serve (FCFS)
- Shortest Remaining Time First (SRTF)
- Round Robin (RR)
- Priority Scheduling (Preemptive)

---

## 2. Algorithms Implemented

### 2.1 First Come First Serve (FCFS)

**Type:** Non-preemptive  
**Strategy:** Processes are executed in the order they arrive

**Characteristics:**
- Simple to understand and implement
- Uses FIFO queue structure
- No process starvation
- Can lead to convoy effect (short processes waiting behind long ones)

**Test Data:**
| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 9          |
| P4      | 3            | 5          |

### 2.2 Shortest Remaining Time First (SRTF)

**Type:** Preemptive  
**Strategy:** Always execute the process with the shortest remaining burst time

**Characteristics:**
- Preemptive version of Shortest Job First (SJF)
- Minimizes average waiting time
- Can cause starvation of longer processes
- Requires knowledge of burst times

**Test Data:**
| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 3            | 1          |
| P2      | 1            | 4          |
| P3      | 4            | 2          |
| P4      | 0            | 6          |
| P5      | 2            | 3          |

### 2.3 Round Robin (RR)

**Type:** Preemptive  
**Strategy:** Each process gets a fixed time quantum in cyclic order  
**Time Quantum:** 2 units

**Characteristics:**
- Fair allocation of CPU time
- Good response time for interactive systems
- Performance depends on time quantum size
- No starvation

**Test Data:**
| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1      | 0            | 5          |
| P2      | 1            | 3          |
| P3      | 2            | 1          |
| P4      | 3            | 2          |
| P5      | 4            | 3          |

### 2.4 Priority Scheduling (Preemptive)

**Type:** Preemptive  
**Strategy:** Execute highest priority process first  
**Note:** Higher number = Higher priority

**Characteristics:**
- Allows important processes to run first
- Can cause starvation of low-priority processes
- Preemption allows dynamic priority handling

**Test Data:**
| Process | Arrival Time | Burst Time | Priority |
|---------|--------------|------------|----------|
| P1      | 0            | 4          | 2        |
| P2      | 1            | 3          | 3        |
| P3      | 2            | 1          | 4        |
| P4      | 3            | 5          | 5        |
| P5      | 4            | 2          | 5        |

---

## 3. Implementation Details

### 3.1 Technology Stack

- **Python 3.x:** Core algorithm implementation
- **HTML/CSS/JavaScript:** Interactive web interface
- **Git/GitHub:** Version control

### 3.2 Key Formulas

**Completion Time:** Time at which process finishes execution

**Turnaround Time (TAT):**
```
TAT = Completion Time - Arrival Time
```

**Waiting Time (WT):**
```
WT = Turnaround Time - Burst Time
```

**Average Waiting Time:**
```
Avg WT = Σ(Waiting Time) / Number of Processes
```

**Average Turnaround Time:**
```
Avg TAT = Σ(Turnaround Time) / Number of Processes
```

### 3.3 Algorithm Implementation Approach

#### FCFS Implementation
```
1. Sort processes by arrival time
2. For each process:
   - Start time = max(current_time, arrival_time)
   - Completion = start_time + burst_time
   - Calculate TAT and WT
   - Update current_time
```

#### SRTF Implementation
```
1. Initialize remaining burst times
2. While processes remain:
   - Find process with shortest remaining time
   - Execute for 1 time unit
   - If completed, calculate metrics
```

#### Round Robin Implementation
```
1. Initialize queue with arrived processes
2. While processes remain:
   - Dequeue process
   - Execute for min(quantum, remaining_time)
   - Add newly arrived processes to queue
   - If not finished, re-queue process
```

#### Priority Implementation
```
1. Initialize remaining burst times
2. While processes remain:
   - Find highest priority process that has arrived
   - Execute for 1 time unit
   - If completed, calculate metrics
```

---

## 4. Results and Analysis

### 4.1 FCFS Results

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---------|---------|-------|------------|------------|---------|
| P1      | 0       | 8     | 8          | 8          | 0       |
| P2      | 1       | 4     | 12         | 11         | 7       |
| P3      | 2       | 9     | 21         | 19         | 10      |
| P4      | 3       | 5     | 26         | 23         | 18      |

**Average Waiting Time:** 8.75 units  
**Average Turnaround Time:** 15.25 units

**Observations:**
- P1 has no waiting time as it arrives first
- Later processes suffer from convoy effect
- Simple but not optimal for minimizing wait times

### 4.2 SRTF Results

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---------|---------|-------|------------|------------|---------|
| P1      | 3       | 1     | 4          | 1          | 0       |
| P2      | 1       | 4     | 15         | 14         | 10      |
| P3      | 4       | 2     | 7          | 3          | 1       |
| P4      | 0       | 6     | 16         | 16         | 10      |
| P5      | 2       | 3     | 10         | 8          | 5       |

**Average Waiting Time:** 5.20 units  
**Average Turnaround Time:** 8.40 units

**Observations:**
- Best average waiting time among all algorithms
- Short processes (P1, P3) complete quickly
- Longer processes (P2, P4) experience more waiting

### 4.3 Round Robin Results

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---------|---------|-------|------------|------------|---------|
| P1      | 0       | 5     | 13         | 13         | 8       |
| P2      | 1       | 3     | 9          | 8          | 5       |
| P3      | 2       | 1     | 5          | 3          | 2       |
| P4      | 3       | 2     | 11         | 8          | 6       |
| P5      | 4       | 3     | 14         | 10         | 7       |

**Average Waiting Time:** 5.60 units  
**Average Turnaround Time:** 8.40 units

**Observations:**
- Fair distribution of CPU time
- Good response time for all processes
- Time quantum of 2 provides good balance

### 4.4 Priority Scheduling Results

| Process | Arrival | Burst | Priority | Completion | Turnaround | Waiting |
|---------|---------|-------|----------|------------|------------|---------|
| P1      | 0       | 4     | 2        | 15         | 15         | 11      |
| P2      | 1       | 3     | 3        | 10         | 9          | 6       |
| P3      | 2       | 1     | 4        | 3          | 1          | 0       |
| P4      | 3       | 5     | 5        | 8          | 5          | 0       |
| P5      | 4       | 2     | 5        | 10         | 6          | 4       |

**Average Waiting Time:** 4.20 units  
**Average Turnaround Time:** 7.20 units

**Observations:**
- Lowest average waiting time
- High-priority processes (P4, P5) get immediate attention
- Low-priority process (P1) experiences significant waiting

---

## 5. Performance Comparison

### 5.1 Average Waiting Time Comparison

| Algorithm | Avg Waiting Time |
|-----------|------------------|
| Priority  | 4.20 units       |
| SRTF      | 5.20 units       |
| RR        | 5.60 units       |
| FCFS      | 8.75 units       |

### 5.2 Average Turnaround Time Comparison

| Algorithm | Avg Turnaround Time |
|-----------|---------------------|
| Priority  | 7.20 units          |
| SRTF      | 8.40 units          |
| RR        | 8.40 units          |
| FCFS      | 15.25 units         |

### 5.3 Analysis

**Best for Minimizing Wait Time:**
- Priority Scheduling and SRTF perform best
- FCFS performs worst due to convoy effect

**Best for Fairness:**
- Round Robin provides most equitable CPU distribution
- Priority Scheduling can starve low-priority processes

**Best for Simplicity:**
- FCFS is easiest to implement
- No complex decision-making required

**Best for Interactive Systems:**
- Round Robin with appropriate quantum
- Good response time for all processes

---

## 6. Conclusions

### 6.1 Key Findings

1. **Priority Scheduling** achieved the best average waiting time (4.20 units) but at the cost of potential starvation
2. **SRTF** provides excellent performance (5.20 units) but requires burst time knowledge
3. **Round Robin** offers the best balance between performance and fairness
4. **FCFS** is simple but suboptimal for minimizing wait times

### 6.2 Real-World Applications

- **FCFS:** Batch processing systems, print queues
- **SRTF:** Systems where process times are predictable
- **Round Robin:** Time-sharing systems, interactive applications
- **Priority:** Real-time systems, critical task handling

### 6.3 Recommendations

- Use **Round Robin** for general-purpose interactive systems
- Use **Priority** for real-time or mission-critical applications
- Use **SRTF** when process durations are known and predictable
- Avoid **FCFS** except for simplest scenarios

---

## 7. References

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson.
3. Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson.
4. Course lecture notes and materials

---

**Project Repository:** https://github.com/Seyia07/OS_Assignment.git  
**Submission Date:** November 14, 2025


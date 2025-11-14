# OS Assignment - CPU Scheduling Algorithms

**Course:** Operating Systems  
**Due Date:** November 14, 2025  
**Repository:** https://github.com/Seyia07/OS_Assignment.git

---

## 👥 Group Members

1. Annie Wanjohi - 171001
2.Seyianoi Sankok - 190384



---

## 📋 Project Overview

This project implements **four CPU scheduling algorithms** with automatic calculation of:
- ✅ **Turnaround Time** = Completion Time - Arrival Time
- ✅ **Waiting Time** = Turnaround Time - Burst Time
- ✅ **Average Waiting Time**
- ✅ **Average Turnaround Time**

---

## 🎯 Implemented Algorithms

### Task 1: First Come First Serve (FCFS)
- **Type:** Non-preemptive
- **Strategy:** FIFO queue based on arrival time
- **Processes:** 4 (P1-P4)
- **Data:**
  | Process | Arrival Time | Burst Time |
  |---------|--------------|------------|
  | P1      | 0            | 8          |
  | P2      | 1            | 4          |
  | P3      | 2            | 9          |
  | P4      | 3            | 5          |

### Task 2: Shortest Remaining Time First (SRTF)
- **Type:** Preemptive (SJF preemptive mode)
- **Strategy:** Select process with shortest remaining burst time
- **Processes:** 5 (P1-P5)
- **Data:**
  | Process | Arrival Time | Burst Time |
  |---------|--------------|------------|
  | P1      | 3            | 1          |
  | P2      | 1            | 4          |
  | P3      | 4            | 2          |
  | P4      | 0            | 6          |
  | P5      | 2            | 3          |

### Task 3: Round Robin (RR)
- **Type:** Preemptive
- **Time Quantum:** 2 units
- **Strategy:** Cyclic allocation with fixed time slice
- **Processes:** 5 (P1-P5)
- **Data:**
  | Process | Arrival Time | Burst Time |
  |---------|--------------|------------|
  | P1      | 0            | 5          |
  | P2      | 1            | 3          |
  | P3      | 2            | 1          |
  | P4      | 3            | 2          |
  | P5      | 4            | 3          |

### Task 4: Priority Scheduling (Preemptive)
- **Type:** Preemptive
- **Priority:** Higher number = Higher priority
- **Strategy:** Execute highest priority process first
- **Processes:** 5 (P1-P5)
- **Data:**
  | Process | Arrival Time | Burst Time | Priority |
  |---------|--------------|------------|----------|
  | P1      | 0            | 4          | 2        |
  | P2      | 1            | 3          | 3        |
  | P3      | 2            | 1          | 4        |
  | P4      | 3            | 5          | 5        |
  | P5      | 4            | 2          | 5        |

---

## 🚀 How to Run

### Method 1: Python Implementation (Command Line)
```bash



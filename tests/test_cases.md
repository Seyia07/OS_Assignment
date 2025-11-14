# Test Cases and Expected Outputs

**Repository:** https://github.com/Seyia07/OS_Assignment.git

---

## Task 1: FCFS Test Case

### Input Data
| Process ID | Arrival Time | Burst Time |
|------------|--------------|------------|
| P1         | 0            | 8          |
| P2         | 1            | 4          |
| P3         | 2            | 9          |
| P4         | 3            | 5          |

### Expected Output

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---------|---------|-------|------------|------------|---------|
| P1      | 0       | 8     | 8          | 8          | 0       |
| P2      | 1       | 4     | 12         | 11         | 7       |
| P3      | 2       | 9     | 21         | 19         | 10      |
| P4      | 3       | 5     | 26         | 23         | 18      |

**Average Waiting Time:** 8.75 units  
**Average Turnaround Time:** 15.25 units

### Calculation Verification

**P1:**
- Completion = 0 + 8 = 8
- Turnaround = 8 - 0 = 8
- Waiting = 8 - 8 = 0 ✓

**P2:**
- Completion = 8 + 4 = 12
- Turnaround = 12 - 1 = 11
- Waiting = 11 - 4 = 7 ✓

**P3:**
- Completion = 12 + 9 = 21
- Turnaround = 21 - 2 = 19
- Waiting = 19 - 9 = 10 ✓

**P4:**
- Completion = 21 + 5 = 26
- Turnaround = 26 - 3 = 23
- Waiting = 23 - 5 = 18 ✓

**Averages:**
- Avg WT = (0 + 7 + 10 + 18) / 4 = 35 / 4 = 8.75 ✓
- Avg TAT = (8 + 11 + 19 + 23) / 4 = 61 / 4 = 15.25 ✓

---

## Task 2: SRTF Test Case

### Input Data
| Process ID | Arrival Time | Burst Time |
|------------|--------------|------------|
| P1         | 3            | 1          |
| P2         | 1            | 4          |
| P3         | 4            | 2          |
| P4         | 0            | 6          |
| P5         | 2            | 3          |

### Expected Output

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---------|---------|-------|------------|------------|---------|
| P1      | 3       | 1     | 4          | 1          | 0       |
| P2      | 1       | 4     | 15         | 14         | 10      |
| P3      | 4       | 2     | 7          | 3          | 1       |
| P4      | 0       | 6     | 16         | 16         | 10      |
| P5      | 2       | 3     | 10         | 8          | 5       |

**Average Waiting Time:** 5.20 units  
**Average Turnaround Time:** 8.40 units

### Execution Timeline

| Time | Running Process | Remaining Times |
|------|----------------|-----------------|
| 0    | P4             | P4:6            |
| 1    | P2             | P4:5, P2:4      |
| 2    | P2             | P4:5, P2:3, P5:3 |
| 3    | P1             | P4:5, P2:2, P5:3, P1:1 |
| 4    | P2             | P4:5, P2:2, P5:3, P3:2 |
| 5    | P2             | P4:5, P2:1, P5:3, P3:2 |
| 6    | P3             | P4:5, P5:3, P3:2 |
| 7    | P3             | P4:5, P5:3, P3:1 |
| 8    | P5             | P4:5, P5:3 |
| 9    | P5             | P4:5, P5:2 |
| 10   | P5             | P4:5, P5:1 |
| 11   | P2             | P4:5, P2:1 |
| 12   | P4             | P4:5 |
| 13   | P4             | P4:4 |
| 14   | P4             | P4:3 |
| 15   | P4             | P4:2 |
| 16   | P4             | Complete |

### Calculation Verification

**P1:**
- Arrives at 3, completes at 4
- Turnaround = 4 - 3 = 1
- Waiting = 1 - 1 = 0 ✓

**P4:**
- Arrives at 0, completes at 16
- Turnaround = 16 - 0 = 16
- Waiting = 16 - 6 = 10 ✓

**Averages:**
- Avg WT = (0 + 10 + 1 + 10 + 5) / 5 = 26 / 5 = 5.20 ✓
- Avg TAT = (1 + 14 + 3 + 16 + 8) / 5 = 42 / 5 = 8.40 ✓

---

## Task 3: Round Robin Test Case

### Input Data
| Process ID | Arrival Time | Burst Time |
|------------|--------------|------------|
| P1         | 0            | 5          |
| P2         | 1            | 3          |
| P3         | 2            | 1          |
| P4         | 3            | 2          |
| P5         | 4            | 3          |

**Time Quantum:** 2 units

### Expected Output

| Process | Arrival | Burst | Completion | Turnaround | Waiting |
|---------|---------|-------|------------|------------|---------|
| P1      | 0       | 5     | 13         | 13         | 8       |
| P2      | 1       | 3     | 9          | 8          | 5       |
| P3      | 2       | 1     | 5          | 3          | 2       |
| P4      | 3       | 2     | 11         | 8          | 6       |
| P5      | 4       | 3     | 14         | 10         | 7       |

**Average Waiting Time:** 5.60 units  
**Average Turnaround Time:** 8.40 units

### Execution Sequence (Step-by-Step)

**Time 0-2:** P1 executes for 2 units
- P1 remaining: 5 - 2 = 3
- Queue: [P1, P2] (P2 arrived at time 1)

**Time 2-4:** P2 executes for 2 units
- P2 remaining: 3 - 2 = 1
- Queue: [P1, P2, P3] (P3 arrived at time 2)

**Time 4-5:** P3 executes for 1 unit (only needs 1)
- P3 remaining: 1 - 1 = 0 ✅ **P3 COMPLETES**
- Queue: [P1, P4] (P4 arrived at time 3)

**Time 5-7:** P1 executes for 2 units
- P1 remaining: 3 - 2 = 1
- Queue: [P4, P5, P1] (P5 arrived at time 4)

**Time 7-9:** P4 executes for 2 units
- P4 remaining: 2 - 2 = 0 ✅ **P4 COMPLETES**
- Queue: [P5, P1]

**Time 9-10:** P2 executes for 1 unit (only needs 1)
- P2 remaining: 1 - 1 = 0 ✅ **P2 COMPLETES**
- Queue: [P5, P1]

**Time 10-12:** P5 executes for 2 units
- P5 remaining: 3 - 2 = 1
- Queue: [P1, P5]

**Time 12-13:** P1 executes for 1 unit (only needs 1)
- P1 remaining: 1 - 1 = 0 ✅ **P1 COMPLETES**
- Queue: [P5]

**Time 13-14:** P5 executes for 1 unit (only needs 1)
- P5 remaining: 1 - 1 = 0 ✅ **P5 COMPLETES**
- Queue: []

### Gantt Chart
```
|-- P1 --|-- P2 --|P3|-- P1 --|-- P4 --|P2|-- P5 --|P1|P5|
0        2        4  5        7        9  10       12 13 14
```

### Calculation Verification

**P1:**
- Arrives at 0, completes at 13
- Turnaround = 13 - 0 = 13
- Waiting = 13 - 5 = 8 ✓

**P3:**
- Arrives at 2, completes at 5
- Turnaround = 5 - 2 = 3
- Waiting = 3 - 1 = 2 ✓

**Averages:**
- Avg WT = (8 + 5 + 2 + 6 + 7) / 5 = 28 / 5 = 5.60 ✓
- Avg TAT = (13 + 8 + 3 + 8 + 10) / 5 = 42 / 5 = 8.40 ✓

---

## Task 4: Priority Scheduling Test Case

### Input Data
| Process ID | Arrival Time | Burst Time | Priority |
|------------|--------------|------------|----------|
| P1         | 0            | 4          | 2        |
| P2         | 1            | 3          | 3        |
| P3         | 2            | 1          | 4        |
| P4         | 3            | 5          | 5        |
| P5         | 4            | 2          | 5        |

**Note:** Higher number = Higher priority

### Expected Output

| Process | Arrival | Burst | Priority | Completion | Turnaround | Waiting |
|---------|---------|-------|----------|------------|------------|---------|
| P1      | 0       | 4     | 2        | 15         | 15         | 11      |
| P2      | 1       | 3     | 3        | 10         | 9          | 6       |
| P3      | 2       | 1     | 4        | 3          | 1          | 0       |
| P4      | 3       | 5     | 5        | 8          | 5          | 0       |
| P5      | 4       | 2     | 5        | 10         | 6          | 4       |

**Average Waiting Time:** 4.20 units  
**Average Turnaround Time:** 7.20 units

### Execution Timeline (Step-by-Step)

**Time 0:** Only P1 available (Priority 2)
- Execute P1

**Time 1:** P1 (Priority 2), P2 (Priority 3) available
- P2 has higher priority → **Preempt P1, execute P2**
- P1 has executed 1 unit, 3 remaining

**Time 2:** P1 (Priority 2), P2 (Priority 3), P3 (Priority 4) available
- P3 has highest priority → **Preempt P2, execute P3**
- P2 has executed 1 unit, 2 remaining

**Time 3:** P1 (Priority 2), P2 (Priority 3), P3 (Priority 4), P4 (Priority 5) available
- P4 has highest priority → **Preempt P3, execute P4**
- P3 has executed 1 unit, 0 remaining ✅ **P3 COMPLETES**

**Time 3-8:** P4 continues (Priority 5, highest)
- P4 executes all 5 units
- ✅ **P4 COMPLETES at time 8**

**Time 8:** P1 (Priority 2), P2 (Priority 3), P5 (Priority 5) available
- P5 has highest priority → **Execute P5**

**Time 8-10:** P5 executes (Priority 5)
- P5 executes all 2 units
- ✅ **P5 COMPLETES at time 10**

**Time 10:** P1 (Priority 2), P2 (Priority 3) available
- P2 has higher priority → **Execute P2**

**Time 10-12:** P2 executes remaining 2 units
- ✅ **P2 COMPLETES at time 12**

**Time 12-15:** Only P1 remaining
- P1 executes remaining 3 units
- ✅ **P1 COMPLETES at time 15**

### Gantt Chart
```
|P1|-- P2 --|P3|------- P4 -------|-- P5 --|-- P2 --|---- P1 ----|
0  1        2  3                  8       10       12           15
```

### Calculation Verification

**P3 (Highest priority first):**
- Arrives at 2, completes at 3
- Turnaround = 3 - 2 = 1
- Waiting = 1 - 1 = 0 ✓

**P1 (Lowest priority):**
- Arrives at 0, completes at 15
- Turnaround = 15 - 0 = 15
- Waiting = 15 - 4 = 11 ✓

**Averages:**
- Avg WT = (11 + 6 + 0 + 0 + 4) / 5 = 21 / 5 = 4.20 ✓
- Avg TAT = (15 + 9 + 1 + 5 + 6) / 5 = 36 / 5 = 7.20 ✓

---

## Validation Checklist

### Your Program Must Calculate:

✅ **Completion Time** - When each process finishes  
✅ **Turnaround Time** = Completion Time - Arrival Time  
✅ **Waiting Time** = Turnaround Time - Burst Time  
✅ **Average Waiting Time** = Sum of all Waiting Times / Number of Processes  
✅ **Average Turnaround Time** = Sum of all Turnaround Times / Number of Processes

### Common Mistakes to Avoid:

❌ **Wrong Formula:**
```python
# INCORRECT
waiting_time = completion_time - arrival_time

# CORRECT
turnaround_time = completion_time - arrival_time
waiting_time = turnaround_time - burst_time
```

❌ **Forgetting CPU Idle Time:**
```python
# If CPU is idle, jump to next arrival
if current_time < process.arrival:
    current_time = process.arrival
```

❌ **Round Robin Queue Management:**
```python
# Add newly arrived processes BEFORE re-queuing current process
add_arrived_processes(current_time)
if process.remaining > 0:
    queue.append(process)
```

---

## Performance Summary

| Algorithm | Avg Waiting Time | Avg Turnaround Time | Ranking |
|-----------|-----------------|---------------------|---------|
| Priority  | 4.20 units      | 7.20 units         | 1st (Best) |
| SRTF      | 5.20 units      | 8.40 units         | 2nd |
| RR        | 5.60 units      | 8.40 units         | 3rd |
| FCFS      | 8.75 units      | 15.25 units        | 4th (Worst) |

---

## How to Test Your Program

### 1. Run Python Implementation
```bash
cd src
python scheduler.py
```

### 2. Compare Your Output
- Check if each process has correct Completion Time
- Verify Turnaround Time = Completion - Arrival
- Verify Waiting Time = Turnaround - Burst
- Check averages match exactly

### 3. Test Web Interface
```bash
cd web
# Open index.html in browser
```
- Click each algorithm button
- Click "Run Algorithm"
- Verify results match the expected outputs above

---

**If your outputs match these test cases exactly, your implementation is CORRECT!** ✅

**Repository:** https://github.com/Seyia07/OS_Assignment.git  
**Last Updated:** November 14, 2025

<<<<<<< HEAD
=======

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
# Navigate to src folder
cd src

# Run the scheduler
python scheduler.py
```

**Requirements:** Python 3.6 or higher

### Method 2: Interactive Web Interface
```bash
# Navigate to web folder
cd web

# Option A: Open directly
# Just double-click index.html

# Option B: Use local server (recommended)
python -m http.server 8000
# Then open browser to: http://localhost:8000
```

**Requirements:** Any modern web browser (Chrome, Firefox, Edge, Safari)

---

## 📊 Sample Output
```
======================================================================================
Algorithm: First Come First Serve (FCFS)
======================================================================================
Process   Arrival   Burst     Completion    Turnaround    Waiting
--------------------------------------------------------------------------------------
P1        0         8         8             8             0
P2        1         4         12            11            7
P3        2         9         21            19            10
P4        3         5         26            23            18
--------------------------------------------------------------------------------------
Average Waiting Time: 8.75 units
Average Turnaround Time: 15.25 units
======================================================================================
```

---

## 📁 Project Structure
```
OS_Assignment/
├── README.md                          # This file
├── .gitignore                         # Git ignore rules
├── src/
│   └── scheduler.py                   # Python implementation
├── web/
│   └── index.html                     # Interactive web simulator
├── docs/
│   ├── REPORT.md                      # Detailed project report
│   └── ALGORITHM_EXPLANATION.md       # Algorithm explanations
└── tests/
    └── test_cases.md                  # Test cases & outputs
```

---

## 🌟 Features

✅ Handles multiple processes automatically  
✅ Calculates all required metrics precisely  
✅ Clean, formatted output  
✅ Interactive web visualization  
✅ Comprehensive documentation  
✅ Test cases with expected outputs  
✅ Easy to understand and modify  

---

## 📚 Documentation

- **[REPORT.md](docs/REPORT.md)** - Complete project report with analysis and observations
- **[ALGORITHM_EXPLANATION.md](docs/ALGORITHM_EXPLANATION.md)** - Detailed explanation of each algorithm
- **[test_cases.md](tests/test_cases.md)** - All test cases with expected outputs

---

## 🧪 Testing

All algorithms have been tested with the provided data sets. See `tests/test_cases.md` for:
- Input data for each algorithm
- Expected outputs
- Validation results

---

## 📖 References

1. Operating Systems Concepts (Silberschatz, Galvin, Gagne)
2. Modern Operating Systems (Andrew S. Tanenbaum)
3. Course lecture notes and materials

---

## 📄 License

This is an educational project for the Operating Systems course.

---

## 🔗 Links

- **GitHub Repository:** https://github.com/Seyia07/OS_Assignment.git
- **Web Demo:** Open `web/index.html` in your browser

---

**Last Updated:** November 14, 2025


>>>>>>> 961a3df2e06f7bc145fc7e609940f716eee28ce4

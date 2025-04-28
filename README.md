# OSProject2-CPU-Scheduling-Simulator-
 A Python project that implements and compares three CPU scheduling algorithms (FCFS, HRRN, SRTF). This repository includes:  Core modules for process representation and metrics computation  Scheduler implementations in core/schedulers/  A main script to run and compare algorithms
 
Installation
git clone https://github.com/KimaniGordon/OSProject2.git
cd OSProject2

Create and activate a virtual environment (optional but recommended):
- python3 -m venv venv
- source venv/bin/activate

Install dependencies 
- pip install -r requirements.txt 

Project Structure

OSProject2/
├── .gitignore
├── README.md
├── requirements.txt     
└── core/
    ├── __init__.py
    ├── main.py
    ├── metrics.py
    ├── process.py
    └── schedulers/
        ├── __init__.py
        ├── fcfs_scheduler.py
        ├── hrrn_scheduler.py
        └── srtf_scheduler.py




.gitignore
venv/
__pycache__/
*.pyc

Usage

- Run the main comparison script from the project root:
- python3 -m core.main
- This will execute FCFS, HRRN, and SRTF schedulers on a predefined test set and print metrics and a comparison table.

This project is licensed under the MIT License.

References
- `tabulate` library from [PyPI Tabulate](https://pypi.org/project/tabulate/)


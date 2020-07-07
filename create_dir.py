import sys
import os
import re

if __name__ == "__main__": 
    if len(sys.argv) != 2: 
        data_file = "employee.txt"
    else:
        data_file = sys.argv[1]
    employees = []
    with open(data_file, "r") as f: 
        for line in f.readlines(): 
            line = line.strip()
            employees.append(re.split(r'[;,\t ]+',line))
    print employees
    for e in employees: 
        os.mkdir("emp-%s-%s" % (e[0], e[1]))

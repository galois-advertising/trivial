import sys
import os
import re
from shutil import copyfile


def get_emp_list(list_file): 
    employees = []
    with open(list_file, "r") as f: 
        for line in f.readlines(): 
            line = line.strip()
            employees.append(re.split(r'[;,\t ]+',line))
    return employees


def dirname(e):
    return "emp-%s-%s" % (e[0], e[1])


def mkdir(list_file): 
    if os.path.exists(list_file):
        employees = get_emp_list(list_file)
        for e in employees: 
            os.mkdir(dirname(e))
    else: 
        print "[%s] does not exists" % (list_file)


def get_data_list(data_path): 
    result = dict()
    for root, dirs, files in os.walk(data_path):  
        for file in files: 
            result[file] = os.sep.join([root, file])
    return result


def arrange(list_file, data_path): 
    if os.path.exists(list_file) and os.path.exists(data_path): 
        emp_list = get_emp_list(list_file)
        data_files = get_data_list(data_path)
        for emp in emp_list: 
            name, id = emp[0], emp[1]
            for file, filepath in data_files.items():
                if name in file: 
                    try: 
                        copyfile(filepath, os.sep.join([dirname(emp), file]))
                        print "cp [%s] to [%s]" % (filepath, dirname(emp))
                    except:
                        print "cp file [%s] to [%s] failed." % (filepath, dirname(emp))
    else: 
        print "[%s] or [%s] does not exists" % (list_file, data_path)

if __name__ == "__main__": 
    if len(sys.argv) >= 3: 
        if sys.argv[1] == "mkdir": 
            mkdir(sys.argv[2])
            exit(0)
        elif sys.argv[1] == "arrange" and len(sys.argv) == 4:
            arrange(sys.argv[2], sys.argv[3])
            exit(0)
    print "%s [mkdir|arrange] list_file [search_path]" % sys.argv[0]

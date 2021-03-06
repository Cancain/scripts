#! /bin/python3

import os
import sys

current_folder = os.getcwd()
main_path = "%s/src/main.cpp" % current_folder

def make_folder(folder_name):
    full_folder_path = current_folder + "/" + folder_name
    try:
        os.mkdir(full_folder_path)
    except:
        sys.exit("mkdir failed: %s" % full_folder_path )
    print("folder %s created" % folder_name)

    
def create_cpp_main():
    main_cpp = open(main_path, "w")
    headers = "#include <iostream>\n"
    main_function = "\nint main(){\n  return 0;\n}"

    template = headers + main_function
    main_cpp.write(template);

def create_executables():
    os.system("cp ~/scripts/cppstart/run.py %s" %current_folder)
    os.system("cp ~/scripts/cppstart/debug.py %s" %current_folder)

def copy_vscode_config():
    os.system("cp ~/scripts/cppstart/.vscode %s -r" %current_folder)

def main():
    make_folder("src")
    make_folder("build")
    create_cpp_main()
    create_executables()
    copy_vscode_config()

if __name__ == "__main__":
    main()

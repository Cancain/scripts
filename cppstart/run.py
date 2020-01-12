#! /bin/python3
import os

current_folder = os.getcwd()

def get_cpp_files():
   src_folder = "%s/src" % current_folder
   files = os.listdir(src_folder)                    
   cpp_files = [fi for fi in files if fi.endswith(".cpp")]    

   return cpp_files

def make_files_string():
    files = get_cpp_files()
    files_string = ""
    for file in files:
        files_string = files_string + " src/%s" %file

    return files_string

def compile_files():
    files = make_files_string() 
    os.system("g++ -Wall -std=c++17 " + files + " -o build/main")

def run():
    os.system("./build/main")

def main():
    compile_files()
    run()

if __name__ == "__main__":
    main()

import os
import subprocess


# compile ui file
def compile_file(name: str):
    py = name.replace('.ui', '.py')
    subprocess.run(f"pyside6-uic {name} -o {py}")


# compile all files in ../ui folder
def compile_all(path):
    os.chdir(path)

    cur_dir = os.getcwd()
    filenames = os.listdir(cur_dir)
    for file in filenames:
        if file.endswith(".ui"):
            compile_file(file)


if __name__ == "__main__":
    compile_all("../ui")

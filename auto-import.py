import os
import sys

def SearchFiles(path):
    files_in_dir = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files_in_dir.append(file)
    return files_in_dir

def SearchInFile(name, file):
    file = open(file).readlines()
    chosen = []
    for line in file:
        if name in line:
            if not line.startswith("#"):
                chosen.append(line)
    return chosen


def ManageFileImports(file, game_path, log_path):
    modules_list = []
    imports_line = SearchInFile("import", f"{game_path}{file}")
    game_modules_path = game_path.replace("../", "").replace("/", ".")
    game_files = SearchFiles(game_path)
    modules_name_from_files = []
    for module_name in game_files:
        modules_name_from_files.append(module_name.replace(".py", ""))
    for import_statement in imports_line:
        if import_statement.startswith("from"):
            modules_list.append(import_statement.split(" import").pop(0).replace("from ", ""))
    for module in modules_list:
        try:
            exec(f"""import {game_modules_path}{module}""")
        except ModuleNotFoundError:
            os.system("python -m pip install --user {}".format(module.split(".")[0]))
        except ImportError:
            if module in modules_name_from_files:
                open(f"{log_path}/log.txt", "w").write(f"ImportError: In-game module \"{module}\" can't be found")
            else:
                try:
                    os.system("python -m pip install --user {}".format(module))
                except Exception:
                    print(f"We can't import the {module} module")

def main(path):
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:] # First element of args is the file name

    if len(args) == 0:
        print('You have not passed any commands in!')
    else:
        for a in args:
            if a == '--help':
                print('Basic command line program')
                print('Options:')
                print(' --help -> show this basic help menu.')
                print(' --handle-imports -> launch script to handle imports.')
                print(' --handle-imports-dev -> launch script to hande imports then launch the "__dev__.py" script of the directory.')
            elif a == '--handle-imports':
                files_dir = SearchFiles(path)
                for file in files_dir:
                    if file.endswith(".py"):
                        ManageFileImports(file, path, ".")
                        print(f"[auto-import.py] {file}'s imports checked and managed")
            elif a == '--handle-imports-dev':
                files_dir = SearchFiles(path)
                for file in files_dir:
                    ManageFileImports(file, path, ".")
                    print(f"(DEV)[auto-import.py] {file}'s imports checked and managed")
                os.system(f"python3 {path}__dev__.py")
            else:
                print('Unrecognised argument.')


path = r"cours/Nsi/algo_knn/"
files_dir = []


if __name__ == '__main__':
    main(path)
import os
import subprocess

# Define the five checks to monitor
checks = [
    'C0301',  # Line too long
    'E1101',  # Module 'X' has no 'Y' member
    'W0401',  # Wildcard import
    'R0201',  # Method could be a function
    'C0111'   # Missing docstring
]

# Get a list of all Python files in the repository
def get_python_files():
    python_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

# Run pylint for each Python file and check for the specific errors
def run_pylint():
    python_files = get_python_files()
    for file in python_files:
        print(f"Running Pylint on {file}")
        result = subprocess.run(
            ['pylint', '--disable=all', '--enable=' + ','.join(checks), file],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if result.stdout:
            print(result.stdout)

if __name__ == "__main__":
    run_pylint()

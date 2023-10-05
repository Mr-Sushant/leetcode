import os

while True:
    folder_name = input("Enter question name (or 'q' to quit): ")

    if folder_name.lower() == 'q':
        break

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create a README.md file inside the folder
    readme_file_path = os.path.join(folder_name, 'README.md')
    with open(readme_file_path, 'w') as readme_file:
        readme_file.write("# " + folder_name + "\n\n")
    # Create a python file inside the folder
    python_file_path = os.path.join(folder_name, 'solution.py')
    with open(python_file_path, 'w') as readme_file:
        readme_file.write("# Start coding")
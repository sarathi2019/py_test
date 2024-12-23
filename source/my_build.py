import os

# Define the parent directory where you want to create the "Check" folder
parent_directory = r"C:\WareHouse\2023-2024\mygit"

# Define the folder name to create
folder_name = "Check"

# Combine the parent directory and folder name into a full path
directory_path = os.path.join(parent_directory, folder_name)

# Debugging: Print the directory path to verify
print(f"Directory Path: {directory_path}")

# Check if the directory already exists
if not os.path.exists(parent_directory):
    print(f"Parent directory does not exist: {parent_directory}")
elif not os.path.exists(directory_path):
    try:
        # Create the directory using os.makedirs()
        os.makedirs(directory_path)
        print(f"The folder '{folder_name}' has been successfully created at {directory_path}.")
    except Exception as e:
        print(f"Error occurred while creating the folder: {e}")
else:
    print(f"The folder '{folder_name}' already exists at {directory_path}.")




'''
def open_command_window_and_greet():
    message = 'Hi, you are in the build stage'
    os.system(f'start cmd /k echo {message}')
    os.system('start cmd /k "python --version"')
    print("hello build -- inside the repo")

if __name__ == "__main__":
    open_command_window_and_greet()
'''
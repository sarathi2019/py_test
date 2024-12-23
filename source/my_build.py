import os

def open_command_window_and_greet():
    message = 'Hi, you are in the build stage'
    os.system(f'start cmd /k echo {message}')
    os.system('start cmd /k "python --version"')
    print("hello build -- inside the repo")

if __name__ == "__main__":
    open_command_window_and_greet()

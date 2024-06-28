import os
import platform

def check_os():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('python .\\windows\\run.py')
    elif os_name == 'Linux':
        # Check if running in Termux
        if 'com.termux' in os.listdir('/data/data'):
            print("Can't run this on Termux")
        else:
            os.system('cd linux && python3 run.py')
    else:
        print(f'Unsupported OS: {os_name}')

check_os()

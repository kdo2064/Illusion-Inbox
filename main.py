import os
import platform

def check_os():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('python .\\windows\\run.py')
    elif os_name == 'Linux':
        if 'TERMUX_PREFIX' in os.environ:
            print("Can't run this on Termux")
        else:
            os.system('cd linux && python3 run.py')
    else:
        print(f'Unsupported OS: {os_name}')

check_os()

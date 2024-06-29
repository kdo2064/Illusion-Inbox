import os
import platform
try:
    import pytz
    import httpx
except:
    _ = os.system('pip install illusionanime illusioncolor httpx datetime pytz' if os.name == 'nt' else 'pip3 install illusionanime illusioncolor httpx datetime pytz')
def check_os():
    os_name = platform.system()

    if os_name == 'Windows':
        os.system('python .\\windows\\run.py')
    elif os_name == 'Linux':
        # Check if running in Termux
        if 'com.termux' in os.listdir('/data/data'):
            os.system('cd linux && python3 run.py')
        else:
            os.system('cd linux && python3 run.py')
    else:
        print(f'Unsupported OS: {os_name}')

check_os()

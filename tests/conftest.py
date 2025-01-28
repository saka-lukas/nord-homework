import pytest
from appium import webdriver
import psutil
import subprocess
import os

@pytest.fixture(scope="session")
def setup():
    start_winappdriver()
    desired_caps = {
        "app": "C:/Program Files/NordVPN/NordVPN.exe",
        "platformName": "Windows"
    }
    global driver 
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", desired_capabilities=desired_caps)
    yield driver
    driver.quit()

def is_winappdriver_running():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == 'WinAppDriver.exe':
            return True
    return False

def start_winappdriver():
    winappdriver_path = r"C:\\Program Files (x86)\\Windows Application Driver\\WinAppDriver.exe"
    if not is_winappdriver_running():
        subprocess.Popen(winappdriver_path, creationflags=subprocess.CREATE_NEW_CONSOLE)

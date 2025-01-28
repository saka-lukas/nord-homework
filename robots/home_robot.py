from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomeRobot():
    def __init__(self, driver):
        self.driver = driver

    def disconnect(self):
        self.driver.find_element_by_accessibility_id("DashboardVpnDisconnect").click()
        self.driver.find_element_by_name("Pause auto-connect").click()
        return self
    
    def connect_to_specific_country(self, country_name):
        self.driver.find_element_by_accessibility_id("ServersListSearchInputField").clear()
        self.driver.find_element_by_accessibility_id("ServersListSearchInputField").send_keys(country_name)
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.NAME, country_name)))
        self.driver.find_element_by_name(country_name).click()
        return self
    
    def verify_is_connected_to_country(self, expected_country):
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.NAME, "Pause")))
        connectedTitle = self.driver.find_element_by_accessibility_id("VpnTitleText").text
        assert expected_country.lower() in connectedTitle.lower(), f"Expected '{expected_country}' country name in title, but got '{connectedTitle}'"
        return self

    def verify_is_disconnected(self):
        WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.NAME, "NOT CONNECTED")))
        return self
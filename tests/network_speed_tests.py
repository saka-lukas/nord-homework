import pytest
from helpers.speedtest_helper import SpeedTest
from robots.home_robot import HomeRobot

@pytest.fixture(scope="session")
def speed_test_server():
    speedTest = SpeedTest()
    return speedTest.get_nearest_speed_test_server()

@pytest.mark.usefixtures("setup")
class TestNetworkSpeed:
    COUNTRY = "Switzerland"

    def test_network_speed_disconnected_and_connected(self, setup, speed_test_server):
        speedTest = SpeedTest()
        homeRobot = HomeRobot(setup)

        homeRobot.verify_is_disconnected()
        speedTest.run_network_speed_test("Disconnected", speed_test_server)

        homeRobot \
            .connect_to_specific_country(self.COUNTRY) \
            .verify_is_connected_to_country(self.COUNTRY)
        speedTest.run_network_speed_test("Connected", speed_test_server)
        homeRobot.disconnect()
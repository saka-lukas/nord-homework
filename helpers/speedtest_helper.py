import subprocess
import json
from helpers.influxdb_helper import InfluxDbHelper

class SpeedTest:
    def __init__(self, executable="./executables/speedtest.exe"):
        self.executable = executable

    def run_network_speed_test(self, connection_status, server_id):
        result = self.execute_speedtest_with_args([self.executable, '--accept-gdpr', '--accept-license', '-s', str(server_id), '-f', 'json'])

        if result.returncode != 0:
            print(f"Error running speedtest: {result.stderr}")
            return

        speedtest_data = json.loads(result.stdout)
        helper = InfluxDbHelper()
        helper.push_data_to_influx_db(speedtest_data=speedtest_data, connection_status=connection_status)

    def get_nearest_speed_test_server(self):
        result = self.execute_speedtest_with_args([self.executable, '--servers', '-f', 'json'])
        data = json.loads(result.stdout)
        first_server_id = data["servers"][0]["id"]
        return first_server_id


    def execute_speedtest_with_args(self, args):
        return subprocess.run(
            args,
            capture_output=True,
            text=True
        )
import os
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDbHelper:

    def __init__(self):
        self.bucket = "nord_speed_tests"
        self.org = "979e375da8e0c440"
        self.token = os.getenv("INFLUXDB_TOKEN")
        self.url = os.getenv("INFLUXDB_URL")

        self.client = influxdb_client.InfluxDBClient(
            url=self.url,
            token=self.token,
            org=self.org
        )

        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)


    def push_data_to_influx_db(self, speedtest_data, connection_status):
        download_speed = speedtest_data['download']['bandwidth'] * 8 / 1_000_000  # Convert to Mbps
        upload_speed = speedtest_data['upload']['bandwidth'] * 8 / 1_000_000  # Convert to Mbps
        ping = speedtest_data['ping']['latency']
        server_info = speedtest_data['server']
        server_name = server_info['name']
        server_location = server_info['location']
        server_country =  server_info['country']
        external_ip = speedtest_data['interface']['externalIp']

        dataPoint = influxdb_client.Point("network_speed_results") \
            .tag("vpn_status", connection_status) \
            .tag("server_name", server_name) \
            .tag("server_location", server_location) \
            .tag("country", server_country) \
            .tag("public_ip", external_ip) \
            .field("download_speed", int(download_speed)) \
            .field("upload_speed", int(upload_speed)) \
            .field("ping", int(ping)) 
        
        self.write_api.write(bucket=self.bucket, org=self.org, record=dataPoint)
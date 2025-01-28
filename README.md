# Introduction

This is a project repository for Nord VPN homework. The goal of this project is to get VPN speed results when user is connected and disconnect from VPN.

## How to run tests?
```python -m pytest .\tests\network_speed_tests.py```

To run multiple times. Make sure ```pytest-repeat``` is installed:

```python -m pytest .\tests\network_speed_tests.py --count 10```

## Prerequisites

```INFLUXDB_TOKEN``` - Used for auth, when pushing data to influx db instance.

```INFLUXDB_URL``` - URL where DB is stored.

```pip install -r ./requirements.txt``` to install all required packages to run this project.

Download WinAppDriver and launch it. It should be launched on http://127.0.0.1:4723:

https://github.com/microsoft/WinAppDriver

## IMPORTANT!!!
**User has to be logged in manually before running the tests. Login Automation was not implemented due to time constraints. Since this would require using different structure + handling of different states, like popups, saved usernames and etc... If I could spend more time I'd implement it using same appium framework, which would open driver to browser and enter all required credentials. We can discuss this more during interview**

## Link to dashboard with results
https://lukasmakas.grafana.net/public-dashboards/c8465c545b124c88b3cc1c6a0cae7f65

## Main Technologies used

- Grafana
- InfluxDB
- PyTest
- Appium
- WinAppDriver

# Things that could be improved if I had more time to spend on this project

- Automatize login flow
- Wrap appium actions, which would have more configurability, better error handling.
- Investigate more in depth why older appium versions have to be used...

If there are more questions please write email: makaravicius@protonmail.com
import requests

# Zabbix API URL
url = "http://zabbix.example.com/api_jsonrpc.php"

# Zabbix API header
header = {
    "Content-Type": "application/json"
}

# Zabbix API authentication data
auth_data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "zabbix_api_user",
        "password": "zabbix_api_password"
    },
    "id": 1
}

# Get Zabbix API authentication token
response = requests.post(url, json=auth_data, headers=header)
auth_token = response.json()['result']

# SLA data to be inserted
sla_data = {
    "jsonrpc": "2.0",
    "method": "service.create",
    "params": {
        "name": "Example SLA",
        "algorithm": "Max",
        "showsla": "1",
        "sortorder": "0",
        "goodsla": "96.00"
    },
    "auth": auth_token,
    "id": 2
}

# Insert SLA into Zabbix
response = requests.post(url, json=sla_data, headers=header)
print(response.json())

import requests

ZABBIX_URL = "https://your-zabbix-server.com/zabbix/api_jsonrpc.php"
ZABBIX_USERNAME = "your-zabbix-username"
ZABBIX_PASSWORD = "your-zabbix-password"

def get_zabbix_auth_token():
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_USERNAME,
            "password": ZABBIX_PASSWORD
        },
        "id": 1
    }
    response = requests.post(ZABBIX_URL, headers=headers, json=data)
    return response.json()["result"]

def get_zabbix_groups():
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": "extend"
        },
        "auth": get_zabbix_auth_token(),
        "id": 1
    }
    response = requests.post(ZABBIX_URL, headers=headers, json=data)
    return response.json()["result"]

if __name__ == "__main__":
    groups = get_zabbix_groups()
    for group in groups:
        print("Group ID:", group["groupid"], "Group Name:", group["name"])

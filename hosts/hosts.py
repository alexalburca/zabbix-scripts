import requests

ZABBIX_URL = "https://your-zabbix-server.com/api_jsonrpc.php"
ZABBIX_USERNAME = "your-zabbix-username"
ZABBIX_PASSWORD = "your-zabbix-password"

def get_auth_token(zabbix_url, username, password):
    headers = { "Content-Type": "application/json" }
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 1,
    }
    
    response = requests.post(zabbix_url, json=data, headers=headers)
    response_json = response.json()
    return response_json["result"]

def get_all_hosts(zabbix_url, auth_token):
    headers = { "Content-Type": "application/json" }
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": "extend",
        },
        "auth": auth_token,
        "id": 2,
    }
    
    response = requests.post(zabbix_url, json=data, headers=headers)
    response_json = response.json()
    return response_json["result"]

if __name__ == "__main__":
    auth_token = get_auth_token(ZABBIX_URL, ZABBIX_USERNAME, ZABBIX_PASSWORD)
    hosts = get_all_hosts(ZABBIX_URL, auth_token)
    for host in hosts:
        print(host["hostid"], host["host"])

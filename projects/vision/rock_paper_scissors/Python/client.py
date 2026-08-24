import socket


def run_client():
    global client 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.2.21"
    server_port = 34170
    try: 
        client.connect((server_ip, server_port))
    except TimeoutError:
        print("TimeoutError")
        return "TimeoutError"


def get_request():
    global client
    request = client.recv(1024)
    request = client.recv(1024)
    request = request.decode("utf-8")

    return request


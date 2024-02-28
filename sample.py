import socket

def get_hostname():
    hostname = socket.gethostname()
    return hostname

if __name__ == "__main__":
    print(get_hostname())

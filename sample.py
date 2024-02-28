import socket

def main():
    # Get the hostname of the system
    hostname = socket.gethostname()
    
    # Write the hostname to the specified file
    with open('/metrics', 'w') as file:
        file.write(f'hostname: {hostname}')

if __name__ == "__main__":
    main()

import socket
import time

HOST = '192.168.144.49'
PORT = 8888
DELAY = 1.2
#created a request
def create_request(pin):
    """Create an HTTP POST request for the given PIN."""
    pin_str = f"{pin:03d}"
    body = f"magicNumber={pin_str}"
    headers = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(body)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    return headers + body, pin_str
    
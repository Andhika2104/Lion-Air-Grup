import json
from xmlrpc.client import ServerProxy
import time

# Buat objek proxy untuk berkomunikasi dengan server
server = ServerProxy("http://localhost:8000/")

# Fungsi untuk mengirim pesan


def send_notification(boarding_schedule, transit_location):
    message = {
        "boarding_schedule": boarding_schedule,
        "transit_location": transit_location
    }

    response = server.process_message(message)
    print(response)


# Simulasi pengiriman pesan
send_notification("2023-12-01 10:00:00", "CityA")

# Tunggu beberapa detik
time.sleep(2)

# Simulasi pengiriman pesan baru
send_notification("2023-12-02 12:30:00", "CityB")

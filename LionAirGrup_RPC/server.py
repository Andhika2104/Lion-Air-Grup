import json
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Inisialisasi data awal jadwal boarding dan lokasi transit
current_boarding_schedule = None
current_transit_location = None

# Fungsi untuk memproses pesan dan menyimpannya ke file

def process_message(message):
    global current_boarding_schedule, current_transit_location

    if "boarding_schedule" in message:
        if current_boarding_schedule != message["boarding_schedule"]:
            current_boarding_schedule = message["boarding_schedule"]
            with open("boarding.txt", "a") as file:
                file.write(json.dumps(message) + "\n")

    if "transit_location" in message:
        if current_transit_location != message["transit_location"]:
            current_transit_location = message["transit_location"]
            with open("lokasi.txt", "a") as file:
                file.write(message["transit_location"] + "\n")

    return "Pesan berhasil diproses."

# Buat server XML-RPC
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)

# Tambahkan fungsi ke server
server.register_function(process_message, "process_message")

print("Server Lion Air siap menerima pesan.")
server.serve_forever()

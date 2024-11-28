from flask import Flask, jsonify
import random
import time
import threading

class BaseStation:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.current_load = 0

    def add_traffic(self, load):
        self.current_load += load

    def offload_traffic(self, load):
        self.current_load -= load

    def is_overloaded(self):
        return self.current_load > self.capacity

# Baz istasyonları oluştur
base_stations = [
    BaseStation("Station A", 100),
    BaseStation("Station B", 80),
    BaseStation("Station C", 120)
]

def simulate_traffic():
    while True:
        for station in base_stations:
            traffic = random.randint(10, 50)  # Rastgele trafik oluştur
            station.add_traffic(traffic)

            if station.is_overloaded():
                print(f"{station.name} is overloaded! Current load: {station.current_load}")
                redistribute_traffic(station)

            print(f"{station.name} - Load: {station.current_load}/{station.capacity}")

        time.sleep(5)

def redistribute_traffic(overloaded_station):
    excess_load = overloaded_station.current_load - overloaded_station.capacity
    overloaded_station.offload_traffic(excess_load)

    for station in base_stations:
        if station != overloaded_station and not station.is_overloaded():
            station.add_traffic(excess_load // 2)
            print(f"Redirecting {excess_load // 2} traffic to {station.name}")
            break

# Flask API
app = Flask(__name__)

@app.route('/metrics')
def metrics():
    output = []
    for station in base_stations:
        # Metrik bilgilerini Prometheus formatında ekle
        metric_name = station.name.lower().replace(" ", "_")  # İsimleri Prometheus formatına uygun hale getir
        output.append(f"# HELP {metric_name}_current_load Current load of {station.name}")
        output.append(f"# TYPE {metric_name}_current_load gauge")
        output.append(f"{metric_name}_current_load {station.current_load}")

        output.append(f"# HELP {metric_name}_capacity Capacity of {station.name}")
        output.append(f"# TYPE {metric_name}_capacity gauge")
        output.append(f"{metric_name}_capacity {station.capacity}")

    # Prometheus formatında metrikleri döndür
    return "\n".join(output), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    # Trafik simülasyonunu ayrı bir thread'de başlat
    traffic_thread = threading.Thread(target=simulate_traffic, daemon=True)
    traffic_thread.start()

    # Flask uygulamasını farklı bir portta çalıştır
    app.run(host='0.0.0.0', port=8080)
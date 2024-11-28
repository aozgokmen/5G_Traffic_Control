
# 5G Traffic Control Project

This project demonstrates a 5G network traffic monitoring and alerting system using **Prometheus**, **Grafana**, and a Python-based traffic simulation tool.

## Overview

Modern telecommunication networks face challenges with dynamic traffic loads. This project simulates traffic in a 5G network environment, monitors the load on base stations, and provides real-time alerts when traffic exceeds the capacity of a base station.

### Key Features:
- **Traffic Simulation:** A Python script (`traffic_simulator.py`) simulates dynamic traffic loads on base stations.
- **Prometheus Integration:** Monitors and collects metrics from the Python simulation in real time.
- **Alerting:** Configured alerts notify when any base station is overloaded.
- **Grafana Dashboards:** Provides detailed visualizations of traffic metrics and alert states.
- **Dockerized Deployment:** Easily deployable via Docker Compose.

---

## How It Works

### Traffic Simulation (`traffic_simulator.py`)
The `traffic_simulator.py` script simulates three base stations:
- **Station A**
- **Station B**
- **Station C**

Each base station has:
- **Current Load:** The simulated traffic currently being handled.
- **Capacity:** The maximum traffic it can handle before becoming overloaded.

The script exposes these metrics in a Prometheus-compatible format via an HTTP endpoint (`/metrics`).

#### Example Metrics:
```plaintext
station_a_current_load 130
station_a_capacity 100
station_b_current_load 90
station_b_capacity 80
station_c_current_load 120
station_c_capacity 120

Monitoring and Alerting

Prometheus scrapes metrics from the Python script and evaluates predefined alert rules:

	•	Overload Alerts: Triggered when the current_load exceeds the capacity for any base station.

Visualization

Grafana dashboards display real-time metrics and alert statuses, allowing network operators to monitor the load distribution and identify bottlenecks.

Setup and Run

Prerequisites

	•	Docker and Docker Compose installed on your system.
	•	Python 3.12 or higher.

Steps:

	1.	Clone the repository:

git clone https://github.com/aozgokmen/5G_Traffic_Control.git
cd 5G_Traffic_Control


	2.	Start the services:

docker-compose up -d


	3.	Start the traffic simulator:

python3 traffic_simulator.py


	4.	Access the services:
	•	Prometheus: http://localhost:9090
	•	Grafana: http://localhost:3000

Project Files

	•	traffic_simulator.py: Simulates 5G network traffic and exposes metrics.
	•	prometheus.yml: Configures Prometheus to scrape metrics and define alert rules.
	•	alerts.yml: Contains alert rules for detecting overloaded base stations.
	•	docker-compose.yml: Deploys Prometheus and Grafana.
	•	README.md: Documentation for the project.

Example Alerts

Alerts are configured in alerts.yml. Examples include:

	•	Station Overloaded: Alerts when a base station’s current_load exceeds its capacity for more than 1 minute.

Future Enhancements

	•	Add more granular traffic metrics, such as latency and packet loss.
	•	Implement automatic load balancing based on overload conditions.
	•	Expand to simulate multiple network regions.


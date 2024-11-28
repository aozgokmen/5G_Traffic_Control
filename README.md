# 5G Traffic Control Project

This project demonstrates a 5G network traffic monitoring and alerting system using **Prometheus**, **Grafana**, and a Python-based traffic simulation tool.

---

## Monitoring and Alerting

Prometheus scrapes metrics from the Python script and evaluates predefined alert rules:

- **Overload Alerts:** Triggered when the `current_load` exceeds the `capacity` for any base station.

---

## Visualization

Grafana dashboards display real-time metrics and alert statuses, allowing network operators to monitor the load distribution and identify bottlenecks.

---

## Setup and Run

### Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.12 or higher.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/aozgokmen/5G_Traffic_Control.git
   cd 5G_Traffic_Control

2. Start the services:
   To start the Prometheus and Grafana services using Docker Compose, run the following command:
   ```bash
   docker-compose up -d

3. Start the traffic simulator:
   To start the Python-based traffic simulation script, run the following command:
   ```bash
   python3 traffic_simulator.py
4. Access the services:
   After starting the simulator and services, you can access the monitoring tools using the following URLs:
	•	Prometheus: http://localhost:9090
	•	Grafana: http://localhost:3000

5. Verify Alerts:
You can verify the alerting rules by visiting Prometheus’s alerts page:
```bash
http://localhost:9090/alerts
6. Customize Dashboards:
   To create custom dashboards in Grafana, follow these steps:
   - Log in to Grafana: [http://localhost:3000](http://localhost:3000)
   - Use the default credentials:
     - **Username:** `admin`
     - **Password:** `admin` (or the one you set in the `docker-compose.yml`)
   - Add Prometheus as a data source:
     1. Navigate to **Configuration** → **Data Sources**.
     2. Click **Add data source** and select **Prometheus**.
     3. Set the URL to:
        ```plaintext
        http://prometheus:9090
        ```
     4. Save and test the connection.
   - Create panels and dashboards to visualize the following metrics:
     - `station_a_current_load`
     - `station_b_current_load`
     - `station_c_current_load`

7. Trigger Alerts:
   To test the alerting system:
   - Increase the `current_load` values in the traffic simulator script to exceed the `capacity`.
   - Wait for Prometheus to detect the change (based on the scrape interval).
   - Check for active alerts in Prometheus at:
     ```bash
     http://localhost:9090/alerts
     ```

8. Monitor in Grafana:
   - Visualize the active alerts and traffic metrics in your Grafana dashboards.
   - Customize alert panels to show real-time status.

9. Shut Down Services:
   When you are finished testing, you can stop all running containers with the following command:
   ```bash
   docker-compose down

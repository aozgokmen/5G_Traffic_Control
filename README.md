# 5G Traffic Control Project

This project demonstrates a 5G network traffic monitoring and alerting system using **Prometheus**, **Grafana**, and a **Python-based traffic simulation tool**.

---

## **Overview**
Modern telecommunication networks face significant challenges with dynamic traffic loads. This project simulates traffic in a 5G network environment, monitors the load on base stations, and provides real-time alerts when traffic exceeds the capacity of a base station.

### **Key Features**
- **Monitoring and Alerting**: Prometheus scrapes metrics from the Python script and evaluates predefined alert rules.
  - **Overload Alerts**: Triggered when the `current_load` exceeds the capacity for any base station.
- **Visualization**: Grafana dashboards display real-time metrics and alert statuses, allowing network operators to monitor the load distribution and identify bottlenecks.

---

## **Setup and Run**

### **Prerequisites**
- Docker and Docker Compose installed on your system.
- Python 3.12 or higher.

### **Steps to Run the Project**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/aozgokmen/5G_Traffic_Control.git
   cd 5G_Traffic_Control

2. Start the services:
   ```bash
   docker-compose up -d
3. Start the traffic simulator:
   ```bash
   python3 traffic_simulator.py

4. Access the services:
   
	• Prometheus: http://localhost:9090
	• Grafana: http://localhost:3000

6. Verify Alerts:
   
	• http://localhost:9090/alerts

8. Explore Metrics:

	•	Use the Prometheus query page to explore metrics such as:
	•	station_a_current_load
	•	station_b_current_load
	•	station_c_current_load
	•	Compare these metrics against the capacity metrics to test if alerts are being triggered.

7. Customize Dashboards:

	•	Log in to Grafana and create custom dashboards to visualize:
	•	Real-time traffic load.
	•	Capacity utilization.
	•	Triggered alerts.

Adding Prometheus as a Data Source in Grafana

	1.	Navigate to Configuration → Data Sources.
	2.	Select Prometheus.
	3.	Set the URL to http://prometheus:9090.

Shut Down Services

When testing is complete, stop all running containers with:

docker-compose down

Project Files

	•	traffic_simulator.py: Simulates 5G network traffic and exposes metrics.
	•	prometheus.yml: Configures Prometheus to scrape metrics and define alert rules.
	•	alerts.yml: Contains alert rules for detecting overloaded base stations.
	•	docker-compose.yml: Deploys Prometheus and Grafana.
	•	README.md: Documentation for the project.

Example Metrics

The traffic_simulator.py script exposes metrics for three base stations:

Metric	Value
station_a_current_load	130
station_a_capacity	100
station_b_current_load	90
station_b_capacity	80
station_c_current_load	120
station_c_capacity	120

Example Alerts

Alerts are configured in alerts.yml. Examples include:

	•	Station Overloaded: Alerts when a base station’s current_load exceeds its capacity for more than 1 minute.

Future Enhancements

	•	Add more granular traffic metrics, such as latency and packet loss.
	•	Implement automatic load balancing to mitigate overload conditions.
	•	Expand the simulation to include multiple network regions or additional stations.


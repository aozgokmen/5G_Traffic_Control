

# Prometheus + Grafana Alerting Project

This project demonstrates the setup of Prometheus and Grafana for monitoring network traffic with alerting capabilities.

## Features
- **Prometheus** for real-time metrics collection and alerting.
- **Grafana** for data visualization and dashboard creation.
- **Docker Compose** for simplified deployment and management.

## Setup and Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>

	2.	Start the services:

docker-compose up -d


	3.	Access the services:
	•	Prometheus: http://localhost:9090
	•	Grafana: http://localhost:3000

Alerting

Alerts are configured in alerts.yml. The following alerts are included:

	•	Station Overloaded: Alerts when the current load of a station exceeds its capacity.

Project Files

	•	prometheus.yml: Prometheus configuration file for scrape targets and rules.
	•	alerts.yml: Prometheus alert rules for monitoring traffic.
	•	docker-compose.yml: Docker Compose configuration for setting up Prometheus and Grafana.
	•	README.md: Documentation for the project.

Dashboard

Grafana dashboards can be customized to visualize the collected metrics and alert states. Use the Prometheus data source to query the metrics.

License

This project is licensed under the MIT License.

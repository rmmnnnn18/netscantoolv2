# NetScan v2 - Network Discovery & Analysis Tool

NetScan is a powerful and elegant web-based tool for discovering, analyzing, and monitoring devices on your network. Built with Flask and a modern, responsive frontend, it provides a comprehensive overview of your network's health and security.

 ## ✨ Features

* **Effortless Network Discovery**: Automatically detects and lists available subnets for scanning.
* **Flexible Scan Options**: Choose between a "Quick Scan" for rapid device discovery or a "Deep Scan" for detailed port analysis.
* **Comprehensive Device Insights**: Gathers detailed information for each device, including IP address, hostname, MAC address, vendor, latency, and open ports.
* **Intelligent Device Classification**: Attempts to identify the device type (e.g., Router, Printer, Windows, Linux) based on its properties.
* **Performance Monitoring**: Classifies device latency into categories like "Excellent," "Good," "Fair," and "Poor" for at-a-glance network health assessment.
* **Modern & Responsive UI**: Features a sleek, intuitive interface with light and dark modes, live filtering, and real-time updates.
* **Data Export**: Easily export scan results to a CSV file for reporting and analysis.
* **Single Device Refresh**: Update the details of a single device without needing to rescan the entire network.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* Python 3.6+
* `pip`
* `venv` (recommended)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rmmnnnn18/netscantoolv2.git](https://github.com/rmmnnnn18/netscantoolv2.git)
    cd netscantoolv2
    ```

2.  **Use the setup script (recommended):**
    The `setup.sh` script will create all the necessary files and directories for you.
    ```bash
    bash setup.sh
    ```

3.  **Create a virtual environment and install dependencies:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

### Running the Application

Once the setup is complete, you can run the application with a single command:

```bash
python app.py

The application will be available at http://localhost:5000 in your web browser.

🛠️ Project Structure

.
├── api/
│   ├── __init__.py
│   └── routes.py         # Flask API routes
├── scanner/
│   ├── __init__.py
│   ├── device.py         # DeviceInfo data class
│   ├── network.py        # Core network scanning logic
│   └── utils.py          # Helper functions (ping, DNS, etc.)
├── templates/
│   └── index.html        # Main HTML frontend
├── .env                  # Environment variables
├── app.py                # Main Flask application entrypoint
├── config.py             # Application configuration
├── requirements.txt      # Python dependencies
└── setup.sh              # Automatic project setup script
```
### 💻 Technologies Used

    Backend: Flask, Python

    Frontend: HTML5, CSS3, JavaScript (Vanilla)

### 📜 License

This project is licensed under the MIT License - see the LICENSE.md file for details.

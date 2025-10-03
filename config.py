import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True') == 'True'
    MAX_WORKERS = int(os.environ.get('MAX_WORKERS', 100))
    DEFAULT_TIMEOUT = float(os.environ.get('SCAN_TIMEOUT', 1.0))
    PORT_SCAN_TIMEOUT = float(os.environ.get('PORT_TIMEOUT', 0.3))
    EXCLUDE_INTERFACES = ['lo', 'docker', 'br-', 'veth', 'virbr', 'kube', 'tailscale', 'zt', 'wg']
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 5432, 5900, 8080, 8443]

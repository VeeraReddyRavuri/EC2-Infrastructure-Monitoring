# Proactive Infrastructure Monitoring with CI/CD

This project implements an automated infrastructure monitoring solution for AWS EC2 instances using Python, Amazon CloudWatch, and GitHub Actions CI/CD.
The monitoring script continuously tracks CPU, memory, and disk usage on the EC2 instance, sends alerts via Amazon SNS, and integrates with GitHub Actions for automatic deployment of updates.

## Features
- Real-time Monitoring: Collects CPU, memory, and disk metrics from Linux EC2 instances using psutil.
- Automated Alerts: Sends SNS notifications when thresholds are exceeded (e.g., high CPU usage).
- CI/CD Pipeline: GitHub Actions workflow automatically deploys updates to EC2 on every push to main.
- Scalable Setup: Easily extendable to multiple EC2 instances.
- Lightweight & Reliable: Runs in the background using nohup with minimal resource overhead.

## Project Structure
EC2-Monitoring/
|--monitoring .py
|--requirements.txt
|--README.md
|--.github/
|--|--workflows/
|--|--deploy.yml	

## Setup Instructions
1. **Clone the Repository**
- git clone https://github.com/VeeraReddyRavuri/EC2-Infrastructure-Monitoring.git
- cd EC2-Monitoring
2. **Create Virtual Environment**
- python3 -m venv venv
- source venv/bin/activate
3. **Install Dependencies**
- pip install -r requirements.txt
4. **Run & Check Script**
- nohup python monitoring.py > monitor.log 2>&1 &
- tail -f monitor.log
- ps aux | grep monitoring.py
- kill PID

### CI/CD Pipeline
- Trigger: Every push to main branch.
- **Steps:**
- Check out repository.
- SSH into EC2 instance using GitHub Secrets.
- Sync code and restart monitoring script.
- **Secrets used:**
- EC2_PUBLIC_IP → Public IP of EC2 instance
- EC2_SSH_KEY → Private key (.pem contents)

## Tech Stack
- **Language**: Python (psutil, boto3)
- **Infrastructure**: AWS EC2, CloudWatch, SNS
- **Automation**: GitHub Actions (CI/CD)
- **OS**: Linux (Ubuntu)

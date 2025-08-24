import psutil
import boto3
import time
from datetime import datetime, timezone

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='eu-north-1')

def publish_metric(metric_name, value, unit="Percent"):
    """Helper to push metrics to CloudWatch"""
    cloudwatch.put_metric_data(
        Namespace='EC2/CustomMonitoring',
        MetricData=[
            {
                'MetricName': metric_name,
                'Timestamp': datetime.now(timezone.utc),
                'Value': value,
                'Unit': unit
            },
        ]
    )

def collect_and_push():
    # CPU usage %
    cpu = psutil.cpu_percent(interval=1)

    # Memory usage %
    memory = psutil.virtual_memory().percent

    # Disk usage %
    disk = psutil.disk_usage('/').percent

    # Disk read/write in bytes
    disk_io = psutil.disk_io_counters()
    read_bytes = disk_io.read_bytes
    write_bytes = disk_io.write_bytes

    # Push to CloudWatch
    publish_metric("CPU_Usage", cpu)
    publish_metric("Memory_Usage", memory)
    publish_metric("Disk_Usage", disk)
    publish_metric("Disk_Read_Bytes", read_bytes, unit="Bytes")
    publish_metric("Disk_Write_Bytes", write_bytes, unit="Bytes")

    print(f"Metrics pushed: CPU={cpu}%, Memory={memory}%, Disk={disk}%")

if __name__ == "__main__":
    while True:
        collect_and_push()
        time.sleep(60)  # send every 1 minute

# this comment is to check the CI/CD workflow

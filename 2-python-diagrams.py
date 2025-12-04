"""
Python Diagrams - Cloud Architecture Visualization
Install: pip install diagrams
"""

from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, Lambda
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB, CloudFront
from diagrams.aws.storage import S3

# Create a cloud architecture diagram
with Diagram("Web Service Architecture", show=False, direction="LR"):
    cdn = CloudFront("CDN")
    
    with Cluster("Load Balancing"):
        lb = ELB("Load Balancer")
    
    with Cluster("Web Tier"):
        web_servers = [EC2("web1"), EC2("web2"), EC2("web3")]
    
    with Cluster("Application Tier"):
        app_servers = [Lambda("app1"), Lambda("app2")]
    
    with Cluster("Data Tier"):
        db_primary = RDS("Primary DB")
        db_replica = RDS("Replica DB")
        cache = ElastiCache("Cache")
    
    storage = S3("Static Assets")
    
    # Define connections
    cdn >> lb >> web_servers >> app_servers
    app_servers >> db_primary
    db_primary >> db_replica
    app_servers >> cache
    cdn >> storage

print("Diagram saved as 'web_service_architecture.png'")

# Real-Time Fleet Tracking System
**Real-time Fleet Telemetry System using Apache Kafka**

A robust, high-throughput data streaming pipeline designed to monitor delivery vehicle locations and telemetry in real-time. The system leverages Apache Kafka to handle massive data ingestion with geographic-based partitioning for seamless scaling.

## Key Features
- **Modular Architecture:** Separation of concerns (Ingester, Simulator, Config).
- **Real-time Streaming:** Powered by Confluent Kafka for high-throughput data ingestion.
- **Dynamic Simulation:** Realistic truck movement simulation with regional metadata.
- **Environment Isolation:** Clean dependency management using Conda/Venv.



### Pipeline
```
[ Data Source ]        [ Ingestion Layer ]       [ Processing Layer ]       [ Presentation/Action ]
   (Trucks)                 (Kafka)               (Monitor Service)            (End Results)
      |                        |                         |                         |
      |  (1) JSON Data         |                         |                         |
      |----------------------->|                         |                         |
      |  (Lat, Lon, Speed)     |   (2) Poll Message      |                         |
      |                        |------------------------>|                         |
      |                        |   (Bytes -> JSON)       |   (3) Business Logic    |
      |                        |                         |   (ETA Calculation)     |
      |                        |                         |   (Speed Check)         |
      |                        |                         |                         |
      |                        |                         |   (4) Final Output      |
      |                        |                         |------------------------>|
      |                        |                         |   - Display on Map      |
      |                        |                         |   - Send SMS Alert      |
```
### Setup
#### kafka
1.  Downloading and Installing Kafka  

```bash
cd ~
wget https://archive.apache.org/dist/kafka/3.7.0/kafka_2.13-3.7.0.tgz

tar -xzf kafka_2.13-3.7.0.tgz

cd kafka_2.13-3.7.0
```

2. Activationg ZooKeeper Server
``` bash
cd ~/kafka_2.13-3.7.0
bin/zookeeper-server-start.sh config/zookeeper.properties
```

3. Starting Kafka Broker

```bash
cd ~/kafka_2.13-3.7.0
bin/kafka-server-start.sh config/server.properties

```
4. Preparing Python Environmrnt

- Downloading Conda Environment `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
- Installing Conda `bash Miniconda3-latest-Linux-x86_64.sh`
- Restart your Terminal `source ~/.bashrc`
- Verify the Installation `conda --version`
- Create and activate your project environement 
```bash
conda create -n logistics_env
conda activate logistics_env
```
- Installing pip if doesn't exist `conda install pip -y`
- Install Required Packeges `pip install -r requirements.txt`

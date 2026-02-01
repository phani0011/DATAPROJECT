<img width="1536" height="1024" alt="ChatGPT Image Feb 2, 2026 at 12_11_47 AM" src="https://github.com/user-attachments/assets/a8938484-178e-4c3e-846c-636ee177edb5" />


# 🌐 DataProject – Distributed Data Platform with Flask, Dockers, Kubernetes & Spark

## 📌 Overview

**DataProject** is an end-to-end distributed data engineering platform that demonstrates how modern data systems collect, process, and analyze data using microservices, containers, orchestration, and distributed computing.

The project exposes a public data ingestion API using Flask and ngrok, deploys services using Docker and Kubernetes, and processes data using Apache Spark following a Bronze–Silver–Gold data lake architecture.

This project simulates a real-world data platform where data is collected from external users, stored in a data lake, processed using Spark, and converted into business insights.

---

## 🎯 Project Goals

- Build a public data ingestion system  
- Deploy applications using Docker & Kubernetes  
- Expose local services using ngrok  
- Design a Bronze–Silver–Gold data lake  
- Process data using Apache Spark  
- Understand real-world data platform architecture  

---

## 🏗️ System Architecture

Users (Internet)
|
ngrok (Public URL)
|
Flask Application (API)
|
Kubernetes (Minikube)
|
Docker Containers
|
Data Lake (Bronze)
|
Apache Spark
|
Silver (Clean Data)
|
Gold (Insights)


---

## 🔁 Project Workflow

### 1. Application Deployment
- Flask application is containerized using Docker.  
- Docker containers are deployed on Kubernetes (Minikube).  
- Flask runs as a Kubernetes Pod.  

### 2. Public Exposure
- ngrok exposes the Flask service to the internet.  
- Users can access the API via a public URL.  

### 3. Data Ingestion
- Users submit data via Flask forms or JSON APIs.  
- Data is stored in the Bronze layer of the data lake.  

### 4. Data Processing
- Apache Spark reads data from Bronze.  
- Applies transformations and cleaning.  
- Writes refined data to Silver layer.  
- Generates analytics and insights in Gold layer.  

---

## 🧱 Data Lake Architecture

| Layer  | Description                  |
|--------|------------------------------|
| Bronze | Raw user-submitted data      |
| Silver | Cleaned and structured data  |
| Gold   | Aggregated business insights |

---

## ⚙️ Technologies Used

| Technology | Purpose |
|-----------|--------|
| Flask | Data ingestion API |
| ngrok | Public IP exposure |
| Docker | Containerization |
| Kubernetes (Minikube) | Orchestration |
| Apache Spark | Distributed processing |
| Python | Core programming |
| Jenkins | Automation |
| GitHub | Version control |
| Data Lake | Storage system |

---

## 🧠 What This Project Demonstrates

- Public API exposure using ngrok  
- Containerized application deployment  
- Kubernetes-based orchestration  
- Real data ingestion from users  
- Distributed processing using Spark  
- Bronze–Silver–Gold data lake design  
- End-to-end data platform architecture  

---

## 🏆 Real-World Mapping

| This Project | Industry Equivalent |
|-------------|---------------------|
| Flask + ngrok | Public REST APIs |
| Minikube | AWS EKS / Azure AKS |
| Docker | Container platforms |
| Spark | Databricks / EMR |
| Data Lake | S3 / ADLS / GCS |

---

## 📈 Learning Outcomes

- Strong understanding of distributed systems  
- Hands-on experience with Kubernetes  
- Practical knowledge of Apache Spark  
- Real implementation of data lake architecture  
- System-level thinking for data engineering  

---

## 🧩 Final Note

DataProject is a system-level project, not just a coding exercise.  
It demonstrates how real data platforms are designed, deployed, and operated using modern cloud-native technologies.





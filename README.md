# 🌐 Round-Robin Load Balancer

## ✍️ Author: Wayne Mataruse

**Version:** 1.0.1

---

## 📌 Project Overview

This project implements a **Round-Robin Load Balancer** using Python and Flask. The load balancer efficiently distributes incoming requests across multiple backend servers, optimising resource utilisation and enhancing system performance. This approach is particularly beneficial in high-traffic environments where balancing server load is crucial for stability and responsiveness.

## 🚀 Key Features

- **Round-Robin Scheduling**: Evenly distributes incoming requests across multiple backend servers.
- **Multi-threading Support**: Enables concurrent request handling for improved responsiveness.
- **Fault Tolerance**: Dynamically manages server availability to ensure seamless operation.
- **Lightweight & Scalable**: Designed for easy deployment and expansion as needed.

## 📂 Project Structure
```sh
/round-robin-load-balancer 
│-- server1.py # Flask-based Backend Server 1 
│-- server2.py # Flask-based Backend Server 2 
│-- server3.py # Flask-based Backend Server 3 
│-- load_balancer.py # Load Balancer with Round-Robin Scheduling 
│-- README.md # Project Documentation
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/waynecancode/round-robin-load-balancer.git
cd round-robin-load-balancer
```

### 2️⃣ Install Dependencies
Ensure Python is installed, then install the required libraries:

```sh
pip install flask requests
```
### 3️⃣ Start Backend Servers
```sh
python server1.py
python server2.py
python server3.py
```
### 4️⃣ Launch the Load Balancer
```sh
python load_balancer.py
```

### 5️⃣ Test the Load Balancer
You can verify functionality using a web browser or cURL:

```sh
curl http://127.0.0.1:5000/
```
Each request will be forwarded to a different backend server in a cyclic manner.

## 🔥 Future Enhancements

- **Health Monitoring**: Automatically detect and exclude unresponsive servers.
- **Logging & Metrics**: Capture request distribution data for performance analysis.
- **Containerisation**: Deploy using Docker and orchestrate with Kubernetes for scalable infrastructure.
- **Weighted Load Balancing**: Assign server priority based on computational capacity.
- **Auto Scaling**: Dynamically adjust server instances according to traffic demand.

## 📜 License

This project is **open source**.

---

**© Wayne Mataruse - 2025**  
For questions or suggestions, feel free to reach out! 🚀

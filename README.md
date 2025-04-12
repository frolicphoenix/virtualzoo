# 🐾 Virtual Zoo — IaC Playground

Welcome to **Virtual Zoo** — a minimal Infrastructure as Code (IaC) experiment where pets are deployed, aged, and cared for like virtual machines in a cloud. This small app combines Go (for backend and lifecycle simulation) with Python (for a GUI dashboard) to simulate a live zoo where pets get hungry, grow old, and can be fed or destroyed through buttons. It's simple, fun, and a great base to explore server lifecycles and control panels.

---

## 📦 Project Overview

This project demonstrates how to:

- Simulate infrastructure resources using virtual pets
- Use **Go** to manage state and background timers (goroutines)
- Use **Python (Tkinter)** to interact with the backend via a GUI
- Apply Infrastructure-as-Code ideas using a YAML config file
- Practice concurrency, REST API design, and full-stack interactions

---

## 🧰 Tech Stack

| Tech | Purpose |
|------|---------|
| **Go** | Backend server, REST API, concurrency (goroutines), pet lifecycle |
| **Python** | Frontend GUI using Tkinter |
| **YAML** | Zoo configuration (as an analogy to IaC templates) |
| **HTTP (REST)** | Communication between frontend and backend |
| **Mutex** | Safe concurrent access to pet data |

---

## 🐾 Features

- Create a zoo from a YAML file (`my_zoo.yaml`)
- View live pet list and their status (lifespan, hunger)
- Pets age and get hungrier every 5 seconds
- Pets with zero lifespan are removed automatically
- Feed all pets to reduce their hunger
- Destroy the entire zoo in one click (use wisely)

---

## 🧠 Concepts Explored

- Background processing in Go using `time.Ticker` + `goroutines`
- Data races avoided with `sync.Mutex`
- Frontend-backend communication via REST APIs
- YAML as declarative infrastructure (IaC metaphor)
- Simple stateful system simulation

---

## 🚀 How to Run

### 1. Start the Go server

```bash
go run main.go
```

Make sure it runs on `localhost:8080`.

### 2. Run the Python UI

```bash
python zoo_ui.py
```

Ensure you have `requests`, `pyyaml`, and `tkinter` installed.

### 3. Use the App

- 🪄 Create Zoo → loads `my_zoo.yaml` into backend
- 🔄 Refresh → view pet status
- 🍗 Feed All Pets → reduce their hunger
- 💀 Destroy Zoo → wipes everything

---

## ✨ Author

Made with curiosity and code by pranjall

---

## 🐉 License

MIT — feel free to evolve this zoo into whatever you want.

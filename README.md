# Navoiyazot Logistics · Breakdown Report & Predictive Maintenance

Enterprise fleet reliability and breakdown analytics platform for the **Navoiyazot industrial logistics operation**.

---

## Key Capabilities

* **Workload-Normalized Rankings**: Evaluates vehicle breakdowns relative to completed freight trips rather than raw dates, eliminating bias from idle vehicles.
* **Predictive Maintenance Risk Scoring**: Assigns proactive risk tiers (`HIGH`, `MEDIUM`, `LOW`) using multivariate indicators (repeat failures, overdue maintenance, aggressive driving, aged parts).
* **Cohort Reliability Benchmarking**: Compares breakdowns against peer cohorts of identical vehicle makes and models.
* **Driver Reliability Correlation**: Identifies correlation between specific vehicle breakdowns and driver handling patterns.

---

## Tech Stack

* **Language**: Python 3.12+
* **Framework**: FastAPI (REST)
* **Metrics**: MTBF, MTTR, cohort peer comparison, trip-normalized failure rates
* **Database Driver**: Psycopg2-binary (PostgreSQL)

---

## Core Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/breakdown-report/scan` | Comprehensive breakdown report, vehicle rankings, and predictive risks |
| `GET` | `/breakdown-report/summary` | Fleet-wide summary broken down by component, brand, and vehicle type |
| `GET` | `/healthz` | Service health status |

---

## Quick Start

### 1. Installation
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=atil_navoiyazot
DB_USER=postgres
DB_PASSWORD=your_password
```

### 3. Run Service
```bash
python main.py
# Server runs on http://localhost:8005 (Docs: http://localhost:8005/docs)
```

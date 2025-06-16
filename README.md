# alphacare-insurance-risk-analytics

## Project Overview

This project implements an end-to-end machine learning pipeline for detecting fraudulent insurance claims at AlphaCare Insurance Solutions. It covers data preprocessing, feature engineering, model training, evaluation, deployment, and monitoring.

The goal is to build an accurate and reliable fraud detection model to reduce false claims and improve operational efficiency.

---

## Repository Structure

``` bash
alphacare-insurance-risk-analytics
├── app
├── datasets
│   ├── insurance_data_cleaned.csv
│   ├── insurance_data_cleaned.csv.dvc
│   ├── local_dvc_storage
│   └── MachineLearningRating_v3.txt
├── images
│   ├── MonthlyChange_Top10ZipCodes.png
│   ├── monthly_total_premium_by_cover_type.png
│   ├── TotalClaims_per_CoverType.png
│   ├── TotalClaims_per_VehicleType.png
│   ├── total_premium_per_claims.png
│   ├── total_premium_per_province.png
│   ├── total_premium_per_vehicle_boxplot.png
│   ├── total_premium_per_vehicle.png
│   ├── total_premium.png
│   └── tSumInsured_vs_TotalClaims.png
├── LICENSE
├── models
├── README.md
├── requirements.txt
├── scripts
├── src
│   └── __pycache__
│       ├── alphacare_insurance.cpython-312.pyc
│       └── insurance_visualization.cpython-312.pyc
└── test

```

---

## Setup and Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/alphacare-fraud-detection.git
cd alphacare-fraud-detection
```

``` bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate     # Windows

```
``` bash
pip install -r requirements.txt

```
## Set up DVC and pull data

``` bash

pip install dvc
dvc init
```
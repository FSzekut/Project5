# Vehicle Listings Explorer

Small Streamlit app for exploring a vehicle listings dataset with interactive
histogram and scatter plot views.

Live app: https://project5-bktb.onrender.com/

## What It Shows

- Odometer distribution through an interactive histogram.
- Price versus odometer relationship through a scatter plot.
- Simple Streamlit tab layout with button and checkbox controls.

## Repository Layout

```text
.
├── app.py                 # Streamlit application
├── vehicles.csv           # Dataset used by the app
├── notebooks/EAD.ipynb    # Exploratory analysis notebook
├── requirements.txt       # Python dependencies
└── streamlit/config.toml  # Streamlit configuration for deployment
```

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Notes

This project was built as an introductory data-app exercise and deployed on
Render. It is intentionally small, but it demonstrates the full path from local
EDA to a hosted Streamlit app.

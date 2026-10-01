#!/bin/sh
set -e

echo "Starting Deep Learning Tutor RAG..."

python -m uvicorn app.api.main:app \
    --host 0.0.0.0 \
    --port 8000 &

streamlit run streamlit_app.py \
    --server.address 0.0.0.0 \
    --server.port 8501
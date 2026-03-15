#!/bin/bash

echo "TruthLens UA Analytics - Starting..."
echo "=================================="

if grep -q Microsoft /proc/version 2>/dev/null; then
    PROJECT_PATH="/mnt/c/Users/home2/Downloads/truthlens-ua-analytics"
else
    PROJECT_PATH="$(pwd)"
fi

cd "$PROJECT_PATH" || exit 1

if command -v docker >/dev/null 2>&1 && command -v docker-compose >/dev/null 2>&1; then
    echo "Docker found - checking daemon..."
    if docker info >/dev/null 2>&1; then
        docker-compose up --build -d
        if [ $? -eq 0 ]; then
            echo ""
            echo "Services started:"
            echo "  Dashboard: http://localhost:8501"
            echo "  API: http://localhost:8000"
            echo "  API Docs: http://localhost:8000/docs"
            echo ""
            echo "Logs: docker-compose logs -f"
            echo "Stop: docker-compose down"
            exit 0
        fi
    fi
    echo "Docker daemon unavailable or compose failed - falling back to local mode"
else
    echo "Docker not found - using local mode"
fi

echo "Starting API server..."
python -m uvicorn app.main:app --reload --port 8000 &
API_PID=$!

sleep 3

echo "Starting Dashboard..."
cd dashboard || exit 1
streamlit run app.py --server.port 8501 &
DASHBOARD_PID=$!

echo ""
echo "Services started:"
echo "  Dashboard: http://localhost:8501"
echo "  API: http://localhost:8000"
echo ""
echo "Stop: Ctrl+C"

trap "kill $API_PID $DASHBOARD_PID 2>/dev/null; exit" INT TERM
wait

=== QUICK START COMMANDS ===

# Docker (найпростіше — один запуск):
docker-compose up --build -d
# API:       http://localhost:8000/docs
# Dashboard: http://localhost:8501

# Windows PowerShell:
cd C:\Users\home2\Downloads\truthlens-ua-analytics
python -m uvicorn app.main:app --reload --port 8000
# (новий термінал):
cd dashboard && streamlit run app.py --server.port 8501

# WSL / Linux:
cd ~/truthlens-ua-analytics
python -m uvicorn app.main:app --reload --port 8000

# Smoke test:
curl http://localhost:8000/health
curl -X POST http://localhost:8000/check \
  -H "Content-Type: application/json" \
  -d '{"text":"ТЕРМІНОВО!!! ЗСУ ЗДАЛИ Харків!"}'

# Public demo:
# https://truthlens-ua-analytics.onrender.com

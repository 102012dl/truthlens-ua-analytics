FROM python:3.12-slim
WORKDIR /app
<<<<<<< HEAD
=======
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
>>>>>>> c8044a54feafecac1b7a862c9206bccc05e21870
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
<<<<<<< HEAD
=======
HEALTHCHECK CMD curl -f http://localhost:8501/_stcore/health || exit 1
>>>>>>> c8044a54feafecac1b7a862c9206bccc05e21870
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]

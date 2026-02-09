FROM python:3.9-slim
WORKDIR /app
# Copy requirements first to leverage Docker cache
# If requirements.txt doesn't change, Docker skips 'pip install' on rebuilds
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application
COPY main.py .
CMD ["python", "main.py"]
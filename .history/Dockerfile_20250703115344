FROM python:3.9-slim

WORKDIR /app

# Install curl for downloading kubectl
RUN apt-get update && apt-get install -y curl && apt-get clean

# ✅ Install kubectl from official binary release
RUN curl -LO "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the orchestrator
CMD ["python", "-m", "main.main_orchestrator"]

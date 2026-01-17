FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and model
COPY src ./src
COPY model ./model

# Expose port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "src.serve:app", "--host", "0.0.0.0", "--port", "8000"]

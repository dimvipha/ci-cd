FROM python:3.9

WORKDIR /app

COPY .  /app/

RUN pip install -r requirements.txt

EXPOSE 8000

# Option 1: Using uvicorn directly (Recommended)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
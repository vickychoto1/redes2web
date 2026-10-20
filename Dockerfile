FROM python:3.10-slim
WORKDIR /app
RUN pip install --no-cache-dir flask
COPY main.py .
EXPOSE 5000
CMD ["python", "main.py"]
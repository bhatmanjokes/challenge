FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY analytics /app/analytics 
COPY data /app/data
COPY parser /app/parser
COPY main.py /app/
COPY entrypoint.sh /app/entrypoint.sh

RUN pip install jupyter

RUN chmod 644 /app/analytics/exploratory_analysis.ipynb
RUN chmod -R 777 /app/analytics
RUN chmod -R 777 /app/data
RUN chmod -R 777 /app/parser
RUN chmod +x /app/entrypoint.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["/app/entrypoint.sh"]

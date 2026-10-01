FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN git clone \
    --depth 1 \
    https://github.com/d2l-ai/d2l-en.git \
    /d2l-en

RUN python -m scripts.build_index

RUN chmod +x start.sh

EXPOSE 8501

CMD ["./start.sh"]
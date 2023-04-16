FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y git gcc libpq-dev

WORKDIR /app

RUN git clone https://github.com/ConsenSys/mythril.git && \
    cd mythril && \
    pip install -r requirements.txt && \
    pip install . && \
    cd ..

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "mythril.api.app:create_app()"]

FROM python:3.14
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./src
EXPOSE 8084
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8084"]
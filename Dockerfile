FROM python-3.14
WORKDIR /app
COPY requirement.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["fastapi", "run", "./src/main.py"]
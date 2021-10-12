FROM python:3.9.7-slim-buster

WORKDIR /app

RUN pip install Flask>=1.1.2 Jinja2>=2.11.2 Werkzeug==1.0.1 gunicorn>=20.0.4 torch==1.9.0+cpu torchvision==0.10.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

CMD ["python", "app.py"]
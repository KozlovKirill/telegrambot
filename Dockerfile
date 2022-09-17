FROM python

WORKDIR /app

COPY . .

RUN pip install aiogram

RUN pip install Pillow

CMD ["python", "bot.py"]
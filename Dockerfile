FROM python:3
WORKDIR /PieTester_bot
COPY requirements.txt /PieTester_bot
RUN python3 -m pip install -r requirements.txt
COPY . /PieTester_bot
EXPOSE 8888
CMD ["python", "piebot.py"]

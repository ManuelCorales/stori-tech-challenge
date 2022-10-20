FROM python
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
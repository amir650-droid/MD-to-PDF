FROM kivy/buildozer:latest

# نصب expect
RUN apt-get update && apt-get install -y expect && rm -rf /var/lib/apt/lists/*

# کپی اسکریپت wrapper
COPY buildozer-expect /usr/local/bin/
RUN chmod +x /usr/local/bin/buildozer-expect

ENTRYPOINT ["/usr/local/bin/buildozer-expect"]
CMD []

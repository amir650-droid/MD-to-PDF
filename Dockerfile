FROM kivy/buildozer:latest

# نصب expect برای خودکارسازی پاسخ به سوالات
RUN apt-get update && apt-get install -y expect && rm -rf /var/lib/apt/lists/*

# ایجاد یک اسکریپت wrapper با expect
RUN echo '#!/usr/bin/expect -f' > /usr/local/bin/buildozer-expect && \
    echo 'set timeout -1' >> /usr/local/bin/buildozer-expect && \
    echo 'spawn /home/user/.venv/bin/buildozer {*}$argv' >> /usr/local/bin/buildozer-expect && \
    echo 'expect "Are you sure you want to continue [y/n]? " { send "y\r" }' >> /usr/local/bin/buildozer-expect && \
    echo 'interact' >> /usr/local/bin/buildozer-expect && \
    chmod +x /usr/local/bin/buildozer-expect

ENTRYPOINT ["/usr/local/bin/buildozer-expect"]
CMD []

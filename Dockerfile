FROM kivy/buildozer:latest

# نصب expect
RUN apt-get update && apt-get install -y expect && rm -rf /var/lib/apt/lists/*

# ایجاد اسکریپت wrapper با expect (با استفاده از cat و heredoc)
RUN cat > /usr/local/bin/buildozer-expect << 'EOF'
#!/usr/bin/expect -f
set timeout -1
spawn /home/user/.venv/bin/buildozer {*}$argv
expect -exact "Are you sure you want to continue [y/n]? " { send "y\r" }
interact
EOF

RUN chmod +x /usr/local/bin/buildozer-expect

ENTRYPOINT ["/usr/local/bin/buildozer-expect"]
CMD []

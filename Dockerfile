FROM kivy/buildozer:latest

# غیرفعال کردن بررسی root با تغییر کد buildozer
RUN sed -i '/def check_root/,/^$/d' /home/user/.venv/lib/python3.14/site-packages/buildozer/__init__.py && \
    sed -i '/self.check_root()/d' /home/user/.venv/lib/python3.14/site-packages/buildozer/__init__.py

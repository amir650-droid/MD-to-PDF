[app]

# نام برنامه (همانطور که روی گوشی نمایش داده می‌شود)
title = تبدیل مارک‌داون به پی‌دی‌اف

# نام داخلی (فقط حروف کوچک، اعداد و زیرخط)
package.name = mypdfapp

# دامنه (برعکس نوشته می‌شود)
package.domain = org.example

# کتابخانه‌های مورد نیاز (خیلی مهم!)
requirements = python3,kivy,markdown,weasyprint

# مسیر پوشه‌ی کد منبع (همان پوشه‌ی فعلی)
source.dir = .

# تنظیمات اندروید
android.api = 31
android.minapi = 21

# مجوزهای لازم
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# تنظیمات پیش‌فرض
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0

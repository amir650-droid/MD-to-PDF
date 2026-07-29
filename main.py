import markdown
from weasyprint import HTML

# 1. خواندن فایل مارک‌داون
with open("my_document.md", "r", encoding="utf-8") as f:
    md_text = f.read()

# 2. تبدیل به HTML
html_body = markdown.markdown(md_text, extensions=['extra'])

# 3. خواندن CSS
with open("style.css", "r", encoding="utf-8") as f:
    css_code = f.read()

# 4. ساخت HTML نهایی با بهترین تنظیمات راست‌چینی
final_html = f"""
<!DOCTYPE html>
<html dir="rtl" style="margin:0; padding:0; background-color:#f3efe8; width:100%; height:100%;">
<head>
    <meta charset="UTF-8">
    <style>{css_code}</style>
</head>
<body style="margin:0.1cm 0.6cm; padding:0.1cm 0.3cm; background-color:#f3efe8; width:auto; height:auto; min-height:100%;">
    {html_body}
</body>
</html>
"""

# 5. تبدیل به PDF با تنظیمات خاص برای راست‌چینی
HTML(string=final_html).write_pdf(
    "output_final.pdf",
    # تنظیمات اضافی برای WeasyPrint جهت پشتیبانی بهتر از راست‌چین
    presentational_hints=True,
)

print("✅ فایل PDF با بهترین راست‌چینی ممکن ساخته شد!")

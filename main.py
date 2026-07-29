from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.core.window import Window
import markdown
from weasyprint import HTML
import os

# تنظیم اندازه پنجره برای نمایش بهتر در کامپیوتر (اختیاری)
Window.size = (400, 700)

class PDFConverterApp(App):
    def build(self):
        # طرح اصلی
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # عنوان
        title = Label(text='📄 تبدیل مارک‌داون به PDF', font_size=24, size_hint_y=0.15)
        layout.add_widget(title)
        
        # دکمه انتخاب فایل
        btn_select = Button(text='انتخاب فایل .md', size_hint_y=0.15, background_color=(0.2, 0.6, 0.8, 1))
        btn_select.bind(on_press=self.open_file_chooser)
        layout.add_widget(btn_select)
        
        # برچسب وضعیت
        self.status_label = Label(text='لطفاً یک فایل مارک‌داون انتخاب کنید', size_hint_y=0.15, halign='center')
        layout.add_widget(self.status_label)
        
        return layout
    
    def open_file_chooser(self, instance):
        # ایجاد FileChooser
        filechooser = FileChooserListView(filters=['*.md'])
        
        # دکمه‌های انتخاب و لغو
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=0.15, spacing=5)
        btn_cancel = Button(text='لغو')
        btn_confirm = Button(text='انتخاب', background_color=(0.2, 0.8, 0.2, 1))
        
        btn_layout.add_widget(btn_cancel)
        btn_layout.add_widget(btn_confirm)
        
        # popup اصلی
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(filechooser)
        popup_layout.add_widget(btn_layout)
        
        popup = Popup(title='انتخاب فایل مارک‌داون', content=popup_layout, size_hint=(0.9, 0.9))
        
        # تابع انتخاب فایل
        def confirm_selection(instance):
            if filechooser.selection:
                selected_file = filechooser.selection[0]
                popup.dismiss()
                self.convert_to_pdf(selected_file)
            else:
                self.status_label.text = '⚠️ لطفاً یک فایل انتخاب کنید'
        
        btn_confirm.bind(on_press=confirm_selection)
        btn_cancel.bind(on_press=popup.dismiss)
        
        popup.open()
    
    def convert_to_pdf(self, md_file_path):
        try:
            self.status_label.text = '⏳ در حال تبدیل...'
            
            # خواندن فایل مارک‌داون
            with open(md_file_path, 'r', encoding='utf-8') as f:
                md_text = f.read()
            
            # تبدیل به HTML
            html_body = markdown.markdown(md_text, extensions=['extra'])
            
            # مسیر فایل CSS (اگر وجود دارد)
            css_code = ''
            css_path = os.path.join(os.path.dirname(md_file_path), 'style.css')
            if os.path.exists(css_path):
                with open(css_path, 'r', encoding='utf-8') as f:
                    css_code = f.read()
            else:
                # CSS پیش‌فرض زیبا
                css_code = """
                body {
                    font-family: 'Helvetica', 'Arial', sans-serif;
                    font-size: 12pt;
                    line-height: 1.8;
                    color: #2c3e50;
                }
                h1, h2, h3 {
                    color: #1a5490;
                }
                pre {
                    background: #f5f5f5;
                    padding: 10px;
                    border-radius: 5px;
                    direction: ltr;
                    text-align: left;
                }
                code {
                    background: #f5f5f5;
                    padding: 2px 5px;
                    border-radius: 3px;
                }
                """
            
            # ساخت HTML نهایی
            final_html = f"""
            <!DOCTYPE html>
            <html dir="rtl" style="margin:0; padding:0; background-color:#f3efe8; width:100%; height:100%;">
            <head>
                <meta charset="UTF-8">
                <style>{css_code}</style>
            </head>
            <body style="margin:0.5cm 0.8cm; padding:0.2cm 0.5cm; background-color:#f3efe8;">
                {html_body}
            </body>
            </html>
            """
            
            # تولید فایل PDF در همان پوشه فایل ورودی
            output_pdf = md_file_path.replace('.md', '.pdf')
            HTML(string=final_html).write_pdf(output_pdf, presentational_hints=True)
            
            self.status_label.text = f'✅ تبدیل شد: {os.path.basename(output_pdf)}'
            
        except Exception as e:
            self.status_label.text = f'❌ خطا: {str(e)}'

if __name__ == '__main__':
    PDFConverterApp().run()

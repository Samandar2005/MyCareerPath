import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tracker.models import DailyPlan

# 30 Kunlik Professional Reja
plans = [
    # 1-HAFTA: FUNDAMENT
    (1, "OOP va Python Fundamenti", "Class, Object, Inheritance tushunchalarini mustahkamlash. User klassini yaratish.", "hard", "https://mohirdev.uz"),
    (2, "Fayllar va API Tushunchasi", "JSON nima? Requests kutubxonasi qanday ishlaydi? Fayldan o'qish/yozish.", "medium", "https://youtube.com"),
    (3, "API Amaliyot (Valyuta)", "Markaziy bank APIsi orqali valyuta kurslarini oluvchi script yozish.", "medium", None),
    (4, "SQL va Bazalar (SQLite)", "Ma'lumotlarni bazaga saqlash. SQL so'rovlari (SELECT, INSERT).", "hard", None),
    (5, "Pandas: Excel bilan ishlash 1", "Excel faylni ochish, DataFrame yaratish va ma'lumot o'qish.", "medium", None),
    (6, "Pandas: Excel Avtomatlashtirish", "Ma'lumotlarni filtrlash, tozalash va yangi faylga saqlash.", "hard", None),
    (7, "Haftalik Yakun va GitHub", "Barcha kodlarni GitHub repozitoriysiga joylash va README yozish.", "easy", "https://github.com"),
    
    # 2-HAFTA: SCRAPING
    (8, "Web Scraping: HTML & BS4", "BeautifulSoup yordamida sayt sarlavhalarini ko'chirish.", "medium", None),
    (9, "Selenium va Dinamik Saytlar", "Brauzerni avtomatlashtirish, tugmalarni bosish.", "hard", None),
    (10, "Avto-Login Scriptlar", "Instagram yoki Facebookga avtomatik kirish scriptini yozish.", "hard", None),
    (11, "OLX/Uzum Parseri", "Real saytdan narxlarni yig'ib Excelga tashlash.", "hard", None),
    (12, "Ma'lumotni Tozalash", "Yig'ilgan ma'lumotni (str) raqam (int) formatiga o'tkazish.", "medium", None),
    (13, "Scriptni Optimallashtirish", "Try/Except va Time.sleep qo'shish. Xatolarni oldini olish.", "medium", None),
    (14, "Portfolio Loyiha: Scraper", "To'liq ishlaydigan parserni tugatib GitHubga yuklash.", "hard", None),

    # 3-HAFTA: TELEGRAM BOTLAR
    (15, "Aiogram: Bot Asoslari", "BotFather, Token va birinchi 'Hello World' bot.", "easy", None),
    (16, "Bot Tugmalari (UI)", "Inline va Reply klaviaturalar bilan ishlash.", "medium", None),
    (17, "FSM (Holatlar Mashinasi)", "Foydalanuvchidan ketma-ket ma'lumot olish (Anketa).", "hard", None),
    (18, "Bot + API Integratsiyasi", "Bot orqali Ob-havo yoki Valyutani ko'rsatish.", "hard", None),
    (19, "Bot + Database", "Foydalanuvchilarni SQLite bazasida saqlash.", "hard", None),
    (20, "Bot + Scraping (Gibrid)", "Saytdan ma'lumot olib botga uzatish (Instagram Downloader).", "hard", None),
    (21, "Portfolio Loyiha: Super Bot", "Mukammal botni serverga tayyorlash.", "hard", None),

    # 4-HAFTA: DAROMAD VA KARERA
    (22, "Deploy: Serverga Joylash", "Docker asoslari. Render yoki Railwayga botni yuklash.", "hard", None),
    (23, "Freelance Profillar", "Upwork va Fiverrda professional profil ochish.", "medium", "https://upwork.com"),
    (24, "Gig Yaratish (Fiverr)", "Sotiladigan xizmatlarni (Scraping, Bot) joylash.", "medium", "https://fiverr.com"),
    (25, "Upwork Cover Letter", "Taklif xati yozishni mashq qilish.", "easy", None),
    (26, "Mijoz Qidiruv (Outreach)", "LinkedIn orqali mijozlarga yozish.", "medium", "https://linkedin.com"),
    (27, "Yordamchi Scriptlar", "PDF to Word, Image Resizer kabi mini toolar yozish.", "easy", None),
    (28, "Faol Apply qilish", "Kuniga 10 ta ishga topshirish.", "medium", None),
    (29, "Texnik Interview Tayyorgarlik", "Python bo'yicha savol-javoblarni takrorlash.", "hard", None),
    (30, "YAKUNIY IMTIHON", "Birinchi real buyurtmani olish yoki o'z loyihasini taqdim etish.", "hard", None),
]

def load():
    print("🚀 Professional reja yuklanmoqda...")
    DailyPlan.objects.all().delete() # Eski rejalarni tozalash
    
    for num, title, desc, diff, url in plans:
        DailyPlan.objects.create(
            day_number=num,
            title=title,
            description=desc,
            difficulty=diff,
            video_url=url
        )
        print(f"✅ {num}-kun: {title}")
    print("🎉 Barcha ma'lumotlar bazaga yozildi!")

if __name__ == '__main__':
    load()
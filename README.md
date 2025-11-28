# MyCareerPath

MyCareerPath — bu Django asosida yaratilgan ta’lim yo‘nalishini boshqarish tizimi. Dastur yordamida kunlik o‘quv maqsadlarini rejalash, bajarilishni kuzatish va o‘zlashtirish jarayonini tahlil qilish mumkin. Har bir kun uchun mavzu, murakkablik darajasi, holati, qo‘shimcha resurslar hamda shaxsiy izohlarni jamlab borish osonlashadi.

## Asosiy imkoniyatlar
- Har bir kun uchun mavzular, tavsiflar va mos resurslar kiritish.
- `pending`, `in_progress`, `completed` holatlari orqali jarayonni kuzatish.
- `easy`, `medium`, `hard` murakkablik darajalarini belgilash.
- Sarflangan vaqt va shaxsiy qaydlarni yozib borish.
- Dashboard va kun tafsilotlari orqali umumiy natijalarni ko‘rish.

## O‘rnatish va ishga tushirish
1. Reponi yuklab oling yoki klonlang.
2. Virtual muhit yarating: `python -m venv venv`, so‘ng Windowsda `venv\Scripts\activate`.
3. Kerakli paketlarni o‘rnating (masalan, `pip install django`).
4. Migratsiyalarni bajaring: `python manage.py migrate`.
5. Istasangiz, boshlang‘ich reja ma’lumotlarini yuklang: `python load_plan.py`.
6. Serverni ishga tushiring: `python manage.py runserver` va ko‘rsatilgan URL manzilni brauzerda oching.

## Tuzilma
- `config/` — loyiha sozlamalari, URL marshrutlari, WSGI/ASGI konfiguratsiyasi.
- `tracker/` — barcha modellar, viewlar, URLlar va testlar joylashgan asosiy ilova.
- `tracker/templates/` — `base.html`, `dashboard.html`, `day_detail.html` kabi HTML shablonlar.
- `load_plan.py` — ma’lumotlar bazasiga tayyor kunlik reja ma’lumotlarini kirituvchi skript.
- `manage.py` — Django boshqaruv buyruqlari uchun standart kirish nuqtasi.

## Foydalanish ssenariysi
1. Admin yoki konsol orqali `DailyPlan` yozuvlarini qo‘shing.
2. Har bir kun uchun mavzu nomi, batafsil tavsif, resurslar va statusni belgilang.
3. Kun yakunida sarflangan vaqt va izohlarni kiriting — bu statistikani tahlil qilishga yordam beradi.
4. Dashboard orqali qaysi kunlar bajarilganini, qaysilari hali jarayonda ekanini kuzating.

## Hissa qo‘shish
1. Fork qiling va yangi branch yarating.
2. O‘zgartirishlarni kiriting va testdan o‘tkazing.
3. Pull request yuboring va o‘zgarishlarni qisqacha tushuntiring.

## Litsenziya
Loyiha `LICENSE` faylida ko‘rsatilgan shartlar asosida tarqatiladi. Shu shartlarga amal qilgan holda foydalanishingiz mumkin.


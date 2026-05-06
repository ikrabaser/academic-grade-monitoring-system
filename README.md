# Academic Grade Monitoring System

Üniversite not sistemindeki değişiklikleri takip ederek Telegram üzerinden anlık bildirim gönderen otomasyon sistemi.

---

## Özellikler

- Otomatik oturum desteği
- Not takip sistemi
- Telegram bildirim entegrasyonu
- Oturum düşmesi tespiti
- Playwright ile tarayıcı otomasyonu
- BeautifulSoup ile HTML ayrıştırma
- Kalıcı tarayıcı profili desteği

---

## Kullanılan Teknolojiler

- Python
- Playwright
- BeautifulSoup4
- Telegram Bot API
- Requests
- dotenv

---

## Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/kullaniciadi/academic-grade-monitoring-system.git
```

Gerekli kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

Playwright tarayıcısını kurun:

```bash
playwright install
```

---

## Ortam Değişkenleri

Proje klasöründe `.env` dosyası oluşturun:

```env
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```

---

## Projeyi Çalıştırma

```bash
python app.py
```

---

## Sistem İşleyişi

1. Kullanıcı üniversite sistemine giriş yapar
2. Sistem belirli aralıklarla not sayfasını kontrol eder
3. Not değişiklikleri otomatik olarak algılanır
4. Telegram üzerinden anlık bildirim gönderilir
5. Oturum düşmesi sürekli kontrol edilir

---

## Not

Bu proje eğitim ve kişisel otomasyon amacıyla geliştirilmiştir.

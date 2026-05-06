from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import time
import json
import random
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

KONTROL_ARALIGI = 180  # 3 dakika


def telegram_mesaj(mesaj):
    if not BOT_TOKEN or not CHAT_ID:
        print("BOT_TOKEN veya CHAT_ID bulunamadı.")
        return

    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": mesaj
            },
            timeout=10
        )
    except Exception as e:
        print("Telegram hatası:", e)


def notlari_parse_et(html):
    soup = BeautifulSoup(html, "html.parser")
    tablo = soup.find("table", {"id": "grd_not_listesi"})

    if not tablo:
        return []

    not_listesi = []

    for satir in tablo.find_all("tr")[1:]:
        hucreler = satir.find_all("td")

        if len(hucreler) < 8:
            continue

        not_listesi.append({
            "ders": hucreler[2].text.strip(),
            "sinav": hucreler[4].text.strip(),
            "ortalama": hucreler[5].text.strip(),
            "harf": hucreler[6].text.strip(),
            "durum": hucreler[7].text.strip()
        })

    return not_listesi


def sayfadaki_notlari_bul(page):
    notlar = notlari_parse_et(page.content())

    if notlar:
        return notlar

    for frame in page.frames:
        try:
            notlar = notlari_parse_et(frame.content())

            if notlar:
                return notlar
        except Exception:
            pass

    return []


def not_imzasi_olustur(notlar):
    return json.dumps(notlar, sort_keys=True, ensure_ascii=False)


def telegram_not_mesaji_olustur(notlar):
    mesaj = "📢 NOT DEĞİŞTİ!\n\n"

    for not_bilgisi in notlar:
        mesaj += f"📌 Ders: {not_bilgisi['ders']}\n"
        mesaj += f"📝 Sınav: {not_bilgisi['sinav']}\n"
        mesaj += f"📊 Ortalama: {not_bilgisi['ortalama']}\n"
        mesaj += f"🔤 Harf: {not_bilgisi['harf']}\n"
        mesaj += f"✅ Durum: {not_bilgisi['durum']}\n\n"

    return mesaj


def insan_gibi_davran(page):
    try:
        if random.random() < 0.3:
            page.mouse.move(
                random.randint(100, 600),
                random.randint(100, 600)
            )
            page.mouse.wheel(0, random.randint(50, 200))
            page.keyboard.press("Shift")
    except Exception:
        pass


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch_persistent_context(
            "profil",
            headless=False
        )

        page = browser.new_page()
        page.goto("https://obs.kku.edu.tr/oibs/login.aspx")

        print("OBS'ye giriş yap.")
        print("Not sayfasını aç.")
        print("Hazır olduğunda ENTER tuşuna bas.")
        input()

        eski_not_imzasi = ""
        ilk_okuma = True
        oturum_gitti = False

        telegram_mesaj("🟢 Not takip sistemi başladı.")

        while True:
            try:
                insan_gibi_davran(page)

                notlar = sayfadaki_notlari_bul(page)

                if notlar:
                    oturum_gitti = False
                    yeni_not_imzasi = not_imzasi_olustur(notlar)

                    if yeni_not_imzasi != eski_not_imzasi:
                        print("Not değişikliği algılandı.")

                        if ilk_okuma:
                            print("İlk okuma yapıldı. Bildirim gönderilmedi.")
                            ilk_okuma = False
                        else:
                            mesaj = telegram_not_mesaji_olustur(notlar)
                            telegram_mesaj(mesaj)

                        eski_not_imzasi = yeni_not_imzasi

                    else:
                        print("Değişiklik yok:", time.strftime("%H:%M"))

                else:
                    print("Oturum yok veya not tablosu bulunamadı.")

                    if not oturum_gitti:
                        telegram_mesaj("⚠️ Oturum düşmüş olabilir. Lütfen tekrar giriş yap.")
                        oturum_gitti = True

                time.sleep(KONTROL_ARALIGI)

            except KeyboardInterrupt:
                telegram_mesaj("🔴 Not takip sistemi kapatıldı.")
                print("Sistem kapatıldı.")
                break

            except Exception as e:
                print("Hata:", e)
                time.sleep(KONTROL_ARALIGI)


if __name__ == "__main__":
    main()
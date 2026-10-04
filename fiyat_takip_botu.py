import os
import smtplib # YENİ: E-posta sunucusuna bağlanmak için
import time
from email.mime.text import MIMEText #YENİ; E-posta içeriğini HTML/metin formatlamak için
from bs4 import BeautifulSoup #Yeni EKLENDİ: Sayfayı ayrıştırmak için.
from dotenv import load_dotenv # .env dosyasındaki değişkenleri yüklemek için
import requests

# .env dosyasındaki gizli bilgileri (SENDER_EMAIL, APP_PASSWORD vb.) hafızaya yüklüyoruz
load_dotenv()

#! -------------------------------------------------------------
#* E-POSTA GÖNDERME FONKSİYONU
#! -------------------------------------------------------------

def eposta_gonder(urun_fiyati):
    # 1. Bilgilerin tanımlanması
    gonderen_eposta = os.getenv("SENDER_EMAIL")
    uygulama_sifresi = os.getenv("APP_PASSWORD")
    alici_eposta = os.getenv("RECEIVER_EMAIL") #? bildirimin gideceği e posta

    #! 2. E-posta Başlığı ve İçeriği
    konu = "🔔 İNDİRİM ALARMI: Ürün Fiyatı Düştü!"
    icerik = (
        f"Takip ettiğiniz ürünün fiyatı hedefinize düştü!\n"
        f"Güncel Fiyat: £{urun_fiyati}\n\n"
        f"Ürün Linki: https://books.toscrape.com/"
    )

    #! 3. Mesaj Objesinin Hazırlanması (UTF-8 desteği türkçe karakter hatasını önler)
    msg = MIMEText(icerik, "plain", "utf-8")
    msg["Subject"] = konu
    msg["From"] = gonderen_eposta
    msg["To"] = alici_eposta

    try:
        #! 4. Gmail SMTP Sunucusuna bağlanma (port 587)
        sunucu = smtplib.SMTP("smtp.gmail.com", 587)

        #! 5. Güvenli tünel Oluşturma (TLS - Transport Layer Security)
        sunucu.starttls()

        #! 6. Sunucuya giriş yapma
        sunucu.login(gonderen_eposta, uygulama_sifresi)

        #! 7. E-postayı gönderme
        sunucu.sendmail(gonderen_eposta, alici_eposta, msg.as_string())

        print("✅ E posta başarıyla gönderildi!")

        #! 8. Bağlantıyı Güvenli Şekilde Kapatma
        sunucu.quit()

    except Exception as hata:
        print("❌ E-posta gönderilirken bir hata oluştu:", hata)



#! -------------------------------------------------------------
#* 2. FİYAT KONTROL FONKSİYONU
#! -------------------------------------------------------------

def fiyat_kontrol_et():
    url = "https://books.toscrape.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 "
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            fiyat_etiketi = soup.find("p", class_="price_color")

            temiz_fiyat = fiyat_etiketi.text.replace("£", "").replace("Â", "")
            fiyat_sayi = float(temiz_fiyat)

            hedef_fiyat = 60.00
            zaman = time.strftime("%H:%M:%S")

            print(
                f"[{zaman}] Kontrol edildi -> Güncel Fiyat: £{fiyat_sayi} | {hedef_fiyat}"
            )

            if fiyat_sayi < hedef_fiyat:
                print("🔔 Fiyat hedefin altında! E-posta gönderiliyor...")
                eposta_gonder(fiyat_sayi)
            else:
                print("❌ Fiyat hala yüksek")
        else:
            print(f"⚠️ Siteye erişilemedi, Durum Kodu: {response.status_code}")
    except Exception as e:
        print("Sorgu sırasında hata oluştu", e)


#! -------------------------------------------------------------
#* 3. ZAMANLAYICI DÖNGÜSÜ (OTOMASYON)
#! -------------------------------------------------------------

if __name__ == "__main__":
    print("🚀Fiyat Takip Botu Çalıştırıldı...")
    print("-----------------------------------------------------")


    #? Botu durdurana kadar sonsuz döngüde çalıştırıyoruz
    while True:
        fiyat_kontrol_et()
        # Test amaçlı 10 saniyede bir kontrol eder (Gerçek Kullanımda 3600 yapıp 1 saatte bir kontrol edebilirsin.)
        print(" 10 saniye sonra tekrar kontrol edilecek... \n")
        time.sleep(10)

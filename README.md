# 📈 Akıllı E-Ticaret Fiyat Takip Botu

Bu proje, belirlenen e-ticaret sayfalarındaki ürün fiyatlarını otomatik ve periyodik olarak takip eden, fiyat belirlenen hedef seviyenin altına düştüğünde kullanıcıya e-posta bildirimi gönderen bir Python otomasyon botudur.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x**
* **Requests:** HTTP istekleri ile web sayfalarına erişim sağlama
* **BeautifulSoup4 (BS4):** HTML yapısını ayrıştırma ve veri kazıma (Web Scraping)
* **smtplib & email.mime:** SMTP protokolü üzerinden şifreli ve güvenli e-posta bildirimi gönderme
* **python-dotenv:** E-posta adresi ve uygulama şifresi gibi hassas verilerin `.env` mimarisiyle güvenli saklanması

## 🚀 Öne Çıkan Özellikler

* **Bot Tespiti Engelleme:** Özel `User-Agent` başlıkları kullanılarak isteklerin güvenli şekilde iletilmesi.
* **Veri Temizleme & Tip Dönüşümü:** Metin (string) formatındaki karmaşık fiyat verisinin ayıklanarak matematiksel kıyaslamalara uygun `float` tipe dönüştürülmesi.
* **Güvenli Mimari (Environment Variables):** Hassas bilgilerin koda gömülmesini engelleyen `.env` ve `.gitignore` entegrasyonu.
* **Zamanlayıcı Otomasyonu:** Arka planda belirlenen periyotlarla kesintisiz kontrol sağlayan döngü yapısı.

## 💻 Kurulum ve Çalıştırma

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/yigithanenez/fiyat-takip-botu.git](https://github.com/yigithanenez/fiyat-takip-botu.git)
   cd fiyat-takip-botu
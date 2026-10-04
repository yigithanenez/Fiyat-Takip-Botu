# 📈 Akıllı E-Ticaret Fiyat Takip Botu

Bu proje, belirlenen e-ticaret sayfalarındaki ürün fiyatlarını otomatik ve periyodik olarak takip eden, fiyat belirlenen hedef seviyenin altına düştüğünde kullanıcıya e-posta bildirimi gönderen bir Python otomasyon botudur.

## 🛠️ Kullanılan Teknolojiler

* **Python 3.x** - Programlama dili
* **Requests:** HTTP istekleri ile web sayfalarına erişim sağlama
* **BeautifulSoup4 (BS4):** HTML yapısını ayrıştırma ve veri kazıma (Web Scraping)
* **smtplib & email.mime:** SMTP protokolü üzerinden şifreli ve güvenli e-posta bildirimi gönderme
* **python-dotenv:** E-posta adresi ve uygulama şifresi gibi hassas verilerin `.env` mimarisiyle güvenli saklanması

## 🚀 Öne Çıkan Özellikler

* **Bot Tespiti Engelleme:** Özel `User-Agent` başlıkları kullanılarak isteklerin güvenli şekilde iletilmesi.
* **Veri Temizleme & Tip Dönüşümü:** Metin (string) formatındaki karmaşık fiyat verisinin ayıklanarak matematiksel kıyaslamalara uygun `float` tipe dönüştürülmesi.
* **Güvenli Mimari (Environment Variables):** Hassas bilgilerin koda gömülmesini engelleyen `.env` ve `.gitignore` entegrasyonu.
* **Zamanlayıcı Otomasyonu:** Arka planda belirlenen periyotlarla kesintisiz kontrol sağlayan döngü yapısı.
* **E-posta Bildirimleri:** Fiyat düştüğünde otomatik olarak bildirim gönderme.

## 📋 Proje Yapısı

fiyatTakipBotu/
├── fiyat_takip_botu.py # Ana bot dosyası
├── requirements.txt # Bağımlılıklar
├── .env.example # Ortam değişkenleri template'i
├── .gitignore # Git ignore kuralları
├── README.md # Bu dosya
└── LICENSE # MIT Lisansı

# 💻 Kurulum ve Çalıştırma

### 1. Repoyu Klonla

```bash
git clone https://github.com/yigithanenez/fiyatTakipBotu.git
cd fiyatTakipBotu
```

### 2. Virtual Environment Oluştur

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Bağımlılıkları Yükle

```bash
pip install -r requirements.txt
```

### 4. `.env` Dosyasını Yapılandır

`.env` dosyası oluştur ve şunları ekle:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
TARGET_PRICE=5000
CHECK_INTERVAL=3600
```

> **Not:** Gmail kullanıyorsan, [App Password](https://myaccount.google.com/apppasswords) oluşturmalısın (2FA aktif olmalı)

### 5. Botu Çalıştır

```bash
python fiyat_takip_botu.py
```

## 📝 Örnek Çıktı
[2024-01-15 10:30:45] Bot başlatıldı...
[2024-01-15 10:30:50] Ürün fiyatı kontrol ediliyor: iPhone 15 Pro
[2024-01-15 10:30:52] Güncel Fiyat: 35,999 TL
[2024-01-15 10:30:53] Hedef Fiyat: 30,000 TL
[2024-01-15 10:30:53] Fiyat henüz hedef seviyeye ulaşmadı. 5,999 TL fark var.
[2024-01-15 10:30:54] Sonraki kontrol: 10:31:54


Fiyat hedef seviyeye düştüğünde:
[2024-01-16 14:22:10] ✅ FİYAT DÜŞTÜ!
[2024-01-16 14:22:10] Ürün: iPhone 15 Pro
[2024-01-16 14:22:10] Yeni Fiyat: 29,500 TL
[2024-01-16 14:22:11] E-posta gönderildi: your_email@gmail.com

## ⚙️ Konfigürasyon

`fiyat_takip_botu.py` dosyasında şu değişkenleri özelleştirebilirsin:

| Değişken | Açıklama | Örnek |
|----------|----------|-------|
| `URL` | Takip edilecek e-ticaret sayfası | `https://example.com/product` |
| `TARGET_PRICE` | Hedef fiyat (TL) | `5000` |
| `CHECK_INTERVAL` | Kontrol aralığı (saniye) | `3600` (1 saat) |
| `EMAIL_ADDRESS` | Bildirimlerin gönderileceği mail | `your@email.com` |

## 🐛 Sorun Giderme

### Bot `[SSL: CERTIFICATE_VERIFY_FAILED]` hatası veriyor

```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

### E-posta gönderilmiyor

- Gmail kullanıyorsan [App Password](https://myaccount.google.com/apppasswords) oluştur
- `.env` dosyasının doğru yolda olduğunu kontrol et
- İnternet bağlantını kontrol et

### Fiyat verileri alınamıyor

- Web sitesinin yapısı değişmiş olabilir
- CSS selector'ları güncelle
- Tarayıcının Developer Tools'unda HTML yapısını kontrol et (F12)

## 🤝 Katkıda Bulunma

Projemize katkıda bulunmak istiyorsan, lütfen şu adımları izle:

1. Repository'yi **fork** et
2. **Feature branch** oluştur: `git checkout -b feature/YeniOzellik`
3. Değişiklikleri **commit** et: `git commit -m 'Add: Yeni özellik'`
4. Branch'i **push** et: `git push origin feature/YeniOzellik`
5. **Pull Request** aç

## 📄 Lisans

Bu proje **MIT License** altında lisanslanmıştır.  
Detaylar için [LICENSE](LICENSE) dosyasını incele.

## 👨‍💻 Geliştirici

**Yiğit Hanenez**  
📧 E-posta: [email'in varsa]  
🔗 GitHub: [@yigithanenez](https://github.com/yigithanenez)  
💼 LinkedIn: [linkedinprofilin varsa ekle]

---

⭐ **Eğer bu proje sana yardımcı olduysa, lütfen bir yıldız vermeyi unutma!**

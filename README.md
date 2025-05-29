# 🎵 Şarkı Sözü Üretici

Bu proje, kullanıcıdan alınan bir **anahtar kelime** ile özgün şarkı sözleri üretebilen bir doğal dil işleme (NLP) uygulamasıdır. **Markov Zinciri** tabanlı bu sistem, sıfırdan geliştirilmiş olup herhangi bir dış API veya önceden eğitilmiş büyük modele bağımlı değildir.

## 🚀 Proje Amacı

Amaç; yaratıcı yazarlar, müzisyenler ve içerik üreticileri gibi kullanıcıların yalnızca bir kelime girerek **çeşitli ve özgün şarkı sözleri** elde etmesini sağlamaktır. Her üretim benzersizdir, bu sayede sistem ilham verici bir araç olarak kullanılabilir.

## ⚙️ Özellikler

- 🎯 Anahtar kelimeye göre özgün şarkı sözü üretimi yapar. 
- 📌 Girilen kelime mutlaka ilk satırda yer alır.  
- 🧠 Veri kümesinde olmayan kelimeler için en yakın eşleşme bulunur.  
- 💻 Web arayüzü sade, kullanıcı dostu ve mobil uyumludur.  
- 🔒 Dış servis veya API kullanımı yok – tamamen yerel çalışır. 

## 🛠 Kullanılan Teknolojiler

- Python 3.x  
- Flask  
- HTML & CSS  
- Jupyter Notebook (testler için)  
- Git ve GitHub  

## 🧪 Test Senaryoları

- Geçerli ve geçersiz kelime girişleriyle üretim kontrolü  
- Çeşitlilik testleri (aynı kelime → farklı çıktılar)  
- Mobil görünüm testleri  
- Tarayıcı uyumluluğu  

## 🧱 Sistem Mimarisi

- Flask tabanlı web uygulaması  
- Şarkı verisi `songs1.txt` dosyasından okunur  
- Markov modeli bellekte çalışır, her istek sonrası yeni üretim yapılır  
- Veritabanı kullanılmaz

## 🚀 Nasıl Kullanılır?

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Projeyi Klonlayın:**
    Öncelikle, projenin GitHub deposunu bilgisayarınıza klonlayın. Eğer projenin bir GitHub deposu varsa, aşağıdaki gibi bir komut kullanabilirsiniz (URL'yi kendi projenizin adresiyle değiştirmeyi unutmayın):
    ```bash
    git clone https://github.com/Gulnaz-Aydemir/Uretken-Yapay-Zeka
    cd Uretken-Yapay-Zeka
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    Projenin çalışabilmesi için Python 3.x ve Flask kütüphanesinin kurulu olması gerekmektedir. Eğer sisteminizde Flask kurulu değilse, terminal veya komut istemcisi üzerinden aşağıdaki komut ile yükleyebilirsiniz:
    ```bash
    pip install Flask
    ```

3.  **Uygulamayı Çalıştırın:**
    Proje dosyalarının bulunduğu ana dizindeyken aşağıdaki komutu terminalde veya komut istemcisinde çalıştırarak Flask geliştirme sunucusunu başlatın:
    ```bash
    python app.py
    ```

4.  **Tarayıcıda Açın:**
    Uygulama başarıyla başlatıldığında, terminalde genellikle şöyle bir mesaj görürsünüz:
    `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
    Bu durumda, web tarayıcınızı açıp adres çubuğuna `http://127.0.0.1:5000/` yazarak şarkı sözü üretme arayüzüne erişebilirsiniz.

## 📅 Geliştirme Planı

| Sprint | Görev                                      | Süre |
|--------|--------------------------------------------|------|
| 1      | Veri seti temizleme                        | 2 gün |
| 2      | Markov zinciri modeli                      | 3 gün |
| 3      | Flask arayüz geliştirme                    | 2 gün |
| 4      | UI/UX ve mobil uyumluluk                   | 1 gün |
| 5      | Testler ve GitHub entegrasyonu             | 1 gün |

> Tüm geliştirme çalışmaları bireysel olarak gerçekleştirilmiştir. Agile metodolojiyle iteratif şekilde ilerlenmiştir.

## 📌 Gelecek Geliştirmeler

- Müzik türlerine özel şarkı sözü üretimi  
- Ritim ve ölçü uyumu  
- Daha gelişmiş dil modelleriyle karşılaştırmalı testler  

## 📚 Kaynakça

- Jurafsky & Martin – *Speech and Language Processing*  
- [Python Docs](https://docs.python.org)  
- [Flask Docs](https://flask.palletsprojects.com)  
- Medium ve Towards Data Science blog yazıları  
- `songs1.txt` – Kullanılan şarkı verisi
- 'songs2.txt' - Kullanılan şarkı verisi
- 'songs3.txt' - Kullanılan şarkı verisi
- 'songs4.txt' - Kullanılan şarkı verisi
- 'songs5.txt' - Kullanılan şarkı verisi

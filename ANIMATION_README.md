# Manim Animasyon Projesi - Bölüm 1

Bu proje, "Kaosun Düzene Dönüşümü" temalı bir Manim animasyonu içerir.

## Kurulum

1. Python 3.8 veya üzeri gereklidir
2. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

## Animasyonu Render Etme

### Düşük kalite (hızlı önizleme)
```bash
manim -pql main.py ChaosToOrderScene
```

### Orta kalite
```bash
manim -pqm main.py ChaosToOrderScene
```

### Yüksek kalite
```bash
manim -pqh main.py ChaosToOrderScene
```

### 4K kalite (prodüksiyon)
```bash
manim -pqk main.py ChaosToOrderScene
```

## Animasyon Detayları

### Zaman Çizelgesi (Toplam ~50 saniye)

1. **0:00 - 0:05**: Siyah ekran (bekle)
2. **0:05 - 0:15**: Parlak beyaz nokta ortada belirir ve "pulse" (nefes alma) efekti
3. **0:15 - 0:30**: Rastgele noktalar belirir:
   - İlk 10 nokta (5 saniye)
   - Sonraki 20 nokta (5 saniye)
   - Son 70 nokta (5 saniye)
4. **0:30 - 0:50**: Sinematik yazılar:
   - "KAOS..." (3 saniye belirir, 2 saniye kalır, 2 saniye kaybolur)
   - "...DÜZENİ DOĞURABİLİR Mİ?" (3 saniye belirir, 5 saniye kalır)

### Özellikler

- Siyah arkaplan (BLACK)
- Parlak beyaz noktalar
- Pulse animasyonu (scale efekti ile)
- LaggedStart ile kademeli nokta oluşumu
- Cinematic fade efektleri

## Gelecek Geliştirmeler

- Ses dosyası ekleme (prodüksiyon aşamasında)
- Glow efekti iyileştirmeleri
- Daha karmaşık animasyon geçişleri
- Ek sahneler (Bölüm 2, 3, vb.)

## Notlar

- Video dosyası `media/videos/main/` klasöründe oluşturulacaktır
- Render süresi seçilen kaliteye göre değişir (düşük: ~1-2 dakika, 4K: ~10-15 dakika)
- İlk render sırasında Manim gerekli font ve bağımlılıkları indirecektir

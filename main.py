"""
Manim Animation - Part 1: Chaos and Order
Bu animasyon, kaosun düzene dönüşümünü görselleştirir.

Zaman Çizelgesi:
- 0:00 - 0:05: Siyah ekran (bekleme)
- 0:05 - 0:15: Parlak beyaz nokta ortada belirir ve pulse efekti
- 0:15 - 0:30: Rastgele noktalar belirir (10, 20, 70 aşamalı)
- 0:30 - 0:50: "KAOS..." ve "...DÜZENİ DOĞURABİLİR Mİ?" yazıları
"""

from manim import *
import random

class ChaosToOrderScene(Scene):
    def construct(self):
        # Arkaplan siyah olarak ayarlanır (varsayılan)
        self.camera.background_color = BLACK
        
        # ===== SAHNE BAŞLANGICI (0:00 - 0:05) =====
        # İlk 5 saniye boyunca ekranda hiçbir şey görünmez
        self.wait(5)
        
        # ===== MİNİK PARLAK NOKTA (0:05 - 0:15) =====
        # Ekranın ortasında parlak beyaz bir nokta belirir
        center_dot = Dot(point=ORIGIN, color=WHITE, radius=0.1)
        
        # Nokta belirir (FadeIn) - 1 saniye
        self.play(FadeIn(center_dot), run_time=1)
        
        # Pulse (nefes alma) efekti - nokta büyüyüp küçülür
        # 9 saniye boyunca 3 kez pulse efekti (her biri 3 saniye)
        for _ in range(3):
            self.play(
                center_dot.animate.scale(2),
                run_time=3,
                rate_func=there_and_back
            )
        
        # ===== NOKTALARIN OLUŞUMU (0:15 - 0:30) =====
        # Rastgele konumlarda noktalar belirir
        
        # İlk grup: 10 nokta
        dots_group_1 = VGroup()
        for _ in range(10):
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            dot = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
            dots_group_1.add(dot)
        
        # İkinci grup: 20 nokta
        dots_group_2 = VGroup()
        for _ in range(20):
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            dot = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
            dots_group_2.add(dot)
        
        # Üçüncü grup: 70 nokta
        dots_group_3 = VGroup()
        for _ in range(70):
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            dot = Dot(point=[x, y, 0], color=WHITE, radius=0.05)
            dots_group_3.add(dot)
        
        # LaggedStart ile noktaları sırayla belirir
        # İlk 10 nokta (5 saniye içinde)
        self.play(
            LaggedStart(*[FadeIn(dot) for dot in dots_group_1], lag_ratio=0.5),
            run_time=5
        )
        
        # Sonraki 20 nokta (5 saniye içinde)
        self.play(
            LaggedStart(*[FadeIn(dot) for dot in dots_group_2], lag_ratio=0.25),
            run_time=5
        )
        
        # Son 70 nokta (5 saniye içinde)
        self.play(
            LaggedStart(*[FadeIn(dot) for dot in dots_group_3], lag_ratio=0.07),
            run_time=5
        )
        
        # ===== SİNEMATİK YAZI (0:30 - 0:50) =====
        # "KAOS..." yazısı belirir
        text_kaos = Text("KAOS...", font_size=72, color=WHITE)
        text_kaos.move_to(ORIGIN)
        
        # Yavaşça belirir (3 saniye)
        self.play(FadeIn(text_kaos, shift=UP*0.5), run_time=3)
        
        # 2 saniye ekranda kalır
        self.wait(2)
        
        # Kaybolur (2 saniye)
        self.play(FadeOut(text_kaos, shift=DOWN*0.5), run_time=2)
        
        # "...DÜZENİ DOĞURABİLİR Mİ?" yazısı belirir
        text_duzen = Text("...DÜZENİ DOĞURABİLİR Mİ?", font_size=48, color=WHITE)
        text_duzen.move_to(ORIGIN)
        
        # Yavaşça belirir (3 saniye)
        self.play(FadeIn(text_duzen, shift=UP*0.5), run_time=3)
        
        # Son kare için 10 saniye bekle (toplam 20 saniye için)
        self.wait(10)
        
        # NOT: Daha fazla geliştirme için:
        # - Ses eklemek için: self.add_sound("ses_dosyasi.mp3")
        # - Glow efekti için ek shader veya büyütülmüş opacity efektleri
        # - Daha karmaşık animasyonlar için Transform ve morph kullanılabilir
        # - Video render: manim -pql main.py ChaosToOrderScene (düşük kalite)
        #                 manim -pqh main.py ChaosToOrderScene (yüksek kalite)
        #                 manim -pqk main.py ChaosToOrderScene (4K kalite)

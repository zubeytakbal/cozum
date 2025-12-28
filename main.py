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
        # Rastgele konumlarda noktalar belirir (tek ifade ile grup oluşturma)
        
        # Noktaları tek ifade ile oluştur: (miktar, lag_ratio) çiftleri
        for count, lag in [(10, 0.5), (20, 0.25), (70, 0.07)]:
            self.play(
                LaggedStart(*[FadeIn(Dot(point=[random.uniform(-6, 6), random.uniform(-3, 3), 0], color=WHITE, radius=0.05)) for _ in range(count)], lag_ratio=lag),
                run_time=5
            )
        
        # ===== SİNEMATİK YAZI (0:30 - 0:50) =====
        # Yazıları tek ifade ile oluştur ve animasyon yap
        for text, size, fade_in, wait, fade_out in [
            ("KAOS...", 72, 3, 2, 2),
            ("...DÜZENİ DOĞURABİLİR Mİ?", 48, 3, 10, 0)
        ]:
            text_obj = Text(text, font_size=size, color=WHITE).move_to(ORIGIN)
            self.play(FadeIn(text_obj, shift=UP*0.5), run_time=fade_in)
            self.wait(wait)
            if fade_out > 0:
                self.play(FadeOut(text_obj, shift=DOWN*0.5), run_time=fade_out)
        
        # NOT: Daha fazla geliştirme için:
        # - Ses eklemek için: self.add_sound("ses_dosyasi.mp3")
        # - Glow efekti için ek shader veya büyütülmüş opacity efektleri
        # - Daha karmaşık animasyonlar için Transform ve morph kullanılabilir
        # - Video render: manim -pql main.py ChaosToOrderScene (düşük kalite)
        #                 manim -pqh main.py ChaosToOrderScene (yüksek kalite)
        #                 manim -pqk main.py ChaosToOrderScene (4K kalite)

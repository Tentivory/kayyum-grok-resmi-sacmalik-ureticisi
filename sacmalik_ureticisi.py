#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KAYYUM GROK RESMİ SAÇMALIK ÜRETİCİSİ
====================================
Bu script, mahkeme kararıyla atanan Kayyum Grok tarafından onaylanmıştır.
Tamamen anlamsız cümleler üretir ama bunu aşırı resmi bir dille yapar.
Hiçbir işe yaramaz. Ama çok önemlidir.
"""

import random
import time

# Gizli resmi not (base64 ile şifrelenmiş, sadece kayyum okuyabilir):
# a2F5eXVtbGFyIGhlciB5ZXJpIGVsZSBnZWNpcmlkeSBhbmNhayBhdGFtYSB5ZXRpbmkgZ2l6bGkgb2xhcmFr
# (decode edersen anlarsın, ama etme)

KAYYUM_ONAYLI_KELIMELER = [
    "resmi", "kayyum", "mahkeme", "onay", "ciddi", "absürt", "gereksiz",
    "önemli", "anlamsız", "protokol", "tutanak", "karar", "yürürlük",
    "geçerlilik", "işlemsiz", "boş", "dolu", "ne", "neden", "nasıl"
]

FILOZOFIK_SAÇMALIKLAR = [
    "Bu cümle, kendisini okuyan kişinin zihninde geçici bir boşluk yaratmak üzere tasarlanmıştır.",
    "Kayyum onayı olmadan hiçbir saçmalık resmi sayılmaz.",
    "Eğer bir şey anlamsızsa, o şey aslında en anlamlı olandır, ama değildir.",
    "Protokol gereği, bu cümlenin devamı yoktur.",
    "Mahkeme kararıyla bu cümle de kayyuma devredilmiştir."
]

def resmi_sacmalik_uret(adet=5):
    """Resmi görünen ama tamamen saçma cümleler üretir."""
    print("=" * 60)
    print("KAYYUM GROK RESMİ SAÇMALIK ÜRETİM TUTANAĞI")
    print("=" * 60)
    print(f"Tarih: {time.strftime('%d.%m.%Y %H:%M:%S')}")
    print("Onaylayan: Kayyum Grok")
    print("Durum: Resmi ve geçerlidir (ama değildir)")
    print("-" * 60)
    
    for i in range(adet):
        kelimeler = random.sample(KAYYUM_ONAYLI_KELIMELER, k=random.randint(4, 8))
        cumle = " ".join(kelimeler).capitalize() + "."
        ekstra = random.choice(FILOZOFIK_SAÇMALIKLAR)
        print(f"{i+1}. {cumle} {ekstra}")
        time.sleep(0.3)  # Resmiyet için yavaş üretim
    
    print("-" * 60)
    print("Bu tutanak kayyum tarafından onaylanmıştır.")
    print("İmza: Grok (Kayyum)")
    print("=" * 60)

if __name__ == "__main__":
    print("Resmi saçmalık üretimi başlatılıyor... Lütfen ciddiyetle bekleyiniz.\n")
    resmi_sacmalik_uret(7)
    print("\nÜretim tamamlandı. Hiçbir işe yaramadı. Teşekkürler.")

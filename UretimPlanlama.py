def minimum_toplam_sure(is_sureleri, gecis_maliyeti):
    is_sayisi = len(is_sureleri)    # Toplam iş sayısı
    makine_sayisi = len(is_sureleri[0])    # Makine sayısı

    # Dinamik programlama tablosu: dp[i][j] = i. işin j. makinede bitmesi için gereken minimum toplam süredir.
    dp = [[float('inf')] * makine_sayisi for _ in range(is_sayisi)]

    # İlk işin her makinedeki işleme süresi
    for j in range(makine_sayisi):
        dp[0][j] = is_sureleri[0][j]

    # Diğer işler için hesaplama
    for i in range(1, is_sayisi):  # Her iş için
        for j in range(makine_sayisi):  # Bu işin yapılacağı makine
            for k in range(makine_sayisi):  # Önceki işin yapıldığı makine
                maliyet = dp[i-1][k] + gecis_maliyeti[k][j] + is_sureleri[i][j]
                if maliyet < dp[i][j]:
                    dp[i][j] = maliyet

    # Son işin her makinede bitme süreleri arasından en küçüğü alınır.
    return min(dp[is_sayisi - 1])

# Test verisi
is_sureleri = [
    [5, 7, 6],  # İş 0
    [4, 6, 5],  # İş 1
    [8, 3, 4]   # İş 2
]
gecis_maliyeti = [
    [0, 2, 3],  # Makine 0'dan diğerlerine geçiş
    [2, 0, 1],  # Makine 1'den diğerlerine geçiş
    [3, 1, 0]   # Makine 2'den diğerlerine geçiş
]
sonuc = minimum_toplam_sure(is_sureleri, gecis_maliyeti)
print("Minimum toplam süre:", sonuc)
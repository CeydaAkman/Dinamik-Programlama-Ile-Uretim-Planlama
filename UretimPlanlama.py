def minimum_toplam_sure(is_sureleri, gecis_maliyeti):
    is_sayisi = len(is_sureleri)
    makine_sayisi = len(is_sureleri[0])

    dp = [[float('inf')] * makine_sayisi for _ in range(is_sayisi)]

    for j in range(makine_sayisi):
        dp[0][j] = is_sureleri[0][j]

    for i in range(1, is_sayisi):
        for j in range(makine_sayisi):
            for k in range(makine_sayisi):
                maliyet = dp[i-1][k] + gecis_maliyeti[k][j] + is_sureleri[i][j]
                if maliyet < dp[i][j]:
                    dp[i][j] = maliyet

    return min(dp[is_sayisi - 1])

is_sureleri = [
    [5, 7, 6], 
    [4, 6, 5],  
    [8, 3, 4]   
]
gecis_maliyeti = [
    [0, 2, 3],  
    [2, 0, 1], 
    [3, 1, 0]  
]
sonuc = minimum_toplam_sure(is_sureleri, gecis_maliyeti)
print("Minimum toplam süre:", sonuc)

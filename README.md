# Dinamik Programlama İle Üretim Planlama 

Bu proje, üretim sürecinde arka arkaya gerçekleştirilecek işler için en uygun makine sıralamasını bularak toplam süreyi en aza indirmeyi amaçlar. Her iş, farklı makinelerde farklı sürelerde tamamlanabilir ve bir işin bir makinede yapıldıktan sonra diğer işin farklı bir makinede yapılması durumunda belirli bir geçiş maliyeti oluşur. Proje, bu geçiş maliyetlerini ve iş sürelerini dikkate alarak tüm işleri sırasıyla en kısa sürede tamamlamak üzere dinamik programlama temelli bir çözüm sunar.

# Kullanım Adımları

1. Projeyi bilgisayarınıza indirin veya GitHub'dan klonlayın.
2. Python yüklü olduğundan emin olun.
3. Terminal veya komut istemcisinde UretimPlanlama.py komutunu çalıştırarak projeyi çalıştırın.
4. Program içinde tanımlı test verileriyle otomatik olarak çalışır ve minimum toplam süreyi ekrana yazdırır.

# Kod Yapısı

Veri Girişi: is_sureleri ve gecis_maliyeti matrisleri kullanıcı tarafından belirlenir.

İlk İşin Süreleri: Her makinede ilk işin süresi doğrudan alınır.

Dinamik Programlama Tablosu: dp[i][j] i. işin j. makinede yapılması durumundaki minimum toplam süredir. Bu süre, önceki işin yapıldığı makinedeki süre, geçiş maliyeti ve o makinedeki işlem süresi toplanarak hesaplanır.

Geçiş Maliyetleri Dikkate Alınarak Hesaplama: Her iş ve her makine için, en uygun önceki makine kombinasyonu bulunur. Daha düşük maliyetli geçiş ve işlem süresi ile dp tablosu güncellenir.

Minimum Süre Hesaplama: Son işin her makinede bitme süresi hesaplandıktan sonra, en küçük değer seçilir.

Sonuç Yazdırma: Konsola hesaplanan minimum toplam süre yazdırılır.

# Programın İşleyişi

1. İlk olarak, her işin her makinedeki sürelerini içeren dp tablosu oluşturulur.
2. İlk işin her makinedeki işlem süreleri doğrudan dp tablosuna aktarılır.
3. Sonraki işler için, her işin hangi makinede yapılacağına ve geçiş maliyetlerine göre minimum süre hesaplanır.
4. Her işin her makine için bitiş süresi, önceki işin bitiş süresi ve geçiş maliyeti dikkate alınarak güncellenir.
5. Son işin her makinedeki bitiş sürelerinden en küçük olanı seçilir.
6. Minimum toplam süre ekrana yazdırılır.

# Kullanılan Teknolojiler

Programlama Dili: Proje Python dilinde yazılmıştır.

Dinamik Programlama: Bu projede dinamik programlama alt problemlerin çözümlerini saklayarak tekrar hesaplama yapılmadan en optimal sonuca ulaşmak için kullanılmıştır.

# Ekran Çıktısı

![Üretim Planlam Ekran Çıktısı](https://github.com/user-attachments/assets/f0279980-0708-4c18-a99a-9867ddb85e4e)

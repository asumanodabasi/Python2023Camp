Decorators in the PyTest
  
Dekoratörler diğer fonksiyonların işlevselliğini değiştiren fonksiyonlardır. Kodu kısaltırlar ve daha anlaşılır hale getirirler. Bir dekoratör aslında fonksiyon çağıran bir fonksiyodan başka bir şey değildir. Kendisinden önce, @ işareti ile geldiği fonksiyonu çalıştırmadan önce kendi içinde sarmanlanmış işleri yapar ve sonra kendisinden sonra gelen fonksiyonu çağırarak onun görevini yerine getirmesini sağlar.

@pytest.fixture: Bu dekoratör, testler arasında ortak bir durum veya kaynak paylaşmak için kullanılır. Örneğin, testlerinizin bir veritabanına bağlanmasını gerektiriyorsa, bu dekoratörü kullanarak veritabanı bağlantısı oluşturabilirsiniz.

@pytest.mark.parametrize: Bu dekoratör, aynı test fonksiyonunu farklı parametrelerle birden fazla kez çalıştırmak için kullanılır. Bu, testlerinizi daha kapsamlı hale getirmenize ve farklı durumlarda farklı sonuçlar alıp almadığınızı kontrol etmenize olanak tanır.

@pytest.mark.skip: Bu dekoratör, belirli testlerin atlanmasını sağlar. Örneğin, belirli bir test henüz tamamlanmamışsa veya hata verdiği için geçici olarak devre dışı bırakmak istiyorsanız, bu dekoratörü kullanabilirsiniz.

@pytest.mark.xfail: Bu dekoratör, belirli testlerin başarısız olmasını beklediğinizi belirtmek için kullanılır. Örneğin, bir hata oluşmasını beklediğiniz bir durumu test ediyorsanız, bu dekoratörü kullanarak testin başarısız olmasını bekleyebilirsiniz.

@pytest.mark.timeout: Bu dekoratör, belirli bir testin belirli bir süre içinde tamamlanmasını zorlar. Örneğin, bir testin belirli bir sürede yanıt vermesi gerekiyorsa veya sonsuza kadar çalışmaması gerekiyorsa, bu dekoratörü kullanabilirsiniz.

@pytest.mark.dependency: Testler arasında bağımlılıklar belirlemek için kullanılır.

@pytest.mark.usefixtures: Test fonksiyonlarına, belirli bir fixture'ı otomatik olarak eklemek için kullanılır.

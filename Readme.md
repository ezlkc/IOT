# Panda

# Proje Ne İş Yapıyor?

	Projemizin amacı, sürekli kullanılan alanlar için kolay bir şekilde nem, sıcaklık gibi verileri uzakdan alabilecek şekilde son kullanıcıya ileterek son kullanıcının gelen veriler sonucunda durum değerlendirmesine göre kolayca o ortamı olması gereken normal değerlerine getirebilmesini sağlamaktadır.

# Fonksiyonel Gereksenim Detayları

Uygulamamızın çalışması için yerine getirmesi gereken bazı fonksiyonlar vardır.

	* nem,sıcaklık vs ölçümleri için sensör kullanılmaktadır bu sensörlerde Wi-Fi
	 bulunmaktadır veri göndermek için.
	* Bu sensörlerden verleri alması ve bu verileri web servisine göndermesi için raspberyPi 	  cihazına ihtiyaç duyulmaktadır.
	* Sensörler ile RPİ arasındaki iletişim için CoAP kullanılacaktır.
	* RPİ içinde:
		* verilerin girişi ve çıkışı için fonksiyon gerekmektedir
		* verilerin ne sıklık ile web servisine gönderilmesi gerektiği ile ilgili bir  			  fonksiyona ihtiyac duyulmaktadır.
		
	* RPİ den gelen verileri gösterebilmek için bir web servisine ihtiyaç duyulmaktadır.

# Fonksiyonel Olmayan Detayları

## Kullanabilirlilik
	* Kullanıcının kolayca kullanabileceği menü tasarımları yapılmalıdır.
	* Kısa yollar ve hızlı erişim olanakları olmalıdır.
	* Menulerde ve kısayollardaki standartlara uyulmalıdır.
	* Butonlar uygun yerlere koyulmalıdır.
	* Yerleşim,fontlar,renk ayarları vs. dikkatle yapılmalıdır.

## Güvenirlik
	* Veri kayıpları mümkün oldugunca sıfıra indirlmelidir.
	* Yazılım mantık hatalarından arındırılmalı ve yazılımın beklenmeyenhareketler           		 yapmasının önüne geçilmelidir.
	* Hata yakalama prosedürleri çalıştırılmalı ve yazılımın kesilmesi durumunda uygun hata 	  mesajları sunulmalıdır.

## Perfonmans
	* Sistem aynı anda kaç kullanıcıyla çalışabileceği belirlenmelidir.
	* Perfonmans ihtiyacı varsa yazılımsal veya donanımsal olarak çözümüne gidilmelidir.

## Desteklenebilirlik
	* Yazılım butun işletim sistemleri tarafından desteklenmelidir(desteklenmektedir).

## Arayüz
	* Verilerin alımı klayve ve fare ile yapılacaktır.
	* Veriler internet varlığında alınacaktır.

# Gizlilik Gereksinimi
	* Kullanılardan sadece kullanım hakları olanlar verilere erişimi olacaktır.

---

# Proje Geliştirme Süreci Adım Adım

RaspberryPi CoAP arasındaki ilişkiyi anlamak için bolca araştırmalar yapıldı document/ dizininde bakılan bir kaç site link verilmiştir.

RaspberryPi CoAP arasındaki ilişki için client-server kodları üzerinde çalışıldı fakat sonuç alınmadı.

Sorun tespiti yapıldı yönlendirme sorunu saptandı ve gerekli ayarlamalar yapıldı.

CoAP client bağlantısını test etmek için firefox eklensi ile Cooper kullanıldı. Bağlantı sağlandıktan sonra client olan firefox u devre dışı bırakıp kendimizi client yapmak için npmjs nin sunduğu coap kullanıldı ve terminalden veriler alındı ve index.html dosyası oluşturuldu fakat bu yapı bilgisayarda sorun çıkardığı için vazgeçildi  ve projeden çıkarıldı.

CoAP client bağlantısı için python kütüphanesinin sunduğu aiocoap kullanıldı ve verilerin alındığı gözlemlendi. Web uygulaması için ise flask kütüphanesi kullanıldı ve doğru sonuçlar alındı.

Veri alınımı sağlandı ve kullanıcı arayüzü için dashboard tasarımı üzerinde çalışıldı. Ön yüz tasarımında material css frameworku kullanıldı. Sensör verilerini ajax sorgusuyla alan methodlar tanımlandı. İstenilen sensörün verisi gerekli butona tıklanarak elde edilmesi sağlanmaya çalışıldı. 



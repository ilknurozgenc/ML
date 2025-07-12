Kalp Krizi Tahmin Modeli 
2025 yılı lisans bitirme tezimde çalışmış olduğum makine öğrenmesi yöntemleri ile kalp krizi model tahmini projemi sizlerle paylaşmaktan mutluluk duyarım. Öğrenme yöntemleri, veri seti, analiz ve daha fazlası.
Bu proje, kalbin elektriksel aktivitesini değerlendirmede temel bir rol oynayan EKG segmentlerinin incelenmesine odaklanmaktadır. EKG, kalbin farklı bölgeleri arasındaki elektriksel iletim süreçlerini anlamamıza yardımcı olan bir tanı aracıdır. Segmentler, EKG dalgaları arasındaki düz çizgi bölgeleri temsil eder ve bu bölgeler, kalbin belirli evrelerdeki elektriksel davranışlarını yansıtır.
Özellikle P-Q (veya PR) segmenti, atriyumlardan ventriküllere doğru gerçekleşen elektriksel iletim sırasında oluşan kısa süreli gecikmeyi gösterir. Bu, kalbin doğal ritminin düzenlenmesinde kritik bir rol oynar. S-T segmenti ise ventriküllerin kasıldığı, fakat kalbin elektriksel olarak izoelektrik (hareketsiz) olduğu dönemi temsil eder. Bu segmentte meydana gelen anormal yükselmeler veya düşüşler, genellikle kalp krizi (miyokard enfarktüsü) gibi ciddi kardiyak problemlerin bir göstergesi olabilir.

MAKİNE ÖĞRENMESİ
Makine öğrenmesi, verileri analiz ederek hastaların kalp krizi riskini tahmin etmeyi hedeflemektedir. Bu süreçte, yaş, cinsiyet, kan basıncı, kolesterol seviyesi, vücut kitle indeksi, diyabet durumu ve yaşam tarzı alışkanlıkları gibi değişkenler modele dahil edilir. Makine öğrenimi algoritmaları, bu veriler üzerinde örüntüleri tanımlayarak, hastaların gelecekte kalp krizi geçirme olasılığını belirler. Makine öğrenme türleri üç ana gruba ayrılmaktadır. Bunlar, denetimli öğrenme, denetimsiz öğrenme ve pekiştirmeli öğrenme olarak adlandırılır;
Denetimli öğrenme, bir giriş ve çıkış katmanlarını vererek yeni verinin tahmin edilme süreci. Verilerin tümü etiketlidir.  
Denetimsiz öğrenme, çıktı katmanı verilmeden verinin doğru olarak sınıflandırılması, etiketsiz verilerden oluşur.
Pekiştirmeli öğrenme; modelin veri seti içerisinde deneme yanılma yolu ile öğrenmeyi sağlamaktadır. En iyi çıktıya karar verme sürecidir.
 
Proje sistem diyagramı 
Son yıllarda makine öğrenmesi, sağlık sektöründe erken teşhis ve hastalık tahmini gibi kritik alanlarda büyük bir dönüşüm sağlamaktadır. Kalp hastalıkları gibi birçok kronik rahatsızlık, genellikle uzun yıllar boyunca belirti vermeden ilerleyebilir ve ani kalp krizlerine yol açabilir. Bu nedenle, risk faktörlerinin analiz edilmesi ve erken müdahale için tahmin modellerinin geliştirilmesi büyük önem taşır.

Makine öğrenme yöntemleri ikiye ayrılır:
1.	Kümeleme algoritmaları: 
2.	Sınıflandırma algoritmaları:

SINIFLANDIRMA ALGORİTMALARI
1.	KNN: 
K-En Yakın Komşu (KNN), gözetimli öğrenme yöntemlerinden biri olup, yeni bir verinin sınıflandırılmasında, daha önce sınıflandırılmış verilere olan benzerliği temel alır. Bu yöntemde, sınıflandırılacak olan yeni bir örnek, eğitim verisindeki en yakın k adet komşusuna göre değerlendirilir. Bu komşuların ait olduğu sınıflar sayılır ve en fazla üyeye sahip olan sınıfa yeni örnek atanır.Algoritmanın ilk adımı, veri noktaları arasındaki mesafeyi ölçmek için uygun bir mesafe ölçüm yöntemi (örneğin Öklidyen, Manhattan, Minkowski vb.) belirlemektir. Ardından, sınıflandırılacak veri ile eğitim verileri arasındaki mesafeler hesaplanarak en yakın k komşu belirlenir. Bu noktada, her bir komşuya belirli bir ağırlık da atanabilir; genellikle daha yakın olan komşulara daha yüksek ağırlık verilir.
 
2.	KARAR AĞAÇLARI
Karar ağaçları, sınıflandırma, kümeleme ve tahmin gibi problemlerde sıklıkla kullanılan etkili bir makine öğrenmesi yöntemidir. Bu teknik, analiz edilen problemi daha küçük ve yönetilebilir alt parçalara ayırmak için karar noktaları oluşturarak çalışır. Her karar, veriyi belirli bir özelliğe göre dallara ayırır ve bu süreç, verilerin yapısına göre hiyerarşik bir yapı oluşturur.

Karar ağaçlarında her düğüm (node), bir özelliği temsil eder; dallar (branches), bu özelliğe göre alınan kararları; yapraklar (leaves) ise elde edilen sınıflandırma sonuçlarını veya tahminleri ifade eder. Bu yapı sayesinde, karar ağaçları görsel olarak kolayca yorumlanabilir ve hangi koşullar altında hangi sonuçların elde edildiği şeffaf bir şekilde izlenebilir.

3.	RASTGELE ORMAN
Rastgele Ormanlar, birden çok karar ağacının bir araya gelmesiyle oluşan bir topluluk öğrenme algoritmasıdır. Tek bir karar ağacının potansiyel zayıflıklarını gidermek ve daha güçlü, daha kararlı ve genelleme yeteneği daha yüksek bir model oluşturmak amacıyla geliştirilmiş algoritmalardandır.

4.	SVC
Bu tür sınıflandırma algoritmalarında amaç, verileri temsil eden noktaları bir düzlem üzerinde ayıracak en uygun doğru (iki boyutlu uzayda) veya hiper düzlemi (çok boyutlu uzayda) bulmaktır. Örneğin, bir sınıflandırma problemi kapsamında veriler iki sınıfa ayrılmışsa, bu algoritma sınıflar arasında en iyi ayrımı sağlayacak sınırı belirler. Doğrunun bir tarafında kalan noktalar bir sınıfa (örneğin "0", hasta bireyler), diğer tarafında kalan noktalar ise diğer sınıfa (örneğin "1", sağlıklı bireyler) ait kabul edilir.

Bu ayrım çizgisi, genellikle noktaların düzleme olan mesafeleri hesaplanarak belirlenir. En iyi ayrımı sağlamak amacıyla sınıflar arasındaki marj (boşluk) maksimum olacak şekilde hiper düzlem seçilir. Yeni bir veri noktası geldiğinde, bu noktanın düzleme göre hangi tarafta kaldığı hesaplanır ve buna göre uygun sınıfa atanır.

Bu yöntem, özellikle destek vektör makineleri (SVM) gibi algoritmaların temel çalışma prensibini oluşturur ve yüksek doğruluk oranlarıyla birlikte birçok sınıflandırma probleminde başarılı sonuçlar verir.

VERİ SETİ
Çalışmadaki veriler, bireylerin yaş, cinsiyet, sistolik ve diyastolik kan basıncı, kalp atım hızı, kan şekeri seviyesi, CK-MB düzeyi ve troponin değerleri gibi önemli klinik parametreleri içermektedir. Amaç, kalp krizi tahmin verileri ışığında makine öğrenmesi algoritmaları aracılığıyla kalp krizine dair risk faktörlerinin belirlenmesi ve erken müdahale imkanlarının artırılmasıdır.

ROC ANALİZİ
ROC eğrisi, sınıflandırma modelinin farklı eşik (threshold) değerleri altında pozitif ve negatif sınıfların doğru ayırt edebildiğini değerlendirmeye dayanan bir grafiktir. ROC eğrisi, Doğru Pozitif Oranı (TPR) ve yanlış Pozitif Oranı (FPR) arasındaki ilişkiyi inceler. 

ANALİZLER
Veri seti dağılım grafiği, modelleme sürecinden önce veri setinin yapısını ve özelliklerini anlamak, olası aykırı durumları saptamak amacıyla oluşturuldu. Yaş, sistolik ve diyastolik kan basıncı gibi sürekli değişkenlerin histogramları, bu değişkenlerin normal ya da çarpık dağılıma sahip olup olmadığını görmeye imkân tanımaktadır. 
Korelasyon matrisi, özel seçimlerinde de sıkça kullanılmakta olan korelasyon matrisi -1,0,1 değenlerinden oluşur, bu değerler negatif doğrusal ilişki (-1), pozitif doğrusal ilişki (+1), korelasyonun olmadığı (0) değerleri temsil etmektedir. Renk tonuna göre sınıflandırılan matris tablosunda değer 1’e ne kadar yakınsa o kadar mükemmel bir doğrulama sunar.
Karmaşıklık matrisi
Çalışmada elde edilen karmaşıklık matrisi, modelin pozitif ve negatif sınıfları ne ölçüde doğru tahmin ettiğini sayısal olarak ortaya koymaktadır. Matrisin satırları gerçek sınıfları, sütunları ise tahmin edilen sınıfları temsil eder
0 kalp krizi riski yok, negatif
1 kalp krizi riski var, pozitif
TP, için örneğin tıbbı geçmişinde kalp krizi riski olan bir bireyin doğru bir tahmin ile pozitif değer olduğu gözlemlenir. (Kalp krizi riski (T), 1=pozitif (P))
Sağlıklı olan birini model risk var olarak tahmini ise FP

ROC Analizi
ROC eğrisi, modelin pozitif ve negatif sınıfları ayırt etme başarısını görsel olarak temsil ederken, eğri altında kalan alan (AUC) değeri modelin genel doğruluk kapasitesini sayısal olarak ifade etmektedir. 
Accurary- doğruluk: modelin % kaç doğru tahmin ettiği
Precision- kesinlik: FP oranını kontrol eder, yanlış tahmini önlemek için
recall-Hassasiyet: riskli hataları atlamamak için FN durumunu kontrol eder.

Makine öğrenmesi algoritmalarının sağlık verileri üzerinde uygulanabilirliğini ortaya koyan bu çalışma, kullanılan veri setinin sınıflandırma problemleri için uygun olduğunu ve makine öğrenmesi tabanlı yöntemlerin tıbbi karar destek sistemlerinde etkili biçimde kullanılabileceğini göstermektedir. Literatürde benzer çalışmalar yer almış olsa da yalnızca makine öğrenme teknikleri kullanılarak tahminde bulunmak ve doğruluk skorlarını bu denli yüksek çıkaran pek az çalışma mevcuttur.

---

title: "Dompdf: PHP&#8217;de zarif PDF&#8217;ler nasıl oluşturulur?"
slug: "dompdf-phpde-zarif-pdfler-nasil-olusturulur"
excerpt: "Dompdf&#8217;e Giriş Dompdf, HTML içeriğinden PDF dosyaları oluşturmanıza olanak tanıyan bir PHP kütüphanesidir. Bu çözüm, raporlar, faturalar veya PDF formatında başka herhangi bir belge oluşturmak için çok kullanışlıdır. Bu makalede Dompdf&#8217;in temel özelliklerini keşfedeceğiz ve onu şık ve işlevsel PDF&#8217;ler oluşturmak için nasıl kullanacağımızı öğreneceğiz. Önkoşullar Dompdf&#8217;i kurmadan önce aşağıdakilere sahip olduğunuzdan emin olun: Dompdf [&hellip;]"
date: "2024-03-09T12:43:36"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["bilgisayar-ve-veri-tr", "teknoloji-ve-dijital-tr"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Dompdfe_Giris" >Dompdf&#8217;e Giriş</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Onkosullar" >Önkoşullar</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Dompdf_kurulumu" >Dompdf kurulumu</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Dompdfli_ilk_PDF_belgem" >Dompdf'li ilk PDF belgem</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#PHPde_Zarif_bir_PDF_olusturma" >PHP&#8217;de Zarif bir PDF oluşturma</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Dompdfi_kurmanin_ve_kullanmanin_baska_bir_yontemi" >Dompdf&#8217;i kurmanın ve kullanmanın başka bir yöntemi</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#HTML_sablonundan_PDF_olusturma" >HTML şablonundan PDF oluşturma</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Goruntuleri_ve_yazi_tiplerini_yonetme" >Görüntüleri ve yazı tiplerini yönetme</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/tr/dompdf-phpde-zarif-pdfler-nasil-olusturulur/#Olusturmayi_optimize_etme_ve_Dompdf_sorunlarini_duzeltme" >Oluşturmayı optimize etme ve Dompdf sorunlarını düzeltme</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Dompdfe_Giris"></span>Dompdf&#8217;e Giriş<span class="ez-toc-section-end"></span></h2>



<p>Dompdf, HTML içeriğinden PDF dosyaları oluşturmanıza olanak tanıyan bir PHP kütüphanesidir. Bu çözüm, raporlar, faturalar veya PDF formatında başka herhangi bir belge oluşturmak için çok kullanışlıdır. Bu makalede Dompdf&#8217;in temel özelliklerini keşfedeceğiz ve onu şık ve işlevsel PDF&#8217;ler oluşturmak için nasıl kullanacağımızı öğreneceğiz.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Onkosullar"></span>Önkoşullar<span class="ez-toc-section-end"></span></h3>



<p>Dompdf&#8217;i kurmadan önce aşağıdakilere sahip olduğunuzdan emin olun:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf, PHP >= 5.4 gerektirir. PHP&#8217;nin 7.x sürümleriyle uyumludur.</li>



<li><strong>PHP uzantıları:</strong> Şu PHP uzantılarını etkinleştirdiğinizden emin olun: mbstring, DOM ve GD. Bu uzantılar Dompdf&#8217;in düzgün çalışması için gereklidir.</li>



<li><strong>Oluşturun:</strong> Dompdf, PHP için bir bağımlılık yöneticisi olan Composer aracılığıyla dağıtılır. Sisteminizde Composer&#8217;ın kurulu olduğundan emin olun.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_kurulumu"></span>Dompdf kurulumu<span class="ez-toc-section-end"></span></h4>



<p>Dompdf&#8217;i yüklemek için aşağıdaki adımları izleyin:</p>



<ol class="wp-block-list">
<li><strong>Yeni bir PHP projesi oluşturun:</strong> Halihazırda mevcut bir projeniz yoksa, seçtiğiniz temel yapıyı kullanarak yeni bir proje oluşturun.</li>



<li><strong>Composer aracılığıyla Dompdf bağımlılığını ekleyin:</strong> Bir konsol açın ve proje dizininize gidin. Dompdf&#8217;i projenize eklemek için aşağıdaki komutu çalıştırın:     <pre><code>besteci dompdf/dompdf gerektirir</code></pre>     Bu komut Dompdf&#8217;i bağımlılıklarıyla birlikte otomatik olarak indirip yükleyecektir.</li>



<li><strong>Uygulamanızda Dompdf&#8217;i kullanın:</strong> Artık projenizde Dompdf&#8217;i kullanabilirsiniz. Dompdf ile PDF dosyaları oluşturmanın birçok yolu vardır, ancak burada başlamanıza yardımcı olacak temel bir örnek verilmiştir:
<pre><code>// Composer otomatik yükleyicisini dahil et
'vendor/autoload.php' gerektirir;

// Yeni bir Dompdf nesnesi oluştur
$dompdf = yeni Dompdf();

// HTML içeriğini bir dosyadan veya dizeden yükle
$html = '<h1><span class="ez-toc-section" id="Dompdfli_ilk_PDF_belgem"></span>Dompdf'li ilk PDF belgem<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// PDF belgesini oluştur
$dompdf->oluşturma();

// PDF belgesini çıktıya gönder
$dompdf->stream('document.pdf');</code></pre>
    Bu örnek, başlıklı yeni bir PDF belgesi oluşturur ve bunu &#8220;document.pdf&#8221; dosyası olarak yükler. HTML içeriğini ihtiyaçlarınıza göre özelleştirebilirsiniz.</li>
</ol>



<p>Artık Dompdf&#8217;i yüklediğinize göre web uygulamalarınızda zarif ve işlevsel PDF dosyaları oluşturmaya başlayabilirsiniz. Dompdf, PDF oluşturmayı özelleştirmek için görüntüleri, özel yazı tiplerini ve CSS stillerini yönetme gibi birçok gelişmiş özellik sunar.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="PHPde_Zarif_bir_PDF_olusturma"></span>PHP&#8217;de Zarif bir PDF oluşturma<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Dompdfi_kurmanin_ve_kullanmanin_baska_bir_yontemi"></span>Dompdf&#8217;i kurmanın ve kullanmanın başka bir yöntemi<span class="ez-toc-section-end"></span></h3>



<p>İzlenecek adımlar şunlardır:<br>1. Dompdf&#8217;in en son sürümünü resmi web sitesinden indirin.<br>2. İndirilen dosyaları çıkarın ve PHP projenize yerleştirin.<br>3. Kütüphaneyi PHP betiğinize yüklemek için Dompdfautoload.php dosyasını ekleyin.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="HTML_sablonundan_PDF_olusturma"></span>HTML şablonundan PDF oluşturma<span class="ez-toc-section-end"></span></h4>



<p>Artık Dompdf&#8217;i kurduğumuza göre, HTML şablonu kullanarak nasıl PDF oluşturulacağını göreceğiz. Bu adımları takip et:</p>



<p>1. PDF&#8217;niz için istediğiniz yapıyı ve düzeni içeren bir HTML dosyası oluşturun.<br>2. Font-family, font-size, border vb. özellikleri kullanarak belgenize stil vermek için CSS özelliklerini kullanın.<br>3. &#8220;{{name}}&#8221; veya &#8220;{{address}}&#8221; gibi Dompdf&#8217;ye özgü etiketleri kullanarak dinamik verileri ekleyin.<br>4. Oluşturduğunuz HTML şablonunu kullanarak PDF oluşturmak için Dompdf sınıfını kullanın.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Goruntuleri_ve_yazi_tiplerini_yonetme"></span>Görüntüleri ve yazı tiplerini yönetme<span class="ez-toc-section-end"></span></h4>



<p>Zarif PDF&#8217;ler oluştururken genellikle görsel eklemek veya belirli yazı tiplerini kullanmak gerekir. Dompdf ile bunu nasıl yapacağınız aşağıda açıklanmıştır:</p>



<p>1. Etiketini kullanarak görselleri HTML şablonunuza ekleyin <img decoding="async" src="chemin_vers_image">.<br>2. Dompdf&#8217;in varsayılan olarak tüm yazı tiplerini içermediğini lütfen unutmayın. CSS&#8217;nizde @font-face kullanarak veya Dompdf tarafından sağlanan yazı tiplerini kullanarak özel yazı tipleri ekleyebilirsiniz.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Olusturmayi_optimize_etme_ve_Dompdf_sorunlarini_duzeltme"></span>Oluşturmayı optimize etme ve Dompdf sorunlarını düzeltme<span class="ez-toc-section-end"></span></h4>



<p>Bazen PDF&#8217;nizi oluştururken veya dosyaları oluştururken sorunlarla karşılaşabilirsiniz. İşte bunları çözmek için bazı ipuçları:</p>



<p>1. HTML şablonunuzun doğru şekilde oluşturulduğunu ve geçerli olduğunu kontrol edin.<br>2. Tüm harici kaynakların (resimler, yazı tipleri vb.) sunucudan erişilebilir olduğundan emin olun.<br>3. Dompdf hata ayıklama modunu etkinleştirip görüntülenen hataları kontrol ederek kodunuzda hata ayıklayın.<br>4. Yaygın yapılandırmalar ve sorunlar hakkında daha fazla bilgi için Dompdf belgelerine bakın.</p>



<p>Dompdf&#8217;i kullanarak profesyonel ve iyi formatlanmış PDF belgeleri sunarak gelişmiş bir kullanıcı deneyimi sağlayabilirsiniz. Raporlar, faturalar veya diğer belge türlerini oluştururken Dompdf güvenilir ve güçlü bir seçimdir.</p>



<p>Sonuç olarak Composer sayesinde Dompdf&#8217;i kurmak hızlı ve kolaydır. Kurulduktan sonra web uygulaması ihtiyaçlarınızı karşılayacak yüksek kaliteli PDF dosyaları oluşturmaya başlayabilirsiniz. Özellikleri ve mevcut özelleştirme seçenekleri hakkında daha fazla bilgi edinmek için resmi Dompdf belgelerine göz atmayı unutmayın.</p>



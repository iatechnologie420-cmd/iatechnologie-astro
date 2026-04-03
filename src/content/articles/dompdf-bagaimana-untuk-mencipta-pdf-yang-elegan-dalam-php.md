---

title: "Dompdf: Bagaimana untuk mencipta PDF yang elegan dalam PHP?"
slug: "dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php"
excerpt: "Pengenalan kepada Dompdf Dompdf ialah perpustakaan PHP yang membolehkan anda menjana fail PDF daripada kandungan HTML. Penyelesaian ini sangat berguna untuk menjana laporan, invois atau sebarang dokumen lain dalam format PDF. Dalam artikel ini, kami akan menemui ciri asas Dompdf dan mempelajari cara menggunakannya untuk mencipta PDF yang elegan dan berfungsi. Prasyarat Sebelum memasang Dompdf, [&hellip;]"
date: "2024-03-09T12:42:06"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["pengkomputeran-dan-data-ms", "teknologi-dan-digital-ms"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Pengenalan_kepada_Dompdf" >Pengenalan kepada Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Prasyarat" >Prasyarat</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Pemasangan_Dompdf" >Pemasangan Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Dokumen_PDF_pertama_saya_dengan_Dompdf" >Dokumen PDF pertama saya dengan Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Mencipta_PDF_Elegan_dalam_PHP" >Mencipta PDF Elegan dalam PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Kaedah_lain_untuk_memasang_dan_menggunakan_Dompdf" >Kaedah lain untuk memasang dan menggunakan Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Mencipta_PDF_daripada_templat_HTML" >Mencipta PDF daripada templat HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Mengurus_imej_dan_fon" >Mengurus imej dan fon</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ms/dompdf-bagaimana-untuk-mencipta-pdf-yang-elegan-dalam-php/#Mengoptimumkan_pemaparan_dan_membetulkan_isu_Dompdf" >Mengoptimumkan pemaparan dan membetulkan isu Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Pengenalan_kepada_Dompdf"></span>Pengenalan kepada Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf ialah perpustakaan PHP yang membolehkan anda menjana fail PDF daripada kandungan HTML. Penyelesaian ini sangat berguna untuk menjana laporan, invois atau sebarang dokumen lain dalam format PDF. Dalam artikel ini, kami akan menemui ciri asas Dompdf dan mempelajari cara menggunakannya untuk mencipta PDF yang elegan dan berfungsi.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Prasyarat"></span>Prasyarat<span class="ez-toc-section-end"></span></h3>



<p>Sebelum memasang Dompdf, pastikan anda mempunyai yang berikut:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf memerlukan PHP >= 5.4. Ia serasi dengan versi 7.x PHP.</li>



<li><strong>Sambungan PHP:</strong> Pastikan anda telah mendayakan sambungan PHP berikut: mbstring, DOM dan GD. Sambungan ini penting untuk Dompdf berfungsi dengan baik.</li>



<li><strong>Karang :</strong> Dompdf diedarkan melalui Komposer, yang merupakan pengurus pergantungan untuk PHP. Pastikan anda telah memasang Komposer pada sistem anda.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pemasangan_Dompdf"></span>Pemasangan Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Untuk memasang Dompdf, ikuti langkah berikut:</p>



<ol class="wp-block-list">
<li><strong>Buat projek PHP baharu:</strong> Jika anda belum mempunyai projek sedia ada, buat projek baharu menggunakan struktur asas pilihan anda.</li>



<li><strong>Tambahkan kebergantungan Dompdf melalui Komposer:</strong> Buka konsol dan navigasi ke direktori projek anda. Jalankan arahan berikut untuk menambah Dompdf ke projek anda:     <pre><code>komposer memerlukan dompdf/dompdf</code></pre>     Perintah ini akan memuat turun dan memasang Dompdf secara automatik bersama-sama dengan kebergantungannya.</li>



<li><strong>Gunakan Dompdf dalam permohonan anda:</strong> Anda kini boleh menggunakan Dompdf dalam projek anda. Terdapat banyak cara untuk membuat fail PDF dengan Dompdf, tetapi berikut ialah contoh asas untuk anda bermula:
<pre><code>// Sertakan pemuat auto Komposer
memerlukan 'vendor/autoload.php';

// Cipta objek Dompdf baharu
$dompdf = new Dompdf();

// Muatkan kandungan HTML daripada fail atau rentetan
$html = '<h1><span class="ez-toc-section" id="Dokumen_PDF_pertama_saya_dengan_Dompdf"></span>Dokumen PDF pertama saya dengan Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Berikan dokumen PDF
$dompdf->render();

// Hantar dokumen PDF ke output
$dompdf->stream('document.pdf');</code></pre>
    Contoh ini mencipta dokumen PDF baharu dengan tajuk dan memuat naiknya sebagai fail &#8220;document.pdf&#8221;. Anda boleh menyesuaikan kandungan HTML mengikut keperluan anda.</li>
</ol>



<p>Sekarang setelah anda memasang Dompdf, anda boleh mula menjana fail PDF yang elegan dan berfungsi dalam aplikasi web anda. Dompdf menawarkan banyak ciri lanjutan untuk menyesuaikan pemaparan PDF, seperti mengurus imej, fon tersuai dan gaya CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Mencipta_PDF_Elegan_dalam_PHP"></span>Mencipta PDF Elegan dalam PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kaedah_lain_untuk_memasang_dan_menggunakan_Dompdf"></span>Kaedah lain untuk memasang dan menggunakan Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Berikut adalah langkah-langkah yang perlu diikuti:<br>1. Muat turun versi terkini Dompdf dari laman web rasmi.<br>2. Ekstrak fail yang dimuat turun dan letakkannya dalam projek PHP anda.<br>3. Sertakan fail Dompdfautoload.php untuk memuatkan perpustakaan ke dalam skrip PHP anda.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mencipta_PDF_daripada_templat_HTML"></span>Mencipta PDF daripada templat HTML<span class="ez-toc-section-end"></span></h4>



<p>Sekarang kita telah memasang Dompdf, kita akan melihat cara membuat PDF menggunakan templat HTML. Ikut langkah-langkah ini:</p>



<p>1. Buat fail HTML yang mengandungi struktur dan susun atur yang anda inginkan untuk PDF anda.<br>2. Gunakan ciri CSS untuk menggayakan dokumen anda, menggunakan sifat seperti font-family, font-size, border, dsb.<br>3. Sertakan data dinamik menggunakan teg khusus Dompdf, seperti &#8220;{{name}}&#8221; atau &#8220;{{address}}&#8221;.<br>4. Gunakan kelas Dompdf untuk menjana PDF menggunakan templat HTML yang anda buat.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mengurus_imej_dan_fon"></span>Mengurus imej dan fon<span class="ez-toc-section-end"></span></h4>



<p>Apabila mencipta PDF yang bergaya, selalunya perlu memasukkan imej atau menggunakan fon tertentu. Begini cara melakukannya dengan Dompdf:</p>



<p>1. Sertakan imej dalam templat HTML anda menggunakan teg <img decoding="async" src="chemin_vers_image">.<br>2. Sila ambil perhatian bahawa Dompdf tidak termasuk semua fon secara lalai. Anda boleh menambah fon tersuai menggunakan @font-face dalam CSS anda atau menggunakan fon yang disediakan oleh Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mengoptimumkan_pemaparan_dan_membetulkan_isu_Dompdf"></span>Mengoptimumkan pemaparan dan membetulkan isu Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Kadangkala anda mungkin menghadapi masalah dengan memaparkan PDF anda atau menjana fail. Berikut ialah beberapa petua untuk menyelesaikannya:</p>



<p>1. Semak sama ada templat HTML anda dibina dengan betul dan sah.<br>2. Pastikan semua sumber luaran (imej, fon, dsb.) boleh diakses daripada pelayan.<br>3. Nyahpepijat kod anda dengan mengaktifkan mod nyahpepijat Dompdf dan menyemak ralat yang dipaparkan.<br>4. Lihat dokumentasi Dompdf untuk mendapatkan maklumat lanjut tentang konfigurasi dan isu biasa.</p>



<p>Menggunakan Dompdf, anda boleh memberikan pengalaman pengguna yang dipertingkatkan dengan menyampaikan dokumen PDF yang profesional dan diformat dengan baik. Sama ada menjana laporan, invois atau jenis dokumen lain, Dompdf ialah pilihan yang boleh dipercayai dan berkuasa.</p>



<p>Kesimpulannya, memasang Dompdf adalah pantas dan mudah terima kasih kepada Komposer. Setelah dipasang, anda boleh mula mencipta fail PDF berkualiti tinggi untuk memenuhi keperluan aplikasi web anda. Jangan lupa untuk menyemak dokumentasi rasmi Dompdf untuk mengetahui lebih lanjut tentang ciri dan pilihan penyesuaian yang tersedia.</p>



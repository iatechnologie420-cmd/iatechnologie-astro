---
title: "Dompdf: Bagaimana cara membuat PDF yang elegan di PHP?"
slug: "dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php"
excerpt: "Pengantar Dompdf Dompdf adalah perpustakaan PHP yang memungkinkan Anda menghasilkan file PDF dari konten HTML. Solusi ini sangat berguna untuk menghasilkan laporan, faktur, atau dokumen lainnya dalam format PDF. Pada artikel ini, kita akan menemukan fitur dasar Dompdf dan mempelajari cara menggunakannya untuk membuat PDF yang elegan dan fungsional. Prasyarat Sebelum menginstal Dompdf, pastikan Anda [&hellip;]"
date: "2024-03-09T12:40:32"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["komputasi-dan-data-id", "teknologi-dan-digital-id"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Pengantar_Dompdf" >Pengantar Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Prasyarat" >Prasyarat</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Instalasi_dompdf" >Instalasi dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Dokumen_PDF_pertama_saya_dengan_Dompdf" >Dokumen PDF pertama saya dengan Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Membuat_PDF_Elegan_di_PHP" >Membuat PDF Elegan di PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Metode_lain_untuk_menginstal_dan_menggunakan_Dompdf" >Metode lain untuk menginstal dan menggunakan Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Membuat_PDF_dari_template_HTML" >Membuat PDF dari template HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Mengelola_gambar_dan_font" >Mengelola gambar dan font</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/id/dompdf-bagaimana-cara-membuat-pdf-yang-elegan-di-php/#Mengoptimalkan_rendering_dan_memperbaiki_masalah_Dompdf" >Mengoptimalkan rendering dan memperbaiki masalah Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Pengantar_Dompdf"></span>Pengantar Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf adalah perpustakaan PHP yang memungkinkan Anda menghasilkan file PDF dari konten HTML. Solusi ini sangat berguna untuk menghasilkan laporan, faktur, atau dokumen lainnya dalam format PDF. Pada artikel ini, kita akan menemukan fitur dasar Dompdf dan mempelajari cara menggunakannya untuk membuat PDF yang elegan dan fungsional.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Prasyarat"></span>Prasyarat<span class="ez-toc-section-end"></span></h3>



<p>Sebelum menginstal Dompdf, pastikan Anda memiliki hal berikut:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf membutuhkan PHP >= 5.4. Ini kompatibel dengan PHP versi 7.x.</li>



<li><strong>Ekstensi PHP:</strong> Pastikan Anda telah mengaktifkan ekstensi PHP berikut: mbstring, DOM dan GD. Ekstensi ini penting agar Dompdf berfungsi dengan baik.</li>



<li><strong>Menulis :</strong> Dompdf didistribusikan melalui Composer, yang merupakan manajer ketergantungan untuk PHP. Pastikan Anda telah menginstal Komposer di sistem Anda.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Instalasi_dompdf"></span>Instalasi dompdf<span class="ez-toc-section-end"></span></h4>



<p>Untuk menginstal Dompdf, ikuti langkah-langkah berikut:</p>



<ol class="wp-block-list">
<li><strong>Buat proyek PHP baru:</strong> Jika Anda belum memiliki proyek, buat proyek baru menggunakan struktur dasar pilihan Anda.</li>



<li><strong>Tambahkan ketergantungan Dompdf melalui Komposer:</strong> Buka konsol dan navigasikan ke direktori proyek Anda. Jalankan perintah berikut untuk menambahkan Dompdf ke proyek Anda:     <pre><code>komposer memerlukan dompdf/dompdf</code></pre>     Perintah ini akan secara otomatis mengunduh dan menginstal Dompdf beserta dependensinya.</li>



<li><strong>Gunakan Dompdf di aplikasi Anda:</strong> Anda sekarang dapat menggunakan Dompdf di proyek Anda. Ada banyak cara untuk membuat file PDF dengan Dompdf, namun berikut ini contoh dasar untuk Anda mulai:
<pre><code>// Sertakan pemuat otomatis Komposer
memerlukan 'vendor/autoload.php';

// Buat objek Dompdf baru
$dompdf = Dompdf baru();

// Memuat konten HTML dari file atau string
$html = '<h1><span class="ez-toc-section" id="Dokumen_PDF_pertama_saya_dengan_Dompdf"></span>Dokumen PDF pertama saya dengan Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Render dokumen PDF
$dompdf->render();

// Kirim dokumen PDF ke output
$dompdf->stream('dokumen.pdf');</code></pre>
    Contoh ini membuat dokumen PDF baru dengan judul dan mengunggahnya sebagai file &#8220;document.pdf&#8221;. Anda dapat menyesuaikan konten HTML sesuai kebutuhan Anda.</li>
</ol>



<p>Sekarang setelah Anda menginstal Dompdf, Anda dapat mulai membuat file PDF yang elegan dan fungsional di aplikasi web Anda. Dompdf menawarkan banyak fitur lanjutan untuk menyesuaikan rendering PDF, seperti mengelola gambar, font khusus, dan gaya CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Membuat_PDF_Elegan_di_PHP"></span>Membuat PDF Elegan di PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Metode_lain_untuk_menginstal_dan_menggunakan_Dompdf"></span>Metode lain untuk menginstal dan menggunakan Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Berikut langkah-langkah yang harus diikuti:<br>1. Unduh Dompdf versi terbaru dari situs resminya.<br>2. Ekstrak file yang diunduh dan letakkan di proyek PHP Anda.<br>3. Sertakan file Dompdfautoload.php untuk memuat perpustakaan ke dalam skrip PHP Anda.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Membuat_PDF_dari_template_HTML"></span>Membuat PDF dari template HTML<span class="ez-toc-section-end"></span></h4>



<p>Sekarang kita telah menginstal Dompdf, kita akan melihat cara membuat PDF menggunakan template HTML. Ikuti langkah ini:</p>



<p>1. Buat file HTML yang berisi struktur dan tata letak yang Anda inginkan untuk PDF Anda.<br>2. Gunakan fitur CSS untuk menata gaya dokumen Anda, menggunakan properti seperti font-family, font-size, border, dll.<br>3. Sertakan data dinamis menggunakan tag khusus Dompdf, seperti &#8220;{{name}}&#8221; atau &#8220;{{address}}&#8221;.<br>4. Gunakan kelas Dompdf untuk menghasilkan PDF menggunakan template HTML yang Anda buat.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mengelola_gambar_dan_font"></span>Mengelola gambar dan font<span class="ez-toc-section-end"></span></h4>



<p>Saat membuat PDF bergaya, sering kali perlu menyertakan gambar atau menggunakan font tertentu. Berikut cara melakukannya dengan Dompdf:</p>



<p>1. Sertakan gambar dalam template HTML Anda menggunakan tag <img decoding="async" src="chemin_vers_image">.<br>2. Harap dicatat bahwa Dompdf tidak menyertakan semua font secara default. Anda dapat menambahkan font khusus menggunakan @font-face di CSS Anda atau menggunakan font yang disediakan oleh Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mengoptimalkan_rendering_dan_memperbaiki_masalah_Dompdf"></span>Mengoptimalkan rendering dan memperbaiki masalah Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Terkadang Anda mungkin mengalami masalah saat merender PDF atau membuat file. Berikut beberapa tip untuk mengatasinya:</p>



<p>1. Periksa apakah template HTML Anda dibuat dengan benar dan valid.<br>2. Pastikan semua sumber daya eksternal (gambar, font, dll.) dapat diakses dari server.<br>3. Debug kode Anda dengan mengaktifkan mode debug Dompdf dan memeriksa kesalahan yang ditampilkan.<br>4. Lihat dokumentasi Dompdf untuk informasi lebih lanjut tentang konfigurasi dan masalah umum.</p>



<p>Dengan menggunakan Dompdf, Anda dapat memberikan pengalaman pengguna yang lebih baik dengan memberikan dokumen PDF yang profesional dan berformat baik. Baik membuat laporan, faktur, atau jenis dokumen lainnya, Dompdf adalah pilihan yang andal dan kuat.</p>



<p>Kesimpulannya, menginstal Dompdf menjadi cepat dan mudah berkat Composer. Setelah terinstal, Anda dapat mulai membuat file PDF berkualitas tinggi untuk memenuhi kebutuhan aplikasi web Anda. Jangan lupa untuk memeriksa dokumentasi resmi Dompdf untuk mempelajari lebih lanjut tentang fitur-fiturnya dan opsi penyesuaian yang tersedia.</p>



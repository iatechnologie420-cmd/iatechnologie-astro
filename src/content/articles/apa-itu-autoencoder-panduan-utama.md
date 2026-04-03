---
title: "Apa itu autoencoder? Panduan utama!"
slug: "apa-itu-autoencoder-panduan-utama"
excerpt: "Autoencoder, atau autoencoder dalam bahasa Inggris, memposisikan diri mereka sebagai alat yang ampuh di bidang pembelajaran mesin dan kecerdasan buatan. Jaringan saraf khusus ini digunakan untuk reduksi dimensi, deteksi anomali, penolakan data, dan banyak lagi. Artikel ini memberikan pengenalan tentang teknologi menakjubkan ini, menyoroti prinsip kerjanya, penerapannya, dan semakin pentingnya teknologi ini dalam penelitian dan [&hellip;]"
date: "2024-03-09T12:05:42"
categories: ["komputasi-dan-data-id", "teknologi-dan-digital-id"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tracking Corn &amp; Weed with Yolov5 and Auto Encoder - Tracker" width="500" height="281" src="https://www.youtube.com/embed/8-jWgsGWaR0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>Autoencoder, atau <em>autoencoder</em> dalam bahasa Inggris, memposisikan diri mereka sebagai alat yang ampuh di bidang pembelajaran mesin dan kecerdasan buatan. Jaringan saraf khusus ini digunakan untuk reduksi dimensi, deteksi anomali, penolakan data, dan banyak lagi. Artikel ini memberikan pengenalan tentang teknologi menakjubkan ini, menyoroti prinsip kerjanya, penerapannya, dan semakin pentingnya teknologi ini dalam penelitian dan industri.</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/id/apa-itu-autoencoder-panduan-utama/#Apa_itu_autoencoder" >Apa itu autoencoder?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-2" href="/id/apa-itu-autoencoder-panduan-utama/#Bagaimana_cara_kerja_autoencoder" >Bagaimana cara kerja autoencoder?</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-3" href="/id/apa-itu-autoencoder-panduan-utama/#Aplikasi_praktis_autoencoder" >Aplikasi praktis autoencoder</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-4" href="/id/apa-itu-autoencoder-panduan-utama/#Autoencoder_pengkodean_kemacetan_dan_decoding" >Autoencoder: pengkodean, kemacetan dan decoding</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/id/apa-itu-autoencoder-panduan-utama/#Pengkodean" >Pengkodean</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/id/apa-itu-autoencoder-panduan-utama/#Kemacetan" >Kemacetan</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/id/apa-itu-autoencoder-panduan-utama/#Penguraian_kode" >Penguraian kode</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/id/apa-itu-autoencoder-panduan-utama/#Aplikasi_praktis_dan_variasi_autoencoder" >Aplikasi praktis dan variasi autoencoder</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/id/apa-itu-autoencoder-panduan-utama/#Aplikasi_praktis_autoencoder-2" >Aplikasi praktis autoencoder</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/id/apa-itu-autoencoder-panduan-utama/#Pengurangan_dimensi" >Pengurangan dimensi</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/id/apa-itu-autoencoder-panduan-utama/#Peredam_Kebisingan_Denoising" >Peredam Kebisingan (Denoising)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/id/apa-itu-autoencoder-panduan-utama/#Kompresi_data" >Kompresi data</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/id/apa-itu-autoencoder-panduan-utama/#Pembuatan_dan_imputasi_data" >Pembuatan dan imputasi data</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/id/apa-itu-autoencoder-panduan-utama/#Varian_autoencoder" >Varian autoencoder</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/id/apa-itu-autoencoder-panduan-utama/#Autoencoder_Variasi_VAE" >Autoencoder Variasi (VAE)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/id/apa-itu-autoencoder-panduan-utama/#Autoencoder_Jarang" >Autoencoder Jarang</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/id/apa-itu-autoencoder-panduan-utama/#Menolak_Autoencoder" >Menolak Autoencoder</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/id/apa-itu-autoencoder-panduan-utama/#Autoencoder_Berurutan" >Autoencoder Berurutan</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-19" href="/id/apa-itu-autoencoder-panduan-utama/#Cara_melatih_autoencoder_dan_contoh_kode" >Cara melatih autoencoder dan contoh kode</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/id/apa-itu-autoencoder-panduan-utama/#Proses_pelatihan_autoencoder" >Proses pelatihan autoencoder</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-21" href="/id/apa-itu-autoencoder-panduan-utama/#Contoh_kode_dengan_Keras" >Contoh kode dengan Keras</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-22" href="/id/apa-itu-autoencoder-panduan-utama/#Tip_untuk_latihan_yang_baik" >Tip untuk latihan yang baik</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-23" href="/id/apa-itu-autoencoder-panduan-utama/#Aplikasi_autoencoder" >Aplikasi autoencoder</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Apa_itu_autoencoder"></span>Apa itu autoencoder?<span class="ez-toc-section-end"></span></h2>



<p>A <strong>autoencoder</strong> adalah jenis jaringan saraf tiruan yang digunakan untuk pembelajaran tanpa pengawasan. Tujuan utama autoencoder adalah menghasilkan representasi kompak (encoding) dari sekumpulan data masukan dan kemudian merekonstruksi data dari representasi tersebut. Idenya adalah untuk menangkap aspek data yang paling penting, sering kali untuk reduksi dimensi. Struktur autoencoder biasanya terdiri dari dua bagian utama:</p>



<ul class="wp-block-list">
<li><strong>Pembuat enkode</strong> (<em>Menyandi</em>): Bagian pertama dari jaringan ini bertanggung jawab untuk mengompresi data masukan menjadi bentuk yang diperkecil.</li>



<li><strong>Dekoder</strong> (<em>Membaca sandi</em>): Bagian kedua menerima pengkodean terkompresi dan mencoba merekonstruksi data asli.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Bagaimana_cara_kerja_autoencoder"></span>Bagaimana cara kerja autoencoder?<span class="ez-toc-section-end"></span></h2>



<p>Pengoperasian autoencoder dapat dijelaskan dalam beberapa langkah:</p>



<ol class="wp-block-list">
<li>Jaringan menerima data sebagai input.</li>



<li>Encoder memampatkan data menjadi vektor fitur, yang disebut kode atau ruang laten.</li>



<li>Decoder mengambil vektor ini dan mencoba merekonstruksi data awal.</li>



<li>Kualitas rekonstruksi diukur menggunakan fungsi kerugian, yang mengevaluasi perbedaan antara masukan asli dan keluaran yang direkonstruksi.</li>



<li>Jaringan menyesuaikan bobotnya melalui algoritma propagasi mundur untuk meminimalkan fungsi kerugian ini.</li>
</ol>



<p>Melalui proses berulang ini, autoencoder mempelajari representasi data yang efisien, dengan penekanan pada pelestarian fitur terpenting selama proses rekonstruksi.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Aplikasi_praktis_autoencoder"></span>Aplikasi praktis autoencoder<span class="ez-toc-section-end"></span></h3>



<p>Autoencoder sangat serbaguna dan dapat diterapkan di beberapa area:</p>



<ul class="wp-block-list">
<li><strong>Pengurangan Dimensi</strong>: Seperti PCA (Principal Component Analysis), tetapi dengan kapasitas non-linier.</li>



<li><strong>Mencela</strong>: mereka dapat belajar mengabaikan &#8220;noise&#8221; dalam data.</li>



<li><strong>Kompresi data</strong>: mereka dapat mempelajari pengkodean yang lebih efisien dibandingkan metode kompresi tradisional.</li>



<li><strong>Pembuatan data</strong>: dengan menavigasi ruang laten, mereka mengizinkan pembuatan instance data baru yang menyerupai entri asli.</li>



<li><strong>Deteksi Anomali</strong>: Autoencoder dapat membantu menemukan data yang tidak sesuai dengan distribusi yang dipelajari.</li>
</ul>



<p>Singkatnya, kemampuan autoencoder untuk menemukan dan menentukan karakteristik data yang bermakna menjadikannya instrumen yang harus dimiliki dalam perangkat praktisi AI mana pun.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoder_pengkodean_kemacetan_dan_decoding"></span>Autoencoder: pengkodean, kemacetan dan decoding<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png" alt="" class="wp-image-1191" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Pengkodean"></span>Pengkodean<span class="ez-toc-section-end"></span></h3>



<p>Pengkodean, atau fase pengkodean, melibatkan transformasi data masukan menjadi representasi terkompresi. Data awal, yang mungkin berukuran besar, dimasukkan ke dalam jaringan autoencoder. Lapisan jaringan secara bertahap akan mengurangi dimensi data, mengompresi informasi penting ke dalam ruang representasi yang lebih kecil. Setiap lapisan jaringan terdiri dari neuron yang menerapkan transformasi non-linier, misalnya menggunakan fungsi aktivasi seperti ReLU atau Sigmoid, untuk menghasilkan representasi data baru yang menyimpan informasi penting.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kemacetan"></span>Kemacetan<span class="ez-toc-section-end"></span></h4>



<p>Kemacetan adalah bagian utama dari autoencoder tempat representasi data mencapai dimensi terendahnya, yang juga disebut kode. Representasi terkompresi inilah yang mempertahankan karakteristik paling penting dari data masukan. Kemacetan bertindak sebagai filter yang memaksa autoencoder mempelajari cara efisien untuk memadatkan informasi. Hal ini dapat dibandingkan dengan bentuk kompresi data, namun kompresi dipelajari secara otomatis dari data dan bukan ditentukan oleh algoritma standar.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Penguraian_kode"></span>Penguraian kode<span class="ez-toc-section-end"></span></h4>



<p>Fase decoding adalah langkah yang simetris dengan pengkodean, di mana representasi terkompresi direkonstruksi menuju keluaran yang bertujuan agar sesetia mungkin dengan masukan asli. Dimulai dari representasi hambatan, jaringan saraf secara bertahap akan meningkatkan dimensi data. Ini adalah proses kebalikan dari pengkodean: lapisan-lapisan yang berurutan merekonstruksi karakteristik awal dari representasi yang direduksi. Jika decoding efisien, keluaran autoencoder harus mendekati data asli.</p>



<p>Dalam pembelajaran tanpa pengawasan, autoencoder sangat berguna untuk memahami struktur dasar data. Efektivitas jaringan ini diukur bukan melalui kemampuannya mereproduksi input secara sempurna, melainkan melalui kemampuannya menangkap atribut data yang paling menonjol dan relevan dalam kode. Kode ini kemudian dapat digunakan untuk tugas-tugas seperti pengurangan dimensi, visualisasi, atau bahkan pra-pemrosesan untuk jaringan saraf lainnya dalam arsitektur yang lebih kompleks.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Aplikasi_praktis_dan_variasi_autoencoder"></span>Aplikasi praktis dan variasi autoencoder<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png" alt="" class="wp-image-1192" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>aku<strong>autoencoder</strong>, komponen kunci dalam pembelajaran mendalam yang didukung oleh Kecerdasan Buatan (AI), adalah jaringan saraf yang dirancang untuk menyandikan data menjadi representasi dimensi yang lebih rendah dan menguraikannya sedemikian rupa sehingga rekonstruksi yang relevan dapat dilakukan. Mari kita periksa <strong>aplikasi praktis</strong> dan varian yang muncul di bidang menarik ini.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Aplikasi_praktis_autoencoder-2"></span>Aplikasi praktis autoencoder<span class="ez-toc-section-end"></span></h3>



<p>Autoencoder telah menemukan jalannya ke banyak aplikasi karena kemampuannya mempelajari representasi data yang efisien dan bermakna tanpa pengawasan. Berikut beberapa contohnya:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pengurangan_dimensi"></span>Pengurangan dimensi<span class="ez-toc-section-end"></span></h4>



<p>Seperti PCA (Principal Component Analysis), autoencoder sering digunakan untuk <strong>pengurangan dimensi</strong>. Teknik ini memungkinkan penyederhanaan pemrosesan data dengan mengurangi jumlah variabel yang perlu diperhitungkan sekaligus mempertahankan sebagian besar informasi yang terdapat dalam kumpulan data asli.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Peredam_Kebisingan_Denoising"></span>Peredam Kebisingan (Denoising)<span class="ez-toc-section-end"></span></h4>



<p>Dengan kemampuannya untuk belajar merekonstruksi masukan dari data yang dihancurkan sebagian, autoencoder sangat berguna <strong>pembatalan kebisingan</strong>. Mereka berhasil mengenali dan memulihkan data yang berguna meskipun ada gangguan kebisingan.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kompresi_data"></span>Kompresi data<span class="ez-toc-section-end"></span></h4>



<p>Dengan belajar menyandikan data ke dalam bentuk yang lebih ringkas, autoencoder dapat digunakan <strong>kompresi data</strong>. Meskipun dalam praktiknya belum banyak digunakan untuk tujuan ini, potensinya cukup besar, terutama untuk mengompresi tipe data tertentu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pembuatan_dan_imputasi_data"></span>Pembuatan dan imputasi data<span class="ez-toc-section-end"></span></h4>



<p>Autoencoder dapat menghasilkan instance data baru yang menyerupai data pelatihannya. Kemampuan ini juga bisa digunakan <strong>tuduhan</strong>, yang melibatkan pengisian data yang hilang dalam kumpulan data.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Varian_autoencoder"></span>Varian autoencoder<span class="ez-toc-section-end"></span></h3>



<p>Selain autoencoder standar, berbagai varian telah dikembangkan untuk beradaptasi dengan spesifikasi data dan tugas yang diperlukan. Berikut beberapa variasi penting:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoder_Variasi_VAE"></span>Autoencoder Variasi (VAE)<span class="ez-toc-section-end"></span></h4>



<p>ITU <strong>Autoencoder Variasi</strong> (<strong>VAE</strong>) tambahkan lapisan stokastik yang memungkinkan data dihasilkan. VAE sangat populer dalam pembuatan konten, seperti gambar atau musik, karena memungkinkan untuk menghasilkan elemen baru dan bervariasi yang masuk akal menurut model yang sama.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoder_Jarang"></span>Autoencoder Jarang<span class="ez-toc-section-end"></span></h4>



<p>ITU <strong>autoencoder yang jarang</strong> memasukkan penalti yang memberlakukan aktivitas terbatas di node tersembunyi. Mereka efektif dalam menemukan karakteristik data yang berbeda, yang membuatnya berguna <strong>klasifikasi</strong> dan itu <strong>deteksi anomali</strong>.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Menolak_Autoencoder"></span>Menolak Autoencoder<span class="ez-toc-section-end"></span></h4>



<p>ITU <strong>autoencoder yang didenormalisasi</strong> dirancang untuk menahan masuknya noise ke dalam data masukan. Mereka ampuh untuk mempelajari representasi yang kuat dan untuk <strong>pemrosesan awal data</strong> sebelum melakukan tugas pembelajaran mesin lainnya.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoder_Berurutan"></span>Autoencoder Berurutan<span class="ez-toc-section-end"></span></h4>



<p>ITU <strong>autoencoder berurutan</strong> memproses data yang diatur dalam urutan, seperti teks atau deret waktu. Mereka sering menggunakan jaringan berulang seperti LSTM (Memori Jangka Pendek Panjang) untuk menyandikan dan mendekode informasi dari waktu ke waktu.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Cara_melatih_autoencoder_dan_contoh_kode"></span>Cara melatih autoencoder dan contoh kode<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png" alt="" class="wp-image-1193" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Pelatihan a <strong>autoencoder</strong> adalah tugas penting dalam bidang pembelajaran mesin untuk pengurangan dimensi dan deteksi anomali, di antara aplikasi lainnya. Di sini kita akan melihat cara melatih model seperti itu menggunakan Python dan perpustakaan <strong>keras</strong>, dengan contoh kode yang dapat Anda uji dan sesuaikan dengan proyek Anda.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Proses_pelatihan_autoencoder"></span>Proses pelatihan autoencoder<span class="ez-toc-section-end"></span></h4>



<p>Untuk melatih autoencoder, biasanya digunakan metrik kerugian, seperti mean square error (MSE), yang mengukur perbedaan antara masukan asli dan rekonstruksinya. Tujuan pelatihan adalah untuk meminimalkan fungsi kerugian ini.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Contoh_kode_dengan_Keras"></span>Contoh kode dengan Keras<span class="ez-toc-section-end"></span></h4>



<p>Berikut adalah contoh sederhana pelatihan penggunaan autoencoder <strong>keras</strong>:</p>



<pre class="wp-block-code"><code>

dari keras.layers impor Input, Padat
dari keras.models impor Model

# Ukuran masuk
# Dimensi ruang laten (representasi fitur)
pengkodean_dim = 32

# Definisi pembuat enkode
input_img = Masukan(bentuk=(input_dim,))
dikodekan = Padat(encoding_dim, aktivasi='relu')(input_img)

# Definisi dekoder
diterjemahkan = Padat(input_dim, aktivasi='sigmoid')(dikodekan)

# Model pembuat enkode otomatis
autoencoder = Model(input_img, diterjemahkan)

# Kompilasi model
autoencoder.kompilasi(optimizer='adam', loss='binary_crossentropy')

# Pelatihan autoencoder
autoencoder.fit(X_train,
                zaman=50,
                ukuran_batch=256,
                acak=Benar,
                validasi_data=(X_test, X_test))

</code></pre>



<p>Dalam contoh ini, `X_train` dan `X_test` mewakili data pelatihan dan pengujian. Perhatikan bahwa autoencoder dilatih untuk memprediksi masukannya sendiri `X_train` sebagai keluaran.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Tip_untuk_latihan_yang_baik"></span>Tip untuk latihan yang baik<span class="ez-toc-section-end"></span></h4>



<p></p>



<p>Gunakan teknik seperti <strong>validasi silang</strong>, di sana <strong>normalisasi batch</strong> dan itu <strong>panggilan balik</strong> Keras juga dapat membantu meningkatkan kinerja dan stabilitas drive autoencoder.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Aplikasi_autoencoder"></span>Aplikasi autoencoder<span class="ez-toc-section-end"></span></h4>



<p>Setelah pelatihan, autoencoder dapat digunakan untuk:</p>



<ul class="wp-block-list">
<li>pengurangan dimensi,</li>



<li>deteksi anomali,</li>



<li>pembelajaran deskriptor tanpa pengawasan yang berguna untuk tugas pembelajaran mesin lainnya.</li>
</ul>



<p>Kesimpulannya, melatih autoencoder adalah tugas yang memerlukan pemahaman tentang arsitektur jaringan saraf dan pengalaman dalam menyempurnakan hyperparameter. Namun, kesederhanaan dan fleksibilitas autoencoder menjadikannya alat yang berharga untuk banyak masalah pemrosesan data.</p>



---
title: "Teorem Bayes dan penggunaannya dalam AI"
slug: "teorem-bayes-dan-penggunaannya-dalam-ai"
excerpt: "Pengenalan kepada teorem Bayes THE Teorem Bayes ialah formula asas dalam kebarangkalian dan statistik yang menerangkan pengemaskinian kepercayaan kita dengan kehadiran maklumat baharu. Dinamakan sebagai penghormatan kepada Reverend Thomas Bayes, teorem ini memainkan peranan penting dalam banyak bidang dari pembelajaran mesin kepada membuat keputusan di bawah ketidakpastian. Intipati teorem Bayes Hati daripada Teorem Bayes ialah [&hellip;]"
date: "2024-03-09T12:13:38"
categories: ["pengkomputeran-dan-data-ms", "teknologi-dan-digital-ms"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Probabilités S3 Probabilités Conditionnelles: le Théorème de Bayes #ep14" width="500" height="281" src="https://www.youtube.com/embed/cCQlN6FhHvo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Pengenalan_kepada_teorem_Bayes" >Pengenalan kepada teorem Bayes</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Intipati_teorem_Bayes" >Intipati teorem Bayes</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Penggunaan_teorem_Bayes" >Penggunaan teorem Bayes</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Kepentingan_dalam_AI_dan_Pembelajaran_Mesin" >Kepentingan dalam AI dan Pembelajaran Mesin</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Asas_Inferens_Bayesian" >Asas Inferens Bayesian</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Teorem_Bayes" >Teorem Bayes</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#A_priori_dan_kebarangkalian_posterior" >A priori dan kebarangkalian posterior</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Bukti" >Bukti</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Inferens_Bayesian_dalam_amalan" >Inferens Bayesian dalam amalan</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-10" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Teorem_Bayes_dalam_Algoritma_Pembelajaran_Mesin" >Teorem Bayes dalam Algoritma Pembelajaran Mesin</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-11" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Aplikasi_teorem_Bayes_dalam_AI" >Aplikasi teorem Bayes dalam AI</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Kepentingan_pembelajaran_Bayesian" >Kepentingan pembelajaran Bayesian</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Contoh_algoritma_Bayesian" >Contoh algoritma Bayesian</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/ms/teorem-bayes-dan-penggunaannya-dalam-ai/#Teorem_Bayes_dalam_amalan" >Teorem Bayes dalam amalan</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Pengenalan_kepada_teorem_Bayes"></span>Pengenalan kepada teorem Bayes<span class="ez-toc-section-end"></span></h2>



<p>THE <strong>Teorem Bayes</strong> ialah formula asas dalam kebarangkalian dan statistik yang menerangkan pengemaskinian kepercayaan kita dengan kehadiran maklumat baharu. Dinamakan sebagai penghormatan kepada Reverend Thomas Bayes, teorem ini memainkan peranan penting dalam banyak bidang dari pembelajaran mesin kepada membuat keputusan di bawah ketidakpastian.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Intipati_teorem_Bayes"></span>Intipati teorem Bayes<span class="ez-toc-section-end"></span></h3>



<p>Hati daripada <strong>Teorem Bayes</strong> ialah kebarangkalian bersyarat. Dalam bentuk yang paling mudah, ia menyatakan bagaimana kebarangkalian posterior dikemas kini daripada kebarangkalian a priori dengan mengambil kira kebarangkalian kejadian yang diperhatikan. Dalam erti kata lain, ia memungkinkan untuk menyemak semula kebarangkalian awal berdasarkan bukti baharu.</p>



<p>Ia biasanya diwakili dalam bentuk persamaan berikut:</p>



<p><strong>P(A|B) = (P(B|A) * P(A)) / P(B)</strong></p>



<p>Atau:</p>



<ul class="wp-block-list">
<li><strong>P(A|B)</strong> ialah kebarangkalian kejadian A diberi B (kebarangkalian posteriori)</li>



<li><strong>P(B|A)</strong> ialah kebarangkalian kejadian B diberi A</li>



<li><strong>P(A)</strong> ialah kebarangkalian awal kejadian A (kebarangkalian priori)</li>



<li><strong>P(B)</strong> ialah kebarangkalian awal bagi peristiwa B</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Penggunaan_teorem_Bayes"></span>Penggunaan teorem Bayes<span class="ez-toc-section-end"></span></h4>



<p>Aplikasi daripada <strong>Teorem Bayes</strong> boleh ditemui dalam pelbagai senario praktikal, seperti diagnosis perubatan, penapisan spam atau inferens statistik dalam penyelidikan saintifik. Dalam bidang perubatan, sebagai contoh, teorem memungkinkan untuk menganggarkan kebarangkalian pesakit mempunyai penyakit berdasarkan keputusan ujian, mengetahui kebarangkalian bahawa ujian ini memberikan positif benar atau palsu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kepentingan_dalam_AI_dan_Pembelajaran_Mesin"></span>Kepentingan dalam AI dan Pembelajaran Mesin<span class="ez-toc-section-end"></span></h4>



<p>Dalam Kecerdasan Buatan (AI) dan <strong>pembelajaran mesin</strong>, teorem Bayes ialah asas pembelajaran Bayesian. Rangka kerja pembelajaran ini menggunakan kepercayaan terdahulu dan mengemas kininya dengan data baharu untuk membuat ramalan. Akibatnya, model boleh menjadi lebih tepat apabila mereka menerima data tambahan.</p>



<p>Secara ringkasnya, <strong>Teorem Bayes</strong> ialah alat yang berkuasa untuk memahami kebarangkalian bersyarat dan untuk memperhalusi kepercayaan kita dengan mengambil kira maklumat baharu. Kesederhanaan matematiknya berbeza dengan implikasi dan aplikasinya yang luas, menjadikannya subjek asas yang mesti dibaca bagi sesiapa yang berminat dalam statistik, membuat keputusan dan kecerdasan buatan.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Asas_Inferens_Bayesian"></span>Asas Inferens Bayesian<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA.png" alt="" class="wp-image-1314" srcset="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA.png 1792w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-300x171.png 300w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1024x585.png 1024w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-150x86.png 150w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-768x439.png 768w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>inferens Bayesian</strong> ialah cabang statistik yang menyediakan rangka kerja teori untuk mentafsir peristiwa dari segi kebarangkalian. Ia berdasarkan kepada <strong>Teorem Bayes</strong>, yang merupakan formula untuk mengemas kini kebarangkalian peristiwa berlaku berdasarkan data baharu. </p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Teorem_Bayes"></span>Teorem Bayes<span class="ez-toc-section-end"></span></h3>



<p>Teorem Bayes ialah tulang belakang inferens Bayesian. Secara matematik, ia dinyatakan seperti berikut:</p>



<p><strong>P(H|E) = (P(E|H) * P(H)) / P(E)</strong></p>



<p>Atau:</p>



<ul class="wp-block-list">
<li><strong>P(H|E)</strong> ialah kebarangkalian hipotesis H mengetahui peristiwa E telah berlaku.</li>



<li><strong>P(E|H)</strong> ialah kebarangkalian peristiwa E akan berlaku jika hipotesis H adalah benar.</li>



<li><strong>P(H)</strong> ialah kebarangkalian a priori hipotesis H sebelum melihat data E.</li>



<li><strong>P(E)</strong> ialah kebarangkalian a priori bagi peristiwa E.</li>
</ul>



<p>Teorem ini membolehkan kita mengemas kini kepercayaan kita dari segi kebarangkalian pada hipotesis H selepas menyedari peristiwa E.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="A_priori_dan_kebarangkalian_posterior"></span>A priori dan kebarangkalian posterior<span class="ez-toc-section-end"></span></h4>



<p>Dua konsep utama dalam inferens Bayesian ialah tanggapan kebarangkalian <strong>a priori</strong> Dan <strong>posterior</strong> :</p>



<ul class="wp-block-list">
<li>Kebarangkalian <strong>a priori</strong>, dilambangkan P(H), mewakili apa yang kita tahu sebelum mengambil kira maklumat baharu.</li>



<li>Kebarangkalian <strong>posterior</strong>, dilambangkan P(H|E), mewakili apa yang kita tahu selepas mengambil kira maklumat baharu.</li>
</ul>



<p>Inferens Bayesian melibatkan pergerakan daripada kebarangkalian terdahulu kepada kebarangkalian belakang menggunakan teorem Bayes.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Bukti"></span>Bukti<span class="ez-toc-section-end"></span></h4>



<p>Dalam teorem Bayes, P(E) sering dipanggil faktor bagi<strong>bukti</strong>. Ia boleh dianggap sebagai ukuran keserasian data yang diperhatikan dengan semua hipotesis yang mungkin. Dalam amalan, ia bertindak sebagai faktor normalisasi dalam mengemas kini kepercayaan kita.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Inferens_Bayesian_dalam_amalan"></span>Inferens Bayesian dalam amalan<span class="ez-toc-section-end"></span></h4>



<p>Dalam amalan, inferens Bayesian digunakan dalam banyak bidang seperti pembelajaran mesin, analisis data statistik, membuat keputusan dengan adanya ketidakpastian, dsb. Khususnya, ia membolehkan:</p>



<ul class="wp-block-list">
<li>Untuk membangunkan model ramalan kebarangkalian.</li>



<li>Untuk mengesan anomali atau menyimpulkan corak tersembunyi dalam data kompleks.</li>



<li>Membuat keputusan berdasarkan data yang tidak lengkap atau tidak pasti.</li>
</ul>



<p>L&#8217;<strong>inferens Bayesian</strong> menyediakan rangka kerja yang kuat untuk menaakul dengan ketidakpastian dan menyepadukan maklumat baharu secara koheren. Aplikasinya adalah luas dan penggunaannya dalam bidang lanjutan seperti<strong>kecerdasan buatan</strong> Dimanakah <strong>data besar</strong> berkembang secara berterusan. Oleh itu, memahami prinsip asasnya adalah penting bagi mereka yang ingin mentafsir dunia melalui prisma kebarangkalian.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Teorem_Bayes_dalam_Algoritma_Pembelajaran_Mesin"></span>Teorem Bayes dalam Algoritma Pembelajaran Mesin<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1.png" alt="" class="wp-image-1315" srcset="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1.png 1792w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-300x171.png 300w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-1024x585.png 1024w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-150x86.png 150w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-768x439.png 768w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Dunia kecerdasan buatan (AI) sentiasa berkembang, dan antara konsep asas yang mendorong revolusi ini ialah teorem Bayes. Alat matematik ini memainkan peranan penting dalam algoritma pembelajaran mesin, membolehkan mesin membuat keputusan termaklum berdasarkan kebarangkalian.</p>



<p>THE <strong>Teorem Bayes</strong>, dibangunkan oleh Rev. Thomas Bayes pada abad ke-18, ialah formula yang menerangkan kebarangkalian bersyarat sesuatu peristiwa, berdasarkan pengetahuan terdahulu yang berkaitan dengan peristiwa itu. Secara formal, ia memungkinkan untuk mengira kebarangkalian (P(A|B)) bagi peristiwa A, mengetahui bahawa B adalah benar, menggunakan kebarangkalian B mengetahui bahawa A adalah benar (P(B|A)), kebarangkalian daripada A ( P(A) ), dan kebarangkalian B ( P(B) ).</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Aplikasi_teorem_Bayes_dalam_AI"></span>Aplikasi teorem Bayes dalam AI<span class="ez-toc-section-end"></span></h3>



<p>Dalam konteks pembelajaran mesin, teorem Bayes digunakan untuk membina model kebarangkalian. Model ini dapat melaraskan ramalan mereka berdasarkan data baharu yang disediakan, membolehkan penambahbaikan dan penghalusan prestasi berterusan. Proses ini amat berguna dalam pengelasan, di mana matlamatnya adalah untuk memberikan label kepada input yang diberikan berdasarkan ciri yang diperhatikan.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kepentingan_pembelajaran_Bayesian"></span>Kepentingan pembelajaran Bayesian<span class="ez-toc-section-end"></span></h4>



<p>Salah satu kelebihan utama pembelajaran Bayesian ialah keupayaannya untuk menangani ketidakpastian dan memberikan ukuran keyakinan dalam ramalan. Ini adalah asas dalam bidang kritikal seperti perubatan atau kewangan, di mana setiap ramalan boleh memberi kesan yang besar. Selain itu, pendekatan ini menyediakan rangka kerja untuk menggabungkan pengetahuan sedia ada dan pembelajaran daripada sejumlah kecil data.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Contoh_algoritma_Bayesian"></span>Contoh algoritma Bayesian<span class="ez-toc-section-end"></span></h4>



<p>Terdapat beberapa algoritma pembelajaran mesin yang bergantung pada teorem Bayes, termasuk:</p>



<ul class="wp-block-list">
<li><strong>Naif Bayes</strong>: Pengelas kebarangkalian yang, walaupun namanya &#8216;naif&#8217;, adalah luar biasa kerana kesederhanaan dan keberkesanannya, terutamanya apabila kebarangkalian ciri adalah bebas.</li>



<li><strong>Rangkaian Bayesian</strong>: Model grafik yang mewakili hubungan kebarangkalian antara satu set pembolehubah, dan yang boleh digunakan untuk ramalan, pengelasan dan membuat keputusan.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Teorem_Bayes_dalam_amalan"></span>Teorem Bayes dalam amalan<span class="ez-toc-section-end"></span></h4>



<p>Untuk menggambarkan pelaksanaan pembelajaran Bayesian, pertimbangkan contoh aplikasi mudah: penapisan spam dalam e-mel. Menggunakan algoritma <strong>Naif Bayes</strong>, sistem boleh belajar untuk membezakan mesej yang sah daripada spam dengan mengira kebarangkalian bahawa e-mel adalah spam, berdasarkan kekerapan kejadian kata kunci tertentu. </p>



<p>Apabila sistem menerima e-mel baharu, ia melaraskan kebarangkaliannya, menjadi lebih dan lebih tepat dalam klasifikasinya.</p>



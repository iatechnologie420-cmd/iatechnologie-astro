---
title: "Apakah Sharding? definisi dan kelebihan"
slug: "apakah-sharding-definisi-dan-kelebihan"
excerpt: "Memahami sharding: definisi dan prinsip asas Dunia pangkalan data dan storan data berskala besar adalah kompleks dan sentiasa berkembang. Untuk mengurus volum data yang meningkat secara eksponen, seni bina IT mesti berinovasi dan mencari penyelesaian untuk mengoptimumkan prestasi dan pengurusan data ini. Satu pendekatan untuk masalah ini ialah teknik yang dipanggil serpihan. Dalam artikel ini, [&hellip;]"
date: "2024-03-09T12:32:26"
featuredImage: "/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-3.png"
categories: ["infrastruktur-dan-rangkaian-ms", "teknologi-dan-digital-ms"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Database Sharding and Partitioning" width="500" height="281" src="https://www.youtube.com/embed/wXvljefXyEo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Memahami_sharding_definisi_dan_prinsip_asas" >Memahami sharding: definisi dan prinsip asas</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Apa_itu_Sharding" >Apa itu Sharding?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Bagaimanakah_sharding_berfungsi" >Bagaimanakah sharding berfungsi?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Faedah_Sharding" >Faedah Sharding</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Cabaran_dan_Pertimbangan" >Cabaran dan Pertimbangan</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Bagaimanakah_data_diedarkan" >Bagaimanakah data diedarkan?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Penyimpanan_data_dalam_serpihan" >Penyimpanan data dalam serpihan</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Kelemahan_Sharding" >Kelemahan Sharding</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Cabaran_teknikal_sharding" >Cabaran teknikal sharding</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ms/apakah-sharding-definisi-dan-kelebihan/#Pertimbangan_Praktikal_untuk_Sharding" >Pertimbangan Praktikal untuk Sharding</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Memahami_sharding_definisi_dan_prinsip_asas"></span>Memahami sharding: definisi dan prinsip asas<span class="ez-toc-section-end"></span></h2>



<p>Dunia pangkalan data dan storan data berskala besar adalah kompleks dan sentiasa berkembang. Untuk mengurus volum data yang meningkat secara eksponen, seni bina IT mesti berinovasi dan mencari penyelesaian untuk mengoptimumkan prestasi dan pengurusan data ini. Satu pendekatan untuk masalah ini ialah teknik yang dipanggil <strong>serpihan</strong>. </p>



<p>Dalam artikel ini, kami akan mentakrifkan sharding, memahami prinsip asasnya, dan mengapa ia penting dalam sistem pangkalan data moden.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Apa_itu_Sharding"></span>Apa itu Sharding?<span class="ez-toc-section-end"></span></h3>



<p>THE <strong>serpihan</strong> ialah kaedah pembahagian data secara mendatar dalam pangkalan data teragih atau sistem pengurusan pangkalan data. Teknik ini terdiri daripada membahagikan pangkalan data kepada bahagian yang lebih kecil dipanggil <em>serpihan</em>, yang boleh diedarkan merentasi beberapa pelayan. Setiap serpihan mengandungi subset data dan berfungsi sebagai pangkalan data bebas. Kelebihan utama ini ialah ia membolehkan sejumlah besar data dan transaksi diuruskan dengan lebih cekap dengan mengurangkan beban pada setiap pelayan individu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Bagaimanakah_sharding_berfungsi"></span>Bagaimanakah sharding berfungsi?<span class="ez-toc-section-end"></span></h4>



<p>Sharding adalah berdasarkan logik pengedaran data yang ditentukan oleh algoritma sharding. Terdapat algoritma yang berbeza, tetapi pilihan selalunya bergantung pada sifat data dan pertanyaan yang mesti dikendalikan oleh sistem. Contoh biasa algoritma termasuk sharding berasaskan julat (di mana data diedarkan mengikut julat nilai), sharding hash (di mana cincang kekunci tertentu menentukan lokasi data) atau sharding berasaskan direktori (dengan jadual carian untuk mencari data itu).</p>



<p>Setelah serpihan dibuat dan data diedarkan, sistem pengurusan berpusat, sering dipanggil <em>pengurus serpihan</em> Ataupun <em>hayun</em>, adalah perlu untuk menyelaraskan transaksi dan permintaan antara serpihan yang berbeza. Sistem ini memastikan bahawa pertanyaan diarahkan ke serpihan yang betul, dengan itu membenarkan interaksi dengan hanya bahagian pangkalan data yang berkaitan.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Faedah_Sharding"></span>Faedah Sharding<span class="ez-toc-section-end"></span></h4>



<p>Sharding menawarkan beberapa kelebihan yang menjadikannya menarik untuk sistem besar:</p>



<ul class="wp-block-list">
<li><strong>Kebolehskalaan</strong> : Sharding membolehkan pangkalan data mudah menyesuaikan diri dengan peningkatan beban dengan hanya menambah lebih banyak pelayan.</li>



<li><strong>Prestasi</strong> : Dengan mengurangkan beban pada setiap pelayan, prestasi pertanyaan boleh dipertingkatkan dengan banyak, terutamanya untuk operasi tulis.</li>



<li><strong>Ketersediaan</strong> : Walaupun satu serpihan jatuh, yang lain terus berfungsi, meningkatkan kebolehpercayaan sistem secara keseluruhan.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Cabaran_dan_Pertimbangan"></span>Cabaran dan Pertimbangan<span class="ez-toc-section-end"></span></h4>



<p>Walau bagaimanapun, sharding juga datang dengan bahagian cabarannya:</p>



<ul class="wp-block-list">
<li>Kerumitan menguruskan serpihan boleh meningkat dengan bilangan serpihan.</li>



<li>Urus niaga yang memerlukan maklumat merentas serpihan berbeza adalah lebih rumit untuk diuruskan.</li>



<li>Konsistensi data mungkin menjadi lebih sukar untuk dipastikan apabila bilangan serpihan bertambah.</li>
</ul>



<p>Oleh itu, adalah penting untuk mempertimbangkan dengan teliti sama ada sharding adalah strategi yang tepat untuk aplikasi tertentu. Kadangkala pendekatan lain seperti pembahagian menegak, replikasi data atau menggunakan pangkalan data bukan perhubungan mungkin lebih sesuai.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Bagaimanakah_data_diedarkan"></span>Bagaimanakah data diedarkan?<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png" alt="" class="wp-image-1070" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Pengedaran data dalam persekitaran sharded boleh dijalankan mengikut algoritma yang berbeza. Berikut adalah beberapa yang paling biasa:</p>



<ul class="wp-block-list">
<li><strong>Perkongsian berdasarkan julat kunci:</strong> Data dibahagikan mengikut kunci tertentu, di mana setiap serpihan bertanggungjawab untuk julat nilai.</li>



<li><strong>Sharding berasaskan hash:</strong> Fungsi cincang digunakan untuk menentukan shard mana yang akan menyimpan rekod tertentu, berdasarkan kunci.</li>



<li><strong>Sharding berasaskan direktori:</strong> Direktori mengekalkan pemetaan antara rekod dan serpihan tempat ia disimpan.</li>
</ul>



<p>Kaedah ini membolehkan pengedaran data yang agak seimbang, pengurangan kesesakan dan peningkatan dalam masa tindak balas.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Penyimpanan_data_dalam_serpihan"></span>Penyimpanan data dalam serpihan<span class="ez-toc-section-end"></span></h4>



<p>Data disimpan dalam setiap serpihan secara bebas daripada serpihan lain. Ini bermakna setiap serpihan bertindak sebagai pangkalan data kendiri, dengan skema dan indeksnya sendiri. Ketekalan data merentas serpihan dikekalkan secara logik dan bukannya secara fizikal, yang kadangkala boleh memperkenalkan kerumitan apabila mengurus urus niaga yang merangkumi berbilang serpihan.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kelemahan_Sharding"></span>Kelemahan Sharding<span class="ez-toc-section-end"></span></h4>



<p>Walau bagaimanapun, sharding juga mempunyai kelemahan tertentu:</p>



<ul class="wp-block-list">
<li><strong>Kerumitan:</strong> Mengurus dan mengekalkan berbilang serpihan boleh menjadi rumit, terutamanya untuk ketekalan data dan pengurusan transaksi.</li>



<li><strong>Risiko pengedaran yang lemah:</strong> Pengedaran data yang tidak sekata boleh membawa kepada &#8220;titik panas&#8221;, di mana beberapa serpihan terlebih muatan.</li>



<li><strong>Kos:</strong> Keperluan untuk mengendalikan dan mengurus lebih banyak infrastruktur boleh meningkatkan kos.</li>



<li></li>
</ul>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png" alt="" class="wp-image-1071" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Cabaran_teknikal_sharding"></span>Cabaran teknikal sharding<span class="ez-toc-section-end"></span></h4>



<p>Pelaksanaan sharding menimbulkan beberapa persoalan teknikal:</p>



<ul class="wp-block-list">
<li><strong>Kerumitan reka bentuk</strong> : Menjadualkan kunci sharding adalah penting dan harus dilakukan dengan berhati-hati, kerana reka bentuk yang lemah boleh menyebabkan ketidakseimbangan dalam pengedaran data dan menjejaskan kecekapan sistem.</li>



<li><strong>Pertanyaan melintang</strong> : Melakukan pertanyaan pada berbilang serpihan boleh menjadi rumit dan menyusahkan kerana ia memerlukan komunikasi dan mekanisme pengagregatan antara serpihan.</li>



<li><strong>Transaksi Teragih</strong> : Mengekalkan integriti urus niaga merentas berbilang serpihan adalah rumit dan memerlukan protokol penyelarasan dan mekanisme penguncian yang canggih.</li>



<li><strong>Penskalaan</strong> : Walaupun sharding membenarkan kebolehskalaan, menambah atau mengalih keluar serpihan selepas fakta boleh menjadi rumit dan selalunya memerlukan pengagihan semula data.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pertimbangan_Praktikal_untuk_Sharding"></span>Pertimbangan Praktikal untuk Sharding<span class="ez-toc-section-end"></span></h4>



<p>Selain cabaran teknikal, terdapat pertimbangan praktikal untuk diambil kira:</p>



<ul class="wp-block-list">
<li><strong>kos</strong> : Kerumitan melaksanakan dan mengekalkan sharding boleh mengakibatkan kos yang besar dari segi perkakasan, perisian dan sumber manusia khusus.</li>



<li><strong>Prestasi</strong> : Memilih strategi sharding yang tidak sesuai boleh membawa kepada prestasi yang lemah, terutamanya jika pengimbangan beban tidak diurus dengan baik.</li>



<li><strong>Ketekalan Data</strong> : Memastikan konsistensi data merentas semua serpihan adalah penting tetapi sukar untuk dicapai, terutamanya dalam persekitaran yang sangat diedarkan.</li>



<li><strong>Pakar teknikal</strong> : Kepakaran teknikal yang mendalam diperlukan untuk menguruskan kerumitan sharding dan bertindak balas terhadap isu.</li>



<li><strong>Sandaran dan Pemulihan</strong> : Menguruskan sandaran dan pemulihan menjadi lebih kompleks dengan sharding, kerana operasi ini mesti diselaraskan merentasi beberapa shard.</li>
</ul>



<p>Kesimpulannya, walaupun sharding adalah teknik yang berkuasa untuk pangkalan data yang memerlukan tahap prestasi dan kebolehskalaan yang tinggi, ia mengenakan satu siri cabaran dan memerlukan pertimbangan praktikal yang penting untuk dilaksanakan secara optimum. Dengan mengetahui isu-isu dan menyediakan strategi sharding dengan teliti, organisasi boleh mendapat manfaat sepenuhnya daripada faedahnya sambil meminimumkan risiko dan kos yang berkaitan.</p>



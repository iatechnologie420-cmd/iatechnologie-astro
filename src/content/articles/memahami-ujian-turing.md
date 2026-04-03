---

title: "Memahami ujian Turing"
slug: "memahami-ujian-turing"
excerpt: "Asal-usul dan prinsip ujian Turing Dalam dunia kecerdasan buatan (AI) dan pengkomputeran, ujian Turing menduduki tempat yang menonjol. Ini adalah kaedah penanda aras yang direka untuk menilai keupayaan mesin untuk meniru kecerdasan manusia. Asal usul dan prinsip ujian revolusi ini bermula pada pertengahan abad ke-20 dan berdasarkan konsep falsafah dan pengiraan yang kompleks. Sejarah Ujian [&hellip;]"
date: "2024-03-09T12:57:17"
featuredImage: "/images/blog/Bien-comprendre-le-test-de-Turing-3.png"
categories: ["latihan-dan-asas-ai-ms"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Comprendre le test de Turing facilement en 2 minutes" width="500" height="281" src="https://www.youtube.com/embed/XnFvfWWqosY?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ms/memahami-ujian-turing/#Asal-usul_dan_prinsip_ujian_Turing" >Asal-usul dan prinsip ujian Turing</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ms/memahami-ujian-turing/#Sejarah_Ujian_Turing" >Sejarah Ujian Turing</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ms/memahami-ujian-turing/#Prinsip_asas_ujian_Turing" >Prinsip asas ujian Turing</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ms/memahami-ujian-turing/#Menjalankan_ujian_Turing" >Menjalankan ujian Turing</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ms/memahami-ujian-turing/#Implikasi_dan_isu_ujian_Turing" >Implikasi dan isu ujian Turing</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/ms/memahami-ujian-turing/#Kriteria_untuk_ujian_Turing_yang_berjaya" >Kriteria untuk ujian Turing yang berjaya</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/ms/memahami-ujian-turing/#Kriteria_tidak_boleh_dibezakan_manusia" >Kriteria tidak boleh dibezakan manusia</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ms/memahami-ujian-turing/#Tempoh_dan_syarat_ujian" >Tempoh dan syarat ujian</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ms/memahami-ujian-turing/#Penilaian_keputusan_dan_kontroversi" >Penilaian keputusan dan kontroversi</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ms/memahami-ujian-turing/#Peranan_interaksi_manusia" >Peranan interaksi manusia</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-11" href="/ms/memahami-ujian-turing/#Evolusi_ujian_Turing_dalam_era_AI" >Evolusi ujian Turing dalam era AI</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-12" href="/ms/memahami-ujian-turing/#Ujian_Turing_asal_dan_batasannya" >Ujian Turing asal dan batasannya</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/ms/memahami-ujian-turing/#Kemajuan_dalam_AI_dan_evolusi_ujian_Turing" >Kemajuan dalam AI dan evolusi ujian Turing</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/ms/memahami-ujian-turing/#Kerumitan_ujian_Turing" >Kerumitan ujian Turing</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/ms/memahami-ujian-turing/#Masa_depan_ujian_Turing" >Masa depan ujian Turing</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Asal-usul_dan_prinsip_ujian_Turing"></span>Asal-usul dan prinsip ujian Turing<span class="ez-toc-section-end"></span></h2>



<p>Dalam dunia kecerdasan buatan (AI) dan pengkomputeran, ujian Turing menduduki tempat yang menonjol. Ini adalah kaedah penanda aras yang direka untuk menilai keupayaan mesin untuk meniru kecerdasan manusia. Asal usul dan prinsip ujian revolusi ini bermula pada pertengahan abad ke-20 dan berdasarkan konsep falsafah dan pengiraan yang kompleks.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Sejarah_Ujian_Turing"></span>Sejarah Ujian Turing<span class="ez-toc-section-end"></span></h3>



<p>Ujian Turing mengambil namanya daripada penciptanya, Alan Turing, seorang ahli matematik British yang dianggap sebagai salah satu perintis sains komputer. Dia pertama kali membentangkan ujian ini dalam artikel 1950nya &#8220;Jentera Pengkomputeran dan Perisikan,&#8221; yang diterbitkan dalam jurnal British Mind. Alan Turing meneroka persoalan sama ada mesin boleh berfikir dan mencadangkan kaedah untuk menilai kecerdasan buatan.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Prinsip_asas_ujian_Turing"></span>Prinsip asas ujian Turing<span class="ez-toc-section-end"></span></h4>



<p>Prinsip asas Ujian Turing adalah sangat mudah. Ia berdasarkan permainan tiruan di mana seorang manusia, hakim, mempunyai tugas untuk menentukan sama ada lawan bicaranya adalah mesin atau manusia lain. Hakim berkomunikasi dengan dua lawan bicara melalui skrin dan papan kekunci, yang menjamin ketidakmungkinan bergantung pada petunjuk fizikal untuk penghakiman.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Menjalankan_ujian_Turing"></span>Menjalankan ujian Turing<span class="ez-toc-section-end"></span></h4>



<p>Ujian dilakukan seperti berikut:<br>1. Hakim bertanyakan pelbagai soalan secara bertulis.<br>2. Teman bicara manusia dan mesin juga bertindak balas secara bertulis.<br>3. Jika hakim tidak dapat membezakan mesin dengan manusia dengan secukupnya, mesin itu lulus ujian.<br>Matlamatnya adalah untuk melihat sama ada mesin boleh bersaing dengan kecerdasan manusia ke tahap di mana tindak balasnya tidak dapat dibezakan daripada lelaki atau wanita.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Implikasi_dan_isu_ujian_Turing"></span>Implikasi dan isu ujian Turing<span class="ez-toc-section-end"></span></h4>



<p>Ujian Turing mempunyai implikasi falsafah dan teknikal yang penting. Ia mengundang refleksi tentang sifat pemikiran dan kesedaran dan apa yang membentuk kecerdasan sebenar. Pada peringkat teknikal, ujian itu telah menggalakkan kemajuan yang ketara dalam bidang AI dan pemprosesan bahasa semula jadi. Sistem seperti IBM Watson atau pembantu suara seperti <strong>Siri</strong> daripada<strong>epal</strong>, <strong>Pembantu Google</strong> Dan <strong>Alexa</strong> daripada<strong>Amazon</strong> adalah contoh kontemporari usaha untuk mencipta mesin yang berpotensi lulus ujian Turing.</p>



<p>Ujian Turing kekal sebagai topik perbincangan dan perdebatan, terutamanya mengenai kesahihan dan kaitannya dalam menilai kecerdasan buatan. Walaupun ada yang berpendapat bahawa ujian itu hanya mengukur simulator perbualan dan bukan kecerdasan semata-mata, yang lain melihatnya sebagai cabaran untuk perkembangan AI masa depan.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kriteria_untuk_ujian_Turing_yang_berjaya"></span>Kriteria untuk ujian Turing yang berjaya<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Bien-comprendre-le-test-de-Turing.png" alt="" class="wp-image-806" srcset="/images/blog/Bien-comprendre-le-test-de-Turing.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Ujian Turing yang berjaya ialah satu cara untuk mengukur kecerdasan mesin dengan menilai keupayaannya untuk meniru tingkah laku manusia sehingga ke tahap di mana pemerhati manusia tidak dapat membezakan antara tindak balas mesin dan tindak balas seseorang yang sebenar. Dalam bidang kecerdasan buatan, ujian Turing yang terkenal, yang dicadangkan oleh Alan Turing pada tahun 1950, kekal sebagai rujukan di tengah-tengah banyak perbincangan mengenai kesedaran dan kecerdasan mesin. Jadi apakah kriteria yang mesti dipenuhi untuk ujian Turing untuk dianggap berjaya?</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kriteria_tidak_boleh_dibezakan_manusia"></span>Kriteria tidak boleh dibezakan manusia<span class="ez-toc-section-end"></span></h3>



<p>Matlamat utama Ujian Turing adalah untuk menguji sama ada penyiasat manusia dapat membezakan mesin daripada manusia, hanya berdasarkan respons mereka kepada soalan atau kenyataan. Jika lawan bicara tidak dapat memberitahu dengan pasti sama ada jawapan datang dari manusia atau mesin, ujian itu dianggap lulus. Dengan ini, beberapa kriteria mesti dihormati:</p>



<p>&#8211; <strong>Kualiti respons</strong> : Mereka mesti koheren dan kelihatan semula jadi, seolah-olah mereka datang dari manusia.<br>&#8211; <strong>Kepelbagaian dalam perbualan</strong> : Keupayaan mesin untuk mengambil bahagian dalam pelbagai topik menunjukkan beberapa bentuk pemahaman atau penyesuaian.<br>&#8211; <strong>Menguruskan kekaburan</strong> : mesin mesti boleh mengendalikan kehalusan dan nuansa bahasa, termasuk metafora, humor dan rujukan budaya.<br>&#8211; <strong>Emosi dan empati</strong>: Kecerdasan buatan harus menunjukkan beberapa bentuk empati atau tindak balas emosi yang sesuai terhadap situasi.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Tempoh_dan_syarat_ujian"></span>Tempoh dan syarat ujian<span class="ez-toc-section-end"></span></h4>



<p>Tiada tempoh piawai untuk ujian Turing, tetapi diterima umum bahawa tempoh yang berpanjangan boleh meningkatkan kebolehpercayaan keputusan yang diperolehi. Syarat berikut juga penting untuk ujian yang sah:</p>



<p>&#8211; <strong>Tanpa nama sepenuhnya</strong> : Penyiasat seharusnya tidak mempunyai sebarang petunjuk visual atau boleh didengar yang boleh membantunya mengenal pasti entiti di sebalik jawapan.<br>&#8211; <strong>Antara muka komunikasi neutral</strong> : Respons mesti dihantar melalui papan kekunci dan skrin untuk mengelakkan diskriminasi berdasarkan suara atau tulisan tangan.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Penilaian_keputusan_dan_kontroversi"></span>Penilaian keputusan dan kontroversi<span class="ez-toc-section-end"></span></h4>



<p>Penilaian mesti berdasarkan kriteria objektif, walaupun pertimbangan subjektif penemuduga manusia memainkan peranan penting dalam keputusan akhir. Aspek berikut adalah penting:<br>&#8211; <strong>Statistik Kejayaan</strong> : peratusan kali hakim ditipu adalah penunjuk penting.<br>&#8211; <strong>Kawalan berat sebelah</strong> : Kecondongan penyoal mesti diminimumkan dengan kaedah penilaian yang baik untuk memastikan keadilan ujian.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Peranan_interaksi_manusia"></span>Peranan interaksi manusia<span class="ez-toc-section-end"></span></h4>



<p>Interaksi semasa Ujian Turing hendaklah semula jadi dan cair, meniru aliran perbualan manusia yang sebenar. Elemen berikut perlu diambil kira:<br>&#8211; <strong>Kereaktifan</strong> : Mesin mesti menjawab soalan pada kadar yang serupa dengan perbualan manusia biasa.<br>&#8211; <strong>Interaksi dua hala</strong> : Mesin bukan sahaja harus menjawab soalan, tetapi juga boleh bertanya soalan untuk menunjukkan bahawa ia mengikuti dan mengambil bahagian secara aktif dalam perbualan.</p>



<p>Ujian Turing yang berjaya bukan sekadar menipu rakan bicara sekali, tetapi melakukannya secara konsisten, dalam keadaan yang berbeza dan dengan hakim yang berbeza. Walaupun ujian ini dibincangkan secara meluas dan kadangkala dikritik kerana kekurangan ketepatan pada pemahaman atau kesedaran sebenar AI, ia kekal sebagai cabaran yang menarik untuk pereka AI.<strong>AI</strong>. Ini terutamanya berlaku untuk syarikat yang berada di barisan hadapan dalam inovasi teknologi, seperti <strong>Google</strong> dengan Penolongnya atau <strong>OpenAI</strong> dengan GPT-3 / GPT-4, yang berusaha untuk mencipta sistem yang lebih canggih. </p>



<p>Walaupun belum ada mesin yang melepasi Ujian Turing dengan meniru manusia dengan sempurna, kemajuan dalam bidang kecerdasan buatan mendorong kita untuk sentiasa menilai semula had apa yang boleh dicapai oleh mesin.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Evolusi_ujian_Turing_dalam_era_AI"></span>Evolusi ujian Turing dalam era AI<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Bien-comprendre-le-test-de-Turing-2.png" alt="" class="wp-image-808" srcset="/images/blog/Bien-comprendre-le-test-de-Turing-2.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-2-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-2-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-2-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Ujian Turing, yang direka oleh Alan Turing pada tahun 1950-an, bertujuan untuk menilai keupayaan mesin meniru tingkah laku manusia sehingga lawan bicara tidak dapat membezakan sama ada korespondennya adalah lelaki atau mesin. Pada zaman AI, ujian Turing terus berfungsi sebagai penanda aras untuk mengukur evolusi kecerdasan buatan, walaupun ia telah dikritik dan direka bentuk semula kerana kemajuan teknologi yang dramatik.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Ujian_Turing_asal_dan_batasannya"></span>Ujian Turing asal dan batasannya<span class="ez-toc-section-end"></span></h3>



<p>Pada asalnya, ujian Turing adalah ujian perbualan teks antara manusia dan mesin. Matlamatnya adalah untuk menentukan sama ada mesin itu boleh menjalankan perbualan yang tidak dapat dibezakan daripada perbualan manusia. Walau bagaimanapun, ujian ini mempunyai had. Sememangnya, lulus ujian tidak semestinya bermakna mesin itu mempunyai kecerdasan atau pemahaman yang sebenar, tetapi sekadar ia dapat meyakinkan manusia tentang kemanusiaannya untuk masa yang singkat.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kemajuan_dalam_AI_dan_evolusi_ujian_Turing"></span>Kemajuan dalam AI dan evolusi ujian Turing<span class="ez-toc-section-end"></span></h3>



<p>Dengan kemajuan pesat kecerdasan buatan, pertukaran teks yang mudah tidak lagi mencukupi untuk menilai kecanggihan AI. Sistem semasa, seperti yang dibangunkan oleh <strong>Google</strong> Ataupun <strong>OpenAI</strong>, mampu melakukan perbualan yang rumit, mengarang muzik, menjana imej realistik dan juga menulis teks yang koheren pada pelbagai subjek.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kerumitan_ujian_Turing"></span>Kerumitan ujian Turing<span class="ez-toc-section-end"></span></h3>



<p>Untuk menyesuaikan diri dengan evolusi AI, penyelidik mencadangkan versi ujian Turing yang lebih terperinci. Versi baharu ini boleh melibatkan interaksi berbilang mod dengan mesin (teks, imej, bunyi), ujian kreativiti atau penilaian pemahaman dan akal sehat, untuk menolak had kecerdasan buatan jauh melebihi tiruan mudah.</p>



<p>Berikut ialah contoh situasi yang mewakili evolusi ujian Turing yang digunakan pada era moden AI:</p>



<p>&#8211; Perbualan mendalam mengenai tema tertentu<br>&#8211; Penciptaan kandungan artistik asli<br>&#8211; Reaksi terhadap peristiwa yang tidak dijangka atau maklumat baharu<br>&#8211; Interaksi masa nyata dengan persekitaran, contohnya melalui robot</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Masa_depan_ujian_Turing"></span>Masa depan ujian Turing<span class="ez-toc-section-end"></span></h2>



<p>Idea asal ujian Turing kini berkembang menjadi satu set penilaian yang lebih luas, bertujuan untuk menguji bukan sahaja keupayaan untuk meniru, tetapi juga autonomi, pembelajaran, kreativiti dan empati kecerdasan buatan. Ujian ini bukan lagi sekadar mengukur kualiti tiruan, tetapi bertujuan untuk menilai sejauh mana AI boleh dianggap pintar mengikut kriteria manusia yang sentiasa berubah.</p>



<p>Ujian Turing terus berkembang seiring dengan kemajuan luar biasa dalam kecerdasan buatan. Walau bagaimanapun, intipatinya tetap sama: berusaha untuk memahami sejauh mana teknologi boleh datang kepada kecerdasan manusia dan, berpotensi, mengatasinya. </p>



<p>Dalam usaha ini, terletak hati ketertarikan dengan AI dan perkembangan masa depannya.</p>



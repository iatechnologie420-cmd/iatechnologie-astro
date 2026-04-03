---

title: "Dompdf: Kako ustvariti elegantne PDF-je v PHP?"
slug: "dompdf-kako-ustvariti-elegantne-pdf-je-v-php"
excerpt: "Uvod v Dompdf Dompdf je knjižnica PHP, ki omogoča ustvarjanje datotek PDF iz vsebine HTML. Ta rešitev je zelo uporabna za ustvarjanje poročil, računov ali katerega koli drugega dokumenta v formatu PDF. V tem članku bomo odkrili osnovne funkcije Dompdf in se naučili, kako ga uporabljati za ustvarjanje elegantnih in funkcionalnih PDF-jev. Predpogoji Preden namestite [&hellip;]"
date: "2024-03-09T12:43:25"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["racunalnistvo-in-podatki-sl", "tehnologija-in-digital-sl"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Uvod_v_Dompdf" >Uvod v Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Predpogoji" >Predpogoji</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Namestitev_Dompdf" >Namestitev Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Moj_prvi_dokument_PDF_z_Dompdf" >Moj prvi dokument PDF z Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Ustvarjanje_elegantnega_PDF-ja_v_PHP" >Ustvarjanje elegantnega PDF-ja v PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Drug_nacin_namestitve_in_uporabe_Dompdf" >Drug način namestitve in uporabe Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Ustvarjanje_PDF_iz_predloge_HTML" >Ustvarjanje PDF iz predloge HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Upravljanje_slik_in_pisav" >Upravljanje slik in pisav</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/sl/dompdf-kako-ustvariti-elegantne-pdf-je-v-php/#Optimizacija_upodabljanja_in_odpravljanje_tezav_z_Dompdf" >Optimizacija upodabljanja in odpravljanje težav z Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Uvod_v_Dompdf"></span>Uvod v Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf je knjižnica PHP, ki omogoča ustvarjanje datotek PDF iz vsebine HTML. Ta rešitev je zelo uporabna za ustvarjanje poročil, računov ali katerega koli drugega dokumenta v formatu PDF. V tem članku bomo odkrili osnovne funkcije Dompdf in se naučili, kako ga uporabljati za ustvarjanje elegantnih in funkcionalnih PDF-jev.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Predpogoji"></span>Predpogoji<span class="ez-toc-section-end"></span></h3>



<p>Preden namestite Dompdf, se prepričajte, da imate naslednje:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf zahteva PHP >= 5.4. Združljiv je z različicami PHP 7.x.</li>



<li><strong>PHP razširitve:</strong> Prepričajte se, da ste omogočili naslednje razširitve PHP: mbstring, DOM in GD. Te razširitve so bistvene za pravilno delovanje Dompdf.</li>



<li><strong>Sestavi:</strong> Dompdf se distribuira prek Composerja, ki je upravitelj odvisnosti za PHP. Prepričajte se, da imate v sistemu nameščen Composer.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Namestitev_Dompdf"></span>Namestitev Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Če želite namestiti Dompdf, sledite naslednjim korakom:</p>



<ol class="wp-block-list">
<li><strong>Ustvarite nov projekt PHP:</strong> Če še nimate obstoječega projekta, ustvarite novega z uporabo osnovne strukture po vaši izbiri.</li>



<li><strong>Dodajte odvisnost Dompdf prek Composerja:</strong> Odprite konzolo in se pomaknite do imenika vašega projekta. Zaženite naslednji ukaz, da dodate Dompdf v svoj projekt:     <pre><code>skladatelj zahteva dompdf/dompdf</code></pre>     Ta ukaz bo samodejno prenesel in namestil Dompdf skupaj z njegovimi odvisnostmi.</li>



<li><strong>Uporabite Dompdf v svoji aplikaciji:</strong> Zdaj lahko uporabite Dompdf v svojem projektu. Obstaja veliko načinov za ustvarjanje datotek PDF z Dompdf, vendar je tukaj osnovni primer za lažji začetek:
<pre><code>// Vključi samodejni nalagalnik Composer
zahtevaj 'vendor/autoload.php';

// Ustvari nov objekt Dompdf
$dompdf = nov Dompdf();

// Naloži vsebino HTML iz datoteke ali niza
$html = '<h1><span class="ez-toc-section" id="Moj_prvi_dokument_PDF_z_Dompdf"></span>Moj prvi dokument PDF z Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Upodobitev dokumenta PDF
$dompdf->render();

// Pošlji dokument PDF v izpis
$dompdf->stream('document.pdf');</code></pre>
    Ta primer ustvari nov dokument PDF z naslovom in ga naloži kot datoteko »document.pdf«. Vsebino HTML lahko prilagodite svojim potrebam.</li>
</ol>



<p>Zdaj, ko imate nameščen Dompdf, lahko začnete ustvarjati elegantne in funkcionalne datoteke PDF v svojih spletnih aplikacijah. Dompdf ponuja številne napredne funkcije za prilagajanje upodabljanja PDF, kot je upravljanje slik, pisav po meri in slogov CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Ustvarjanje_elegantnega_PDF-ja_v_PHP"></span>Ustvarjanje elegantnega PDF-ja v PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Drug_nacin_namestitve_in_uporabe_Dompdf"></span>Drug način namestitve in uporabe Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Sledite korakom:<br>1. Prenesite najnovejšo različico Dompdf z uradnega spletnega mesta.<br>2. Ekstrahirajte prenesene datoteke in jih postavite v vaš PHP projekt.<br>3. Vključite datoteko Dompdfautoload.php, da naložite knjižnico v svoj skript PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Ustvarjanje_PDF_iz_predloge_HTML"></span>Ustvarjanje PDF iz predloge HTML<span class="ez-toc-section-end"></span></h4>



<p>Zdaj, ko smo namestili Dompdf, bomo videli, kako ustvariti PDF s predlogo HTML. Sledite tem korakom:</p>



<p>1. Ustvarite datoteko HTML s strukturo in postavitvijo, ki jo želite za vaš PDF.<br>2. Uporabite funkcije CSS za oblikovanje vašega dokumenta z uporabo lastnosti, kot so družina pisav, velikost pisave, obroba itd.<br>3. Vključite dinamične podatke z uporabo oznak, specifičnih za Dompdf, na primer »{{name}}« ali »{{address}}«.<br>4. Uporabite razred Dompdf, da ustvarite PDF z uporabo predloge HTML, ki ste jo ustvarili.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Upravljanje_slik_in_pisav"></span>Upravljanje slik in pisav<span class="ez-toc-section-end"></span></h4>



<p>Pri ustvarjanju elegantnih PDF-jev je pogosto treba vključiti slike ali uporabiti posebne pisave. Evo, kako to storite z Dompdf:</p>



<p>1. Z oznako vključite slike v svojo predlogo HTML <img decoding="async" src="chemin_vers_image">.<br>2. Upoštevajte, da Dompdf privzeto ne vključuje vseh pisav. Pisave po meri lahko dodate z @font-face v svojem CSS ali s pisavami, ki jih ponuja Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimizacija_upodabljanja_in_odpravljanje_tezav_z_Dompdf"></span>Optimizacija upodabljanja in odpravljanje težav z Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Včasih lahko naletite na težave pri upodabljanju PDF-ja ali generiranju datotek. Tukaj je nekaj nasvetov za njihovo rešitev:</p>



<p>1. Preverite, ali je vaša predloga HTML pravilno sestavljena in veljavna.<br>2. Prepričajte se, da so vsi zunanji viri (slike, pisave itd.) dostopni s strežnika.<br>3. Odpravite kodo tako, da aktivirate način za odpravljanje napak Dompdf in preverite prikazane napake.<br>4. Glejte dokumentacijo Dompdf za več informacij o pogostih konfiguracijah in težavah.</p>



<p>Z uporabo Dompdf lahko zagotovite izboljšano uporabniško izkušnjo z dostavo profesionalnih in dobro oblikovanih dokumentov PDF. Ne glede na to, ali ustvarjate poročila, račune ali druge vrste dokumentov, je Dompdf zanesljiva in zmogljiva izbira.</p>



<p>Skratka, namestitev Dompdf je hitra in enostavna zahvaljujoč Composerju. Ko je nameščen, lahko začnete ustvarjati visokokakovostne datoteke PDF, ki ustrezajo potrebam vaše spletne aplikacije. Ne pozabite preveriti uradne dokumentacije Dompdf, če želite izvedeti več o njegovih funkcijah in razpoložljivih možnostih prilagajanja.</p>



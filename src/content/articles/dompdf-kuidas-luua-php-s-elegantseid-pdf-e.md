---
title: "Dompdf: kuidas luua PHP-s elegantseid PDF-e?"
slug: "dompdf-kuidas-luua-php-s-elegantseid-pdf-e"
excerpt: "Dompdf-i tutvustus Dompdf on PHP teek, mis võimaldab teil HTML-i sisust PDF-faile genereerida. See lahendus on väga kasulik aruannete, arvete või muude PDF-vormingus dokumentide koostamiseks. Selles artiklis avastame Dompdf-i põhifunktsioonid ja õpime seda kasutama elegantsete ja funktsionaalsete PDF-ide loomiseks. Eeldused Enne Dompdf-i installimist veenduge, et teil on järgmised asjad: Dompdf installimine Dompdf-i installimiseks toimige järgmiselt. [&hellip;]"
date: "2024-03-09T12:40:22"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["arvutustehnika-ja-andmed-et", "tehnoloogia-ja-digitaalne-et"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Dompdf-i_tutvustus" >Dompdf-i tutvustus</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Eeldused" >Eeldused</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Dompdf_installimine" >Dompdf installimine</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Minu_esimene_PDF-dokument_Dompdf-iga" >Minu esimene PDF-dokument Dompdf-iga</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Elegantse_PDF-i_loomine_PHP-s" >Elegantse PDF-i loomine PHP-s</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Teine_meetod_Dompdf-i_installimiseks_ja_kasutamiseks" >Teine meetod Dompdf-i installimiseks ja kasutamiseks</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#PDF-i_loomine_HTML-mallist" >PDF-i loomine HTML-mallist</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Piltide_ja_fontide_haldamine" >Piltide ja fontide haldamine</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/et/dompdf-kuidas-luua-php-s-elegantseid-pdf-e/#Renderduse_optimeerimine_ja_Dompdf-i_probleemide_lahendamine" >Renderduse optimeerimine ja Dompdf-i probleemide lahendamine</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf-i_tutvustus"></span>Dompdf-i tutvustus<span class="ez-toc-section-end"></span></h2>



<p>Dompdf on PHP teek, mis võimaldab teil HTML-i sisust PDF-faile genereerida. See lahendus on väga kasulik aruannete, arvete või muude PDF-vormingus dokumentide koostamiseks. Selles artiklis avastame Dompdf-i põhifunktsioonid ja õpime seda kasutama elegantsete ja funktsionaalsete PDF-ide loomiseks.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Eeldused"></span>Eeldused<span class="ez-toc-section-end"></span></h3>



<p>Enne Dompdf-i installimist veenduge, et teil on järgmised asjad:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf nõuab PHP >= 5.4. See ühildub PHP versiooniga 7.x.</li>



<li><strong>PHP laiendused:</strong> Veenduge, et oleksite lubanud järgmised PHP laiendused: mbstring, DOM ja GD. Need laiendused on Dompdf-i nõuetekohaseks toimimiseks hädavajalikud.</li>



<li><strong>Koosta:</strong> Dompdf-i levitatakse Composeri kaudu, mis on PHP sõltuvushaldur. Veenduge, et teie süsteemi oleks installitud Composer.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_installimine"></span>Dompdf installimine<span class="ez-toc-section-end"></span></h4>



<p>Dompdf-i installimiseks toimige järgmiselt.</p>



<ol class="wp-block-list">
<li><strong>Looge uus PHP projekt:</strong> Kui teil pole veel olemasolevat projekti, looge uus, kasutades teie valitud põhistruktuuri.</li>



<li><strong>Lisage Dompdf-i sõltuvus Composeri kaudu:</strong> Avage konsool ja liikuge oma projektikataloogi. Dompdf-i lisamiseks oma projekti käivitage järgmine käsk:     <pre><code>helilooja nõuab dompdf/dompdf</code></pre>     See käsk laadib automaatselt alla ja installib Dompdf-i koos selle sõltuvustega.</li>



<li><strong>Kasutage oma rakenduses Dompdf-i:</strong> Nüüd saate oma projektis kasutada Dompdf-i. PDF-failide loomiseks Dompdf-iga on palju võimalusi, kuid siin on alustuseks üks põhinäide:
<pre><code>// Kaasake helilooja automaatlaadur
nõuavad 'vendor/autoload.php';

// Looge uus Dompdf-objekt
$dompdf = uus Dompdf();

// HTML-i sisu laadimine failist või stringist
$html = '<h1><span class="ez-toc-section" id="Minu_esimene_PDF-dokument_Dompdf-iga"></span>Minu esimene PDF-dokument Dompdf-iga<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Renderdage PDF-dokument
$dompdf->render();

// Saada PDF-dokument väljundisse
$dompdf->stream('dokument.pdf');</code></pre>
    See näide loob uue pealkirjaga PDF-dokumendi ja laadib selle üles failina &#8220;document.pdf&#8221;. Saate kohandada HTML-i sisu vastavalt oma vajadustele.</li>
</ol>



<p>Nüüd, kui olete installinud Dompdf-i, saate hakata oma veebirakendustes elegantseid ja funktsionaalseid PDF-faile genereerima. Dompdf pakub palju täiustatud funktsioone PDF-i renderdamise kohandamiseks, näiteks piltide, kohandatud fontide ja CSS-stiilide haldamiseks.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Elegantse_PDF-i_loomine_PHP-s"></span>Elegantse PDF-i loomine PHP-s<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Teine_meetod_Dompdf-i_installimiseks_ja_kasutamiseks"></span>Teine meetod Dompdf-i installimiseks ja kasutamiseks<span class="ez-toc-section-end"></span></h3>



<p>Siin on järgmised sammud.<br>1. Laadige ametlikult veebisaidilt alla Dompdf-i uusim versioon.<br>2. Pakkige allalaaditud failid lahti ja asetage need oma PHP projekti.<br>3. Kaasake fail Dompdfautoload.php, et laadida teegi oma PHP-skripti.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="PDF-i_loomine_HTML-mallist"></span>PDF-i loomine HTML-mallist<span class="ez-toc-section-end"></span></h4>



<p>Nüüd, kui oleme Dompdf-i installinud, näeme, kuidas luua PDF-i HTML-malli abil. Järgige neid samme.</p>



<p>1. Looge HTML-fail, mis sisaldab teie PDF-i soovitud struktuuri ja paigutust.<br>2. Kasutage oma dokumendi stiili kujundamiseks CSS-i funktsioone, kasutades atribuute nagu fondiperekond, fondi suurus, ääris jne.<br>3. Kaasake dünaamilised andmed, kasutades Dompdf-spetsiifilisi märgendeid, nagu &#8220;{{name}}&#8221; või &#8220;{{address}}&#8221;.<br>4. Kasutage Dompdf-klassi, et luua PDF, kasutades enda loodud HTML-malli.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Piltide_ja_fontide_haldamine"></span>Piltide ja fontide haldamine<span class="ez-toc-section-end"></span></h4>



<p>Stiilsete PDF-ide loomisel on sageli vaja lisada pilte või kasutada kindlaid fonte. Dompdf-iga saate seda teha järgmiselt:</p>



<p>1. Lisage sildi abil pildid oma HTML-malli <img decoding="async" src="chemin_vers_image">.<br>2. Pange tähele, et Dompdf ei sisalda vaikimisi kõiki fonte. Saate lisada kohandatud fonte, kasutades oma CSS-is @font-face või kasutades Dompdf-i pakutavaid fonte.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Renderduse_optimeerimine_ja_Dompdf-i_probleemide_lahendamine"></span>Renderduse optimeerimine ja Dompdf-i probleemide lahendamine<span class="ez-toc-section-end"></span></h4>



<p>Mõnikord võib PDF-i renderdamisel või failide genereerimisel tekkida probleeme. Siin on mõned näpunäited nende lahendamiseks:</p>



<p>1. Kontrollige, kas teie HTML-mall on õigesti koostatud ja kehtiv.<br>2. Veenduge, et kõik välised ressursid (pildid, fondid jne) on serverist juurdepääsetavad.<br>3. Siluge oma kood, aktiveerides Dompdf-i silumisrežiimi ja kontrollides kuvatavaid vigu.<br>4. Levinud konfiguratsioonide ja probleemide kohta lisateabe saamiseks vaadake Dompdfi dokumentatsiooni.</p>



<p>Dompdf-i abil saate pakkuda täiustatud kasutuskogemust, pakkudes professionaalseid ja hästi vormindatud PDF-dokumente. Ükskõik, kas koostate aruandeid, arveid või muud tüüpi dokumente, on Dompdf usaldusväärne ja võimas valik.</p>



<p>Kokkuvõtteks võib öelda, et tänu Composerile on Dompdf-i installimine kiire ja lihtne. Pärast installimist saate hakata looma kvaliteetseid PDF-faile, mis vastavad teie veebirakenduste vajadustele. Ärge unustage tutvuda ametliku Dompdf-i dokumentatsiooniga, et saada lisateavet selle funktsioonide ja saadaolevate kohandamisvõimaluste kohta.</p>



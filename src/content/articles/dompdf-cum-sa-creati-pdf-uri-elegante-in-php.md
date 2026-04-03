---
title: "Dompdf: Cum să creați PDF-uri elegante în PHP?"
slug: "dompdf-cum-sa-creati-pdf-uri-elegante-in-php"
excerpt: "Introducere în Dompdf Dompdf este o bibliotecă PHP care vă permite să generați fișiere PDF din conținut HTML. Aceasta solutie este foarte utila pentru generarea de rapoarte, facturi sau orice alt document in format PDF. În acest articol, vom descoperi caracteristicile de bază ale Dompdf și vom învăța cum să-l folosim pentru a crea PDF-uri [&hellip;]"
date: "2024-03-09T12:43:06"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["calculatoare-si-date-ro", "tehnologie-si-digital-ro"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Introducere_in_Dompdf" >Introducere în Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Cerinte_preliminare" >Cerințe preliminare</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Instalare_Dompdf" >Instalare Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Primul_meu_document_PDF_cu_Dompdf" >Primul meu document PDF cu Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Crearea_unui_PDF_elegant_in_PHP" >Crearea unui PDF elegant în PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#O_alta_metoda_de_instalare_si_utilizare_a_Dompdf" >O altă metodă de instalare și utilizare a Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Crearea_unui_PDF_dintr-un_sablon_HTML" >Crearea unui PDF dintr-un șablon HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Gestionarea_imaginilor_si_a_fonturilor" >Gestionarea imaginilor și a fonturilor</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ro/dompdf-cum-sa-creati-pdf-uri-elegante-in-php/#Optimizarea_redarii_si_remedierea_problemelor_Dompdf" >Optimizarea redării și remedierea problemelor Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introducere_in_Dompdf"></span>Introducere în Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf este o bibliotecă PHP care vă permite să generați fișiere PDF din conținut HTML. Aceasta solutie este foarte utila pentru generarea de rapoarte, facturi sau orice alt document in format PDF. În acest articol, vom descoperi caracteristicile de bază ale Dompdf și vom învăța cum să-l folosim pentru a crea PDF-uri elegante și funcționale.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Cerinte_preliminare"></span>Cerințe preliminare<span class="ez-toc-section-end"></span></h3>



<p>Înainte de a instala Dompdf, asigurați-vă că aveți următoarele:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf necesită PHP >= 5.4. Este compatibil cu versiunile 7.x ale PHP.</li>



<li><strong>Extensii PHP:</strong> Asigurați-vă că ați activat următoarele extensii PHP: mbstring, DOM și GD. Aceste extensii sunt esențiale pentru buna funcționare a Dompdf.</li>



<li><strong>Compune :</strong> Dompdf este distribuit prin Composer, care este un manager de dependențe pentru PHP. Asigurați-vă că aveți Composer instalat pe sistemul dvs.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Instalare_Dompdf"></span>Instalare Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Pentru a instala Dompdf, urmați următorii pași:</p>



<ol class="wp-block-list">
<li><strong>Creați un nou proiect PHP:</strong> Dacă nu aveți deja un proiect existent, creați unul nou folosind structura de bază la alegere.</li>



<li><strong>Adăugați dependența Dompdf prin Composer:</strong> Deschideți o consolă și navigați la directorul proiectului dvs. Rulați următoarea comandă pentru a adăuga Dompdf la proiectul dvs.:     <pre><code>compozitorul necesită dompdf/dompdf</code></pre>     Această comandă va descărca și instala automat Dompdf împreună cu dependențele sale.</li>



<li><strong>Utilizați Dompdf în aplicația dvs.:</strong> Acum puteți utiliza Dompdf în proiectul dvs. Există multe modalități de a crea fișiere PDF cu Dompdf, dar iată un exemplu de bază pentru a începe:
<pre><code>// Includeți încărcătorul automat Composer
necesită „vendor/autoload.php”;

// Creați un nou obiect Dompdf
$dompdf = nou Dompdf();

// Încarcă conținut HTML dintr-un fișier sau șir
$html = '<h1><span class="ez-toc-section" id="Primul_meu_document_PDF_cu_Dompdf"></span>Primul meu document PDF cu Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Redați documentul PDF
$dompdf->render();

// Trimiteți documentul PDF la ieșire
$dompdf->stream('document.pdf');</code></pre>
    Acest exemplu creează un nou document PDF cu un titlu și îl încarcă ca fișier „document.pdf”. Puteți personaliza conținutul HTML în funcție de nevoile dvs.</li>
</ol>



<p>Acum că aveți Dompdf instalat, puteți începe să generați fișiere PDF elegante și funcționale în aplicațiile dvs. web. Dompdf oferă multe funcții avansate pentru personalizarea redării PDF, cum ar fi gestionarea imaginilor, fonturilor personalizate și stilurilor CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Crearea_unui_PDF_elegant_in_PHP"></span>Crearea unui PDF elegant în PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="O_alta_metoda_de_instalare_si_utilizare_a_Dompdf"></span>O altă metodă de instalare și utilizare a Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Iată pașii de urmat:<br>1. Descărcați cea mai recentă versiune a Dompdf de pe site-ul oficial.<br>2. Extrageți fișierele descărcate și plasați-le în proiectul dvs. PHP.<br>3. Includeți fișierul Dompdfautoload.php pentru a încărca biblioteca în scriptul dumneavoastră PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Crearea_unui_PDF_dintr-un_sablon_HTML"></span>Crearea unui PDF dintr-un șablon HTML<span class="ez-toc-section-end"></span></h4>



<p>Acum că am instalat Dompdf, vom vedea cum să creăm un PDF folosind un șablon HTML. Urmați acești pași:</p>



<p>1. Creați un fișier HTML care conține structura și aspectul dorit pentru PDF-ul dvs.<br>2. Utilizați funcțiile CSS pentru a vă stila documentul, folosind proprietăți precum font-family, font-size, chenar etc.<br>3. Includeți date dinamice folosind etichete specifice Dompdf, cum ar fi „{{name}}” sau „{{address}}”.<br>4. Utilizați clasa Dompdf pentru a genera PDF-ul folosind șablonul HTML pe care l-ați creat.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gestionarea_imaginilor_si_a_fonturilor"></span>Gestionarea imaginilor și a fonturilor<span class="ez-toc-section-end"></span></h4>



<p>Când creați PDF-uri elegante, este adesea necesar să includeți imagini sau să utilizați fonturi specifice. Iată cum să o faci cu Dompdf:</p>



<p>1. Includeți imagini în șablonul HTML folosind eticheta <img decoding="async" src="chemin_vers_image">.<br>2. Vă rugăm să rețineți că Dompdf nu include toate fonturile în mod implicit. Puteți adăuga fonturi personalizate folosind @font-face în CSS sau folosind fonturi furnizate de Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimizarea_redarii_si_remedierea_problemelor_Dompdf"></span>Optimizarea redării și remedierea problemelor Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Uneori este posibil să întâmpinați probleme cu redarea PDF-ului sau generarea fișierelor. Iată câteva sfaturi pentru a le rezolva:</p>



<p>1. Verificați dacă șablonul dvs. HTML este corect construit și valid.<br>2. Asigurați-vă că toate resursele externe (imagini, fonturi etc.) sunt accesibile de pe server.<br>3. Depanați codul activând modul de depanare Dompdf și verificând erorile afișate.<br>4. Consultați documentația Dompdf pentru mai multe informații despre configurațiile și problemele comune.</p>



<p>Folosind Dompdf, puteți oferi o experiență de utilizator îmbunătățită prin furnizarea de documente PDF profesionale și bine formatate. Fie că generează rapoarte, facturi sau alte tipuri de documente, Dompdf este o alegere de încredere și puternică.</p>



<p>În concluzie, instalarea Dompdf este rapidă și ușoară datorită Composer. Odată instalat, puteți începe să creați fișiere PDF de înaltă calitate pentru a satisface nevoile aplicației dvs. web. Nu uitați să consultați documentația oficială Dompdf pentru a afla mai multe despre caracteristicile sale și despre opțiunile de personalizare disponibile.</p>



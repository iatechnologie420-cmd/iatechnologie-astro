---
title: "Dompdf: Hvordan lage elegante PDF-filer i PHP?"
slug: "dompdf-hvordan-lage-elegante-pdf-filer-i-php"
excerpt: "Introduksjon til Dompdf Dompdf er et PHP-bibliotek som lar deg generere PDF-filer fra HTML-innhold. Denne løsningen er svært nyttig for å generere rapporter, fakturaer eller andre dokumenter i PDF-format. I denne artikkelen vil vi oppdage de grunnleggende funksjonene til Dompdf og lære hvordan du bruker den til å lage elegante og funksjonelle PDF-er. Forutsetninger Før [&hellip;]"
date: "2024-03-09T12:42:16"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["databehandling-og-data-nb", "teknologi-og-digitalt-nb"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Introduksjon_til_Dompdf" >Introduksjon til Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Forutsetninger" >Forutsetninger</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Dompdf_installasjon" >Dompdf installasjon</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Mitt_forste_PDF-dokument_med_Dompdf" >Mitt første PDF-dokument med Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Opprette_en_elegant_PDF_i_PHP" >Opprette en elegant PDF i PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#En_annen_metode_for_a_installere_og_bruke_Dompdf" >En annen metode for å installere og bruke Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Opprette_en_PDF_fra_en_HTML-mal" >Opprette en PDF fra en HTML-mal</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Administrere_bilder_og_fonter" >Administrere bilder og fonter</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/nb/dompdf-hvordan-lage-elegante-pdf-filer-i-php/#Optimalisere_gjengivelse_og_fikse_Dompdf-problemer" >Optimalisere gjengivelse og fikse Dompdf-problemer</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introduksjon_til_Dompdf"></span>Introduksjon til Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf er et PHP-bibliotek som lar deg generere PDF-filer fra HTML-innhold. Denne løsningen er svært nyttig for å generere rapporter, fakturaer eller andre dokumenter i PDF-format. I denne artikkelen vil vi oppdage de grunnleggende funksjonene til Dompdf og lære hvordan du bruker den til å lage elegante og funksjonelle PDF-er.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Forutsetninger"></span>Forutsetninger<span class="ez-toc-section-end"></span></h3>



<p>Før du installerer Dompdf, sørg for at du har følgende:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf krever PHP >= 5.4. Den er kompatibel med versjon 7.x av PHP.</li>



<li><strong>PHP-utvidelser:</strong> Sørg for at du har aktivert følgende PHP-utvidelser: mbstring, DOM og GD. Disse utvidelsene er avgjørende for riktig funksjon av Dompdf.</li>



<li><strong>Skriv:</strong> Dompdf distribueres via Composer, som er en avhengighetsbehandler for PHP. Sørg for at du har Composer installert på systemet ditt.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_installasjon"></span>Dompdf installasjon<span class="ez-toc-section-end"></span></h4>



<p>Følg disse trinnene for å installere Dompdf:</p>



<ol class="wp-block-list">
<li><strong>Opprett et nytt PHP-prosjekt:</strong> Hvis du ikke allerede har et eksisterende prosjekt, lag et nytt ved å bruke den grunnleggende strukturen du velger.</li>



<li><strong>Legg til Dompdf-avhengigheten via Composer:</strong> Åpne en konsoll og naviger til prosjektkatalogen din. Kjør følgende kommando for å legge til Dompdf til prosjektet ditt:     <pre><code>komponist krever dompdf/dompdf</code></pre>     Denne kommandoen vil automatisk laste ned og installere Dompdf sammen med dens avhengigheter.</li>



<li><strong>Bruk Dompdf i applikasjonen din:</strong> Du kan nå bruke Dompdf i prosjektet ditt. Det er mange måter å lage PDF-filer på med Dompdf, men her er et grunnleggende eksempel for å komme i gang:
<pre><code>// Inkluder Composer autoloader
krever 'leverandør/autoload.php';

// Lag et nytt Dompdf-objekt
$dompdf = ny Dompdf();

// Last inn HTML-innhold fra en fil eller streng
$html = '<h1><span class="ez-toc-section" id="Mitt_forste_PDF-dokument_med_Dompdf"></span>Mitt første PDF-dokument med Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Gjengi PDF-dokumentet
$dompdf->render();

// Send PDF-dokument til utdata
$dompdf->stream('document.pdf');</code></pre>
    Dette eksemplet oppretter et nytt PDF-dokument med en tittel og laster det opp som en &#8220;document.pdf&#8221;-fil. Du kan tilpasse HTML-innholdet etter dine behov.</li>
</ol>



<p>Nå som du har installert Dompdf, kan du begynne å generere elegante og funksjonelle PDF-filer i nettapplikasjonene dine. Dompdf tilbyr mange avanserte funksjoner for å tilpasse PDF-gjengivelse, for eksempel administrasjon av bilder, egendefinerte fonter og CSS-stiler.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Opprette_en_elegant_PDF_i_PHP"></span>Opprette en elegant PDF i PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="En_annen_metode_for_a_installere_og_bruke_Dompdf"></span>En annen metode for å installere og bruke Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Her er trinnene du må følge:<br>1. Last ned den nyeste versjonen av Dompdf fra den offisielle nettsiden.<br>2. Pakk ut de nedlastede filene og plasser dem i PHP-prosjektet.<br>3. Inkluder Dompdfautoload.php-filen for å laste biblioteket inn i PHP-skriptet.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Opprette_en_PDF_fra_en_HTML-mal"></span>Opprette en PDF fra en HTML-mal<span class="ez-toc-section-end"></span></h4>



<p>Nå som vi har installert Dompdf, vil vi se hvordan du lager en PDF ved hjelp av en HTML-mal. Følg disse instruksjonene:</p>



<p>1. Lag en HTML-fil som inneholder strukturen og layouten du ønsker for PDF-en.<br>2. Bruk CSS-funksjoner til å style dokumentet ditt, ved å bruke egenskaper som font-familie, font-size, border, etc.<br>3. Inkluder dynamiske data ved å bruke Dompdf-spesifikke tagger, for eksempel «{{navn}}» eller «{{address}}».<br>4. Bruk Dompdf-klassen til å generere PDF-en ved å bruke HTML-malen du opprettet.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Administrere_bilder_og_fonter"></span>Administrere bilder og fonter<span class="ez-toc-section-end"></span></h4>



<p>Når du lager elegante PDF-er, er det ofte nødvendig å inkludere bilder eller bruke bestemte fonter. Slik gjør du det med Dompdf:</p>



<p>1. Inkluder bilder i HTML-malen ved hjelp av taggen <img decoding="async" src="chemin_vers_image">.<br>2. Vær oppmerksom på at Dompdf ikke inkluderer alle fonter som standard. Du kan legge til egendefinerte skrifter ved å bruke @font-face i CSS-en din eller ved å bruke fonter levert av Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimalisere_gjengivelse_og_fikse_Dompdf-problemer"></span>Optimalisere gjengivelse og fikse Dompdf-problemer<span class="ez-toc-section-end"></span></h4>



<p>Noen ganger kan du støte på problemer med å gjengi PDF-en eller generere filene. Her er noen tips for å løse dem:</p>



<p>1. Sjekk at HTML-malen er riktig konstruert og gyldig.<br>2. Sørg for at alle eksterne ressurser (bilder, fonter osv.) er tilgjengelige fra serveren.<br>3. Feilsøk koden din ved å aktivere Dompdf feilsøkingsmodus og sjekke de viste feilene.<br>4. Se Dompdf-dokumentasjonen for mer informasjon om vanlige konfigurasjoner og problemer.</p>



<p>Ved å bruke Dompdf kan du gi en forbedret brukeropplevelse ved å levere profesjonelle og godt formaterte PDF-dokumenter. Enten du genererer rapporter, fakturaer eller andre typer dokumenter, er Dompdf et pålitelig og kraftig valg.</p>



<p>Avslutningsvis er det raskt og enkelt å installere Dompdf takket være Composer. Når den er installert, kan du begynne å lage PDF-filer av høy kvalitet for å møte behovene dine for nettapplikasjoner. Ikke glem å sjekke ut den offisielle Dompdf-dokumentasjonen for å lære mer om funksjonene og tilgjengelige tilpasningsalternativer.</p>



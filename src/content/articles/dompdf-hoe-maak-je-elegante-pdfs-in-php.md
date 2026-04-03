---

title: "Dompdf: Hoe maak je elegante PDF&#8217;s in PHP?"
slug: "dompdf-hoe-maak-je-elegante-pdfs-in-php"
excerpt: "Inleiding tot Dompdf Dompdf is een PHP-bibliotheek waarmee u PDF-bestanden kunt genereren op basis van HTML-inhoud. Deze oplossing is erg handig voor het genereren van rapporten, facturen of elk ander document in PDF-formaat. In dit artikel ontdekken we de basisfuncties van Dompdf en leren we hoe we deze kunnen gebruiken om elegante en functionele PDF&#8217;s [&hellip;]"
date: "2024-03-09T12:42:25"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["computers-en-gegevens-nl", "technologie-en-digitaal-nl"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Inleiding_tot_Dompdf" >Inleiding tot Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Vereisten" >Vereisten</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Dompdf-installatie" >Dompdf-installatie</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Mijn_eerste_PDF-document_met_Dompdf" >Mijn eerste PDF-document met Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Een_elegante_PDF_maken_in_PHP" >Een elegante PDF maken in PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Een_andere_methode_om_Dompdf_te_installeren_en_te_gebruiken" >Een andere methode om Dompdf te installeren en te gebruiken</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Een_PDF_maken_van_een_HTML-sjabloon" >Een PDF maken van een HTML-sjabloon</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Afbeeldingen_en_lettertypen_beheren" >Afbeeldingen en lettertypen beheren</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/nl/dompdf-hoe-maak-je-elegante-pdfs-in-php/#Weergave_optimaliseren_en_Dompdf-problemen_oplossen" >Weergave optimaliseren en Dompdf-problemen oplossen</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Inleiding_tot_Dompdf"></span>Inleiding tot Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf is een PHP-bibliotheek waarmee u PDF-bestanden kunt genereren op basis van HTML-inhoud. Deze oplossing is erg handig voor het genereren van rapporten, facturen of elk ander document in PDF-formaat. In dit artikel ontdekken we de basisfuncties van Dompdf en leren we hoe we deze kunnen gebruiken om elegante en functionele PDF&#8217;s te maken.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Vereisten"></span>Vereisten<span class="ez-toc-section-end"></span></h3>



<p>Zorg ervoor dat u over het volgende beschikt voordat u Dompdf installeert:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf vereist PHP >= 5.4. Het is compatibel met versie 7.x van PHP.</li>



<li><strong>PHP-extensies:</strong> Zorg ervoor dat je de volgende PHP-extensies hebt ingeschakeld: mbstring, DOM en GD. Deze extensies zijn essentieel voor het goed functioneren van Dompdf.</li>



<li><strong>Samenstellen:</strong> Dompdf wordt gedistribueerd via Composer, een afhankelijkheidsmanager voor PHP. Zorg ervoor dat Composer op uw systeem is geïnstalleerd.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf-installatie"></span>Dompdf-installatie<span class="ez-toc-section-end"></span></h4>



<p>Om Dompdf te installeren, volgt u de volgende stappen:</p>



<ol class="wp-block-list">
<li><strong>Maak een nieuw PHP-project:</strong> Als u nog geen bestaand project heeft, maak dan een nieuw project met de basisstructuur van uw keuze.</li>



<li><strong>Voeg de Dompdf-afhankelijkheid toe via Composer:</strong> Open een console en navigeer naar uw projectmap. Voer de volgende opdracht uit om Dompdf aan uw project toe te voegen:     <pre><code>componist vereist dompdf/dompdf</code></pre>     Met deze opdracht wordt Dompdf automatisch gedownload en geïnstalleerd, samen met de afhankelijkheden ervan.</li>



<li><strong>Gebruik Dompdf in uw toepassing:</strong> U kunt Dompdf nu in uw project gebruiken. Er zijn veel manieren om PDF-bestanden te maken met Dompdf, maar hier is een eenvoudig voorbeeld om u op weg te helpen:
<pre><code>// Voeg de Composer-autoloader toe
vereist 'vendor/autoload.php';

// Maak een nieuw Dompdf-object
$dompdf = nieuwe Dompdf();

// Laad HTML-inhoud uit een bestand of tekenreeks
$html = '<h1><span class="ez-toc-section" id="Mijn_eerste_PDF-document_met_Dompdf"></span>Mijn eerste PDF-document met Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Render het PDF-document
$dompdf->render();

// Stuur een PDF-document naar de uitvoer
$dompdf->stream('document.pdf');</code></pre>
    In dit voorbeeld wordt een nieuw PDF-document met een titel gemaakt en dit geüpload als een &#8220;document.pdf&#8221;-bestand. U kunt de HTML-inhoud aanpassen aan uw behoeften.</li>
</ol>



<p>Nu Dompdf is geïnstalleerd, kunt u beginnen met het genereren van elegante en functionele PDF-bestanden in uw webapplicaties. Dompdf biedt veel geavanceerde functies voor het aanpassen van PDF-weergave, zoals het beheren van afbeeldingen, aangepaste lettertypen en CSS-stijlen.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Een_elegante_PDF_maken_in_PHP"></span>Een elegante PDF maken in PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Een_andere_methode_om_Dompdf_te_installeren_en_te_gebruiken"></span>Een andere methode om Dompdf te installeren en te gebruiken<span class="ez-toc-section-end"></span></h3>



<p>Hier zijn de stappen die u moet volgen:<br>1. Download de nieuwste versie van Dompdf van de officiële website.<br>2. Pak de gedownloade bestanden uit en plaats ze in uw PHP-project.<br>3. Voeg het bestand Dompdfautoload.php toe om de bibliotheek in uw PHP-script te laden.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Een_PDF_maken_van_een_HTML-sjabloon"></span>Een PDF maken van een HTML-sjabloon<span class="ez-toc-section-end"></span></h4>



<p>Nu we Dompdf hebben geïnstalleerd, zullen we zien hoe we een PDF kunnen maken met behulp van een HTML-sjabloon. Volg deze stappen:</p>



<p>1. Maak een HTML-bestand met de gewenste structuur en lay-out voor uw PDF.<br>2. Gebruik CSS-functies om uw document op te maken, met behulp van eigenschappen zoals lettertypefamilie, lettergrootte, rand, enz.<br>3. Voeg dynamische gegevens toe met behulp van Dompdf-specifieke tags, zoals &#8220;{{name}}&#8221; of &#8220;{{address}}&#8221;.<br>4. Gebruik de klasse Dompdf om de PDF te genereren met behulp van de HTML-sjabloon die u hebt gemaakt.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Afbeeldingen_en_lettertypen_beheren"></span>Afbeeldingen en lettertypen beheren<span class="ez-toc-section-end"></span></h4>



<p>Bij het maken van elegante PDF&#8217;s is het vaak nodig om afbeeldingen toe te voegen of specifieke lettertypen te gebruiken. Zo doet u het met Dompdf:</p>



<p>1. Voeg afbeeldingen toe aan uw HTML-sjabloon met behulp van de tag <img decoding="async" src="chemin_vers_image">.<br>2. Houd er rekening mee dat Dompdf niet standaard alle lettertypen bevat. U kunt aangepaste lettertypen toevoegen met @font-face in uw CSS of met lettertypen van Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Weergave_optimaliseren_en_Dompdf-problemen_oplossen"></span>Weergave optimaliseren en Dompdf-problemen oplossen<span class="ez-toc-section-end"></span></h4>



<p>Soms kunt u problemen ondervinden bij het weergeven van uw PDF of het genereren van de bestanden. Hier zijn enkele tips om ze op te lossen:</p>



<p>1. Controleer of uw HTML-sjabloon correct is opgebouwd en geldig is.<br>2. Zorg ervoor dat alle externe bronnen (afbeeldingen, lettertypen, enz.) toegankelijk zijn vanaf de server.<br>3. Debug uw code door de Dompdf-foutopsporingsmodus te activeren en de weergegeven fouten te controleren.<br>4. Zie de Dompdf-documentatie voor meer informatie over veelvoorkomende configuraties en problemen.</p>



<p>Met Dompdf kunt u een verbeterde gebruikerservaring bieden door professionele en goed opgemaakte PDF-documenten te leveren. Of het nu gaat om het genereren van rapporten, facturen of andere soorten documenten, Dompdf is een betrouwbare en krachtige keuze.</p>



<p>Kortom, het installeren van Dompdf is snel en eenvoudig dankzij Composer. Eenmaal geïnstalleerd, kunt u beginnen met het maken van PDF-bestanden van hoge kwaliteit om aan de behoeften van uw webapplicatie te voldoen. Vergeet niet de officiële Dompdf-documentatie te raadplegen voor meer informatie over de functies en beschikbare aanpassingsopties.</p>



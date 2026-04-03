---
title: "Dompdf: come creare PDF eleganti in PHP?"
slug: "dompdf-come-creare-pdf-eleganti-in-php"
excerpt: "Introduzione a Dompdf Dompdf è una libreria PHP che ti consente di generare file PDF da contenuti HTML. Questa soluzione è molto utile per generare report, fatture o qualsiasi altro documento in formato PDF. In questo articolo scopriremo le funzionalità base di Dompdf e impareremo come utilizzarlo per creare PDF eleganti e funzionali. Prerequisiti Prima [&hellip;]"
date: "2024-03-09T12:40:52"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["informatica-e-dati-it", "tecnologia-e-digitale-it"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Introduzione_a_Dompdf" >Introduzione a Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Prerequisiti" >Prerequisiti</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Installazione_di_Dompdf" >Installazione di Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Il_mio_primo_documento_PDF_con_Dompdf" >Il mio primo documento PDF con Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Creazione_di_un_PDF_elegante_in_PHP" >Creazione di un PDF elegante in PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Un_altro_metodo_per_installare_e_utilizzare_Dompdf" >Un altro metodo per installare e utilizzare Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Creazione_di_un_PDF_da_un_modello_HTML" >Creazione di un PDF da un modello HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Gestire_immagini_e_caratteri" >Gestire immagini e caratteri</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/it/dompdf-come-creare-pdf-eleganti-in-php/#Ottimizzazione_del_rendering_e_risoluzione_dei_problemi_di_Dompdf" >Ottimizzazione del rendering e risoluzione dei problemi di Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introduzione_a_Dompdf"></span>Introduzione a Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf è una libreria PHP che ti consente di generare file PDF da contenuti HTML. Questa soluzione è molto utile per generare report, fatture o qualsiasi altro documento in formato PDF. In questo articolo scopriremo le funzionalità base di Dompdf e impareremo come utilizzarlo per creare PDF eleganti e funzionali.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Prerequisiti"></span>Prerequisiti<span class="ez-toc-section-end"></span></h3>



<p>Prima di installare Dompdf, assicurati di avere quanto segue:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf richiede PHP >= 5.4. È compatibile con le versioni 7.x di PHP.</li>



<li><strong>Estensioni PHP:</strong> Assicurati di aver abilitato le seguenti estensioni PHP: mbstring, DOM e GD. Queste estensioni sono essenziali per il corretto funzionamento di Dompdf.</li>



<li><strong>Componi:</strong> Dompdf è distribuito tramite Composer, che è un gestore delle dipendenze per PHP. Assicurati di avere Composer installato sul tuo sistema.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Installazione_di_Dompdf"></span>Installazione di Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Per installare Dompdf, seguire i seguenti passi:</p>



<ol class="wp-block-list">
<li><strong>Crea un nuovo progetto PHP:</strong> Se non hai già un progetto esistente, creane uno nuovo utilizzando la struttura di base di tua scelta.</li>



<li><strong>Aggiungi la dipendenza Dompdf tramite Composer:</strong> Apri una console e vai alla directory del tuo progetto. Esegui il comando seguente per aggiungere Dompdf al tuo progetto:     <pre><code>il compositore richiede dompdf/dompdf</code></pre>     Questo comando scaricherà e installerà automaticamente Dompdf insieme alle sue dipendenze.</li>



<li><strong>Utilizza Dompdf nella tua applicazione:</strong> Ora puoi utilizzare Dompdf nel tuo progetto. Esistono molti modi per creare file PDF con Dompdf, ma ecco un esempio di base per iniziare:
<pre><code>// Include il caricatore automatico Composer
richiedere 'venditore/autoload.php';

// Crea un nuovo oggetto Dompdf
$dompdf = nuovo Dompdf();

// Carica contenuto HTML da un file o una stringa
$html = '<h1><span class="ez-toc-section" id="Il_mio_primo_documento_PDF_con_Dompdf"></span>Il mio primo documento PDF con Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Visualizza il documento PDF
$dompdf->render();

// Invia il documento PDF all'output
$dompdf->stream('document.pdf');</code></pre>
    Questo esempio crea un nuovo documento PDF con un titolo e lo carica come file &#8220;document.pdf&#8221;. Puoi personalizzare il contenuto HTML in base alle tue esigenze.</li>
</ol>



<p>Ora che hai installato Dompdf, puoi iniziare a generare file PDF eleganti e funzionali nelle tue applicazioni web. Dompdf offre molte funzionalità avanzate per personalizzare il rendering dei PDF, come la gestione di immagini, caratteri personalizzati e stili CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Creazione_di_un_PDF_elegante_in_PHP"></span>Creazione di un PDF elegante in PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Un_altro_metodo_per_installare_e_utilizzare_Dompdf"></span>Un altro metodo per installare e utilizzare Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Ecco i passaggi da seguire:<br>1. Scarica l&#8217;ultima versione di Dompdf dal sito ufficiale.<br>2. Estrai i file scaricati e inseriscili nel tuo progetto PHP.<br>3. Includi il file Dompdfautoload.php per caricare la libreria nel tuo script PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Creazione_di_un_PDF_da_un_modello_HTML"></span>Creazione di un PDF da un modello HTML<span class="ez-toc-section-end"></span></h4>



<p>Ora che abbiamo installato Dompdf, vedremo come creare un PDF utilizzando un modello HTML. Segui questi passi:</p>



<p>1. Crea un file HTML contenente la struttura e il layout desiderati per il tuo PDF.<br>2. Utilizza le funzionalità CSS per definire lo stile del tuo documento, utilizzando proprietà come font-family, font-size, border, ecc.<br>3. Includi dati dinamici utilizzando tag specifici di Dompdf, come &#8220;{{nome}}&#8221; o &#8220;{{indirizzo}}&#8221;.<br>4. Utilizza la classe Dompdf per generare il PDF utilizzando il modello HTML che hai creato.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gestire_immagini_e_caratteri"></span>Gestire immagini e caratteri<span class="ez-toc-section-end"></span></h4>



<p>Quando si creano PDF eleganti, spesso è necessario includere immagini o utilizzare caratteri specifici. Ecco come farlo con Dompdf:</p>



<p>1. Includi immagini nel tuo modello HTML utilizzando il tag <img decoding="async" src="chemin_vers_image">.<br>2. Tieni presente che Dompdf non include tutti i caratteri per impostazione predefinita. Puoi aggiungere caratteri personalizzati utilizzando @font-face nel tuo CSS o utilizzando i caratteri forniti da Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Ottimizzazione_del_rendering_e_risoluzione_dei_problemi_di_Dompdf"></span>Ottimizzazione del rendering e risoluzione dei problemi di Dompdf<span class="ez-toc-section-end"></span></h4>



<p>A volte potresti riscontrare problemi con il rendering del tuo PDF o la generazione dei file. Ecco alcuni suggerimenti per risolverli:</p>



<p>1. Verifica che il tuo modello HTML sia costruito correttamente e valido.<br>2. Assicurati che tutte le risorse esterne (immagini, caratteri, ecc.) siano accessibili dal server.<br>3. Eseguire il debug del codice attivando la modalità debug Dompdf e controllando gli errori visualizzati.<br>4. Consulta la documentazione di Dompdf per ulteriori informazioni su configurazioni e problemi comuni.</p>



<p>Utilizzando Dompdf, puoi fornire un&#8217;esperienza utente migliorata fornendo documenti PDF professionali e ben formattati. Che si tratti di generare report, fatture o altri tipi di documenti, Dompdf è una scelta affidabile e potente.</p>



<p>In conclusione, installare Dompdf è semplice e veloce grazie a Composer. Una volta installato, puoi iniziare a creare file PDF di alta qualità per soddisfare le esigenze delle tue applicazioni web. Non dimenticare di consultare la documentazione ufficiale di Dompdf per saperne di più sulle sue funzionalità e sulle opzioni di personalizzazione disponibili.</p>



---
title: "Dompdf: Kaip sukurti elegantiškus PDF failus PHP?"
slug: "dompdf-kaip-sukurti-elegantiskus-pdf-failus-php"
excerpt: "Dompdf įvadas Dompdf yra PHP biblioteka, leidžianti generuoti PDF failus iš HTML turinio. Šis sprendimas labai naudingas kuriant ataskaitas, sąskaitas faktūras ar bet kokį kitą dokumentą PDF formatu. Šiame straipsnyje atrasime pagrindines Dompdf ypatybes ir išmoksime ją naudoti kuriant elegantiškus ir funkcionalius PDF failus. Būtinos sąlygos Prieš diegdami Dompdf įsitikinkite, kad turite: Dompdf diegimas Norėdami [&hellip;]"
date: "2024-03-09T12:41:47"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["skaiciavimas-ir-duomenys-lt", "technologijos-ir-skaitmeninis-lt"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Dompdf_ivadas" >Dompdf įvadas</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Butinos_salygos" >Būtinos sąlygos</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Dompdf_diegimas" >Dompdf diegimas</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Mano_pirmasis_PDF_dokumentas_su_Dompdf" >Mano pirmasis PDF dokumentas su Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Elegantisko_PDF_kurimas_PHP" >Elegantiško PDF kūrimas PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Kitas_Dompdf_diegimo_ir_naudojimo_budas" >Kitas Dompdf diegimo ir naudojimo būdas</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#PDF_kurimas_is_HTML_sablono" >PDF kūrimas iš HTML šablono</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Vaizdu_ir_sriftu_tvarkymas" >Vaizdų ir šriftų tvarkymas</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/lt/dompdf-kaip-sukurti-elegantiskus-pdf-failus-php/#Atvaizdavimo_optimizavimas_ir_Dompdf_problemu_sprendimas" >Atvaizdavimo optimizavimas ir Dompdf problemų sprendimas</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_ivadas"></span>Dompdf įvadas<span class="ez-toc-section-end"></span></h2>



<p>Dompdf yra PHP biblioteka, leidžianti generuoti PDF failus iš HTML turinio. Šis sprendimas labai naudingas kuriant ataskaitas, sąskaitas faktūras ar bet kokį kitą dokumentą PDF formatu. Šiame straipsnyje atrasime pagrindines Dompdf ypatybes ir išmoksime ją naudoti kuriant elegantiškus ir funkcionalius PDF failus.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Butinos_salygos"></span>Būtinos sąlygos<span class="ez-toc-section-end"></span></h3>



<p>Prieš diegdami Dompdf įsitikinkite, kad turite:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf reikia PHP >= 5.4. Jis suderinamas su PHP 7.x versijomis.</li>



<li><strong>PHP plėtiniai:</strong> Įsitikinkite, kad įgalinote šiuos PHP plėtinius: mbstring, DOM ir GD. Šie plėtiniai yra būtini tinkamam Dompdf veikimui.</li>



<li><strong>Sukurti:</strong> Dompdf platinamas per Composer, kuri yra PHP priklausomybės tvarkyklė. Įsitikinkite, kad jūsų sistemoje įdiegtas Composer.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_diegimas"></span>Dompdf diegimas<span class="ez-toc-section-end"></span></h4>



<p>Norėdami įdiegti Dompdf, atlikite šiuos veiksmus:</p>



<ol class="wp-block-list">
<li><strong>Sukurkite naują PHP projektą:</strong> Jei dar neturite esamo projekto, sukurkite naują naudodami pasirinktą pagrindinę struktūrą.</li>



<li><strong>Pridėkite Dompdf priklausomybę naudodami „Composer“:</strong> Atidarykite konsolę ir eikite į savo projekto katalogą. Vykdykite šią komandą, kad pridėtumėte Dompdf prie savo projekto:     <pre><code>kompozitorius reikalauja dompdf/dompdf</code></pre>     Ši komanda automatiškai atsisiųs ir įdiegs „Dompdf“ kartu su jo priklausomybėmis.</li>



<li><strong>Savo programoje naudokite Dompdf:</strong> Dabar savo projekte galite naudoti Dompdf. Yra daug būdų, kaip sukurti PDF failus naudojant Dompdf, tačiau čia yra pagrindinis pavyzdys, kaip pradėti:
<pre><code>// Įtraukite kompozitoriaus automatinį įkėliklį
reikalauti "tiekėjas/autoload.php";

// Sukurkite naują Dompdf objektą
$dompdf = naujas Dompdf();

// Įkelti HTML turinį iš failo arba eilutės
$html = '<h1><span class="ez-toc-section" id="Mano_pirmasis_PDF_dokumentas_su_Dompdf"></span>Mano pirmasis PDF dokumentas su Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Pateikite PDF dokumentą
$dompdf->render();

// Siųsti PDF dokumentą į išvestį
$dompdf->stream('document.pdf');</code></pre>
    Šis pavyzdys sukuria naują PDF dokumentą su pavadinimu ir įkelia jį kaip „document.pdf“ failą. Galite tinkinti HTML turinį pagal savo poreikius.</li>
</ol>



<p>Dabar, kai įdiegėte Dompdf, galite pradėti kurti elegantiškus ir funkcionalius PDF failus savo žiniatinklio programose. Dompdf siūlo daug pažangių funkcijų, skirtų pritaikyti PDF atvaizdavimą, pavyzdžiui, tvarkyti vaizdus, ​​pasirinktinius šriftus ir CSS stilius.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Elegantisko_PDF_kurimas_PHP"></span>Elegantiško PDF kūrimas PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kitas_Dompdf_diegimo_ir_naudojimo_budas"></span>Kitas Dompdf diegimo ir naudojimo būdas<span class="ez-toc-section-end"></span></h3>



<p>Toliau nurodyti veiksmai, kuriuos reikia atlikti:<br>1. Atsisiųskite naujausią Dompdf versiją iš oficialios svetainės.<br>2. Išskleiskite atsisiųstus failus ir įdėkite juos į savo PHP projektą.<br>3. Įtraukite Dompdfautoload.php failą, kad įkeltumėte biblioteką į savo PHP scenarijų.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="PDF_kurimas_is_HTML_sablono"></span>PDF kūrimas iš HTML šablono<span class="ez-toc-section-end"></span></h4>



<p>Dabar, kai įdiegėme Dompdf, pamatysime, kaip sukurti PDF naudojant HTML šabloną. Atlikite šiuos veiksmus:</p>



<p>1. Sukurkite HTML failą su norima PDF struktūra ir išdėstymu.<br>2. Naudokite CSS funkcijas, kad sukurtumėte dokumento stilių, naudodami tokias ypatybes kaip šriftų šeima, šrifto dydis, kraštinė ir kt.<br>3. Įtraukite dinaminius duomenis naudodami specifines „Dompdf“ žymas, pvz., „{{name}}“ arba „{{adresas}}“.<br>4. Naudokite Dompdf klasę, kad sukurtumėte PDF naudodami sukurtą HTML šabloną.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Vaizdu_ir_sriftu_tvarkymas"></span>Vaizdų ir šriftų tvarkymas<span class="ez-toc-section-end"></span></h4>



<p>Kuriant stilingus PDF failus dažnai reikia įtraukti vaizdus arba naudoti specifinius šriftus. Štai kaip tai padaryti naudojant Dompdf:</p>



<p>1. Įtraukite vaizdus į savo HTML šabloną naudodami žymą <img decoding="async" src="chemin_vers_image">.<br>2. Atkreipkite dėmesį, kad pagal numatytuosius nustatymus Dompdf neįtraukia visų šriftų. Galite pridėti pasirinktinių šriftų naudodami @font-face savo CSS arba naudodami Dompdf pateiktus šriftus.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Atvaizdavimo_optimizavimas_ir_Dompdf_problemu_sprendimas"></span>Atvaizdavimo optimizavimas ir Dompdf problemų sprendimas<span class="ez-toc-section-end"></span></h4>



<p>Kartais gali kilti problemų pateikiant PDF arba generuojant failus. Štai keletas patarimų, kaip juos išspręsti:</p>



<p>1. Patikrinkite, ar jūsų HTML šablonas yra tinkamai sukurtas ir galiojantis.<br>2. Įsitikinkite, kad visi išoriniai ištekliai (vaizdai, šriftai ir kt.) yra pasiekiami iš serverio.<br>3. Suderinkite kodą aktyvuodami Dompdf derinimo režimą ir patikrindami rodomas klaidas.<br>4. Daugiau informacijos apie įprastas konfigūracijas ir problemas rasite Dompdf dokumentacijoje.</p>



<p>Naudodami „Dompdf“ galite patobulinti naudotojo patirtį, pateikdami profesionalius ir gerai suformatuotus PDF dokumentus. Nesvarbu, ar kuriate ataskaitas, sąskaitas faktūras ar kitokio tipo dokumentus, Dompdf yra patikimas ir galingas pasirinkimas.</p>



<p>Apibendrinant galima pasakyti, kad „Composer“ dėka Dompdf įdiegimas yra greitas ir paprastas. Įdiegę galite pradėti kurti aukštos kokybės PDF failus, kad atitiktų jūsų žiniatinklio programos poreikius. Nepamirškite perskaityti oficialios Dompdf dokumentacijos, kad sužinotumėte daugiau apie jo funkcijas ir galimas tinkinimo parinktis.</p>



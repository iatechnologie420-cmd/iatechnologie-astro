---
title: "Dompdf: Hvernig á að búa til glæsileg PDF skjöl í PHP?"
slug: "dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php"
excerpt: "Kynning á Dompdf Dompdf er PHP bókasafn sem gerir þér kleift að búa til PDF skrár úr HTML efni. Þessi lausn er mjög gagnleg til að búa til skýrslur, reikninga eða önnur skjöl á PDF formi. Í þessari grein munum við uppgötva grunneiginleika Dompdf og læra hvernig á að nota það til að búa til [&hellip;]"
date: "2024-03-09T12:40:41"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["taekni-og-stafraen-is", "tolvur-og-gogn-is"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Kynning_a_Dompdf" >Kynning á Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Forkrofur" >Forkröfur</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Dompdf_uppsetning" >Dompdf uppsetning</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Fyrsta_PDF_skjalid_mitt_med_Dompdf" >Fyrsta PDF skjalið mitt með Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Ad_bua_til_glaesilegan_PDF_i_PHP" >Að búa til glæsilegan PDF í PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Onnur_adferd_til_ad_setja_upp_og_nota_Dompdf" >Önnur aðferð til að setja upp og nota Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Ad_bua_til_PDF_ur_HTML_snidmati" >Að búa til PDF úr HTML sniðmáti</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Umsjon_med_myndum_og_leturgerdum" >Umsjón með myndum og leturgerðum</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/dompdf-hvernig-a-ad-bua-til-glaesileg-pdf-skjol-i-php/#Finstilla_flutning_og_laga_Dompdf_vandamal" >Fínstilla flutning og laga Dompdf vandamál</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kynning_a_Dompdf"></span>Kynning á Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf er PHP bókasafn sem gerir þér kleift að búa til PDF skrár úr HTML efni. Þessi lausn er mjög gagnleg til að búa til skýrslur, reikninga eða önnur skjöl á PDF formi. Í þessari grein munum við uppgötva grunneiginleika Dompdf og læra hvernig á að nota það til að búa til glæsilegar og hagnýtar PDF-skjöl.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Forkrofur"></span>Forkröfur<span class="ez-toc-section-end"></span></h3>



<p>Áður en þú setur upp Dompdf skaltu ganga úr skugga um að þú hafir eftirfarandi:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf krefst PHP >= 5.4. Það er samhæft við útgáfur 7.x af PHP.</li>



<li><strong>PHP viðbætur:</strong> Gakktu úr skugga um að þú hafir virkjað eftirfarandi PHP viðbætur: mbstring, DOM og GD. Þessar viðbætur eru nauðsynlegar til að Dompdf virki rétt.</li>



<li><strong>Semja:</strong> Dompdf er dreift í gegnum Composer, sem er ávanastjóri PHP. Gakktu úr skugga um að þú hafir Composer uppsett á vélinni þinni.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_uppsetning"></span>Dompdf uppsetning<span class="ez-toc-section-end"></span></h4>



<p>Til að setja upp Dompdf skaltu fylgja eftirfarandi skrefum:</p>



<ol class="wp-block-list">
<li><strong>Búðu til nýtt PHP verkefni:</strong> Ef þú ert ekki þegar með fyrirliggjandi verkefni skaltu búa til nýtt með því að nota grunnbygginguna að eigin vali.</li>



<li><strong>Bættu við Dompdf ósjálfstæði í gegnum Composer:</strong> Opnaðu stjórnborð og farðu í verkefnaskrána þína. Keyrðu eftirfarandi skipun til að bæta Dompdf við verkefnið þitt:     <pre><code>tónskáld þurfa dompdf/dompdf</code></pre>     Þessi skipun mun sjálfkrafa hlaða niður og setja upp Dompdf ásamt ósjálfstæði þess.</li>



<li><strong>Notaðu Dompdf í forritinu þínu:</strong> Þú getur nú notað Dompdf í verkefninu þínu. Það eru margar leiðir til að búa til PDF skrár með Dompdf, en hér er grundvallardæmi til að koma þér af stað:
<pre><code>// Láttu Composer autoloader fylgja með
krefjast 'vendor/autoload.php';

// Búðu til nýjan Dompdf hlut
$dompdf = nýr Dompdf();

// Hladdu HTML efni úr skrá eða streng
$html = '<h1><span class="ez-toc-section" id="Fyrsta_PDF_skjalid_mitt_med_Dompdf"></span>Fyrsta PDF skjalið mitt með Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Gerðu PDF skjalið
$dompdf->render();

// Sendu PDF skjal til úttaks
$dompdf->straum('skjal.pdf');</code></pre>
    Þetta dæmi býr til nýtt PDF skjal með titli og hleður því upp sem &#8220;document.pdf&#8221; skrá. Þú getur sérsniðið HTML innihaldið eftir þínum þörfum.</li>
</ol>



<p>Nú þegar þú hefur uppsett Dompdf geturðu byrjað að búa til glæsilegar og hagnýtar PDF-skrár í vefforritunum þínum. Dompdf býður upp á marga háþróaða eiginleika til að sérsníða PDF flutning, svo sem að stjórna myndum, sérsniðnum leturgerðum og CSS stílum.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Ad_bua_til_glaesilegan_PDF_i_PHP"></span>Að búa til glæsilegan PDF í PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Onnur_adferd_til_ad_setja_upp_og_nota_Dompdf"></span>Önnur aðferð til að setja upp og nota Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Hér eru skrefin til að fylgja:<br>1. Sæktu nýjustu útgáfuna af Dompdf frá opinberu vefsíðunni.<br>2. Dragðu niður skrárnar og settu þær í PHP verkefnið þitt.<br>3. Láttu Dompdfautoload.php skrána fylgja með til að hlaða bókasafninu inn í PHP forskriftina þína.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Ad_bua_til_PDF_ur_HTML_snidmati"></span>Að búa til PDF úr HTML sniðmáti<span class="ez-toc-section-end"></span></h4>



<p>Nú þegar við höfum sett upp Dompdf munum við sjá hvernig á að búa til PDF með HTML sniðmáti. Fylgdu þessum skrefum:</p>



<p>1. Búðu til HTML-skrá sem inniheldur uppbyggingu og útlit sem þú vilt fyrir PDF-skrána þína.<br>2. Notaðu CSS eiginleika til að stíla skjalið þitt, notaðu eiginleika eins og leturfjölskyldu, leturstærð, ramma osfrv.<br>3. Láttu kvik gögn fylgja með því að nota Dompdf-sértæk merki, eins og „{{nafn}}“ eða „{{address}}“.<br>4. Notaðu Dompdf flokkinn til að búa til PDF með því að nota HTML sniðmátið sem þú bjóst til.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Umsjon_med_myndum_og_leturgerdum"></span>Umsjón með myndum og leturgerðum<span class="ez-toc-section-end"></span></h4>



<p>Þegar búið er til stílhrein PDF-skjöl er oft nauðsynlegt að láta myndir fylgja með eða nota sérstakt letur. Svona á að gera það með Dompdf:</p>



<p>1. Settu myndir inn í HTML sniðmátið þitt með því að nota merkið <img decoding="async" src="chemin_vers_image">.<br>2. Vinsamlegast athugaðu að Dompdf inniheldur ekki öll leturgerðir sjálfgefið. Þú getur bætt við sérsniðnum leturgerðum með því að nota @font-face í CSS eða með því að nota leturgerðir sem Dompdf veitir.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Finstilla_flutning_og_laga_Dompdf_vandamal"></span>Fínstilla flutning og laga Dompdf vandamál<span class="ez-toc-section-end"></span></h4>



<p>Stundum gætirðu lent í vandræðum með að skila PDF eða búa til skrárnar. Hér eru nokkur ráð til að leysa þau:</p>



<p>1. Athugaðu hvort HTML sniðmátið þitt sé rétt smíðað og gilt.<br>2. Gakktu úr skugga um að allar ytri auðlindir (myndir, leturgerðir osfrv.) séu aðgengilegar frá þjóninum.<br>3. Villuleitu kóðann þinn með því að virkja Dompdf villuleitarstillingu og athuga villurnar sem sýndar eru.<br>4. Sjá Dompdf skjölin fyrir frekari upplýsingar um algengar stillingar og vandamál.</p>



<p>Með því að nota Dompdf geturðu veitt aukna notendaupplifun með því að afhenda fagleg og vel sniðin PDF skjöl. Hvort sem þú býrð til skýrslur, reikninga eða annars konar skjöl, þá er Dompdf áreiðanlegt og öflugt val.</p>



<p>Að lokum er uppsetning Dompdf fljótleg og auðveld þökk sé Composer. Þegar það hefur verið sett upp geturðu byrjað að búa til hágæða PDF-skrár til að mæta þörfum vefforritsins. Ekki gleyma að skoða opinberu Dompdf skjölin til að læra meira um eiginleika þess og tiltæka sérsniðmöguleika.</p>



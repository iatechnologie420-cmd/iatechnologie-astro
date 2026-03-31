---
title: "Kuidas leida Google Mapsist GPS-koordinaate (laius- ja pikkuskraad)?"
slug: "kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad"
excerpt: "THE GPS (Global Positioning System) on tehnoloogia, mis on muutunud meie igapäevaelus hädavajalikuks. Kasutades satelliitide poolt edastatavaid signaale, GPS süsteem võimaldab meil täpselt määrata oma asukoha geograafiliste koordinaatide kujul. Neid koordinaate esindavad kaks põhielementi: laiuskraad ja pikkuskraad. Selles artiklis uurime GPS-koordinaatide maailma ja mõistame nende olulist rolli geolokatsioonis. Mis on GPS-koordinaadid? GPS-koordinaadid on võrdluspunktid, mis [&hellip;]"
date: "2024-03-09T12:02:47"
featuredImage: "/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-3.png"
categories: ["tehnoloogia-ja-digitaalne-et"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Implanter des points sur Google Earth à partir des coordonnées X et Y" width="500" height="281" src="https://www.youtube.com/embed/9ymcbTqEfNo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>    THE <strong>GPS</strong> (Global Positioning System) on tehnoloogia, mis on muutunud meie igapäevaelus hädavajalikuks. Kasutades satelliitide poolt edastatavaid signaale, <strong>GPS süsteem</strong> võimaldab meil täpselt määrata oma asukoha geograafiliste koordinaatide kujul. </p>



<p>Neid koordinaate esindavad kaks põhielementi: <strong>laiuskraad</strong> ja <strong>pikkuskraad</strong>. Selles artiklis uurime GPS-koordinaatide maailma ja mõistame nende olulist rolli geolokatsioonis.</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-1" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#Mis_on_GPS-koordinaadid" >Mis on GPS-koordinaadid?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-2" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#GPS-koordinaatide_kasulikkus" >GPS-koordinaatide kasulikkus</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#Kuidas_leida_Google_Mapsist_GPS-koordinaate" >Kuidas leida Google Mapsist GPS-koordinaate</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#Napunaide_tapsuse_suurendamiseks" >Näpunäide täpsuse suurendamiseks</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#Lugege_ja_moistate_GPS-koordinaate" >Lugege ja mõistate GPS-koordinaate</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#Kasutage_Google_Mapsis_GPS-koordinaate" >Kasutage Google Mapsis GPS-koordinaate</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/et/kuidas-leida-google-mapsist-gps-koordinaate-laius-ja-pikkuskraad/#Jagamise_ja_koordinaatide_PIN-kood" >Jagamise ja koordinaatide PIN-kood</a></li></ul></li></ul></nav></div>
<h3 class="wp-block-heading"><span class="ez-toc-section" id="Mis_on_GPS-koordinaadid"></span>Mis on GPS-koordinaadid?<span class="ez-toc-section-end"></span></h3>



<p>    GPS-koordinaadid on võrdluspunktid, mis näitavad konkreetset asukohta Maal. Seal <strong>laiuskraad</strong> mõõdab kaugust ekvaatorist põhja- või lõuna pool ja varieerub vahemikus -90 kraadi (lõunapoolusel) kuni +90 kraadi (põhjapoolusel). Seal <strong>pikkuskraad</strong>, omalt poolt mõõdab kaugust Greenwichi meridiaanist ida või lääne suunas ja varieerub vahemikus -180 kuni +180 kraadi. Nende kahe mõõtmise kombinatsioon võimaldab määrata täpse geograafilise punkti.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="GPS-koordinaatide_kasulikkus"></span>GPS-koordinaatide kasulikkus<span class="ez-toc-section-end"></span></h4>



<p>    GPS-koordinaatide pakutaval täpsusel on meie igapäevaelus palju praktilisi rakendusi. Neid kasutatakse navigeerimiseks, võimaldades kasutajatel nutitelefonide ja integreeritud navigatsioonisüsteemide abil autoga, jalgrattaga või jalgsi reisides leida tee sihtkohta või jälgida marsruuti. Need on ka otsingu- ja päästeoperatsioonide jaoks üliolulised, võimaldades eksinud või hädas olevate inimeste täpset asukohta leida.</p>



<p>Teaduses ja uurimistöös mängivad GPS-koordinaadid olulist rolli sellistes uuringutes nagu tektooniliste liikumiste jälgimine, metsloomade jälgimine ja palju muud. Lõpuks on need olulised elemendid sellistes sektorites nagu täppispõllumajandus, geopeitus ja kohaletoimetamisteenused.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kuidas_leida_Google_Mapsist_GPS-koordinaate"></span>Kuidas leida Google Mapsist GPS-koordinaate<span class="ez-toc-section-end"></span></h4>



<p>    Oma laius- ja pikkuskraadi leidmiseks <strong>Google kaardid</strong>, peate järgima mõnda lihtsat sammu:</p>



<ol class="wp-block-list">
<li>Avatud <strong>Google kaardid</strong> oma veebibrauseris või mobiilirakenduses.</li>



<li>Paremklõpsake kaardil huvipunkti (või puudutage ja hoidke mobiiltelefonis).</li>



<li>Ilmuvas menüüs klõpsake &#8220;Millised on koordinaadid?&#8221; või näete koordinaate otse väikeses hüpikaknas.</li>



<li>Kopeerige GPS-koordinaadid, mis on esitatud kahe numbrina (näiteks 48,8566° N, 2,3522° E Pariisi asukoha jaoks).</li>
</ol>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Napunaide_tapsuse_suurendamiseks"></span>Näpunäide täpsuse suurendamiseks<span class="ez-toc-section-end"></span></h4>



<p>Veelgi suurema täpsuse huvides saate pärast soovitud asukohal paremklõpsamist valikut täpsustada, liigutades kursorit veidi, enne kui valite valiku „Lisateave selle asukoha kohta”. See võib olla kasulik väga konkreetse asukoha koordinaatide leidmisel, näiteks hoone sissepääsu või loodusliku huvipunkti jaoks.</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-.png" alt="" class="wp-image-1613" srcset="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-.png 1792w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--300x171.png 300w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--1024x585.png 1024w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--150x86.png 150w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--768x439.png 768w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Lugege_ja_moistate_GPS-koordinaate"></span>Lugege ja mõistate GPS-koordinaate<span class="ez-toc-section-end"></span></h3>



<p>GPS-koordinaadid on tavaliselt kahe numbri kujul, mis tähistavad laius- ja pikkuskraadi. Koordinaatide õigeks tõlgendamiseks on oluline mõista, kuidas neid numbreid lugeda.</p>



<ul class="wp-block-list">
<li><strong>Laiuskraad:</strong> see on mõõtmine kraadides, mis näitab kaugust ekvaatorist põhja või lõuna suunas, varieerudes vahemikus -90° kuni +90°.</li>



<li><strong>Pikkuskraad:</strong> see on mõõtmine kraadides, mis näitab kaugust Greenwichi meridiaanist idas või läänes, varieerudes -180° kuni +180°.</li>
</ul>



<p>            Peal <strong>Google kaardid</strong>, kuvatakse koordinaadid tavaliselt kümnendkoha kujul. Näiteks Pariisi Eiffeli tornil on ligikaudsed koordinaadid <strong>Laiuskraad: 48,8584</strong> Ja <strong>Pikkuskraad: 2,2945</strong>.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kasutage_Google_Mapsis_GPS-koordinaate"></span>Kasutage Google Mapsis GPS-koordinaate<span class="ez-toc-section-end"></span></h4>



<p>Kui teil on soovitud koha GPS-koordinaadid, saate selle hõlpsalt leida <strong>Google kaardid</strong>. Tehke järgmist.</p>



<ol class="wp-block-list">
<li>Tagasi <strong>Google kaardid</strong>.</li>



<li>Tippige otsinguribale saadud koordinaadid, seejärel vajutage sisestusklahvi või klõpsake otsingunuppu.</li>



<li><strong>Google kaardid</strong> viib teid otse täpselt sisestatud koordinaatidele vastavasse asukohta.</li>
</ol>



<p>            See meetod on eriti kasulik navigeerimiseks teest kõrvalekalduvatesse kohtadesse, mille jaoks traditsioonilistest aadressidest ei piisa.</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2.png" alt="" class="wp-image-1615" srcset="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2.png 1792w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-300x171.png 300w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-1024x585.png 1024w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-150x86.png 150w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-768x439.png 768w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Jagamise_ja_koordinaatide_PIN-kood"></span>Jagamise ja koordinaatide PIN-kood<span class="ez-toc-section-end"></span></h4>



<p>        Pärast koordinaatide leidmist või sisestamist <strong>Google kaardid</strong> pakub ka võimalust seda teavet jagada või märgistada see nööpnõelaga edaspidiseks kasutamiseks. Seda saab teha järgmiselt.</p>



<ol class="wp-block-list">
<li>Kui teil on kontaktandmed, kasutage teabe saatmiseks e-posti, sõnumi või sotsiaalmeedia kaudu sisseehitatud jagamisnuppu.</li>



<li>Asukoha kinnitamiseks klõpsake kontaktandmete kõrval oleval nööpnõela ikoonil, et lisada see hiljem hõlpsaks juurdepääsuks jaotisesse „Teie kohad”.</li>
</ol>



<p>            Kas jagada kohtumispaika, urbexi, aardejahi või lihtsalt töö või vaba aja veetmise jaoks, teadke, kuidas leida ja lugeda GPS-koordinaate <strong>Google kaardid</strong> on praktiline oskus. Järgige lihtsalt ülalmainitud samme ja saate täpselt määrata mis tahes punkti Maal.</p>



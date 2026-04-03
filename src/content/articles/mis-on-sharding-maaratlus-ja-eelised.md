---
title: "Mis on Sharding? määratlus ja eelised"
slug: "mis-on-sharding-maaratlus-ja-eelised"
excerpt: "Shardingi mõistmine: määratlus ja põhiprintsiibid Andmebaaside ja suuremahuliste andmehoidlate maailm on keeruline ja pidevalt arenev. Eksponentsiaalselt kasvavate andmemahtude tõhusaks haldamiseks peavad IT-arhitektuurid uuendusi tegema ja leidma lahendusi nende andmete toimivuse ja haldamise optimeerimiseks. Üks lähenemisviis sellele probleemile on tehnika nn killustamine. Selles artiklis määratleme jagamise, mõistame selle põhiprintsiipe ja miks see on tänapäevastes andmebaasisüsteemides hädavajalik. [&hellip;]"
date: "2024-03-09T12:30:32"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-3.png"
categories: ["infrastruktuur-ja-vorgud-et", "tehnoloogia-ja-digitaalne-et"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Database Sharding and Partitioning" width="500" height="281" src="https://www.youtube.com/embed/wXvljefXyEo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Shardingi_moistmine_maaratlus_ja_pohiprintsiibid" >Shardingi mõistmine: määratlus ja põhiprintsiibid</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Mis_on_Sharding" >Mis on Sharding?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Kuidas_jagamine_tootab" >Kuidas jagamine töötab?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Jagamise_eelised" >Jagamise eelised</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Valjakutsed_ja_kaalutlused" >Väljakutsed ja kaalutlused</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Kuidas_andmeid_levitatakse" >Kuidas andmeid levitatakse?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Andmete_salvestamine_kildudes" >Andmete salvestamine kildudes</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Jagamise_puudused" >Jagamise puudused</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Killustamise_tehnilised_valjakutsed" >Killustamise tehnilised väljakutsed</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/et/mis-on-sharding-maaratlus-ja-eelised/#Praktilised_kaalutlused_jagamisel" >Praktilised kaalutlused jagamisel</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Shardingi_moistmine_maaratlus_ja_pohiprintsiibid"></span>Shardingi mõistmine: määratlus ja põhiprintsiibid<span class="ez-toc-section-end"></span></h2>



<p>Andmebaaside ja suuremahuliste andmehoidlate maailm on keeruline ja pidevalt arenev. Eksponentsiaalselt kasvavate andmemahtude tõhusaks haldamiseks peavad IT-arhitektuurid uuendusi tegema ja leidma lahendusi nende andmete toimivuse ja haldamise optimeerimiseks. Üks lähenemisviis sellele probleemile on tehnika nn <strong>killustamine</strong>. </p>



<p>Selles artiklis määratleme jagamise, mõistame selle põhiprintsiipe ja miks see on tänapäevastes andmebaasisüsteemides hädavajalik.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Mis_on_Sharding"></span>Mis on Sharding?<span class="ez-toc-section-end"></span></h3>



<p>THE <strong>killustamine</strong> on meetod andmete horisontaalseks jaotamiseks hajutatud andmebaasis või andmebaasihaldussüsteemis. See meetod seisneb andmebaasi jagamises väiksemateks osadeks, mida nimetatakse <em>killud</em>, mida saab levitada mitme serveri vahel. Iga killuke sisaldab andmete alamhulka ja toimib iseseisva andmebaasina. Selle peamine eelis on see, et see võimaldab tõhusamalt hallata suuri andmemahte ja tehinguid, vähendades iga üksiku serveri koormust.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kuidas_jagamine_tootab"></span>Kuidas jagamine töötab?<span class="ez-toc-section-end"></span></h4>



<p>Jagamine põhineb andmete jaotusloogikal, mille määrab jagamisalgoritm. Algoritme on erinevaid, kuid valik sõltub sageli andmete ja päringute olemusest, mida süsteem peab käsitlema. Algoritmide levinumate näidete hulka kuuluvad vahemikupõhine jagamine (kus andmeid jaotatakse vastavalt väärtusvahemikele), räsi jagamine (kus teatud võtmete räsi määrab andmete asukoha) või kataloogipõhine jagamine (koos otsingutabeliga asukoha leidmiseks andmed).</p>



<p>Kui killud on loodud ja andmed levitatud, kasutatakse sageli tsentraliseeritud haldussüsteemi <em>killuhaldur</em> Või <em>kiik</em>, on vajalik tehingute ja päringute koordineerimiseks erinevate kildude vahel. See süsteem tagab, et päringud suunatakse õigele killule, võimaldades seega suhelda ainult andmebaasi asjakohase osaga.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Jagamise_eelised"></span>Jagamise eelised<span class="ez-toc-section-end"></span></h4>



<p>Jagamine pakub mitmeid eeliseid, mis muudavad selle suurte süsteemide jaoks atraktiivseks:</p>



<ul class="wp-block-list">
<li><strong>Skaleeritavus</strong> : jagamine võimaldab andmebaasidel hõlpsasti kohaneda suurenenud koormusega, lisades lihtsalt rohkem servereid.</li>



<li><strong>Esitus</strong> : vähendades iga serveri koormust, saab päringu jõudlust oluliselt parandada, eriti kirjutamistoimingute puhul.</li>



<li><strong>Kättesaadavus</strong> : Isegi kui üks kild on maas, jätkavad teised tööd, suurendades süsteemi kui terviku töökindlust.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Valjakutsed_ja_kaalutlused"></span>Väljakutsed ja kaalutlused<span class="ez-toc-section-end"></span></h4>



<p>Kuid jagamisega kaasneb ka oma osa väljakutseid:</p>



<ul class="wp-block-list">
<li>Kildude haldamise keerukus võib kildude arvu suurenedes suureneda.</li>



<li>Tehinguid, mis nõuavad teavet erinevate kildude vahel, on keerulisem hallata.</li>



<li>Andmete järjepidevuse tagamine võib muutuda keerulisemaks, kui kildude arv kasvab.</li>
</ul>



<p>Seetõttu on oluline hoolikalt kaaluda, kas killustamine on konkreetse rakenduse jaoks õige strateegia. Mõnikord võivad asjakohasemad olla muud lähenemisviisid, nagu vertikaalne jaotus, andmete replikatsioon või mitterelatsioonilise andmebaasi kasutamine.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kuidas_andmeid_levitatakse"></span>Kuidas andmeid levitatakse?<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png" alt="" class="wp-image-1070" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Andmete jaotamist killustatud keskkonnas saab teostada erinevate algoritmide järgi. Siin on mõned levinumad:</p>



<ul class="wp-block-list">
<li><strong>Jagamine võtmevahemiku alusel:</strong> Andmed jagatakse vastavalt kindlale võtmele, kus iga kild vastutab väärtusvahemiku eest.</li>



<li><strong>Räsipõhine jagamine:</strong> Räsifunktsiooni kasutatakse võtme põhjal, et määrata, milline kild konkreetse kirje salvestab.</li>



<li><strong>Kataloogipõhine jagamine:</strong> Kataloog säilitab kirjete ja kildude vahel, kus neid hoitakse, vastendamist.</li>
</ul>



<p>Need meetodid võimaldavad andmete suhteliselt tasakaalustatud jaotamist, kitsaskohtade vähendamist ja reageerimisaegade paranemist.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Andmete_salvestamine_kildudes"></span>Andmete salvestamine kildudes<span class="ez-toc-section-end"></span></h4>



<p>Andmed salvestatakse igasse kildu teistest kildudest sõltumatult. See tähendab, et iga killuke toimib eraldiseisva andmebaasina, millel on oma skeemid ja indeksid. Andmete järjepidevus kõigis kildudes säilitatakse pigem loogiliselt kui füüsiliselt, mis võib mõnikord tekitada keerukust mitut killust hõlmavate tehingute haldamisel.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Jagamise_puudused"></span>Jagamise puudused<span class="ez-toc-section-end"></span></h4>



<p>Kuid purustamisel on ka teatud puudused:</p>



<ul class="wp-block-list">
<li><strong>Keerukus:</strong> Mitme killu haldamine ja hooldamine võib muutuda keeruliseks, eriti andmete järjepidevuse ja tehingute haldamise jaoks.</li>



<li><strong>Halva levitamise ohud:</strong> Andmete ebaühtlane jaotumine võib põhjustada &#8220;kuumaid kohti&#8221;, kus mõned killud on ülekoormatud.</li>



<li><strong>Kulud:</strong> Vajadus opereerida ja hallata rohkem infrastruktuuri võib suurendada kulusid.</li>



<li></li>
</ul>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png" alt="" class="wp-image-1071" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Killustamise_tehnilised_valjakutsed"></span>Killustamise tehnilised väljakutsed<span class="ez-toc-section-end"></span></h4>



<p>Jaotamise rakendamine tõstatab mitmeid tehnilisi küsimusi:</p>



<ul class="wp-block-list">
<li><strong>Disaini keerukus</strong> : Võtmete jagamise ajastamine on ülioluline ja seda tuleks teha ettevaatlikult, kuna halb disain võib põhjustada andmete levitamise tasakaalustamatust ja kahjustada süsteemi tõhusust.</li>



<li><strong>Transversaalsed päringud</strong> : Päringute esitamine mitmele killule võib olla keeruline ja tülikas, kuna see nõuab kildude vahelist suhtlust ja koondamismehhanisme.</li>



<li><strong>Jaotatud tehingud</strong> : Tehingute terviklikkuse säilitamine mitme killu vahel on keeruline ja nõuab keerukaid koordineerimisprotokolle ja lukustusmehhanisme.</li>



<li><strong>Skaleerimine</strong> : Kuigi killustamine võimaldab skaleeritavust, võib kildude lisamine või eemaldamine pärast tõsiasja olla keeruline ja nõuab sageli andmete ümberjaotamist.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Praktilised_kaalutlused_jagamisel"></span>Praktilised kaalutlused jagamisel<span class="ez-toc-section-end"></span></h4>



<p>Lisaks tehnilistele väljakutsetele tuleb arvesse võtta ka praktilisi kaalutlusi:</p>



<ul class="wp-block-list">
<li><strong>Maksumus</strong> : Jaotuse rakendamise ja hooldamise keerukus võib kaasa tuua märkimisväärseid kulusid riistvara, tarkvara ja spetsiaalsete inimressursside osas.</li>



<li><strong>Esitus</strong> : Ebasobiva jaotamisstrateegia valimine võib viia halva jõudluseni, eriti kui koormuse tasakaalustamine ei ole hästi hallatud.</li>



<li><strong>Andmete järjepidevus</strong> : Andmete järjepidevuse tagamine kõigis kildudes on oluline, kuid seda on raske saavutada, eriti suure hajutusega keskkondades.</li>



<li><strong>Tehniline ekspertiis</strong> : killustatuse keerukuse haldamiseks ja probleemidele reageerimiseks on vaja sügavaid tehnilisi teadmisi.</li>



<li><strong>Varundamine ja taastamine</strong> : varukoopiate ja taaste haldamine muutub killustamisega keerulisemaks, kuna neid toiminguid tuleb koordineerida mitme killu vahel.</li>
</ul>



<p>Kokkuvõtteks võib öelda, et kuigi killustamine on võimas tehnika kõrget jõudlust ja skaleeritavust nõudvate andmebaaside jaoks, tekitab see mitmeid väljakutseid ja nõuab optimaalseks rakendamiseks olulisi praktilisi kaalutlusi. Olles probleemidest teadlik ja valmistades hoolikalt ette jagamisstrateegia, saavad organisatsioonid selle eelistest täit kasu, minimeerides samas sellega seotud riske ja kulusid.</p>



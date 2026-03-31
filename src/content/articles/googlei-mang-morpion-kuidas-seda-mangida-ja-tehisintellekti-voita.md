---
title: "Google&#8217;i mäng Morpion: kuidas seda mängida ja tehisintellekti võita?"
slug: "googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita"
excerpt: "Google&#8217;i Tic-Toe mängu reeglid Mängu eesmärk Morpioni mäng, mida nimetatakse ka Tic-tac-toe&#8217;iks, on strateegiamäng, mida mängitakse 3&#215;3 ruudustikul. Eesmärk on rivistada kolm identset sümbolit (rist või ring) horisontaalselt, vertikaalselt või diagonaalselt vastase ees. Seadistage Google Tic Toe mäng on saadaval võrgus ja seda saab mängida erinevates seadmetes, sealhulgas nutitelefonides, tahvelarvutites või arvutites. Alustamiseks minge lihtsalt [&hellip;]"
date: "2024-03-09T12:42:03"
featuredImage: "/images/blog/Jeu-de-Morpion-de-Google-Comment-y-jouer-et-battre-lintelligence-artificielle-.png"
categories: ["tehnoloogia-ja-digitaalne-et"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Googlei_Tic-Toe_mangu_reeglid" >Google&#8217;i Tic-Toe mängu reeglid</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-2" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Mangu_eesmark" >Mängu eesmärk</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Seadistage" >Seadistage</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Mangu_edenemine" >Mängu edenemine</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Voitmise_tehnikad" >Võitmise tehnikad</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Taiendavad_napunaited" >Täiendavad näpunäited</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-7" href="/et/googlei-mang-morpion-kuidas-seda-mangida-ja-tehisintellekti-voita/#Kokkuvote_strateegiatest_kuidas_voita_tic-tac-toe_mangu_tehisintellekti" >Kokkuvõte strateegiatest, kuidas võita tic-tac-toe mängu tehisintellekti</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Googlei_Tic-Toe_mangu_reeglid"></span>Google&#8217;i Tic-Toe mängu reeglid<span class="ez-toc-section-end"></span></h2>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mangu_eesmark"></span>Mängu eesmärk<span class="ez-toc-section-end"></span></h4>



<p>Morpioni mäng, mida nimetatakse ka Tic-tac-toe&#8217;iks, on strateegiamäng, mida mängitakse 3&#215;3 ruudustikul. Eesmärk on rivistada kolm identset sümbolit (rist või ring) horisontaalselt, vertikaalselt või diagonaalselt vastase ees.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Seadistage"></span>Seadistage<span class="ez-toc-section-end"></span></h4>



<p>Google Tic Toe mäng on saadaval võrgus ja seda saab mängida erinevates seadmetes, sealhulgas nutitelefonides, tahvelarvutites või arvutites. Alustamiseks minge lihtsalt Google&#8217;i veebisaidile ja otsige otsinguribalt &#8220;Tic Toe mäng&#8221;.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mangu_edenemine"></span>Mängu edenemine<span class="ez-toc-section-end"></span></h4>



<p>Kui olete mängulehel, saate valida, kas mängida tehisintellekti (tuntud ka kui Google AI) või mõne teise mängija vastu. Kui otsustate mängida Google AI vastu, saate valida raskusastme: lihtne, keskmine või raske.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Voitmise_tehnikad"></span>Võitmise tehnikad<span class="ez-toc-section-end"></span></h4>



<p>&#8211; Alustage ruudustiku keskpunkti hõivamisest: keskelt alustades suurendate oma võiduvõimalusi, sest see ruut on paljude võimalike joonduste alguspunkt.</p>



<p>&#8211; Blokeerige vastase käigud: hoidke vastase käikudel silm peal ja proovige blokeerida tema potentsiaalseid koosseise, asetades oma sümbolid strateegilistesse kohtadesse.</p>



<p>&#8211; Ennetage järgmisi käike: proovige ennustada vastase käike ja asetage oma sümbolid nende strateegiate vastu.</p>



<p>&#8211; Ole oma lähenemisel paindlik: ära lukusta end ühte strateegiasse, ole valmis taktikat muutma olenevalt vastase käikudest.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Taiendavad_napunaited"></span>Täiendavad näpunäited<span class="ez-toc-section-end"></span></h4>



<p>&#8211; Ärge alahinnake &#8220;lihtsat&#8221; taset: isegi kui olete kogenud mängija, võib &#8220;lihtne&#8221; tase olla hea tava uute strateegiate testimiseks või mängu viimistlemiseks.</p>



<p>&#8211; Lõbutsege: Tic Toe mäng on lihtne ja lõbus mäng, mida saab kiiresti mängida. Kasutage iga mängu ära, et lõbutseda ja oma oskusi parandada.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kokkuvote_strateegiatest_kuidas_voita_tic-tac-toe_mangu_tehisintellekti"></span>Kokkuvõte strateegiatest, kuidas võita tic-tac-toe mängu tehisintellekti<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tuto pour jouer au morpion sur Google" width="500" height="281" src="https://www.youtube.com/embed/CbG0dxF02Uw?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p><br><strong>1. Mängureeglite mõistmine:</strong><br>Enne tehisintellekti võitmise strateegia väljatöötamist on oluline mõista Tic Toe mängu reegleid. Veenduge, et teate eesmärke, lubatud tegevusi ja võidukriteeriume. See võimaldab teil kogu mängu jooksul teha teadlikke otsuseid.</p>



<p><strong>2. Jälgige tehisintellekti käitumist:</strong><br>Üks esimesi samme AI ületamiseks on selle hoolikas jälgimine. Pange tähele tema liigutusi, mustreid, mida ta järgib, ja mis tahes vigu, mida ta teeb. See annab teile vihjeid tema kasutatavate strateegiate kohta ja aitab teil leida viise nende vastu võitlemiseks.</p>



<p><strong>3. Loo ootamatuid mustreid:</strong><br>Kui mõistate tehisintellekti toimingute mustreid, saate neid ootamatute mustrite loomisel oma eeliseks kasutada. Näiteks kui tehisintellekt eelistab horisontaalseid liikumisi, proovige seda petta vertikaalsete või diagonaalsete liigutuste tegemiseks. See võib häirida tema strateegiaid ja tekitada talle raskeid hetki.</p>



<p><strong>4. Blokeerige AI võiduvõimalused:</strong><br>Üks peamisi strateegiaid tehisintellekti võitmiseks on blokeerida selle võiduvõimalused. Kui näete, et tehisintellekt hakkab rea, veeru või diagonaali lõpetama, asetage oma sümbol kasti, mis takistab seda tegemast. See võib sundida teda oma võimalusi ümber hindama ja kasutama vähem etteaimatavat lähenemist.</p>



<p><strong>5. Ennustage tulevasi AI liikumisi.</strong><br>Tehisintellekti ületamiseks on oluline ette näha selle tulevasi liikumisi. Analüüsige mängupositsioone ja proovige ennustada, kuhu AI võib oma järgmise sümboli paigutada. See võimaldab teil tõhusalt blokeerida nende strateegiaid ja saada eeliseid võtmeväljade hõivamisega.</p>



<p><strong>6. Kasutage oma vigu ära:</strong><br>Kuigi tehisintellektid on üldiselt väga pädevad, võivad nad mõnikord teha vigu. Kui märkate viga, kasutage seda võimalust, et sellele vastu astuda ja saada eeliseid. Näiteks kui tehisintellekt unustab teie järgmise võidurea blokeerida, kasutage seda võimalust, et see lõpule viia ja mäng võita.</p>



<p>Neid strateegiaid järgides suurendate oma võimalusi lüüa Tic Toe mängus tehisintellekti. Pidage siiski meeles, et tehisintellektid võivad ka oma vigadest õppida ja kohaneda, seega on oluline kogu mängu vältel oma strateegiaid arendada ja täiustada.</p>



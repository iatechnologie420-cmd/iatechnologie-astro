---
title: "Mis on Datamart / andmeladu?"
slug: "mis-on-datamart-andmeladu"
excerpt: "Sissejuhatus Datamarti kontseptsiooni THE datamart on andmeanalüüsi ja äriteabe (BI) maailmas oluline termin. See on andmelao alamjaotis, st spetsiaalne andmebaas, mis salvestab ettevõtte teabe segmenti. Kui andmeladu võib pidada tohutuks ettevõtte andmete raamatukoguks, siis andmeturgu võib vaadelda kui selle teegi konkreetset jaotist, mis on korraldatud konkreetse teema, näiteks müügi, turunduse või inimressursi, ümber. Selles artiklis [&hellip;]"
date: "2024-03-09T12:15:47"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-1-3.png"
categories: ["arvutustehnika-ja-andmed-et", "tehnoloogia-ja-digitaalne-et"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="What is Data Mart | Beginners | Interview Question | Examples | Tutorial | Types | Features" width="500" height="281" src="https://www.youtube.com/embed/fGxe8l5q20E?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/et/mis-on-datamart-andmeladu/#Sissejuhatus_Datamarti_kontseptsiooni" >Sissejuhatus Datamarti kontseptsiooni</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/et/mis-on-datamart-andmeladu/#Andmemargi_maaratlus" >Andmemargi määratlus?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/et/mis-on-datamart-andmeladu/#Datamarti_eelised" >Datamarti eelised</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/et/mis-on-datamart-andmeladu/#Andmete_Mart_tuubid" >Andmete Mart tüübid</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/et/mis-on-datamart-andmeladu/#Datamarti_ja_Datawarehousei_vordlus" >Datamarti ja Datawarehouse&#8217;i võrdlus</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/et/mis-on-datamart-andmeladu/#Mis_on_andmeladu" >Mis on andmeladu?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/et/mis-on-datamart-andmeladu/#Mis_on_Datamart" >Mis on Datamart?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/et/mis-on-datamart-andmeladu/#Peamised_erinevused_disainis_ja_kasutuses" >Peamised erinevused disainis ja kasutuses</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/et/mis-on-datamart-andmeladu/#Datamarti_ja_Data_Warehousei_vahel_valimine" >Datamarti ja Data Warehouse&#8217;i vahel valimine</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/et/mis-on-datamart-andmeladu/#Tehnoloogiad_ja_turuosalised" >Tehnoloogiad ja turuosalised</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-11" href="/et/mis-on-datamart-andmeladu/#Data_Martsi_kasutusalad" >Data Martsi kasutusalad</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Sissejuhatus_Datamarti_kontseptsiooni"></span>Sissejuhatus Datamarti kontseptsiooni<span class="ez-toc-section-end"></span></h2>



<p>            THE <strong>datamart</strong> on andmeanalüüsi ja äriteabe (BI) maailmas oluline termin. See on andmelao alamjaotis, st spetsiaalne andmebaas, mis salvestab ettevõtte teabe segmenti. </p>



<p>Kui andmeladu võib pidada tohutuks ettevõtte andmete raamatukoguks, siis andmeturgu võib vaadelda kui selle teegi konkreetset jaotist, mis on korraldatud konkreetse teema, näiteks müügi, turunduse või inimressursi, ümber.</p>



<p>            Selles artiklis uurime, mida a <strong>datamart</strong>, milleks seda kasutatakse ja miks on nii oluline, et organisatsioonid, kes soovivad oma andmeid kasutada, saaksid teha teadlikke otsuseid ja parandada oma tegevust.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Andmemargi_maaratlus"></span>Andmemargi määratlus?<span class="ez-toc-section-end"></span></h3>



<p>            A <strong>datamart</strong> on loodud kasutajate vajaduste rahuldamiseks konkreetses funktsionaalses piirkonnas. See on teemadele orienteeritud ja struktureeritud, et aruandlust ja analüüsi oleks lihtne esitada. Näiteks müügiandmete turg sisaldaks andmeid, mis on seotud ainult müügitehingute, klientide ja müüdud toodetega.</p>



<p>            Andmemargi seadistamine on odavam ja kiirem kui täieliku andmelao loomine, muutes selle atraktiivseks konkreetsetele osakondadele, kes soovivad oma andmeanalüüsi täiustada, ootamata suuremahulist ettevõttelahendust.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Datamarti_eelised"></span>Datamarti eelised<span class="ez-toc-section-end"></span></h4>



<p>            Rakendamise peamised eelised a <strong>datamart</strong> sisaldab: </p>



<ul class="wp-block-list">
<li><strong>Toimivus:</strong> Olles väiksemad ja fokusseeritud, on päringud üldiselt kiiremad kui andmelao puhul.</li>



<li><strong>Lihtsus:</strong> ärikasutajatele on seda lihtsam mõista ja kasutada, kuna see on nende domeenile omane.</li>



<li><strong>Agility:</strong> Andmemarte saab välja töötada ja juurutada lühema ajaga kui andmelaod, mis võimaldab investeeringutelt kiiremat tasuvust.</li>



<li><strong>Paindlikkus:</strong> neid saab hõlpsamini kohandada või laiendada, et vastata muutuvatele aruandlusvajadustele.</li>



<li><strong>Töökindlus:</strong> need kipuvad olema asjakohasemad ja koondavad konkreetsete analüüside jaoks kasulikke andmeid.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Andmete_Mart_tuubid"></span>Andmete Mart tüübid<span class="ez-toc-section-end"></span></h4>



<p>            Andmeturgude kategoriseerimiseks on mitu võimalust, kuid teabe hankimise meetodi põhjal jagatakse need sageli kolme põhitüüpi.</p>



<ul class="wp-block-list">
<li><strong>Sõltumatu:</strong> andmemarket, mis luuakse andmeladu andmeallikana kasutamata. Tavaliselt on see väike ja seda haldab üks osakond.</li>



<li><strong>Sõltlane:</strong> andmemarket, mis on ehitatud olemasoleva andmelao andmete põhjal, tagades andmete järjepidevuse ja kvaliteedi organisatsiooni erinevate osade vahel.</li>



<li><strong>Terviklik:</strong> andmemarket, mis ühendab andmeid erinevatest allikatest, sealhulgas andmeladudest ja välistest operatiivandmebaasidest. See on keerulisem, kuid potentsiaalselt kõikehõlmavam lähenemisviis.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Datamarti_ja_Datawarehousei_vordlus"></span>Datamarti ja Datawarehouse&#8217;i võrdlus<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-.png" alt="" class="wp-image-1147" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-.png 1792w, /images/blog/Quest-ce-quun-Datamart--300x171.png 300w, /images/blog/Quest-ce-quun-Datamart--1024x585.png 1024w, /images/blog/Quest-ce-quun-Datamart--150x86.png 150w, /images/blog/Quest-ce-quun-Datamart--768x439.png 768w, /images/blog/Quest-ce-quun-Datamart--1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Mis_on_andmeladu"></span>Mis on andmeladu?<span class="ez-toc-section-end"></span></h3>



<p>A <strong>andmeladu</strong> on tsentraliseeritud andmebaas, mis on loodud toetama ettevõttesiseseid otsustusprotsesse. See on optimeeritud suure hulga heterogeensetest allikatest pärinevate ajalooliste andmete lugemiseks, koondamiseks ja analüüsimiseks. See annab tervikliku ülevaate ettevõtte tegevusest pikema aja jooksul.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mis_on_Datamart"></span>Mis on Datamart?<span class="ez-toc-section-end"></span></h4>



<p>Mis temasse puutub, siis a <strong>datamart</strong> on andmelao alamjaotis. See on suunatud konkreetsele osakonnale, funktsioonile või konkreetse teemaga seotud andmekogumile (nt müügi- või personaliressursid). Andmemart sisaldab vähem andmeid kui andmeladu ja on loodud kiiresti vastama konkreetse kasutajarühma jaoks kohandatud päringutele.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Peamised_erinevused_disainis_ja_kasutuses"></span>Peamised erinevused disainis ja kasutuses<span class="ez-toc-section-end"></span></h4>



<p>Peamine erinevus andmelao ja andmemargi vahel on nende ulatus ja ulatus. Andmeladu salvestab suurel hulgal andmeid kogu ettevõtte kohta, samas kui andmemarket keskendub vaid ühele ettevõtte aspektile. Siin on mõned eristavad omadused:</p>



<ul class="wp-block-list">
<li><strong>Andmete ulatus</strong>: Andmelaol on suurem ulatus ja ulatus ning seetõttu on seda kulukam ja keerulisem ülal pidada. Teisest küljest on konkreetset domeeni sihiv andmekeskus odavam ja hõlpsamini hallatav.</li>



<li><strong>Esitus</strong>: Andmekeskused suudavad oma spetsialiseerumise ja vähem töödeldavate andmete tõttu sageli päringutulemusi kiiremini pakkuda.</li>



<li><strong>Struktuur</strong>: Andmeladu integreerib mitmest allikast pärinevad andmed ja ühtlustab need, samas kui andmepark on sageli üles ehitatud ühe andmeallika või väikese hulga tihedalt seotud allikate ümber.</li>



<li><strong>Kasutajad</strong>: Andmeladusid kasutavad tavaliselt andmeanalüütikud, kes peavad omama täielikku ülevaadet ettevõttest, samas kui andmekeskused teenindavad konkreetsele domeenile spetsialiseerunud kasutajaid.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Datamarti_ja_Data_Warehousei_vahel_valimine"></span>Datamarti ja Data Warehouse&#8217;i vahel valimine<span class="ez-toc-section-end"></span></h4>



<p>Otsus keskenduda andmelaole või andmeturule sõltub suuresti organisatsiooni konkreetsetest vajadustest. Andmeladu on ideaalne ettevõtetele, kes vajavad kõigi oma andmete üksikasjalikku ja täielikku analüüsi. Teisest küljest võib andmemarketist piisata sihipäraste vajaduste rahuldamiseks ja kui eelarve on probleem, pakub see eeliseid lihtsuse ja kulude osas.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Tehnoloogiad_ja_turuosalised"></span>Tehnoloogiad ja turuosalised<span class="ez-toc-section-end"></span></h4>



<p>Turul pakuvad erinevaid andmelao ja data marti lahendusi infotehnoloogiasektori suuremad tegijad, nt <strong>Oraakel</strong>, <strong>Microsoft</strong> tema teenistusega <strong>Azure</strong>, <strong>Amazon</strong> koos <strong>AWS</strong>, <strong>Google&#8217;i pilveplatvorm</strong>ja teised andmehoidla ja äriteabe lahenduste pakkujad.</p>



<p>Lühidalt, kuigi mõnikord võib andmeturte ja andmeladusid pidada omavahel asendatavateks, on neil organisatsiooni andmehaldusstrateegias tegelikult väga erinev roll. Seetõttu peab otsuste tegemine põhinema nende erinevuste kindlal mõistmisel ning olema alati kooskõlas organisatsiooni eesmärkide ja võimalustega.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Data_Martsi_kasutusalad"></span>Data Martsi kasutusalad<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-1-1.png" alt="" class="wp-image-1148" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-1-1.png 1792w, /images/blog/Quest-ce-quun-Datamart-1-1-300x171.png 300w, /images/blog/Quest-ce-quun-Datamart-1-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-Datamart-1-1-150x86.png 150w, /images/blog/Quest-ce-quun-Datamart-1-1-768x439.png 768w, /images/blog/Quest-ce-quun-Datamart-1-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Data Martidel on andmehalduse valdkonnas mitmesuguseid rakendusi:</p>



<ul class="wp-block-list">
<li><strong>Sektori analüüs</strong>: Andmemargi saab kasutada konkreetse tööstusharuga (nt müügi, turunduse või rahanduse) seotud andmete koondamiseks, võimaldades konkreetsete toimingute ja suundumuste süvaanalüüsi.</li>



<li><strong>Projekti juht</strong>: projektimeeskondade jaoks võib andmemarket pakkuda olulist teavet edenemise, ressursside, kulude ja eelnevalt määratletud tähtaegade järgimise kohta.</li>



<li><strong>Isikupärastatud turundus</strong>: Turundusmeeskonnad saavad seda kasutada klientide täpsemaks sihtimiseks, analüüsides kogutud demograafiat, ostuharjumusi ja eelistusi.</li>



<li><strong>Regulatiivsed aruanded</strong>: Sisemiste või väliste aruandlus- ja auditeerimisprotsesside lihtsustamiseks saab luua spetsiaalseid andmeturte, koondades kõik eeskirjade järgimiseks vajalikud andmed.</li>
</ul>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-1-2.png" alt="" class="wp-image-1149" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-Datamart-1-2.png 1792w, /images/blog/Quest-ce-quun-Datamart-1-2-300x171.png 300w, /images/blog/Quest-ce-quun-Datamart-1-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-Datamart-1-2-150x86.png 150w, /images/blog/Quest-ce-quun-Datamart-1-2-768x439.png 768w, /images/blog/Quest-ce-quun-Datamart-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Datamarti edukas rakendamine sõltub ka kasutajate kaasamisest ja koolitusest, tagades, et nad mõistavad, kuidas süsteemi kasutada soovitud teabe iseseisvaks hankimiseks. Samuti on ülioluline tagada tõhus andmehaldus ning vastavus ettevõtte turva- ja privaatsuspoliitikaga.</p>



<p>A <strong>Datamart</strong> hästi kavandatud ja õigesti rakendatud võib saada ettevõtte jaoks võimsaks eeliseks, hõlbustades juurdepääsu teabele, parandades otsuste tegemist ja suurendades organisatsiooni paindlikkust. Keskendudes juurutamise peamistele etappidele ja seades prioriteediks lõppkasutajate vajadused, saavad ettevõtted maksimeerida oma Datamartide eeliseid ja integreerida need tõhusalt oma üldisesse andmehaldusstrateegiasse.</p>



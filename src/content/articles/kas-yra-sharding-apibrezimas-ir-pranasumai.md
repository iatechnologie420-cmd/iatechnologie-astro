---

title: "Kas yra Sharding? apibrėžimas ir pranašumai"
slug: "kas-yra-sharding-apibrezimas-ir-pranasumai"
excerpt: "Smulkinimo supratimas: apibrėžimas ir pagrindiniai principai Duomenų bazių ir didelio masto duomenų saugyklų pasaulis yra sudėtingas ir nuolat tobulinamas. Kad galėtų efektyviai valdyti eksponentiškai didėjančius duomenų kiekius, IT architektūros turi diegti naujoves ir rasti sprendimus, kaip optimizuoti šių duomenų veikimą ir valdymą. Vienas iš šios problemos būdų yra technika, vadinama skaldymas. Šiame straipsnyje apibrėžsime dalijimąsi, [&hellip;]"
date: "2024-03-09T12:32:06"
featuredImage: "/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-3.png"
categories: ["infrastruktura-ir-tinklai-lt", "technologijos-ir-skaitmeninis-lt"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Database Sharding and Partitioning" width="500" height="281" src="https://www.youtube.com/embed/wXvljefXyEo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Smulkinimo_supratimas_apibrezimas_ir_pagrindiniai_principai" >Smulkinimo supratimas: apibrėžimas ir pagrindiniai principai</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Kas_yra_Sharding" >Kas yra Sharding?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Kaip_veikia_dalijimasis" >Kaip veikia dalijimasis?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Dalijimosi_privalumai" >Dalijimosi privalumai</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Issukiai_ir_svarstymai" >Iššūkiai ir svarstymai</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Kaip_paskirstomi_duomenys" >Kaip paskirstomi duomenys?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Duomenu_saugojimas_sukese" >Duomenų saugojimas šukėse</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Dalijimosi_trukumai" >Dalijimosi trūkumai</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Techniniai_smulkinimo_issukiai" >Techniniai smulkinimo iššūkiai</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/lt/kas-yra-sharding-apibrezimas-ir-pranasumai/#Praktines_dalijimosi_aplinkybes" >Praktinės dalijimosi aplinkybės</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Smulkinimo_supratimas_apibrezimas_ir_pagrindiniai_principai"></span>Smulkinimo supratimas: apibrėžimas ir pagrindiniai principai<span class="ez-toc-section-end"></span></h2>



<p>Duomenų bazių ir didelio masto duomenų saugyklų pasaulis yra sudėtingas ir nuolat tobulinamas. Kad galėtų efektyviai valdyti eksponentiškai didėjančius duomenų kiekius, IT architektūros turi diegti naujoves ir rasti sprendimus, kaip optimizuoti šių duomenų veikimą ir valdymą. Vienas iš šios problemos būdų yra technika, vadinama <strong>skaldymas</strong>. </p>



<p>Šiame straipsnyje apibrėžsime dalijimąsi, suprasime pagrindinius jo principus ir kodėl tai būtina šiuolaikinėse duomenų bazių sistemose.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kas_yra_Sharding"></span>Kas yra Sharding?<span class="ez-toc-section-end"></span></h3>



<p>THE <strong>skaldymas</strong> yra horizontalaus duomenų skirstymo paskirstytoje duomenų bazėje arba duomenų bazių valdymo sistemoje metodas. Ši technika susideda iš duomenų bazės padalijimo į mažesnes dalis, vadinamas <em>šukės</em>, kuris gali būti paskirstytas keliuose serveriuose. Kiekviename fragmente yra duomenų poaibis ir ji veikia kaip nepriklausoma duomenų bazė. Pagrindinis to privalumas yra tas, kad jis leidžia efektyviau valdyti didelius duomenų kiekius ir operacijas, sumažinant kiekvieno atskiro serverio apkrovą.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kaip_veikia_dalijimasis"></span>Kaip veikia dalijimasis?<span class="ez-toc-section-end"></span></h4>



<p>Dalijimasis pagrįstas duomenų paskirstymo logika, kurią nustato dalijimosi algoritmas. Yra įvairių algoritmų, tačiau pasirinkimas dažnai priklauso nuo duomenų ir užklausų, kurias turi apdoroti sistema, pobūdžio. Įprasti algoritmų pavyzdžiai: skirstymas pagal diapazoną (kai duomenys paskirstomi pagal reikšmių diapazonus), maišos skirstymas (kai tam tikrų raktų maiša nustato duomenų vietą) arba dalijimasis pagal katalogą (su paieškos lentele, kad būtų galima rasti duomenys).</p>



<p>Sukūrus šukes ir paskirstius duomenis, dažnai vadinama centralizuota valdymo sistema <em>šukių valdytojas</em> Arba <em>sūpynės</em>, būtinas norint koordinuoti sandorius ir užklausas tarp skirtingų šukių. Ši sistema užtikrina, kad užklausos būtų nukreiptos į tinkamą skeveldrą, taip leidžiant sąveikauti tik su atitinkama duomenų bazės dalimi.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dalijimosi_privalumai"></span>Dalijimosi privalumai<span class="ez-toc-section-end"></span></h4>



<p>Dalijimasis turi keletą privalumų, dėl kurių jis patrauklus didelėms sistemoms:</p>



<ul class="wp-block-list">
<li><strong>Mastelio keitimas</strong> : Bendrinimas leidžia duomenų bazėms lengvai prisitaikyti prie padidėjusios apkrovos tiesiog pridedant daugiau serverių.</li>



<li><strong>Spektaklis</strong> : Sumažinus kiekvieno serverio apkrovą, užklausos našumas gali būti labai pagerintas, ypač rašymo operacijoms.</li>



<li><strong>Prieinamumas</strong> : Net jei viena skeveldra neveikia, kitos veikia toliau, padidindamos visos sistemos patikimumą.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Issukiai_ir_svarstymai"></span>Iššūkiai ir svarstymai<span class="ez-toc-section-end"></span></h4>



<p>Tačiau suskaidymas taip pat kelia tam tikrų iššūkių:</p>



<ul class="wp-block-list">
<li>Skaldelių tvarkymo sudėtingumas gali padidėti didėjant šukių skaičiui.</li>



<li>Operacijas, kurioms reikalinga informacija įvairiose skeveldrose, yra sudėtingiau valdyti.</li>



<li>Didėjant šukių skaičiui, gali būti sunkiau užtikrinti duomenų nuoseklumą.</li>
</ul>



<p>Taigi svarbu atidžiai apsvarstyti, ar dalijimas yra tinkama strategija konkrečiai programai. Kartais tinkamesni gali būti kiti metodai, pvz., vertikalus skaidymas, duomenų replikacija arba nesusijusios duomenų bazės naudojimas.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kaip_paskirstomi_duomenys"></span>Kaip paskirstomi duomenys?<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png" alt="" class="wp-image-1070" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Duomenų paskirstymas susmulkintoje aplinkoje gali būti vykdomas pagal skirtingus algoritmus. Štai keletas dažniausiai pasitaikančių:</p>



<ul class="wp-block-list">
<li><strong>Dalijimasis pagal raktų diapazoną:</strong> Duomenys skaidomi pagal konkretų raktą, kur kiekviena skeveldra yra atsakinga už verčių diapazoną.</li>



<li><strong>Maišos atskyrimas:</strong> Maišos funkcija naudojama nustatyti, kuri skeveldra saugos konkretų įrašą, remiantis raktu.</li>



<li><strong>Bendrinimas pagal katalogą:</strong> Katalogas palaiko įrašų ir šukių, kuriose jie saugomi, susiejimą.</li>
</ul>



<p>Šie metodai leidžia palyginti subalansuotai paskirstyti duomenis, sumažinti kliūtis ir pagerinti atsako laiką.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Duomenu_saugojimas_sukese"></span>Duomenų saugojimas šukėse<span class="ez-toc-section-end"></span></h4>



<p>Duomenys saugomi kiekvienoje skeveldrėje nepriklausomai nuo kitų šukių. Tai reiškia, kad kiekviena skeveldra veikia kaip atskira duomenų bazė su savo schemomis ir indeksais. Duomenų nuoseklumas tarp skeveldrų išlaikomas logiškai, o ne fiziškai, todėl kartais gali būti sudėtinga tvarkant operacijas, apimančias kelias dalis.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dalijimosi_trukumai"></span>Dalijimosi trūkumai<span class="ez-toc-section-end"></span></h4>



<p>Tačiau suskaidymas turi ir tam tikrų trūkumų:</p>



<ul class="wp-block-list">
<li><strong>Sudėtingumas:</strong> Kelių skeveldrų tvarkymas ir priežiūra gali tapti sudėtinga, ypač duomenų nuoseklumo ir operacijų valdymo srityse.</li>



<li><strong>Blogo platinimo rizika:</strong> Netolygus duomenų pasiskirstymas gali sukelti „karštuosius taškus“, kur kai kurios skeveldros yra perkraunamos.</li>



<li><strong>Išlaidos:</strong> Poreikis eksploatuoti ir valdyti daugiau infrastruktūros gali padidinti išlaidas.</li>



<li></li>
</ul>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png" alt="" class="wp-image-1071" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Techniniai_smulkinimo_issukiai"></span>Techniniai smulkinimo iššūkiai<span class="ez-toc-section-end"></span></h4>



<p>Smulkinimo diegimas kelia keletą techninių klausimų:</p>



<ul class="wp-block-list">
<li><strong>Dizaino sudėtingumas</strong> : Suplanuoti dalijimosi raktus yra labai svarbu ir tai turėtų būti daroma atsargiai, nes prastas dizainas gali sutrikdyti duomenų paskirstymą ir pakenkti sistemos efektyvumui.</li>



<li><strong>Skersinės užklausos</strong> : užklausų vykdymas keliose skeveldrose gali būti sudėtingas ir sudėtingas, nes tam reikia ryšio ir agregavimo mechanizmų tarp skeveldrų.</li>



<li><strong>Paskirstytos operacijos</strong> : operacijų vientisumo palaikymas keliose skeveldrose yra sudėtingas ir reikalauja sudėtingų koordinavimo protokolų ir užrakinimo mechanizmų.</li>



<li><strong>Mastelio keitimas</strong> : Nors dalijimas leidžia keisti mastelį, skeveldrų pridėjimas arba pašalinimas gali būti sudėtingas ir dažnai reikia perskirstyti duomenis.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Praktines_dalijimosi_aplinkybes"></span>Praktinės dalijimosi aplinkybės<span class="ez-toc-section-end"></span></h4>



<p>Be techninių iššūkių, reikia atsižvelgti į praktinius aspektus:</p>



<ul class="wp-block-list">
<li><strong>Kaina</strong> : Sudėtingas dalijimosi diegimas ir priežiūra gali sukelti didelių išlaidų aparatinei, programinei įrangai ir specializuotiems žmogiškiesiems ištekliams.</li>



<li><strong>Spektaklis</strong> : Pasirinkus netinkamą dalijimosi strategiją, gali sumažėti našumas, ypač jei apkrovos balansavimas nėra tinkamai valdomas.</li>



<li><strong>Duomenų nuoseklumas</strong> : Labai svarbu užtikrinti duomenų nuoseklumą visose skeveldrose, tačiau tai sunku pasiekti, ypač labai paskirstytoje aplinkoje.</li>



<li><strong>Techninė ekspertizė</strong> : norint valdyti suskirstymo sudėtingumą ir reaguoti į problemas, reikalingos gilios techninės žinios.</li>



<li><strong>Atsarginės kopijos ir atkūrimai</strong> : Atsarginių kopijų tvarkymas ir atkūrimas tampa sudėtingesnis naudojant dalijimą, nes šios operacijos turi būti koordinuojamos keliose skeveldrose.</li>
</ul>



<p>Apibendrinant galima pasakyti, kad nors dalijimasis yra galinga duomenų bazių, kurioms reikalingas aukštas našumo ir mastelio keitimo lygis, metodas, jis kelia daugybę iššūkių ir reikalauja svarbių praktinių sumetimų, kad būtų optimaliai įgyvendintas. Žinodamos problemas ir kruopščiai parengdamos dalijimosi strategiją, organizacijos gali visapusiškai pasinaudoti jos teikiamais pranašumais, tuo pačiu sumažindamos susijusią riziką ir išlaidas.</p>



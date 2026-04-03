---
title: "Mis on automaatkooder? Ülim juhend!"
slug: "mis-on-automaatkooder-ulim-juhend"
excerpt: "Autoencoders või autokodeerijad inglise keeles positsioneerida end võimsate tööriistadena masinõppe ja tehisintellekti valdkonnas. Neid spetsiaalseid närvivõrke kasutatakse mõõtmete vähendamiseks, anomaaliate tuvastamiseks, andmete müra vähendamiseks ja muuks. See artikkel tutvustab seda põnevat tehnoloogiat, tuues esile selle tööpõhimõtte, rakendused ja kasvava tähtsuse teadusuuringutes ja tööstuses. Mis on automaatkooder? A autoenkooder on kunstliku närvivõrgu tüüp, mida kasutatakse järelevalveta [&hellip;]"
date: "2024-03-09T12:05:36"
categories: ["arvutustehnika-ja-andmed-et", "tehnoloogia-ja-digitaalne-et"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tracking Corn &amp; Weed with Yolov5 and Auto Encoder - Tracker" width="500" height="281" src="https://www.youtube.com/embed/8-jWgsGWaR0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>Autoencoders või <em>autokodeerijad</em> inglise keeles positsioneerida end võimsate tööriistadena masinõppe ja tehisintellekti valdkonnas. Neid spetsiaalseid närvivõrke kasutatakse mõõtmete vähendamiseks, anomaaliate tuvastamiseks, andmete müra vähendamiseks ja muuks. See artikkel tutvustab seda põnevat tehnoloogiat, tuues esile selle tööpõhimõtte, rakendused ja kasvava tähtsuse teadusuuringutes ja tööstuses.</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/et/mis-on-automaatkooder-ulim-juhend/#Mis_on_automaatkooder" >Mis on automaatkooder?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-2" href="/et/mis-on-automaatkooder-ulim-juhend/#Kuidas_autoenkooderid_tootavad" >Kuidas autoenkooderid töötavad?</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-3" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoenkooderite_praktilised_rakendused" >Autoenkooderite praktilised rakendused</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-4" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoencoder_kodeerimine_kitsaskoht_ja_dekodeerimine" >Autoencoder: kodeerimine, kitsaskoht ja dekodeerimine</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/et/mis-on-automaatkooder-ulim-juhend/#Kodeerimine" >Kodeerimine</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/et/mis-on-automaatkooder-ulim-juhend/#Pudelikael" >Pudelikael</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/et/mis-on-automaatkooder-ulim-juhend/#Dekodeerimine" >Dekodeerimine</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoenkooderite_praktilised_rakendused_ja_variatsioonid" >Autoenkooderite praktilised rakendused ja variatsioonid</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoenkooderite_praktilised_rakendused-2" >Autoenkooderite praktilised rakendused</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/et/mis-on-automaatkooder-ulim-juhend/#Mootmete_vahendamine" >Mõõtmete vähendamine</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/et/mis-on-automaatkooder-ulim-juhend/#Murasummutus_mura_summutamine" >Mürasummutus (müra summutamine)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/et/mis-on-automaatkooder-ulim-juhend/#Andmete_tihendamine" >Andmete tihendamine</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/et/mis-on-automaatkooder-ulim-juhend/#Andmete_genereerimine_ja_imputeerimine" >Andmete genereerimine ja imputeerimine</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoencoderi_variandid" >Autoencoderi variandid</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/et/mis-on-automaatkooder-ulim-juhend/#Variatsioonilised_automaatkodeerijad_VAE" >Variatsioonilised automaatkodeerijad (VAE)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/et/mis-on-automaatkooder-ulim-juhend/#Horedad_automaatkodeerijad" >Hõredad automaatkodeerijad</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoenkooderite_mura_summutamine" >Autoenkooderite müra summutamine</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/et/mis-on-automaatkooder-ulim-juhend/#Jarjestikused_automaatkodeerijad" >Järjestikused automaatkodeerijad</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-19" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoencoderi_koolitamine_ja_koodinaited" >Autoencoderi koolitamine ja koodinäited</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoencoderi_koolitamise_protsess" >Autoencoderi koolitamise protsess</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-21" href="/et/mis-on-automaatkooder-ulim-juhend/#Naidiskood_Kerasega" >Näidiskood Kerasega</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-22" href="/et/mis-on-automaatkooder-ulim-juhend/#Nouanne_heaks_treeninguks" >Nõuanne heaks treeninguks</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-23" href="/et/mis-on-automaatkooder-ulim-juhend/#Autoenkooderite_rakendused" >Autoenkooderite rakendused</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Mis_on_automaatkooder"></span>Mis on automaatkooder?<span class="ez-toc-section-end"></span></h2>



<p>A <strong>autoenkooder</strong> on kunstliku närvivõrgu tüüp, mida kasutatakse järelevalveta õppimiseks. Autoencoderi peamine eesmärk on luua sisendandmete komplekti kompaktne esitus (kodeering) ja seejärel rekonstrueerida andmed selle esituse põhjal. Idee on tabada andmete kõige olulisemad aspektid, sageli mõõtmete vähendamiseks. Autoenkoodri struktuur koosneb tavaliselt kahest põhiosast:</p>



<ul class="wp-block-list">
<li><strong>Kodeerija</strong> (<em>Kodeerida</em>): See võrgu esimene osa vastutab sisendandmete tihendamise eest vähendatud kujul.</li>



<li><strong>Dekooder</strong> (<em>Dekodeerida</em>): Teine osa võtab vastu tihendatud kodeeringu ja proovib taastada algandmed.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kuidas_autoenkooderid_tootavad"></span>Kuidas autoenkooderid töötavad?<span class="ez-toc-section-end"></span></h2>



<p>Autoenkooderite tööd saab kirjeldada mitmes etapis:</p>



<ol class="wp-block-list">
<li>Võrk võtab andmeid vastu sisendina.</li>



<li>Kodeerija tihendab andmed funktsioonivektoriks, mida nimetatakse koodiks või varjatud ruumiks.</li>



<li>Dekooder võtab selle vektori ja proovib algandmeid rekonstrueerida.</li>



<li>Rekonstrueerimise kvaliteeti mõõdetakse kadufunktsiooni abil, mis hindab erinevust algsete sisendite ja rekonstrueeritud väljundite vahel.</li>



<li>Selle kadufunktsiooni minimeerimiseks kohandab võrk oma kaalu tagasilevimise algoritmide abil.</li>
</ol>



<p>Selle iteratiivse protsessi kaudu õpib automaatkooder andmeid tõhusalt esitama, pannes rõhku kõige olulisemate funktsioonide säilitamisele rekonstrueerimisprotsessi ajal.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Autoenkooderite_praktilised_rakendused"></span>Autoenkooderite praktilised rakendused<span class="ez-toc-section-end"></span></h3>



<p>Autoencoderid on väga mitmekülgsed ja neid saab rakendada mitmes valdkonnas:</p>



<ul class="wp-block-list">
<li><strong>Mõõtmete vähendamine</strong>: Nagu PCA (põhikomponentide analüüs), kuid mittelineaarse võimsusega.</li>



<li><strong>Müra vähendamine</strong>: nad on võimelised õppima andmetes leiduvat &#8220;müra&#8221; ignoreerima.</li>



<li><strong>Andmete tihendamine</strong>: nad saavad õppida kodeeringuid, mis on tõhusamad kui traditsioonilised tihendusmeetodid.</li>



<li><strong>Andmete genereerimine</strong>: varjatud ruumis navigeerides võimaldavad need luua uusi andmeeksemplare, mis sarnanevad algsete kirjetega.</li>



<li><strong>Anomaaliate tuvastamine</strong>: automaatkodeerijad võivad aidata tuvastada andmeid, mis ei sobi õpitud jaotusega.</li>
</ul>



<p>Lühidalt, automaatkodeerijate võime avastada ja määratleda andmete tähenduslikke omadusi muudab need iga AI-praktiku tööriistakomplekti kohustuslikuks vahendiks.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoder_kodeerimine_kitsaskoht_ja_dekodeerimine"></span>Autoencoder: kodeerimine, kitsaskoht ja dekodeerimine<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png" alt="" class="wp-image-1191" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kodeerimine"></span>Kodeerimine<span class="ez-toc-section-end"></span></h3>



<p>Kodeerimine ehk kodeerimisfaas hõlmab sisendandmete teisendamist tihendatud esituseks. Algandmed, mis võivad olla suured, sisestatakse autoencoder võrku. Võrgukihid vähendavad järk-järgult andmete mõõtmelisust, surudes olulise teabe väiksemasse esindusruumi. Iga võrgu kiht koosneb neuronitest, mis rakendavad mittelineaarseid teisendusi, kasutades näiteks aktiveerimisfunktsioone, nagu ReLU või Sigmoid, et jõuda andmete uue esituseni, mis säilitab olulist teavet .</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pudelikael"></span>Pudelikael<span class="ez-toc-section-end"></span></h4>



<p>Kitsaskoht on automaatkodeerija keskne osa, kus andmete esitus saavutab madalaima mõõtme, mida nimetatakse ka koodiks. Just see tihendatud esitus säilitab sisendandmete kõige olulisemad omadused. Kitsaskoht toimib filtrina, mis sunnib automaatkodeerijat õppima tõhusat viisi teabe tihendamiseks. Seda saab võrrelda andmete tihendamise vormiga, kuid pakkimist õpitakse andmetest automaatselt, mitte standardsete algoritmide abil.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dekodeerimine"></span>Dekodeerimine<span class="ez-toc-section-end"></span></h4>



<p>Dekodeerimise faas on kodeerimisega sümmeetriline samm, kus tihendatud esitus rekonstrueeritakse väljundi suunas, mille eesmärk on olla algsele sisendile võimalikult truu. Alates pudelikaela esitusest suurendab närvivõrk järk-järgult andmete mõõtmelisust. See on kodeerimise vastupidine protsess: järjestikused kihid rekonstrueerivad esialgsed omadused vähendatud esituse põhjal. Kui dekodeerimine on tõhus, peaks automaatkodeerija väljund olema algandmetele väga lähedane.</p>



<p>Järelevalveta õppimisel on automaatkodeerijad eriti kasulikud andmete aluseks oleva struktuuri mõistmiseks. Nende võrkude tõhusust ei mõõdeta mitte nende võime kaudu sisendeid täiuslikult reprodutseerida, vaid pigem nende võime järgi tabada koodi kõige olulisemad ja asjakohasemad andmete atribuudid. Seda koodi saab seejärel kasutada selliste ülesannete jaoks nagu mõõtmete vähendamine, visualiseerimine või isegi keerukamate arhitektuuride muude närvivõrkude eeltöötlus.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Autoenkooderite_praktilised_rakendused_ja_variatsioonid"></span>Autoenkooderite praktilised rakendused ja variatsioonid<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png" alt="" class="wp-image-1192" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>autoenkooder</strong>, tehisintellekti (AI) toiteallika süvaõppe arsenali põhikomponent, on närvivõrk, mis on loodud andmete kodeerimiseks madalama mõõtmega esitusviisiks ja nende dekomponeerimiseks nii, et asjakohane rekonstrueerimine on võimalik. Uurime neid <strong>praktilisi rakendusi</strong> ja selles põnevas valdkonnas esile kerkinud variante.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Autoenkooderite_praktilised_rakendused-2"></span>Autoenkooderite praktilised rakendused<span class="ez-toc-section-end"></span></h3>



<p>Autokodeerijad on leidnud tee paljudesse rakendustesse tänu nende võimele õppida tõhusaid ja sisukaid andmete esitusi ilma järelevalveta. siin on mõned näidised:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mootmete_vahendamine"></span>Mõõtmete vähendamine<span class="ez-toc-section-end"></span></h4>



<p>Sarnaselt PCA-ga (põhikomponentide analüüs) kasutatakse sageli autoenkoodereid <strong>mõõtmete vähendamine</strong>. See meetod võimaldab andmete töötlemist lihtsustada, vähendades arvesse võetavate muutujate arvu, säilitades samal ajal suurema osa algses andmekogumis sisalduvast teabest.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Murasummutus_mura_summutamine"></span>Mürasummutus (müra summutamine)<span class="ez-toc-section-end"></span></h4>



<p>Tänu oma võimele õppida osaliselt hävitatud andmetest sisendit rekonstrueerima, on automaatkodeerijad eriti kasulikud <strong>mürasummutus</strong>. Neil õnnestub kasulikke andmeid tuvastada ja taastada, hoolimata mürast.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Andmete_tihendamine"></span>Andmete tihendamine<span class="ez-toc-section-end"></span></h4>



<p>Õppides kodeerima andmeid kompaktsemale kujule, saab kasutada automaatkoodereid <strong>andmete tihendamine</strong>. Kuigi praktikas neid selleks otstarbeks veel laialdaselt ei kasutata, on nende potentsiaal märkimisväärne, eriti konkreetsete andmetüüpide tihendamiseks.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Andmete_genereerimine_ja_imputeerimine"></span>Andmete genereerimine ja imputeerimine<span class="ez-toc-section-end"></span></h4>



<p>Autoencoders on võimeline genereerima uusi andmeeksemplare, mis sarnanevad nende treeningandmetega. Seda võimet saab ka kasutada <strong>imputeerimine</strong>, mis hõlmab andmekogumis puuduvate andmete täitmist.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoderi_variandid"></span>Autoencoderi variandid<span class="ez-toc-section-end"></span></h3>



<p>Lisaks standardsele automaatkodeerijale on välja töötatud erinevaid variante, et kohaneda andmete ja vajalike ülesannetega. Siin on mõned märkimisväärsed variatsioonid:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Variatsioonilised_automaatkodeerijad_VAE"></span>Variatsioonilised automaatkodeerijad (VAE)<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>Variatsioonilised automaatkodeerijad</strong> (<strong>VAE</strong>) lisage stohhastiline kiht, mis võimaldab andmeid genereerida. VAE-d on eriti populaarsed sisu, näiteks piltide või muusika genereerimisel, kuna need võimaldavad toota uusi ja mitmekesiseid elemente, mis on sama mudeli järgi usutavad.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Horedad_automaatkodeerijad"></span>Hõredad automaatkodeerijad<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>hõredad autokoodrid</strong> sisaldama karistust, mis seab peidetud sõlmedes piiratud tegevuse. Need on tõhusad andmete eristavate omaduste avastamisel, mis muudab need kasulikuks <strong>klassifikatsioon</strong> ja <strong>anomaalia tuvastamine</strong>.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Autoenkooderite_mura_summutamine"></span>Autoenkooderite müra summutamine<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>denormaliseeritud automaatkodeerijad</strong> on loodud vastu pidama müra lisamisele sisendandmetesse. Need on võimsad tugevate esituste õppimiseks ja <strong>andmete eeltöötlus</strong> enne muude masinõppeülesannete sooritamist.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Jarjestikused_automaatkodeerijad"></span>Järjestikused automaatkodeerijad<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>järjestikused automaatkodeerijad</strong> töödelda andmeid, mis on organiseeritud jadadesse, nagu tekst või aegridad. Nad kasutavad teabe aja jooksul kodeerimiseks ja dekodeerimiseks sageli korduvaid võrke, nagu LSTM (Long Short-Term Memory).</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoderi_koolitamine_ja_koodinaited"></span>Autoencoderi koolitamine ja koodinäited<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png" alt="" class="wp-image-1193" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Koolitus a <strong>autoenkooder</strong> on muude rakenduste hulgas oluline ülesanne masinõppe valdkonnas mõõtmete vähendamiseks ja anomaaliate tuvastamiseks. Siin näeme, kuidas Pythoni ja raamatukogu abil sellist mudelit koolitada <strong>Keras</strong>, koodinäidetega, mida saate testida ja oma projektidega kohandada.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Autoencoderi_koolitamise_protsess"></span>Autoencoderi koolitamise protsess<span class="ez-toc-section-end"></span></h4>



<p>Autoenkoodri koolitamiseks kasutatakse tavaliselt kadumismõõdikut, nagu keskmine ruutviga (MSE), mis mõõdab erinevust algse sisendi ja selle rekonstrueerimise vahel. Treeningu eesmärk on seda kaotusfunktsiooni minimeerida.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Naidiskood_Kerasega"></span>Näidiskood Kerasega<span class="ez-toc-section-end"></span></h4>



<p>Siin on lihtne näide autoencoderi kasutamise treenimisest <strong>Keras</strong>:</p>



<pre class="wp-block-code"><code>

keras.layersist impordi sisend, tihe
keras.models impordist Mudel

# Sissepääsu suurus
# Latentse ruumi mõõde (funktsiooni esitus)
encoding_dim = 32

# Kodeerija määratlus
input_img = Sisend(kuju=(sisend_dim,))
kodeeritud = Tihe(kodeering_dim, aktiveerimine='relu')(input_img)

# Dekoodri määratlus
dekodeeritud = Tihe(sisend_dim, aktiveerimine='sigmoid')(kodeeritud)

# Autoencoder mudel
autoencoder = Mudel (sisend_img, dekodeeritud)

# Mudeli koostamine
autoencoder.comile(optimizer='adam', loss='binary_crossentropy')

# Autoencoder koolitus
autoencoder.fit(X_train,
                epohhid = 50,
                batch_size=256,
                shuffle=Tõsi,
                validation_data=(X_test, X_test))

</code></pre>



<p>Selles näites tähistavad X_train ja X_test treening- ja testiandmeid. Pange tähele, et automaatkoodrit on õpetatud ennustama väljundina oma sisendit &#8220;X_train&#8221;.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Nouanne_heaks_treeninguks"></span>Nõuanne heaks treeninguks<span class="ez-toc-section-end"></span></h4>



<p></p>



<p>Kasutage selliseid tehnikaid nagu <strong>ristvalideerimine</strong>, seal <strong>partii normaliseerimine</strong> ja <strong>tagasihelistamised</strong> Keras võib samuti aidata parandada autoencoder draivi jõudlust ja stabiilsust.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Autoenkooderite_rakendused"></span>Autoenkooderite rakendused<span class="ez-toc-section-end"></span></h4>



<p>Pärast treenimist saab automaatkoodereid kasutada:</p>



<ul class="wp-block-list">
<li>mõõtmete vähendamine,</li>



<li>anomaalia tuvastamine,</li>



<li>muude masinõppeülesannete jaoks kasulike deskriptorite juhendamata õppimine.</li>
</ul>



<p>Kokkuvõtteks võib öelda, et autoencoderi koolitamine on ülesanne, mis nõuab närvivõrgu arhitektuuride mõistmist ja kogemusi hüperparameetrite peenhäälestamisel. Autoenkooderite lihtsus ja paindlikkus muudavad need aga väärtuslikuks tööriistaks paljude andmetöötlusprobleemide lahendamisel.</p>



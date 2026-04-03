---
title: "PyGraft: viskas, ką reikia žinoti apie atvirojo kodo Python įrankį, skirtą DataViz"
slug: "pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz"
excerpt: "PyGraft: nauja atvirojo kodo „DataViz“ žvaigždė PyGraft pasirodo kaip perspektyvus įrankis, skirtas suteikti duomenų profesionalams ir entuziastams praturtinančios ir galingos patirties kuriant duomenų vizualizacijas. Pasižymi pažangiomis apdorojimo galimybėmis ir nepaprastu lankstumu, PyGraft yra projektas atviro kodo apie kurį jau pradėta kalbėti. Bet kas yra PyGraft ir kaip jis gali pakeisti jūsų požiūrį į DataViz? Pasinerkime [&hellip;]"
date: "2024-03-09T12:09:45"
categories: ["skaiciavimas-ir-duomenys-lt", "technologijos-ir-skaitmeninis-lt"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="How to create graph in Microsoft Excel | Microsoft Excel par graph kaise banaye | Graph in Excel" width="500" height="281" src="https://www.youtube.com/embed/FX8hKdFsljs?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#PyGraft_nauja_atvirojo_kodo_%E2%80%9EDataViz%E2%80%9C_zvaigzde" >PyGraft: nauja atvirojo kodo „DataViz“ žvaigždė</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Kas_yra_PyGraft" >Kas yra PyGraft?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Kodel_verta_rinktis_%E2%80%9EPyGraft%E2%80%9C_skirta_%E2%80%9EDataViz%E2%80%9C" >Kodėl verta rinktis „PyGraft“, skirtą „DataViz“?</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-4" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Is_kur_atsiranda_PyGraft" >Iš kur atsiranda PyGraft?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Darbo_su_PyGraft_pradzia" >Darbo su PyGraft pradžia</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Istekliai_ir_bendruomene_aplink_PyGraft" >Ištekliai ir bendruomenė aplink PyGraft</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-7" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Pagrindines_%E2%80%9EPyGraft%E2%80%9C_savybes_unikaliu_jo_galimybiu_tyrinejimas" >Pagrindinės „PyGraft“ savybės: unikalių jo galimybių tyrinėjimas</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-8" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Intuityvi_vartotojo_sasaja" >Intuityvi vartotojo sąsaja</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Integracija_su_Python_bibliotekomis" >Integracija su Python bibliotekomis</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Platus_diagramu_tipu_pasirinkimas" >Platus diagramų tipų pasirinkimas</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Dideliu_duomenu_palaikymas" >Didelių duomenų palaikymas</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Pygrafto_pajegumas_apibendrinti" >Pygrafto pajėgumas: apibendrinti</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-13" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Darbo_su_PyGraft_pradzia_praktinis_vadovas_vartotojams" >Darbo su PyGraft pradžia: praktinis vadovas vartotojams</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#PyGraft_diegimas" >PyGraft diegimas</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Jusu_duomenu_paruosimas" >Jūsų duomenų paruošimas</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Pirmosios_vizualizacijos_kurimas_naudojant_PyGraft" >Pirmosios vizualizacijos kūrimas naudojant PyGraft</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/lt/pygraft-viskas-ka-reikia-zinoti-apie-atvirojo-kodo-python-iranki-skirta-dataviz/#Narsykite_isplestines_funkcijas" >Naršykite išplėstines funkcijas</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="PyGraft_nauja_atvirojo_kodo_%E2%80%9EDataViz%E2%80%9C_zvaigzde"></span>PyGraft: nauja atvirojo kodo „DataViz“ žvaigždė<span class="ez-toc-section-end"></span></h2>



<p><strong>PyGraft</strong> pasirodo kaip perspektyvus įrankis, skirtas suteikti duomenų profesionalams ir entuziastams praturtinančios ir galingos patirties kuriant duomenų vizualizacijas. Pasižymi pažangiomis apdorojimo galimybėmis ir nepaprastu lankstumu, <strong>PyGraft</strong> yra projektas <strong>atviro kodo</strong> apie kurį jau pradėta kalbėti. </p>



<p>Bet kas yra PyGraft ir kaip jis gali pakeisti jūsų požiūrį į DataViz? Pasinerkime į šį įvadinį vadovą, kad sužinotume esminius jo pranašumus ir funkcijas.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kas_yra_PyGraft"></span>Kas yra PyGraft?<span class="ez-toc-section-end"></span></h3>



<p>PyGraft yra atvirojo kodo Python biblioteka, sukurta sintetinėms, bet tikroviškoms schemoms ir žinių diagramoms (KG) generuoti, remiantis vartotojo nurodytais parametrais. </p>



<p>Tai Python programavimo kalbos duomenų vizualizacijos biblioteka. Išnaudodama „Python“ galią, „PyGraft“ leidžia lengvai sukurti sudėtingas ir išsamias duomenų vizualizacijas su mažiau pastangų. </p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kodel_verta_rinktis_%E2%80%9EPyGraft%E2%80%9C_skirta_%E2%80%9EDataViz%E2%80%9C"></span>Kodėl verta rinktis „PyGraft“, skirtą „DataViz“?<span class="ez-toc-section-end"></span></h4>



<p>    Pagrindinis privalumas <strong>PyGraft</strong> slypi intuityviu požiūriu ir lengvu integravimu į duomenų mokslo darbo eigą. Nesvarbu, ar esate analitikas, duomenų mokslininkas ar tiesiog aistringas skaičiams, „PyGraft“ siūlo beveik neribotas galimybes paversti jūsų duomenis patraukliomis vaizdinėmis istorijomis. Kelių duomenų formatų palaikymas ir lengvas integravimas su populiariomis Python duomenų struktūromis, tokiomis kaip pandos, daro PyGraft ypač patrauklų.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Is_kur_atsiranda_PyGraft"></span>Iš kur atsiranda PyGraft?<span class="ez-toc-section-end"></span></h3>



<p>Šis projektas gimė bendradarbiaujant Lotaringijos universitetui ir kitoms institucijoms, ir juo siekiama suteikti galingą įrankį tyrimams tose srityse, kuriose duomenys gali būti jautrūs arba sunkiai gaunami. </p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Darbo_su_PyGraft_pradzia"></span>Darbo su PyGraft pradžia<span class="ez-toc-section-end"></span></h4>



<p>    Išbandyti <strong>PyGraft</strong> yra paprastas procesas. Įdiegę per paketų tvarkykles, tokias kaip pip, vartotojai gali iš karto pradėti tyrinėti įvairias PyGraft siūlomas funkcijas. Nuo pagrindinių grafikų generavimo iki interaktyvių ir dinamiškų vizualizacijų kūrimo, „PyGraft“ turi viską, ko jums reikia, kad padėtumėte pateikti duomenis aiškiausiai ir estetiškai.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Istekliai_ir_bendruomene_aplink_PyGraft"></span>Ištekliai ir bendruomenė aplink PyGraft<span class="ez-toc-section-end"></span></h4>



<p>    Būk projektas <strong>atviro kodo</strong> apima aktyvią bendruomenę ir gausius išteklius. Vartotojai <strong>PyGraft</strong> niekada nebūna vieni. Jie gali pasiekti išsamią dokumentaciją, mokymo programas, kodų pavyzdžius ir net forumus, kuriuose gali užduoti klausimus ir dalytis idėjomis. Bendradarbiavimas ir dalijimasis žiniomis yra giliai įsišakniję PyGraft dvasioje, todėl skatinamas švelnus ir bendradarbiaujantis mokymosi kreivė.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Pagrindines_%E2%80%9EPyGraft%E2%80%9C_savybes_unikaliu_jo_galimybiu_tyrinejimas"></span>Pagrindinės „PyGraft“ savybės: unikalių jo galimybių tyrinėjimas<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz.png" alt="" class="wp-image-1484" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz.png 1792w, /images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz-300x171.png 300w, /images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz-1024x585.png 1024w, /images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz-150x86.png 150w, /images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz-768x439.png 768w, /images/blog/PyGraft-tout-savoir-sur-le-nouvel-outil-Python-open-source-pour-la-DataViz-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Intuityvi_vartotojo_sasaja"></span>Intuityvi vartotojo sąsaja<span class="ez-toc-section-end"></span></h3>



<p>Viena iš pagrindinių stiprybių <strong>PyGraft</strong> yra jo <strong>vartotojo sąsaja</strong> sukurta siekiant maksimaliai padidinti efektyvumą ir sumažinti mokymosi kreivę. Ši sąsaja leidžia visų techninių įgūdžių vartotojams greitai ir be pastangų sukurti duomenų vizualizacijas. Nuvilkite ir numeskite, iš anksto sukurti šablonai ir gausi vizualizacijų biblioteka padeda supaprastinti naudotojo patirtį.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Integracija_su_Python_bibliotekomis"></span>Integracija su Python bibliotekomis<span class="ez-toc-section-end"></span></h4>



<p>Priemonė sklandžiai integruojasi su kitais <strong>Python bibliotekos</strong> naudojami duomenų analizei, pvz., NumPy ir Pandas. Tai leidžia vartotojams naudotis galingomis šių bibliotekų duomenų apdorojimo galimybėmis dirbant PyGraft aplinkoje vizualizavimui.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Platus_diagramu_tipu_pasirinkimas"></span>Platus diagramų tipų pasirinkimas<span class="ez-toc-section-end"></span></h4>



<p>Nesvarbu, ar jums reikia juostinių diagramų, geografinių žemėlapių ar sudėtingų taškinių diagramų, PyGraft turi įspūdingą įvairovę <strong>diagramų tipai</strong> Jūsų žinioje. Kiekvienas diagramos tipas yra labai pritaikomas, todėl vartotojas gali tiksliai suderinti visus vizualinius aspektus, kad tiksliai atitiktų jų duomenų pateikimo poreikius.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dideliu_duomenu_palaikymas"></span>Didelių duomenų palaikymas<span class="ez-toc-section-end"></span></h4>



<p>Su efektyviu valdymu <strong>dideli duomenų rinkiniai</strong>, PyGraft idealiai tinka aplinkoje, kurioje duomenų dydis gali būti kliūtis. Efektyvus išteklių panaudojimas ir apdorojimo našumas leidžia PyGraft tvarkyti didelius duomenų kiekius nepakenkiant vizualizacijos greičiui ar kokybei.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pygrafto_pajegumas_apibendrinti"></span>Pygrafto pajėgumas: apibendrinti<span class="ez-toc-section-end"></span></h4>



<p>Čia yra pagrindinių jo galimybių santrauka:</p>



<ul class="wp-block-list">
<li><strong>Lankstumas kartoje</strong> : PyGraft leidžia pagal užsakymą kurti diagramas, žinių grafikus (KG) arba abu, pritaikytus pagal konkrečius vartotojo poreikius.</li>



<li><strong>Išplėstinė konfigūracija</strong> : Jis suteikia išsamią generavimo proceso valdymą per platų vartotojo nurodytų parametrų spektrą, leidžiantį plačiai pritaikyti rezultatus.</li>



<li><strong>Semantinio žiniatinklio standartų laikymasis</strong> : Su PyGraft sukurtos konstrukcijos remiasi RDFS ir OWL standartais, garantuojančias semantiškai turtingas ir tarptautinius standartus atitinkančias schemas ir KG.</li>



<li><strong>Loginio nuoseklumo užtikrinimas</strong> : Sukurtų duomenų loginis nuoseklumas patikrinamas naudojant aprašomąją logiką HermiT, užtikrinantį gaminamų išteklių vientisumą ir patikimumą.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Darbo_su_PyGraft_pradzia_praktinis_vadovas_vartotojams"></span>Darbo su PyGraft pradžia: praktinis vadovas vartotojams<span class="ez-toc-section-end"></span></h2>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="PyGraft_diegimas"></span>PyGraft diegimas<span class="ez-toc-section-end"></span></h4>



<p>Įrengimas iš <strong>PyGraft</strong> yra pirmasis žingsnis kuriant savo vizualizacijas. Norėdami tai padaryti, atidarykite terminalą ir paleiskite šią komandą:</p>



<pre class="wp-block-code"><code>
pip įdiegti pygraft
</code></pre>



<p>Ši komanda atsisiųs ir įdiegs naujausią versiją <strong>PyGraft</strong> taip pat jo priklausomybės. Įsitikinkite, kad pip paketų tvarkyklė yra atnaujinta, kad išvengtumėte nesuderinamumo.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Jusu_duomenu_paruosimas"></span>Jūsų duomenų paruošimas<span class="ez-toc-section-end"></span></h4>



<p>Prieš pradėdami vizualizuoti duomenis naudodami <strong>PyGraft</strong>, būtina juos tinkamai paruošti. Tai dažnai apima duomenų valymą, struktūrizavimą į tinkamą formatą, pvz., „DataFrame“ su tokiomis bibliotekomis <strong>pandos</strong>, ir suprasti skirtingus kintamuosius, kuriuos norite ištirti.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pirmosios_vizualizacijos_kurimas_naudojant_PyGraft"></span>Pirmosios vizualizacijos kūrimas naudojant PyGraft<span class="ez-toc-section-end"></span></h4>



<p>Sukurkite pagrindinę vizualizaciją naudodami <strong>PyGraft</strong> reikia tik kelių kodo eilučių. Štai paprastas linijinės schemos piešimo pavyzdys:</p>



<pre class="wp-block-code"><code>
importuoti pygraftą kaip psl
importuoti pandas kaip pd

# Įkeliami jūsų duomenys
data = pd.read_csv('kelias/į/jūsų/failą.csv')

# Linijinės grafikos kūrimas
diagrama = pg.LineChart(duomenys)
chart.plot('x_column', 'y_column')
chart.show()

</code></pre>



<p>Šiame pavyzdyje mes importuojame reikiamas bibliotekas, įkeliame duomenų rinkinį iš CSV, sukuriame linijinę diagramą ir parodome rezultatą naudodami metodą</p>



<pre class="wp-block-code"><code>
Rodyti


</code></pre>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Narsykite_isplestines_funkcijas"></span>Naršykite išplėstines funkcijas<span class="ez-toc-section-end"></span></h4>



<p>Kartą susipažinę su pagrindais <strong>PyGraft</strong>, galite tyrinėti pažangesnes funkcijas, kad praturtintumėte savo vizualizacijas, pvz., pridėti interaktyvumo, koreguoti spalvas, mastelius arba integruoti kelias diagramas į vieną ekraną. Oficiali svetainė <strong>PyGraft</strong> siūlo išsamią dokumentaciją ir pavyzdžius.</p>



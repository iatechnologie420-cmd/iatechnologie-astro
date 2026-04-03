---

title: "De Turing-test begrijpen"
slug: "de-turing-test-begrijpen"
excerpt: "Oorsprong en principes van de Turing-test In de wereld van kunstmatige intelligentie (AI) en computing neemt de Turing-test een prominente plaats in. Dit is een benchmarkmethode die is ontworpen om het vermogen van een machine om menselijke intelligentie te imiteren te evalueren. De oorsprong en principes van deze revolutionaire test dateren uit het midden van [&hellip;]"
date: "2024-03-09T12:57:31"
featuredImage: "/images/blog/Bien-comprendre-le-test-de-Turing-3.png"
categories: ["ai-training-en-basisbeginselen-nl"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Comprendre le test de Turing facilement en 2 minutes" width="500" height="281" src="https://www.youtube.com/embed/XnFvfWWqosY?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/nl/de-turing-test-begrijpen/#Oorsprong_en_principes_van_de_Turing-test" >Oorsprong en principes van de Turing-test</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/nl/de-turing-test-begrijpen/#De_geschiedenis_van_de_Turingtest" >De geschiedenis van de Turingtest</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/nl/de-turing-test-begrijpen/#Fundamenteel_principe_van_de_Turing-test" >Fundamenteel principe van de Turing-test</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/nl/de-turing-test-begrijpen/#Uitvoering_van_de_Turing-test" >Uitvoering van de Turing-test</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/nl/de-turing-test-begrijpen/#Implicaties_en_problemen_van_de_Turing-test" >Implicaties en problemen van de Turing-test</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/nl/de-turing-test-begrijpen/#De_criteria_voor_een_succesvolle_Turing-test" >De criteria voor een succesvolle Turing-test</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/nl/de-turing-test-begrijpen/#Criterium_voor_menselijke_ononderscheidbaarheid" >Criterium voor menselijke ononderscheidbaarheid</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/nl/de-turing-test-begrijpen/#Duur_en_voorwaarden_van_de_test" >Duur en voorwaarden van de test</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/nl/de-turing-test-begrijpen/#Evaluatie_van_de_resultaten_en_controverse" >Evaluatie van de resultaten en controverse</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/nl/de-turing-test-begrijpen/#Rol_van_menselijke_interactie" >Rol van menselijke interactie</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-11" href="/nl/de-turing-test-begrijpen/#De_evolutie_van_de_Turing-test_in_het_AI-tijdperk" >De evolutie van de Turing-test in het AI-tijdperk</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-12" href="/nl/de-turing-test-begrijpen/#De_originele_Turing-test_en_zijn_beperkingen" >De originele Turing-test en zijn beperkingen</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/nl/de-turing-test-begrijpen/#Vooruitgang_in_AI_en_de_evolutie_van_de_Turing-test" >Vooruitgang in AI en de evolutie van de Turing-test</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/nl/de-turing-test-begrijpen/#De_complexiteit_van_de_Turing-test" >De complexiteit van de Turing-test</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/nl/de-turing-test-begrijpen/#De_toekomst_van_de_Turing-test" >De toekomst van de Turing-test</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Oorsprong_en_principes_van_de_Turing-test"></span>Oorsprong en principes van de Turing-test<span class="ez-toc-section-end"></span></h2>



<p>In de wereld van kunstmatige intelligentie (AI) en computing neemt de Turing-test een prominente plaats in. Dit is een benchmarkmethode die is ontworpen om het vermogen van een machine om menselijke intelligentie te imiteren te evalueren. De oorsprong en principes van deze revolutionaire test dateren uit het midden van de 20e eeuw en zijn gebaseerd op complexe filosofische en computationele concepten.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="De_geschiedenis_van_de_Turingtest"></span>De geschiedenis van de Turingtest<span class="ez-toc-section-end"></span></h3>



<p>De Turing-test ontleent zijn naam aan zijn uitvinder, Alan Turing, een Britse wiskundige die wordt beschouwd als een van de pioniers van de informatica. Hij presenteerde deze test voor het eerst in zijn artikel uit 1950 “Computing Machinery and Intelligence”, gepubliceerd in het Britse tijdschrift Mind. Alan Turing onderzoekt de vraag of machines kunnen denken en stelt een methode voor om kunstmatige intelligentie te evalueren.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Fundamenteel_principe_van_de_Turing-test"></span>Fundamenteel principe van de Turing-test<span class="ez-toc-section-end"></span></h4>



<p>Het basisprincipe van de Turing-test is opmerkelijk eenvoudig. Het is gebaseerd op een imitatiespel waarbij een mens, de rechter, de taak heeft om te bepalen of zijn gesprekspartner een machine of een ander mens is. De rechter communiceert met de twee gesprekspartners via een scherm en een toetsenbord, wat de onmogelijkheid garandeert om voor de uitspraak op fysieke aanwijzingen te vertrouwen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Uitvoering_van_de_Turing-test"></span>Uitvoering van de Turing-test<span class="ez-toc-section-end"></span></h4>



<p>De test wordt als volgt uitgevoerd:<br>1. De rechter stelt schriftelijk diverse vragen.<br>2. De menselijke gesprekspartner en de machine reageren eveneens schriftelijk.<br>3. Indien de rechter de machine niet voldoende van de mens kan onderscheiden, slaagt de machine voor de test.<br>Het doel is om te zien of een machine kan concurreren met de menselijke intelligentie op een niveau waarop de reacties niet te onderscheiden zijn van die van een man of vrouw.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Implicaties_en_problemen_van_de_Turing-test"></span>Implicaties en problemen van de Turing-test<span class="ez-toc-section-end"></span></h4>



<p>De Turingtest heeft belangrijke filosofische en technische implicaties. Het nodigt uit tot reflectie over de aard van het denken en bewustzijn en wat ware intelligentie inhoudt. Op technisch vlak heeft de test aanzienlijke vooruitgang op het gebied van AI en natuurlijke taalverwerking gestimuleerd. Systemen zoals IBM Watson of stemassistenten zoals <strong>Siri</strong> van<strong>Appel</strong>, <strong>Google Assistent</strong> En <strong>Alexa</strong> van<strong>Amazone</strong> zijn hedendaagse voorbeelden van pogingen om machines te creëren die mogelijk de Turing-test zouden kunnen doorstaan.</p>



<p>De Turingtest blijft een onderwerp van discussie en debat, vooral over de validiteit en relevantie ervan bij het evalueren van kunstmatige intelligentie. Terwijl sommigen beweren dat de test alleen de gesprekssimulator meet en niet per se intelligentie, zien anderen het als een uitdaging voor toekomstige AI-ontwikkelingen.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="De_criteria_voor_een_succesvolle_Turing-test"></span>De criteria voor een succesvolle Turing-test<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Bien-comprendre-le-test-de-Turing.png" alt="" class="wp-image-806" srcset="/images/blog/Bien-comprendre-le-test-de-Turing.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Een succesvolle Turing-test is een manier om de intelligentie van een machine te meten door het vermogen ervan te beoordelen om menselijk gedrag te imiteren tot het punt waarop een menselijke waarnemer geen onderscheid kan maken tussen de reacties van de machine en die van een echte persoon. Op het gebied van kunstmatige intelligentie blijft de beroemde Turing-test, voorgesteld door Alan Turing in 1950, een referentie die centraal staat in veel discussies over het bewustzijn en de intelligentie van machines. Wat zijn de criteria waaraan moet worden voldaan voordat een Turing-test als succesvol kan worden beschouwd?</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Criterium_voor_menselijke_ononderscheidbaarheid"></span>Criterium voor menselijke ononderscheidbaarheid<span class="ez-toc-section-end"></span></h3>



<p>Het centrale doel van de Turing-test is om te testen of een menselijke ondervrager in staat is een machine van een mens te onderscheiden, simpelweg op basis van hun antwoorden op vragen of uitspraken. Als de gesprekspartner niet met zekerheid kan zeggen of de antwoorden van een mens of een machine komen, wordt de test als geslaagd beschouwd. Met dit in gedachten moeten verschillende criteria in acht worden genomen:</p>



<p>&#8211; <strong>Kwaliteit van de reacties</strong> : Ze moeten samenhangend zijn en natuurlijk lijken, alsof ze van een mens komen.<br>&#8211; <strong>Diversiteit in gesprek</strong> : Het vermogen van de machine om deel te nemen aan een breed scala aan onderwerpen duidt op een vorm van begrip of aanpassing.<br>&#8211; <strong>Omgaan met onduidelijkheden</strong> : een machine moet in staat zijn om met de subtiliteiten en nuances van taal om te gaan, inclusief metaforen, humor en culturele verwijzingen.<br>&#8211; <strong>Emotie en empathie</strong>: Kunstmatige intelligentie moet een vorm van empathie of passende emotionele reactie op situaties tonen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Duur_en_voorwaarden_van_de_test"></span>Duur en voorwaarden van de test<span class="ez-toc-section-end"></span></h4>



<p>Er bestaat geen gestandaardiseerde duur voor een Turing-test, maar algemeen wordt aangenomen dat een langere periode de betrouwbaarheid van de verkregen resultaten kan vergroten. Voor een geldige toets zijn daarnaast de volgende voorwaarden van belang:</p>



<p>&#8211; <strong>Totale anonimiteit</strong> : De ondervrager mag geen visuele of hoorbare aanwijzingen hebben die hem kunnen helpen de entiteit achter de antwoorden te identificeren.<br>&#8211; <strong>Neutrale communicatie-interface</strong> : Reacties moeten via een toetsenbord en scherm worden verzonden om discriminatie op basis van stem of handschrift te voorkomen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Evaluatie_van_de_resultaten_en_controverse"></span>Evaluatie van de resultaten en controverse<span class="ez-toc-section-end"></span></h4>



<p>Beoordelingen moeten gebaseerd zijn op objectieve criteria, hoewel het subjectieve oordeel van de menselijke interviewer een centrale rol speelt in de uiteindelijke beslissing. De volgende aspecten zijn cruciaal:<br>&#8211; <strong>Successtatistieken</strong> : het percentage keren dat rechters worden misleid is een belangrijke indicator.<br>&#8211; <strong>Controle van bias</strong> : Vooringenomenheid van de vragensteller moet worden geminimaliseerd door een goede beoordelingsmethode om de eerlijkheid van de toets te garanderen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Rol_van_menselijke_interactie"></span>Rol van menselijke interactie<span class="ez-toc-section-end"></span></h4>



<p>Interacties tijdens de Turing-test moeten natuurlijk en vloeiend zijn en de stroom van een echt menselijk gesprek nabootsen. Er moet rekening worden gehouden met de volgende elementen:<br>&#8211; <strong>Reactiviteit</strong> : De machine moet vragen beantwoorden in een tempo dat vergelijkbaar is met dat van een normaal menselijk gesprek.<br>&#8211; <strong>Interactie in twee richtingen</strong> : De machine moet niet alleen vragen beantwoorden, maar ook vragen kunnen stellen om te laten zien dat hij het gesprek volgt en er actief aan deelneemt.</p>



<p>Een succesvolle Turing-test is niet slechts een kwestie van één keer een gesprekspartner misleiden, maar dit consequent doen, onder verschillende omstandigheden en met verschillende rechters. Hoewel deze test veel wordt besproken en soms bekritiseerd vanwege het gebrek aan nauwkeurigheid van het daadwerkelijke begrip of bewustzijn van een AI, blijft het een interessante uitdaging voor AI-ontwerpers.<strong>AI</strong>. Dit is met name het geval voor bedrijven die voorop lopen op het gebied van technologische innovatie, zoals <strong>Googlen</strong> met zijn assistent of <strong>OpenAI</strong> met GPT-3 / GPT-4, die steeds geavanceerdere systemen proberen te creëren. </p>



<p>Hoewel nog geen enkele machine de Turing-test heeft doorstaan ​​door een mens perfect te imiteren, dwingt de vooruitgang op het gebied van kunstmatige intelligentie ons ertoe voortdurend de grenzen van wat een machine kan bereiken opnieuw te beoordelen.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="De_evolutie_van_de_Turing-test_in_het_AI-tijdperk"></span>De evolutie van de Turing-test in het AI-tijdperk<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Bien-comprendre-le-test-de-Turing-2.png" alt="" class="wp-image-808" srcset="/images/blog/Bien-comprendre-le-test-de-Turing-2.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-2-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-2-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-2-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>De Turing-test, ontworpen door Alan Turing in de jaren vijftig, had tot doel het vermogen van een machine te beoordelen om menselijk gedrag zo te imiteren dat de gesprekspartner niet meer kan onderscheiden of zijn correspondent een mens of een machine is. In het tijdperk van AI blijft de Turing-test dienen als maatstaf voor het meten van de evolutie van kunstmatige intelligentie, ook al is deze bekritiseerd en opnieuw ontworpen vanwege dramatische technologische vooruitgang.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="De_originele_Turing-test_en_zijn_beperkingen"></span>De originele Turing-test en zijn beperkingen<span class="ez-toc-section-end"></span></h3>



<p>Oorspronkelijk is de Turing-test een test van tekstuele conversatie tussen mens en machine. Het doel is om te bepalen of de machine een gesprek kan voeren dat niet te onderscheiden is van dat van een mens. Deze test heeft echter beperkingen. Het doorstaan ​​van de test betekent niet noodzakelijkerwijs dat de machine echte intelligentie of begrip heeft, maar eenvoudigweg dat hij een mens voor een korte tijd kan overtuigen van zijn menselijkheid.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Vooruitgang_in_AI_en_de_evolutie_van_de_Turing-test"></span>Vooruitgang in AI en de evolutie van de Turing-test<span class="ez-toc-section-end"></span></h3>



<p>Met de snelle vooruitgang van kunstmatige intelligentie is eenvoudige tekstuitwisseling niet langer voldoende om de verfijning van een AI te beoordelen. Huidige systemen, zoals ontwikkeld door <strong>Googlen</strong> Of <strong>Open AI</strong>, zijn in staat complexe gesprekken te voeren, muziek te componeren, realistische beelden te genereren en zelfs samenhangende teksten te schrijven over een veelheid aan onderwerpen.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="De_complexiteit_van_de_Turing-test"></span>De complexiteit van de Turing-test<span class="ez-toc-section-end"></span></h3>



<p>Om zich aan te passen aan de evolutie van AI, stellen onderzoekers uitgebreidere versies van de Turing-test voor. Deze nieuwe versies zouden multimodale interactie met machines (tekst, beeld, geluid), creativiteitstests of beoordelingen van begrip en gezond verstand kunnen omvatten, om zo de grenzen van kunstmatige intelligentie veel verder te verleggen dan eenvoudige imitatie.</p>



<p>Hier zijn voorbeelden van situaties die de evolutie van de Turing-test vertegenwoordigen, toegepast op het moderne tijdperk van AI:</p>



<p>&#8211; Diepgaande gesprekken over specifieke thema&#8217;s<br>&#8211; Creatie van originele artistieke inhoud<br>&#8211; Reacties op onverwachte gebeurtenissen of nieuwe informatie<br>&#8211; Realtime interactie met de omgeving, bijvoorbeeld via robots</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="De_toekomst_van_de_Turing-test"></span>De toekomst van de Turing-test<span class="ez-toc-section-end"></span></h2>



<p>Het oorspronkelijke idee van de Turing-test evolueert nu naar een bredere reeks beoordelingen, bedoeld om niet alleen het vermogen om te imiteren, maar ook de autonomie, het leren, de creativiteit en de empathie van kunstmatige intelligentie te testen. Deze tests meten niet langer simpelweg de kwaliteit van imitatie, maar proberen te evalueren in hoeverre een AI als intelligent kan worden beschouwd volgens voortdurend evoluerende menselijke criteria.</p>



<p>De Turing Test blijft zich ontwikkelen naast de ongelooflijke vooruitgang op het gebied van kunstmatige intelligentie. De essentie ervan blijft echter hetzelfde: proberen te begrijpen hoe dicht technologie bij de menselijke intelligentie kan komen en deze mogelijk kan overtreffen. </p>



<p>In deze zoektocht ligt de kern van de fascinatie voor AI en de toekomstige ontwikkelingen ervan.</p>



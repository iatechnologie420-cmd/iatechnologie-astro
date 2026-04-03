---

title: "De stelling van Bayes en het gebruik ervan in AI"
slug: "de-stelling-van-bayes-en-het-gebruik-ervan-in-ai"
excerpt: "Inleiding tot de stelling van Bayes DE De stelling van Bayes is een fundamentele formule in waarschijnlijkheid en statistiek die het bijwerken van onze overtuigingen beschrijft in de aanwezigheid van nieuwe informatie. Deze stelling, genoemd ter ere van dominee Thomas Bayes, speelt een cruciale rol op veel gebieden, variërend van machinaal leren tot besluitvorming onder [&hellip;]"
date: "2024-03-09T12:13:52"
categories: ["computers-en-gegevens-nl", "technologie-en-digitaal-nl"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Probabilités S3 Probabilités Conditionnelles: le Théorème de Bayes #ep14" width="500" height="281" src="https://www.youtube.com/embed/cCQlN6FhHvo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Inleiding_tot_de_stelling_van_Bayes" >Inleiding tot de stelling van Bayes</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#De_essentie_van_de_stelling_van_Bayes" >De essentie van de stelling van Bayes</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Toepassing_van_de_stelling_van_Bayes" >Toepassing van de stelling van Bayes</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Belang_in_AI_en_Machine_Learning" >Belang in AI en Machine Learning</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Grondbeginselen_van_Bayesiaanse_gevolgtrekking" >Grondbeginselen van Bayesiaanse gevolgtrekking</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#De_stelling_van_Bayes" >De stelling van Bayes</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#A_priori_en_posterieure_waarschijnlijkheden" >A priori en posterieure waarschijnlijkheden</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Bewijs" >Bewijs</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Bayesiaanse_gevolgtrekking_in_de_praktijk" >Bayesiaanse gevolgtrekking in de praktijk</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-10" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#De_stelling_van_Bayes_in_machine_learning-algoritmen" >De stelling van Bayes in machine learning-algoritmen</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-11" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#De_toepassing_van_de_stelling_van_Bayes_in_AI" >De toepassing van de stelling van Bayes in AI</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Het_belang_van_Bayesiaans_leren" >Het belang van Bayesiaans leren</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#Voorbeelden_van_Bayesiaanse_algoritmen" >Voorbeelden van Bayesiaanse algoritmen</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/nl/de-stelling-van-bayes-en-het-gebruik-ervan-in-ai/#De_stelling_van_Bayes_in_de_praktijk" >De stelling van Bayes in de praktijk</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Inleiding_tot_de_stelling_van_Bayes"></span>Inleiding tot de stelling van Bayes<span class="ez-toc-section-end"></span></h2>



<p>DE <strong>De stelling van Bayes</strong> is een fundamentele formule in waarschijnlijkheid en statistiek die het bijwerken van onze overtuigingen beschrijft in de aanwezigheid van nieuwe informatie. Deze stelling, genoemd ter ere van dominee Thomas Bayes, speelt een cruciale rol op veel gebieden, variërend van machinaal leren tot besluitvorming onder onzekerheid.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="De_essentie_van_de_stelling_van_Bayes"></span>De essentie van de stelling van Bayes<span class="ez-toc-section-end"></span></h3>



<p>Het hart van <strong>De stelling van Bayes</strong> is de voorwaardelijke waarschijnlijkheid. In zijn eenvoudigste vorm drukt het uit hoe een posterieure waarschijnlijkheid wordt bijgewerkt ten opzichte van een a priori waarschijnlijkheid door rekening te houden met de waarschijnlijkheid van de waargenomen gebeurtenis. Met andere woorden, het maakt het mogelijk om de initiële waarschijnlijkheden te herzien op basis van nieuw bewijsmateriaal.</p>



<p>Het wordt doorgaans weergegeven in de vorm van de volgende vergelijking:</p>



<p><strong>P(A|B) = (P(B|A) * P(A)) / P(B)</strong></p>



<p>Of :</p>



<ul class="wp-block-list">
<li><strong>P(A|B)</strong> is de waarschijnlijkheid van gebeurtenis A gegeven B (posteriori waarschijnlijkheid)</li>



<li><strong>P(B|A)</strong> is de waarschijnlijkheid van gebeurtenis B gegeven A</li>



<li><strong>VADER)</strong> is de initiële waarschijnlijkheid van gebeurtenis A (a priori waarschijnlijkheid)</li>



<li><strong>P(B)</strong> is de initiële waarschijnlijkheid van gebeurtenis B</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Toepassing_van_de_stelling_van_Bayes"></span>Toepassing van de stelling van Bayes<span class="ez-toc-section-end"></span></h4>



<p>De toepassing van <strong>De stelling van Bayes</strong> kan voorkomen in verschillende praktische scenario&#8217;s, zoals medische diagnoses, spamfilters of statistische gevolgtrekkingen in wetenschappelijk onderzoek. In de geneeskunde maakt de stelling het bijvoorbeeld mogelijk om op basis van de uitslag van een test de waarschijnlijkheid in te schatten dat een patiënt een ziekte heeft, waarbij de waarschijnlijkheid bekend is dat deze test juist of fout positief is.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Belang_in_AI_en_Machine_Learning"></span>Belang in AI en Machine Learning<span class="ez-toc-section-end"></span></h4>



<p>Op het gebied van kunstmatige intelligentie (AI) en <strong>machinaal leren</strong>De stelling van Bayes is de hoeksteen van het Bayesiaanse leren. Dit leerraamwerk maakt gebruik van eerdere overtuigingen en werkt deze bij met nieuwe gegevens om voorspellingen te doen. Als gevolg hiervan kunnen modellen nauwkeuriger worden naarmate ze aanvullende gegevens ontvangen.</p>



<p>Samenvattend: de <strong>De stelling van Bayes</strong> is een krachtig hulpmiddel voor het begrijpen van voorwaardelijke waarschijnlijkheden en voor het verfijnen van onze overtuigingen door rekening te houden met nieuwe informatie. De wiskundige eenvoud ervan staat in contrast met de brede implicaties en toepassingen ervan, waardoor het een basisonderwerp is dat je moet lezen voor iedereen die geïnteresseerd is in statistiek, besluitvorming en kunstmatige intelligentie.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Grondbeginselen_van_Bayesiaanse_gevolgtrekking"></span>Grondbeginselen van Bayesiaanse gevolgtrekking<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA.png" alt="" class="wp-image-1314" srcset="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA.png 1792w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-300x171.png 300w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1024x585.png 1024w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-150x86.png 150w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-768x439.png 768w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>Bayesiaanse gevolgtrekking</strong> is een tak van de statistiek die een theoretisch raamwerk biedt voor het interpreteren van gebeurtenissen in termen van waarschijnlijkheden. Het is gebaseerd op de <strong>De stelling van Bayes</strong>, een formule voor het bijwerken van de waarschijnlijkheid dat een gebeurtenis plaatsvindt in het licht van nieuwe gegevens. </p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="De_stelling_van_Bayes"></span>De stelling van Bayes<span class="ez-toc-section-end"></span></h3>



<p>De stelling van Bayes vormt de ruggengraat van de Bayesiaanse gevolgtrekking. Wiskundig gezien wordt het als volgt weergegeven:</p>



<p><strong>P(H|E) = (P(E|H) * P(H)) / P(E)</strong></p>



<p>Of :</p>



<ul class="wp-block-list">
<li><strong>P(H|E)</strong> is de waarschijnlijkheid dat hypothese H weet dat gebeurtenis E heeft plaatsgevonden.</li>



<li><strong>P(E|H)</strong> is de waarschijnlijkheid dat gebeurtenis E zal plaatsvinden als hypothese H waar is.</li>



<li><strong>P(H)</strong> is de a priori waarschijnlijkheid van hypothese H voordat de gegevens E worden gezien.</li>



<li><strong>P(E)</strong> is de a priori waarschijnlijkheid van gebeurtenis E.</li>
</ul>



<p>Deze stelling stelt ons dus in staat onze overtuigingen in termen van waarschijnlijkheid op basis van de hypothese H bij te werken nadat we ons bewust zijn geworden van de gebeurtenis E.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="A_priori_en_posterieure_waarschijnlijkheden"></span>A priori en posterieure waarschijnlijkheden<span class="ez-toc-section-end"></span></h4>



<p>Twee sleutelconcepten in de Bayesiaanse gevolgtrekking zijn de noties van waarschijnlijkheid <strong>a priori</strong> En <strong>a posteriori</strong> :</p>



<ul class="wp-block-list">
<li>De kans <strong>a priori</strong>, aangeduid met P(H), vertegenwoordigt wat we weten voordat we rekening houden met de nieuwe informatie.</li>



<li>De kans <strong>a posteriori</strong>, aangeduid met P(H|E), vertegenwoordigt wat we weten nadat we rekening hebben gehouden met de nieuwe informatie.</li>
</ul>



<p>Bayesiaanse gevolgtrekking omvat het overgaan van de voorafgaande waarschijnlijkheid naar de latere waarschijnlijkheid met behulp van de stelling van Bayes.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Bewijs"></span>Bewijs<span class="ez-toc-section-end"></span></h4>



<p>In de stelling van Bayes wordt P(E) vaak de factor van genoemd<strong>bewijs</strong>. Het kan worden beschouwd als een maatstaf voor de compatibiliteit van de waargenomen gegevens met alle mogelijke hypothesen. In de praktijk fungeert het als een normaliserende factor bij het actualiseren van onze overtuigingen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Bayesiaanse_gevolgtrekking_in_de_praktijk"></span>Bayesiaanse gevolgtrekking in de praktijk<span class="ez-toc-section-end"></span></h4>



<p>In de praktijk wordt Bayesiaanse gevolgtrekking op veel gebieden gebruikt, zoals machinaal leren, statistische gegevensanalyse, besluitvorming in aanwezigheid van onzekerheid, enz. Het maakt met name het volgende mogelijk:</p>



<ul class="wp-block-list">
<li>Probabilistische voorspellende modellen ontwikkelen.</li>



<li>Om afwijkingen te detecteren of verborgen patronen in complexe gegevens af te leiden.</li>



<li>Beslissingen nemen op basis van onvolledige of onzekere gegevens.</li>
</ul>



<p>L&#8217;<strong>Bayesiaanse gevolgtrekking</strong> biedt een krachtig raamwerk voor het redeneren met onzekerheid en het op coherente wijze integreren van nieuwe informatie. De toepassingen ervan zijn enorm en het gebruik ervan op geavanceerde gebieden zoals<strong>kunstmatige intelligentie</strong> waar de <strong>grote gegevens</strong> groeit voortdurend. Het begrijpen van de fundamentele principes ervan is daarom essentieel voor degenen die de wereld willen interpreteren door het prisma van waarschijnlijkheid.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="De_stelling_van_Bayes_in_machine_learning-algoritmen"></span>De stelling van Bayes in machine learning-algoritmen<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1.png" alt="" class="wp-image-1315" srcset="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1.png 1792w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-300x171.png 300w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-1024x585.png 1024w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-150x86.png 150w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-768x439.png 768w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>De wereld van kunstmatige intelligentie (AI) evolueert voortdurend, en een van de fundamentele concepten die deze revolutie aanwakkeren is de stelling van Bayes. Dit wiskundige hulpmiddel speelt een cruciale rol in machine learning-algoritmen, waardoor machines weloverwogen beslissingen kunnen nemen op basis van waarschijnlijkheid.</p>



<p>DE <strong>De stelling van Bayes</strong>, ontwikkeld door ds. Thomas Bayes in de 18e eeuw, is een formule die de voorwaardelijke waarschijnlijkheid van een gebeurtenis beschrijft, gebaseerd op voorkennis die verband houdt met die gebeurtenis. Formeel maakt het het mogelijk om de waarschijnlijkheid (P(A|B)) van een gebeurtenis A te berekenen, wetende dat B waar is, met behulp van de waarschijnlijkheid van B, wetende dat A waar is (P(B|A)), de waarschijnlijkheid van A ( P(A) ), en de waarschijnlijkheid van B ( P(B) ).</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="De_toepassing_van_de_stelling_van_Bayes_in_AI"></span>De toepassing van de stelling van Bayes in AI<span class="ez-toc-section-end"></span></h3>



<p>In de context van machinaal leren wordt de stelling van Bayes toegepast om probabilistische modellen te bouwen. Deze modellen kunnen hun voorspellingen aanpassen op basis van nieuwe gegevens, waardoor continue verbetering en verfijning van de prestaties mogelijk is. Dit proces is vooral nuttig bij classificatie, waarbij het doel is om een ​​label toe te kennen aan een bepaalde invoer op basis van waargenomen kenmerken.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Het_belang_van_Bayesiaans_leren"></span>Het belang van Bayesiaans leren<span class="ez-toc-section-end"></span></h4>



<p>Een van de belangrijkste voordelen van Bayesiaans leren is het vermogen om met onzekerheid om te gaan en een zekere mate van vertrouwen in voorspellingen te bieden. Dit is van fundamenteel belang op cruciale terreinen als de geneeskunde of de financiële wereld, waar elke voorspelling grote gevolgen kan hebben. Bovendien biedt deze aanpak een raamwerk voor het integreren van voorkennis en het leren van kleine hoeveelheden gegevens.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Voorbeelden_van_Bayesiaanse_algoritmen"></span>Voorbeelden van Bayesiaanse algoritmen<span class="ez-toc-section-end"></span></h4>



<p>Er zijn verschillende machine learning-algoritmen die afhankelijk zijn van de stelling van Bayes, waaronder:</p>



<ul class="wp-block-list">
<li><strong>Naïeve Bayes</strong>: Een probabilistische classificator die, ondanks zijn &#8216;naïeve&#8217; naam, opmerkelijk is vanwege zijn eenvoud en effectiviteit, vooral wanneer de waarschijnlijkheid van de kenmerken onafhankelijk is.</li>



<li><strong>Bayesiaanse netwerken</strong>: Een grafisch model dat probabilistische relaties tussen een reeks variabelen weergeeft, en dat kan worden gebruikt voor voorspellingen, classificatie en besluitvorming.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="De_stelling_van_Bayes_in_de_praktijk"></span>De stelling van Bayes in de praktijk<span class="ez-toc-section-end"></span></h4>



<p>Om de implementatie van Bayesiaans leren te illustreren, kunnen we een eenvoudige voorbeeldtoepassing overwegen: spamfiltering in e-mails. Een algoritme gebruiken <strong>Naïeve Bayes</strong>kan een systeem leren legitieme berichten van spam te onderscheiden door de waarschijnlijkheid te berekenen dat een e-mail spam is, op basis van de frequentie waarmee bepaalde trefwoorden voorkomen. </p>



<p>Naarmate het systeem nieuwe e-mails ontvangt, past het zijn kansen aan en wordt het steeds nauwkeuriger in zijn classificaties.</p>



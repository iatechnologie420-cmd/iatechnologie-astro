---

title: "Hvað er Sharding? skilgreiningu og kostum"
slug: "hvad-er-sharding-skilgreiningu-og-kostum"
excerpt: "Skilningur á klippingu: skilgreiningu og grundvallarreglur Heimur gagnagrunna og stórfelldra gagnageymslu er flókinn og í stöðugri þróun. Til að stjórna á áhrifaríkan hátt veldishraða auknu magni gagna verður upplýsingatækniarkitektúr að gera nýsköpun og finna lausnir til að hámarka frammistöðu og stjórnun þessara gagna. Ein nálgun á þetta vandamál er tækni sem kallast riftun. Í þessari [&hellip;]"
date: "2024-03-09T12:30:58"
featuredImage: "/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-3.png"
categories: ["innvidir-og-net-is", "taekni-og-stafraen-is"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Database Sharding and Partitioning" width="500" height="281" src="https://www.youtube.com/embed/wXvljefXyEo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Skilningur_a_klippingu_skilgreiningu_og_grundvallarreglur" >Skilningur á klippingu: skilgreiningu og grundvallarreglur</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Hvad_er_Sharding" >Hvað er Sharding?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Hvernig_virkar_klipping" >Hvernig virkar klipping?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Kostir_Sharding" >Kostir Sharding</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Askoranir_og_hugleidingar" >Áskoranir og hugleiðingar</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Hvernig_er_gognunum_dreift" >Hvernig er gögnunum dreift?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Gagnageymsla_i_molum" >Gagnageymsla í molum</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Okostir_Sharding" >Ókostir Sharding</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Taeknilegar_askoranir_vid_klippingu" >Tæknilegar áskoranir við klippingu</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/is/hvad-er-sharding-skilgreiningu-og-kostum/#Hagnyt_atridi_fyrir_klippingu" >Hagnýt atriði fyrir klippingu</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Skilningur_a_klippingu_skilgreiningu_og_grundvallarreglur"></span>Skilningur á klippingu: skilgreiningu og grundvallarreglur<span class="ez-toc-section-end"></span></h2>



<p>Heimur gagnagrunna og stórfelldra gagnageymslu er flókinn og í stöðugri þróun. Til að stjórna á áhrifaríkan hátt veldishraða auknu magni gagna verður upplýsingatækniarkitektúr að gera nýsköpun og finna lausnir til að hámarka frammistöðu og stjórnun þessara gagna. Ein nálgun á þetta vandamál er tækni sem kallast <strong>riftun</strong>. </p>



<p>Í þessari grein munum við skilgreina sundrun, skilja grunnreglur þess og hvers vegna það er nauðsynlegt í nútíma gagnagrunnskerfum.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Hvad_er_Sharding"></span>Hvað er Sharding?<span class="ez-toc-section-end"></span></h3>



<p>THE <strong>riftun</strong> er aðferð til að skipta gögnum lárétt í dreifðan gagnagrunn eða gagnagrunnsstjórnunarkerfi. Þessi tækni felst í því að skipta gagnagrunninum í smærri hluta sem kallast <em>brot</em>, sem hægt er að dreifa á nokkra netþjóna. Hvert brot inniheldur undirmengi gagna og virkar sem sjálfstæður gagnagrunnur. Helsti kosturinn við þetta er að það gerir kleift að stjórna miklu magni af gögnum og viðskiptum á skilvirkari hátt með því að draga úr álagi á hvern einstakan netþjón.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hvernig_virkar_klipping"></span>Hvernig virkar klipping?<span class="ez-toc-section-end"></span></h4>



<p>Kljúfur er byggður á gagnadreifingarrökfræði sem er ákvörðuð af skurðaralgrími. Það eru mismunandi reiknirit, en valið fer oft eftir eðli gagna og fyrirspurna sem kerfið þarf að sinna. Algeng dæmi um reiknirit eru sviðsbundin sundrun (þar sem gögnum er dreift í samræmi við gildissvið), kjötkássabrot (þar sem kjötkássa tiltekinna lykla ákvarðar staðsetningu gagna) eða sundrun möppu byggt (með uppflettitöflu til að finna gögnin).</p>



<p>Þegar brotin eru búin til og gögnunum dreift, miðstýrt stjórnunarkerfi, oft kallað <em>brotastjóri</em> Eða <em>sveifla</em>, er nauðsynlegt til að samræma viðskipti og beiðnir á milli mismunandi brota. Þetta kerfi tryggir að fyrirspurnum sé beint að réttu broti og leyfir þannig samskipti við aðeins viðkomandi hluta gagnagrunnsins.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kostir_Sharding"></span>Kostir Sharding<span class="ez-toc-section-end"></span></h4>



<p>Rífun býður upp á nokkra kosti sem gera það aðlaðandi fyrir stór kerfi:</p>



<ul class="wp-block-list">
<li><strong>Skalanleiki</strong> : Sharding gerir gagnagrunnum kleift að laga sig auðveldlega að auknu álagi með því einfaldlega að bæta við fleiri netþjónum.</li>



<li><strong>Frammistaða</strong> : Með því að draga úr álagi á hvern netþjón er hægt að bæta árangur fyrirspurna til muna, sérstaklega fyrir skrifaðgerðir.</li>



<li><strong>Framboð</strong> : Jafnvel þótt eitt brot sé niðri halda hinir áfram að virka og auka áreiðanleika kerfisins í heild.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Askoranir_og_hugleidingar"></span>Áskoranir og hugleiðingar<span class="ez-toc-section-end"></span></h4>



<p>Hins vegar fylgir riftun líka sinn hlut af áskorunum:</p>



<ul class="wp-block-list">
<li>Flókið við að stjórna brotum getur aukist með fjölda brota.</li>



<li>Viðskipti sem krefjast upplýsinga um mismunandi brot eru flóknari í stjórnun.</li>



<li>Gagnasamkvæmni gæti orðið erfiðara að tryggja eftir því sem fjöldi brota vex.</li>
</ul>



<p>Þess vegna er mikilvægt að íhuga vandlega hvort klipping sé rétta aðferðin fyrir tiltekið forrit. Stundum gætu aðrar aðferðir eins og lóðrétt skipting, gagnaafritun eða notkun ótengtbundinnar gagnagrunns hentað betur.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hvernig_er_gognunum_dreift"></span>Hvernig er gögnunum dreift?<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png" alt="" class="wp-image-1070" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Gagnadreifing í sundurskornu umhverfi er hægt að framkvæma samkvæmt mismunandi reikniritum. Hér eru nokkrar af þeim algengustu:</p>



<ul class="wp-block-list">
<li><strong>Skipting byggt á lykilsviði:</strong> Gögnum er skipt í samræmi við ákveðinn lykil, þar sem hver brot er ábyrg fyrir ýmsum gildum.</li>



<li><strong>Hash-undirstaða klipping:</strong> Hash aðgerð er notuð til að ákvarða hvaða shard geymir tiltekna skrá, byggt á lykli.</li>



<li><strong>Samnýting sem byggir á möppu:</strong> Mappa heldur utan um kortlagningu milli skráa og brotanna þar sem þær eru geymdar.</li>
</ul>



<p>Þessar aðferðir leyfa tiltölulega jafna dreifingu gagna, draga úr flöskuhálsum og bæta viðbragðstíma.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gagnageymsla_i_molum"></span>Gagnageymsla í molum<span class="ez-toc-section-end"></span></h4>



<p>Gögn eru geymd í hverju broti óháð öðrum brotum. Þetta þýðir að hvert brot virkar sem sjálfstæður gagnagrunnur, með eigin skema og vísitölum. Gagnasamkvæmni á milli brota er viðhaldið rökrétt frekar en líkamlega, sem getur stundum leitt til margbreytileika þegar stjórnað er viðskiptum sem spanna mörg brot.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Okostir_Sharding"></span>Ókostir Sharding<span class="ez-toc-section-end"></span></h4>



<p>Hins vegar hefur riftun einnig ákveðna ókosti:</p>



<ul class="wp-block-list">
<li><strong>Flækjustig:</strong> Að stjórna og viðhalda mörgum brotum getur orðið flókið, sérstaklega fyrir gagnasamkvæmni og viðskiptastjórnun.</li>



<li><strong>Hætta á lélegri dreifingu:</strong> Ójöfn dreifing gagna getur leitt til „heitra punkta“ þar sem sum brot eru ofhlaðin.</li>



<li><strong>Kostnaður:</strong> Þörfin á að reka og stjórna fleiri innviðum getur aukið kostnað.</li>



<li></li>
</ul>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png" alt="" class="wp-image-1071" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Taeknilegar_askoranir_vid_klippingu"></span>Tæknilegar áskoranir við klippingu<span class="ez-toc-section-end"></span></h4>



<p>Innleiðing klippingar vekur upp nokkrar tæknilegar spurningar:</p>



<ul class="wp-block-list">
<li><strong>Flækjustig í hönnun</strong> : Það skiptir sköpum að tímasetja klippingarlykla og ætti að fara varlega þar sem léleg hönnun getur leitt til ójafnvægis í dreifingu gagna og skert skilvirkni kerfisins.</li>



<li><strong>Þverstæðar fyrirspurnir</strong> : Að framkvæma fyrirspurnir á mörgum brotum getur verið flókið og fyrirferðarmikið vegna þess að það krefst samskipta og samsöfnunaraðferða milli brota.</li>



<li><strong>Dreifð viðskipti</strong> : Það er flókið að viðhalda heiðarleika viðskipta á mörgum brotum og krefst háþróaðra samhæfingarferla og læsingaraðferða.</li>



<li><strong>Skala</strong> : Þrátt fyrir að klipping gefi færi á sveigjanleika, getur það verið flókið að bæta við eða fjarlægja brot eftir það og krefjast oft endurdreifingar gagna.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hagnyt_atridi_fyrir_klippingu"></span>Hagnýt atriði fyrir klippingu<span class="ez-toc-section-end"></span></h4>



<p>Fyrir utan tæknilegar áskoranir eru hagnýt atriði sem þarf að taka tillit til:</p>



<ul class="wp-block-list">
<li><strong>Kostnaður</strong> : Það hversu flókið það er að innleiða og viðhalda sundrun getur haft í för með sér verulegan kostnað hvað varðar vélbúnað, hugbúnað og sérhæfðan mannauð.</li>



<li><strong>Frammistaða</strong> : Að velja óviðeigandi klippingaraðferð getur leitt til lélegrar frammistöðu, sérstaklega ef álagsjafnvægi er ekki vel stjórnað.</li>



<li><strong>Gagnasamræmi</strong> : Að tryggja samræmi í gögnum í öllum brotum er nauðsynlegt en erfitt að ná, sérstaklega í mjög dreifðu umhverfi.</li>



<li><strong>Tækniþekking</strong> : Djúp tækniþekking er nauðsynleg til að stjórna margbreytileika klippingar og bregðast við vandamálum.</li>



<li><strong>Afrit og endurheimt</strong> : Umsjón með öryggisafritum og endurheimtum verður flóknari við klippingu, vegna þess að þessar aðgerðir verða að vera samræmdar yfir nokkur brot.</li>
</ul>



<p>Að lokum, þó að klipping sé öflug tækni fyrir gagnagrunna sem krefjast mikils frammistöðu og sveigjanleika, þá skapar hún fjölda áskorana og krefst verulegra hagnýtra íhugunar til að vera útfært sem best. Með því að vera meðvituð um vandamálin og undirbúa sundrunarstefnuna vandlega geta stofnanir notið góðs af ávinningi hennar á sama tíma og tilheyrandi áhættu og kostnaði er lágmarkað.</p>



---

title: "Að skilja Turing prófið"
slug: "ad-skilja-turing-profid"
excerpt: "Uppruni og meginreglur Turing prófsins Í heimi gervigreindar (AI) og tölvunar skipar Turing prófið áberandi sess. Þetta er viðmiðunaraðferð sem er hönnuð til að meta getu vélar til að líkja eftir mannlegri greind. Uppruni og meginreglur þessa byltingarkennda prófs ná aftur til miðrar 20. aldar og eru byggðar á flóknum heimspeki- og reiknihugtökum. Saga Turing [&hellip;]"
date: "2024-03-09T12:56:14"
featuredImage: "/images/blog/Bien-comprendre-le-test-de-Turing-3.png"
categories: ["ai-thjalfun-og-grundvallaratridi-is"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Comprendre le test de Turing facilement en 2 minutes" width="500" height="281" src="https://www.youtube.com/embed/XnFvfWWqosY?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/ad-skilja-turing-profid/#Uppruni_og_meginreglur_Turing_profsins" >Uppruni og meginreglur Turing prófsins</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/ad-skilja-turing-profid/#Saga_Turing_profsins" >Saga Turing prófsins</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/ad-skilja-turing-profid/#Grundvallarregla_Turing_profsins" >Grundvallarregla Turing prófsins</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/is/ad-skilja-turing-profid/#Framkvaemd_Turing_profsins" >Framkvæmd Turing prófsins</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/is/ad-skilja-turing-profid/#Afleidingar_og_vandamal_Turing_profsins" >Afleiðingar og vandamál Turing prófsins</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/is/ad-skilja-turing-profid/#Skilyrdi_fyrir_arangursrikt_Turing_prof" >Skilyrði fyrir árangursríkt Turing próf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/is/ad-skilja-turing-profid/#Vidmidun_um_oadgreinanleika_mannsins" >Viðmiðun um óaðgreinanleika mannsins</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/ad-skilja-turing-profid/#Lengd_og_skilyrdi_profsins" >Lengd og skilyrði prófsins</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/ad-skilja-turing-profid/#Mat_a_arangri_og_deilur" >Mat á árangri og deilur</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/is/ad-skilja-turing-profid/#Hlutverk_mannlegra_samskipta" >Hlutverk mannlegra samskipta</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-11" href="/is/ad-skilja-turing-profid/#THroun_Turing_profsins_a_gervigreindartimanum" >Þróun Turing prófsins á gervigreindartímanum</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-12" href="/is/ad-skilja-turing-profid/#Upprunalega_Turing_profid_og_takmarkanir_thess" >Upprunalega Turing prófið og takmarkanir þess</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/is/ad-skilja-turing-profid/#Framfarir_i_gervigreind_og_throun_Turing_profsins" >Framfarir í gervigreind og þróun Turing prófsins</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/is/ad-skilja-turing-profid/#Flaekjustig_Turing_profsins" >Flækjustig Turing prófsins</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/is/ad-skilja-turing-profid/#Framtid_Turing_profsins" >Framtíð Turing prófsins</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Uppruni_og_meginreglur_Turing_profsins"></span>Uppruni og meginreglur Turing prófsins<span class="ez-toc-section-end"></span></h2>



<p>Í heimi gervigreindar (AI) og tölvunar skipar Turing prófið áberandi sess. Þetta er viðmiðunaraðferð sem er hönnuð til að meta getu vélar til að líkja eftir mannlegri greind. Uppruni og meginreglur þessa byltingarkennda prófs ná aftur til miðrar 20. aldar og eru byggðar á flóknum heimspeki- og reiknihugtökum.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Saga_Turing_profsins"></span>Saga Turing prófsins<span class="ez-toc-section-end"></span></h3>



<p>Turing prófið dregur nafn sitt af uppfinningamanni þess, Alan Turing, breskum stærðfræðingi sem er talinn einn af frumkvöðlum tölvunarfræðinnar. Hann kynnti þetta próf fyrst í grein sinni „Computing Machinery and Intelligence“ árið 1950 sem birt var í breska tímaritinu Mind. Alan Turing kannar spurninguna um hvort vélar geti hugsað og leggur til aðferð til að meta gervigreind.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Grundvallarregla_Turing_profsins"></span>Grundvallarregla Turing prófsins<span class="ez-toc-section-end"></span></h4>



<p>Grunnreglan í Turing prófinu er ótrúlega einföld. Það er byggt á eftirlíkingu leik þar sem manneskjan, dómarinn, hefur það verkefni að ákvarða hvort viðmælandi hans sé vél eða önnur manneskja. Dómarinn hefur samskipti við viðmælendurna tvo í gegnum skjá og lyklaborð, sem tryggir að ómögulegt sé að treysta á líkamlegar vísbendingar fyrir dóminn.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Framkvaemd_Turing_profsins"></span>Framkvæmd Turing prófsins<span class="ez-toc-section-end"></span></h4>



<p>Prófið er gert sem hér segir:<br>1. Dómari spyr ýmissa spurninga skriflega.<br>2. Mannlegur viðmælandi og vélin svara einnig skriflega.<br>3. Ef dómarinn getur ekki greint vélina nægilega frá manneskjunni, stenst vélin prófið.<br>Markmiðið er að sjá hvort vél geti keppt við mannlega upplýsingaöflun að því marki að viðbrögð hennar séu óaðgreinanleg frá svörum karls eða konu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Afleidingar_og_vandamal_Turing_profsins"></span>Afleiðingar og vandamál Turing prófsins<span class="ez-toc-section-end"></span></h4>



<p>Turing prófið hefur mikilvægar heimspekilegar og tæknilegar afleiðingar. Það hvetur til umhugsunar um eðli hugsunar og meðvitundar og hvað felur í sér sanna greind. Á tæknilegu stigi hefur prófið hvatt til verulegra framfara á sviði gervigreindar og náttúrulegrar málvinnslu. Kerfi eins og IBM Watson eða raddaðstoðarmenn eins og <strong>Siri</strong> af<strong>Epli</strong>, <strong>Google aðstoðarmaður</strong> Og <strong>Alexa</strong> af<strong>Amazon</strong> eru samtíma dæmi um tilraunir til að búa til vélar sem gætu hugsanlega staðist Turing prófið.</p>



<p>Turing prófið er enn umræðuefni og umræðuefni, sérstaklega varðandi réttmæti þess og mikilvægi við mat á gervigreind. Þó að sumir haldi því fram að prófið mæli aðeins samtalshermi en ekki greind í sjálfu sér, sjá aðrir það sem áskorun fyrir framtíðar gervigreindarþróun.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Skilyrdi_fyrir_arangursrikt_Turing_prof"></span>Skilyrði fyrir árangursríkt Turing próf<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Bien-comprendre-le-test-de-Turing.png" alt="" class="wp-image-806" srcset="/images/blog/Bien-comprendre-le-test-de-Turing.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Vel heppnað Turing próf er leið til að mæla gáfur vélar með því að meta getu hennar til að líkja eftir mannlegri hegðun að því marki að mannlegur áhorfandi getur ekki greint á milli viðbragða vélarinnar og raunverulegrar manneskju. Á sviði gervigreindar er hið fræga Turing próf, sem Alan Turing lagði til árið 1950, áfram tilvísun í hjarta margra umræðu um meðvitund og greind véla. Svo hver eru skilyrðin sem þarf að uppfylla til að Turing próf teljist vel?</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Vidmidun_um_oadgreinanleika_mannsins"></span>Viðmiðun um óaðgreinanleika mannsins<span class="ez-toc-section-end"></span></h3>



<p>Meginmarkmið Turing prófsins er að prófa hvort mannaspyrjandi sé fær um að greina vél frá manni, einfaldlega byggt á svörum þeirra við spurningum eða fullyrðingum. Ef viðmælandi getur ekki sagt með vissu hvort svörin koma frá manni eða vél telst prófið staðist. Með þetta í huga þarf að virða nokkur skilyrði:</p>



<p>&#8211; <strong>Gæði svara</strong> : Þeir verða að vera samhangandi og virðast náttúrulegir, eins og þeir kæmu frá manni.<br>&#8211; <strong>Fjölbreytni í samræðum</strong> : Hæfni vélarinnar til að taka þátt í fjölmörgum viðfangsefnum gefur til kynna einhvers konar skilning eða aðlögun.<br>&#8211; <strong>Að stjórna tvískinnungum</strong> : vél verður að vera fær um að takast á við fínleika og blæbrigði tungumálsins, þar á meðal myndlíkingar, húmor og menningarlegar tilvísanir.<br>&#8211; <strong>Tilfinningar og samkennd</strong>: Gervigreind ætti að sýna einhvers konar samkennd eða viðeigandi tilfinningaviðbrögð við aðstæðum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Lengd_og_skilyrdi_profsins"></span>Lengd og skilyrði prófsins<span class="ez-toc-section-end"></span></h4>



<p>Það er engin staðlað tímalengd fyrir Turing próf, en almennt er viðurkennt að langur tími getur aukið áreiðanleika niðurstaðna sem fást. Eftirfarandi skilyrði eru einnig mikilvæg fyrir gilt próf:</p>



<p>&#8211; <strong>Algjör nafnleynd</strong> : Spyrjandi ætti ekki að hafa neinar sjónrænar eða heyranlegar vísbendingar sem gætu hjálpað honum að bera kennsl á aðilann á bak við svörin.<br>&#8211; <strong>Hlutlaust samskiptaviðmót</strong> : Svör verða að vera send í gegnum lyklaborð og skjá til að forðast mismunun á grundvelli rödd eða rithönd.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mat_a_arangri_og_deilur"></span>Mat á árangri og deilur<span class="ez-toc-section-end"></span></h4>



<p>Mat verður að byggjast á hlutlægum forsendum þótt huglægt mat hins mannlega spyrils gegni lykilhlutverki í lokaákvörðun. Eftirfarandi þættir skipta sköpum:<br>&#8211; <strong>Tölfræði um árangur</strong> : Hlutfall skipta sem dómarar eru blekktir er mikilvægur mælikvarði.<br>&#8211; <strong>Hlutdrægni stjórna</strong> : Það þarf að lágmarka hlutdrægni fyrirspyrjenda með góðri matsaðferð til að tryggja sanngirni í prófunum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hlutverk_mannlegra_samskipta"></span>Hlutverk mannlegra samskipta<span class="ez-toc-section-end"></span></h4>



<p>Samskipti meðan á Turing prófinu stendur ættu að vera náttúruleg og fljótandi og líkja eftir flæði raunverulegs mannlegs samtals. Taka skal tillit til eftirfarandi þátta:<br>&#8211; <strong>Viðbrögð</strong> : Vélin verður að svara spurningum á svipuðum hraða og í venjulegu mannlegu samtali.<br>&#8211; <strong>Tvíhliða samskipti</strong> : Vélin á ekki aðeins að svara spurningum heldur einnig að geta spurt spurninga til að sýna að hún fylgist með og taki virkan þátt í samtalinu.</p>



<p>Vel heppnað Turing próf er ekki bara spurning um að blekkja viðmælanda einu sinni heldur að gera það stöðugt, við mismunandi aðstæður og með mismunandi dómurum. Þrátt fyrir að þetta próf sé mikið rætt og stundum gagnrýnt fyrir skort á nákvæmni varðandi raunverulegan skilning eða vitund gervigreindar, er það enn áhugaverð áskorun fyrir gervigreindarhönnuði.<strong>AI</strong>. Þetta á sérstaklega við um fyrirtæki sem eru í fararbroddi í tækninýjungum, ss <strong>Google</strong> með aðstoðarmanni sínum eða <strong>OpenAI</strong> með GPT-3 / GPT-4, sem leitast við að búa til sífellt flóknari kerfi. </p>



<p>Þrátt fyrir að engin vél hafi enn staðist Turing prófið með því að líkja fullkomlega eftir manni, þá ýta framfarir á sviði gervigreindar á okkur til að endurmeta stöðugt takmörk þess sem vél getur áorkað.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="THroun_Turing_profsins_a_gervigreindartimanum"></span>Þróun Turing prófsins á gervigreindartímanum<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Bien-comprendre-le-test-de-Turing-2.png" alt="" class="wp-image-808" srcset="/images/blog/Bien-comprendre-le-test-de-Turing-2.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-2-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-2-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-2-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Turing prófið, sem Alan Turing hannaði á fimmta áratugnum, hafði það að markmiði að meta getu vélar til að líkja eftir mannlegri hegðun að því marki að viðmælandi getur ekki greint hvort viðmælandi hennar er maður eða vél. Á tímum gervigreindar heldur Turing prófið áfram að þjóna sem viðmið til að mæla þróun gervigreindar, jafnvel þó að það hafi verið gagnrýnt og endurhannað vegna stórkostlegra tækniframfara.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Upprunalega_Turing_profid_og_takmarkanir_thess"></span>Upprunalega Turing prófið og takmarkanir þess<span class="ez-toc-section-end"></span></h3>



<p>Upphaflega er Turing prófið próf á textasamtal milli manns og vélar. Markmiðið er að ákvarða hvort vélin geti haldið áfram samtali sem er óaðgreinanlegt frá manni. Hins vegar hefur þetta próf takmarkanir. Reyndar, að standast prófið þýðir ekki endilega að vélin hafi raunverulega greind eða skilning, heldur einfaldlega að hún geti sannfært mann um manneskju sína í stuttan tíma.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Framfarir_i_gervigreind_og_throun_Turing_profsins"></span>Framfarir í gervigreind og þróun Turing prófsins<span class="ez-toc-section-end"></span></h3>



<p>Með örum framförum gervigreindar duga einföld textaskipti ekki lengur til að dæma fágun gervigreindar. Núverandi kerfi, eins og þau sem þróuð eru af <strong>Google</strong> Eða <strong>OpenAI</strong>, eru færir um að stjórna flóknum samtölum, semja tónlist, búa til raunsæjar myndir og jafnvel skrifa heildstæðan texta um fjölmörg efni.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Flaekjustig_Turing_profsins"></span>Flækjustig Turing prófsins<span class="ez-toc-section-end"></span></h3>



<p>Til að laga sig að þróun gervigreindar eru vísindamenn að leggja til flóknari útgáfur af Turing prófinu. Þessar nýju útgáfur gætu falið í sér fjölþætt samskipti við vélar (texta, mynd, hljóð), sköpunarpróf eða mat á skilningi og skynsemi, til að ýta takmörk gervigreindar langt út fyrir einfalda eftirlíkingu.</p>



<p>Hér eru dæmi um aðstæður sem tákna þróun Turing prófsins sem beitt er á nútíma gervigreind:</p>



<p>&#8211; Ítarleg samtöl um ákveðin þemu<br>&#8211; Gerð frumlegs listræns efnis<br>&#8211; Viðbrögð við óvæntum atburðum eða nýjum upplýsingum<br>&#8211; Rauntíma samskipti við umhverfið, til dæmis í gegnum vélmenni</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Framtid_Turing_profsins"></span>Framtíð Turing prófsins<span class="ez-toc-section-end"></span></h2>



<p>Upprunalega hugmyndin að Turing prófinu er nú að þróast yfir í breiðari matshóp, sem ætlað er að prófa ekki aðeins hæfni til að líkja eftir, heldur einnig sjálfræði, nám, sköpunargáfu og samkennd gervigreindar. Þessar prófanir mæla ekki lengur bara gæði eftirlíkingar, heldur leitast við að meta að hve miklu leyti gervigreind getur talist greindur samkvæmt stöðugri þróun mannlegra forsendna.</p>



<p>Turing prófið heldur áfram að þróast samhliða ótrúlegum framförum í gervigreind. Hins vegar er kjarni þess sá sami: að leitast við að skilja hversu nálægt tæknin getur komið mannlegri upplýsingaöflun og hugsanlega farið fram úr henni. </p>



<p>Það er í þessari leit sem hjarta hrifningarinnar á gervigreind og framtíðarþróun þess liggur.</p>



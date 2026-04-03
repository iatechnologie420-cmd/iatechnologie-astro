---
title: "Hvað er Datamart / Datawarehouse?"
slug: "hvad-er-datamart-datawarehouse"
excerpt: "Kynning á hugtakinu Datamart THE datamart er ómissandi hugtak í heimi gagnagreiningar og viðskiptagreindar (BI). Það er undirkafli gagnavöruhúss, það er sérhæfður gagnagrunnur sem geymir hluta af upplýsingum fyrirtækisins. Þó að hægt sé að líta á gagnavöruhús sem risastórt safn af fyrirtækjagögnum, er hægt að líta á gagnaverslun sem ákveðinn hluta þess bókasafns, skipulagður í [&hellip;]"
date: "2024-03-09T12:16:03"
featuredImage: "/images/blog/Quest-ce-quun-Datamart-1-3.png"
categories: ["taekni-og-stafraen-is", "tolvur-og-gogn-is"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="What is Data Mart | Beginners | Interview Question | Examples | Tutorial | Types | Features" width="500" height="281" src="https://www.youtube.com/embed/fGxe8l5q20E?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/hvad-er-datamart-datawarehouse/#Kynning_a_hugtakinu_Datamart" >Kynning á hugtakinu Datamart</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/hvad-er-datamart-datawarehouse/#Skilgreining_a_gagnavoruverslun" >Skilgreining á gagnavöruverslun?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/hvad-er-datamart-datawarehouse/#Kostir_Datamart" >Kostir Datamart</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/is/hvad-er-datamart-datawarehouse/#Tegundir_Data_Mart" >Tegundir Data Mart</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/is/hvad-er-datamart-datawarehouse/#Samanburdur_a_milli_Datamart_og_Datawarehouse" >Samanburður á milli Datamart og Datawarehouse</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/is/hvad-er-datamart-datawarehouse/#Hvad_er_gagnavoruhus" >Hvað er gagnavöruhús?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/is/hvad-er-datamart-datawarehouse/#Hvad_er_Datamart" >Hvað er Datamart?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/hvad-er-datamart-datawarehouse/#Lykilmunur_a_honnun_og_notkun" >Lykilmunur á hönnun og notkun</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/hvad-er-datamart-datawarehouse/#Val_a_milli_Datamart_og_Data_Warehouse" >Val á milli Datamart og Data Warehouse</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/is/hvad-er-datamart-datawarehouse/#Taekni_og_markadsadilar" >Tækni og markaðsaðilar</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-11" href="/is/hvad-er-datamart-datawarehouse/#Notkun_Data_Marts" >Notkun Data Marts</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kynning_a_hugtakinu_Datamart"></span>Kynning á hugtakinu Datamart<span class="ez-toc-section-end"></span></h2>



<p>            THE <strong>datamart</strong> er ómissandi hugtak í heimi gagnagreiningar og viðskiptagreindar (BI). Það er undirkafli gagnavöruhúss, það er sérhæfður gagnagrunnur sem geymir hluta af upplýsingum fyrirtækisins. </p>



<p>Þó að hægt sé að líta á gagnavöruhús sem risastórt safn af fyrirtækjagögnum, er hægt að líta á gagnaverslun sem ákveðinn hluta þess bókasafns, skipulagður í kringum tiltekið efni, svo sem sölu, markaðssetningu eða mannauð.</p>



<p>            Í þessari grein munum við kanna hvað a <strong>datamart</strong>, til hvers það er notað og hvers vegna það er svo mikilvægt fyrir stofnanir sem vilja nýta gögn sín til að taka upplýstar ákvarðanir og bæta starfsemi sína.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Skilgreining_a_gagnavoruverslun"></span>Skilgreining á gagnavöruverslun?<span class="ez-toc-section-end"></span></h3>



<p>            A <strong>datamart</strong> er hannað til að mæta þörfum notenda á tilteknu virknisvæði. Það er efnismiðað og byggt upp til að auðvelda skýrslugerð og greiningu. Til dæmis myndi sölugagnamarkaður innihalda gögn sem tengjast eingöngu söluviðskiptum, viðskiptavinum og seldum vörum.</p>



<p>            Uppsetning gagnamarkaðs er hægt að gera ódýrari og hraðari en að búa til fullt gagnavöruhús, sem gerir það aðlaðandi fyrir sérstakar deildir sem vilja bæta gagnagreiningu sína án þess að bíða eftir fyrirtækjalausn í stórum stíl.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Kostir_Datamart"></span>Kostir Datamart<span class="ez-toc-section-end"></span></h4>



<p>            Helstu kostir þess að innleiða a <strong>datamart</strong> innihalda: </p>



<ul class="wp-block-list">
<li><strong>Frammistaða :</strong> Þar sem þær eru minni og einbeittar eru fyrirspurnir almennt hraðari en með gagnageymslu.</li>



<li><strong>Einfaldleiki:</strong> það er auðveldara að skilja og nota af viðskiptanotendum vegna þess að það er sérstakt fyrir lénið þeirra.</li>



<li><strong>Agility:</strong> Gagnamars er hægt að þróa og innleiða á skemmri tíma en gagnavöruhús, sem gerir hraðari arðsemi af fjárfestingu.</li>



<li><strong>Sveigjanleiki:</strong> Auðveldara er að breyta þeim eða stækka til að mæta breyttum skýrsluþörfum.</li>



<li><strong>Áreiðanleiki:</strong> þær hafa tilhneigingu til að vera viðeigandi og safna saman gagnlegum gögnum fyrir sérstakar greiningar.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Tegundir_Data_Mart"></span>Tegundir Data Mart<span class="ez-toc-section-end"></span></h4>



<p>            Það eru nokkrar leiðir til að flokka gagnamars, en þeim er oft skipt í þrjár megingerðir út frá aðferð þeirra við að afla upplýsinga:</p>



<ul class="wp-block-list">
<li><strong>Óháður:</strong> gagnaverslun sem er búin til án þess að nota gagnavöruhús sem gagnagjafa. Það er venjulega lítið og stjórnað af einni deild.</li>



<li><strong>Háður:</strong> gagnamarkaður sem er byggður með því að nota gögn frá núverandi gagnageymslu, sem tryggir gagnasamkvæmni og gæði milli mismunandi hluta stofnunarinnar.</li>



<li><strong>Heildræn:</strong> gagnamarkaður sem sameinar gögn frá mismunandi aðilum, þar á meðal gagnavöruhúsum og ytri rekstrargagnagrunnum. Þetta er flóknari en hugsanlega yfirgripsmeiri nálgun.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Samanburdur_a_milli_Datamart_og_Datawarehouse"></span>Samanburður á milli Datamart og Datawarehouse<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-Datamart-.png" alt="" class="wp-image-1147" srcset="/images/blog/Quest-ce-quun-Datamart-.png 1792w, /images/blog/Quest-ce-quun-Datamart--300x171.png 300w, /images/blog/Quest-ce-quun-Datamart--1024x585.png 1024w, /images/blog/Quest-ce-quun-Datamart--150x86.png 150w, /images/blog/Quest-ce-quun-Datamart--768x439.png 768w, /images/blog/Quest-ce-quun-Datamart--1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Hvad_er_gagnavoruhus"></span>Hvað er gagnavöruhús?<span class="ez-toc-section-end"></span></h3>



<p>A <strong>gagnageymslu</strong> er miðlægur gagnagrunnur sem er hannaður til að styðja við ákvarðanatökuferli innan fyrirtækis. Það er fínstillt til að lesa, safna saman og greina mikið magn af sögulegum gögnum frá ólíkum heimildum. Það gefur yfirgripsmikið yfirlit yfir rekstur fyrirtækis yfir langan tíma.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hvad_er_Datamart"></span>Hvað er Datamart?<span class="ez-toc-section-end"></span></h4>



<p>Hvað hann varðar, a <strong>datamart</strong> er undirkafli gagnavöruhúss. Það miðar að tiltekinni deild, aðgerð eða mengi gagna sem tengjast tilteknu efni, svo sem sölu eða mannauði. Gagnaverslun inniheldur minni gögn en gagnavöruhúsið og er hannað til að bregðast fljótt við sérsniðnum fyrirspurnum fyrir ákveðinn hóp notenda.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Lykilmunur_a_honnun_og_notkun"></span>Lykilmunur á hönnun og notkun<span class="ez-toc-section-end"></span></h4>



<p>Helsti munurinn á gagnavöruhúsi og gagnavöruverslun er umfang þeirra og umfang. Gagnavöruhús geymir mikið magn af gögnum um allt fyrirtækið á meðan gagnaverslun einbeitir sér að aðeins einum þætti fyrirtækisins. Hér eru nokkrar af einkennum:</p>



<ul class="wp-block-list">
<li><strong>Umfang gagna</strong>: Gagnahús hefur stærra umfang og umfang og er því dýrara og flóknara í viðhaldi. Á hinn bóginn er gagnamarkaður, sem miðar á tiltekið lén, ódýrari og auðveldari í umsjón.</li>



<li><strong>Frammistaða</strong>: Gagnamars geta oft veitt fyrirspurnarniðurstöður hraðar vegna sérhæfingar þeirra og minni gagna til að vinna úr.</li>



<li><strong>Uppbygging</strong>: Gagnageymslan samþættir gögn frá mörgum aðilum og gerir þau einsleit, en gagnamarkaður er oft byggður í kringum einn gagnagjafa eða lítið safn af nátengdum heimildum.</li>



<li><strong>Notendur</strong>: Gagnageymslur eru almennt notaðar af gagnasérfræðingum sem þurfa að hafa heildaryfirsýn yfir fyrirtækið, en gagnamar þjóna notendum sem sérhæfa sig á tilteknu léni.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Val_a_milli_Datamart_og_Data_Warehouse"></span>Val á milli Datamart og Data Warehouse<span class="ez-toc-section-end"></span></h4>



<p>Ákvörðunin um að einbeita sér að gagnavöruhúsi eða gagnamarkaði fer að miklu leyti eftir sérstökum þörfum stofnunarinnar. Gagnahús er tilvalið fyrir fyrirtæki sem þurfa nákvæma og fullkomna greiningu á öllum gögnum þeirra. Gagnaverslun getur aftur á móti verið nægjanleg fyrir markvissar þarfir og ef fjárhagsáætlun er vandamál, býður upp á kosti hvað varðar einfaldleika og kostnað.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Taekni_og_markadsadilar"></span>Tækni og markaðsaðilar<span class="ez-toc-section-end"></span></h4>



<p>Á markaðnum eru mismunandi gagnavöruhúsa- og gagnamarkaðslausnir í boði hjá helstu aðilum í upplýsingatæknigeiranum, s.s. <strong>Oracle</strong>, <strong>Microsoft</strong> með þjónustu hans <strong>Azure</strong>, <strong>Amazon</strong> með <strong>AWS</strong>, <strong>Google Cloud Platform</strong>, og öðrum veitendum gagnageymslu og viðskiptagreindarlausna.</p>



<p>Í stuttu máli, þó að stundum megi líta á gagnamars og gagnavöruhús sem skiptanleg, gegna þau í raun mjög mismunandi hlutverkum í gagnastjórnunarstefnu fyrirtækisins. Ákvarðanataka verður því að byggjast á traustum skilningi á þessum mun og verður alltaf að vera í samræmi við markmið og getu skipulagsheilda.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Notkun_Data_Marts"></span>Notkun Data Marts<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-Datamart-1-1.png" alt="" class="wp-image-1148" srcset="/images/blog/Quest-ce-quun-Datamart-1-1.png 1792w, /images/blog/Quest-ce-quun-Datamart-1-1-300x171.png 300w, /images/blog/Quest-ce-quun-Datamart-1-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-Datamart-1-1-150x86.png 150w, /images/blog/Quest-ce-quun-Datamart-1-1-768x439.png 768w, /images/blog/Quest-ce-quun-Datamart-1-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Gagnamarkaður hefur ýmis forrit á sviði gagnastjórnunar:</p>



<ul class="wp-block-list">
<li><strong>Geiragreining</strong>: Gagnaverslun er hægt að nota til að sameina gögn sem tengjast tiltekinni atvinnugrein, svo sem sölu, markaðssetningu eða fjármál, sem gerir ítarlegri greiningu á tilteknum árangri og þróun.</li>



<li><strong>Verkefnastjórn</strong>: Fyrir verkefnateymi getur gagnamarkaður veitt mikilvægar upplýsingar um framvindu, fjármagn, útgjöld og samræmi við áður skilgreinda fresti.</li>



<li><strong>Persónuleg markaðssetning</strong>: Markaðsteymi geta notað það til að miða nánar á viðskiptavini með því að greina lýðfræði, kaupvenjur og óskir sem safnað er.</li>



<li><strong>Reglugerðarskýrslur</strong>: Hægt er að setja upp sérstaka gagnamars til að einfalda innri eða ytri skýrslugerð og endurskoðunarferli með því að safna saman öllum nauðsynlegum gögnum til að uppfylla reglur.</li>
</ul>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-Datamart-1-2.png" alt="" class="wp-image-1149" srcset="/images/blog/Quest-ce-quun-Datamart-1-2.png 1792w, /images/blog/Quest-ce-quun-Datamart-1-2-300x171.png 300w, /images/blog/Quest-ce-quun-Datamart-1-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-Datamart-1-2-150x86.png 150w, /images/blog/Quest-ce-quun-Datamart-1-2-768x439.png 768w, /images/blog/Quest-ce-quun-Datamart-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Árangursrík innleiðing Datamart byggir einnig á þátttöku og þjálfun notenda, sem tryggir að þeir skilji hvernig eigi að nota kerfið til að fá þær upplýsingar sem óskað er eftir sjálfstætt. Það er einnig mikilvægt að tryggja skilvirka gagnastjórnun og samræmi við öryggis- og persónuverndarstefnu fyrirtækisins.</p>



<p>A <strong>Datamart</strong> vel hannað og rétt útfært getur orðið öflugur eign fyrir fyrirtæki, auðveldað aðgang að upplýsingum, bætt ákvarðanatöku og aukið snerpu skipulagsheildar. Með því að einbeita sér að helstu innleiðingarskrefum og forgangsraða þörfum notenda, geta fyrirtæki hámarkað ávinninginn af Datamart þeirra og á áhrifaríkan hátt samþætt þá inn í heildarstefnu gagnastjórnunar.</p>



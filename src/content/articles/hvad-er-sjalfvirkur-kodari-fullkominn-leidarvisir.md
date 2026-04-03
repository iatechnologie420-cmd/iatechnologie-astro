---

title: "Hvað er sjálfvirkur kóðari? Fullkominn leiðarvísir!"
slug: "hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir"
excerpt: "Autoencoders, eða sjálfkóðunartæki á ensku, staðsetja sig sem öflug tæki á sviði vélanáms og gervigreindar. Þessi sérstöku tauganet eru notuð til að minnka víddar, greina frávik, gagnasnúning og fleira. Þessi grein veitir kynningu á þessari heillandi tækni, undirstrikar vinnureglu hennar, notkun hennar og vaxandi mikilvægi hennar í rannsóknum og iðnaði. Hvað er sjálfvirkur kóðari? A [&hellip;]"
date: "2024-03-09T12:05:49"
categories: ["taekni-og-stafraen-is", "tolvur-og-gogn-is"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tracking Corn &amp; Weed with Yolov5 and Auto Encoder - Tracker" width="500" height="281" src="https://www.youtube.com/embed/8-jWgsGWaR0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>Autoencoders, eða <em>sjálfkóðunartæki</em> á ensku, staðsetja sig sem öflug tæki á sviði vélanáms og gervigreindar. Þessi sérstöku tauganet eru notuð til að minnka víddar, greina frávik, gagnasnúning og fleira. Þessi grein veitir kynningu á þessari heillandi tækni, undirstrikar vinnureglu hennar, notkun hennar og vaxandi mikilvægi hennar í rannsóknum og iðnaði.</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Hvad_er_sjalfvirkur_kodari" >Hvað er sjálfvirkur kóðari?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-2" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Hvernig_virka_sjalfvirkir_kodarar" >Hvernig virka sjálfvirkir kóðarar?</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-3" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Hagnyt_forrit_sjalfvirkra_kodara" >Hagnýt forrit sjálfvirkra kóðara</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-4" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Sjalfkodari_kodun_floskuhals_og_afkodun" >Sjálfkóðari: kóðun, flöskuháls og afkóðun</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Kodun" >Kóðun</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Floskuhals" >Flöskuháls</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Afkodun" >Afkóðun</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Hagnyt_forrit_og_afbrigdi_af_sjalfkodara" >Hagnýt forrit og afbrigði af sjálfkóðara</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Hagnyt_forrit_sjalfvirkra_kodara-2" >Hagnýt forrit sjálfvirkra kóðara</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Viddarminnkun" >Víddarminnkun</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Noise_Cancellation_denoising" >Noise Cancellation (denoising)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Gagnathjoppun" >Gagnaþjöppun</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Gagnaoflun_og_utreikningur" >Gagnaöflun og útreikningur</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Sjalfkodunarafbrigdi" >Sjálfkóðunarafbrigði</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Variational_Autoencoders_VAE" >Variational Autoencoders (VAE)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Dreifdir_sjalfvirkir_kodarar" >Dreifðir sjálfvirkir kóðarar</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Denoising_Autoencoders" >Denoising Autoencoders</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Radadar_sjalfvirkir_kodarar" >Raðaðar sjálfvirkir kóðarar</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-19" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Hvernig_a_ad_thjalfa_sjalfvirkan_kodara_og_koda_daemi" >Hvernig á að þjálfa sjálfvirkan kóðara og kóða dæmi</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Adferd_vid_ad_thjalfa_sjalfvirkan_kodara" >Aðferð við að þjálfa sjálfvirkan kóðara</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-21" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Daemi_um_koda_med_Keras" >Dæmi um kóða með Keras</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-22" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Abending_fyrir_goda_aefingu" >Ábending fyrir góða æfingu</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-23" href="/is/hvad-er-sjalfvirkur-kodari-fullkominn-leidarvisir/#Forrit_sjalfvirkra_kodara" >Forrit sjálfvirkra kóðara</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hvad_er_sjalfvirkur_kodari"></span>Hvað er sjálfvirkur kóðari?<span class="ez-toc-section-end"></span></h2>



<p>A <strong>sjálfkóðari</strong> er tegund gervi taugakerfis sem notað er við nám án eftirlits. Meginmarkmið sjálfkóðunartækis er að framleiða þétta framsetningu (kóðun) á mengi inntaksgagna og endurbyggja síðan gögnin úr þessari framsetningu. Hugmyndin er að fanga mikilvægustu þætti gagnanna, oft til að draga úr vídd. Uppbygging sjálfkóðara er venjulega samsett úr tveimur meginhlutum:</p>



<ul class="wp-block-list">
<li><strong>Kóðari</strong> (<em>Kóða</em>): Þessi fyrsti hluti netsins er ábyrgur fyrir því að þjappa inntaksgögnum í minnkað form.</li>



<li><strong>Afkóðari</strong> (<em>Afkóða</em>): Seinni hlutinn tekur við þjöppuðu kóðuninni og reynir að endurgera upprunalegu gögnin.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hvernig_virka_sjalfvirkir_kodarar"></span>Hvernig virka sjálfvirkir kóðarar?<span class="ez-toc-section-end"></span></h2>



<p>Hægt er að lýsa starfsemi sjálfkóðara í nokkrum skrefum:</p>



<ol class="wp-block-list">
<li>Netið fær gögn sem inntak.</li>



<li>Kóðarinn þjappar gögnunum saman í eiginleikavektor, sem kallast kóðinn eða dulda rýmið.</li>



<li>Afkóðarinn tekur þennan vektor og reynir að endurbyggja upphafsgögnin.</li>



<li>Gæði endurgerðarinnar eru mæld með tapfalli, sem metur muninn á upprunalegu inntakinu og endurgerðu úttakinu.</li>



<li>Netið stillir þyngd sína með reikniritum fyrir bakútbreiðslu til að lágmarka þessa tapaðgerð.</li>
</ol>



<p>Í gegnum þetta endurtekna ferli lærir sjálfkóðarinn skilvirka framsetningu gagna, með áherslu á að varðveita mikilvægustu eiginleikana meðan á endurbyggingarferlinu stendur.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Hagnyt_forrit_sjalfvirkra_kodara"></span>Hagnýt forrit sjálfvirkra kóðara<span class="ez-toc-section-end"></span></h3>



<p>Autoencoders eru mjög fjölhæfir og hægt að nota á nokkrum sviðum:</p>



<ul class="wp-block-list">
<li><strong>Víddarskerðing</strong>: Eins og PCA (Principal Component Analysis), en með ólínulega getu.</li>



<li><strong>Dæling</strong>: þeir geta lært að hunsa „hávaða“ í gögnunum.</li>



<li><strong>Gagnaþjöppun</strong>: þeir geta lært kóðun sem eru skilvirkari en hefðbundnar þjöppunaraðferðir.</li>



<li><strong>Gagnagerð</strong>: með því að vafra um dulda rýmið leyfa þeir sköpun nýrra gagnatilvika sem líkjast upprunalegu færslunum.</li>



<li><strong>Fráviksgreining</strong>: Sjálfkóðunartæki geta hjálpað til við að koma auga á gögn sem passa ekki við lærða dreifingu.</li>
</ul>



<p>Í stuttu máli, hæfileiki sjálfkóðara til að uppgötva og skilgreina þýðingarmikla eiginleika gagna gerir þau að nauðsynlegu tæki í verkfærasetti hvers gervigreindarfræðings.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Sjalfkodari_kodun_floskuhals_og_afkodun"></span>Sjálfkóðari: kóðun, flöskuháls og afkóðun<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png" alt="" class="wp-image-1191" srcset="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kodun"></span>Kóðun<span class="ez-toc-section-end"></span></h3>



<p>Kóðun, eða kóðunarfasinn, felur í sér að umbreyta inntaksgögnunum í þjappaða framsetningu. Upphafsgögnin, sem geta verið stór, eru færð inn í sjálfkóðunarkerfi. Lög netkerfisins munu smám saman draga úr stærð gagnanna og þjappa nauðsynlegum upplýsingum í minna framsetningarrými. Hvert lag netsins er samsett af taugafrumum sem beita ólínulegum umbreytingum, til dæmis með því að nota virkjunaraðgerðir eins og ReLU eða Sigmoid, til að komast að nýrri framsetningu gagna sem geymir nauðsynlegar upplýsingar.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Floskuhals"></span>Flöskuháls<span class="ez-toc-section-end"></span></h4>



<p>Flöskuhálsinn er miðhluti sjálfkóðarans þar sem gagnaframsetningin nær lægstu vídd, einnig kallaður kóða. Það er þessi þjappaða framsetning sem heldur mikilvægustu eiginleikum inntaksgagnanna. Flöskuhálsinn virkar sem sía sem neyðir sjálfvirkan kóða til að læra skilvirka leið til að þétta upplýsingarnar. Þessu má líkja við form gagnaþjöppunar, en þar sem þjöppunin lærist sjálfkrafa af gögnunum frekar en að vera skilgreind með stöðluðum reikniritum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Afkodun"></span>Afkóðun<span class="ez-toc-section-end"></span></h4>



<p>Afkóðunarfasinn er skrefið sem er samhverft kóðuninni, þar sem þjappað framsetning er endurgerð í átt að úttak sem miðar að því að vera eins trúr upprunalega inntakinu og mögulegt er. Frá og með flöskuhálsmyndinni mun tauganetið smám saman auka vídd gagnanna. Þetta er hið öfuga ferli kóðunar: lög í röð endurbyggja upphafseinkennin út frá minnkaðri framsetningu. Ef afkóðun er skilvirk ætti framleiðsla sjálfkóðarans að vera mjög náin nálgun við upprunalegu gögnin.</p>



<p>Í námi án eftirlits eru sjálfkóðarar sérstaklega gagnlegir til að skilja undirliggjandi uppbyggingu gagna. Skilvirkni þessara neta er ekki mæld með getu þeirra til að endurskapa inntak fullkomlega, heldur með getu þeirra til að fanga mikilvægustu og viðeigandi eiginleika gagna í kóða. Þennan kóða er síðan hægt að nota fyrir verkefni eins og víddarminnkun, sjónmyndun eða jafnvel forvinnslu fyrir önnur tauganet í flóknari byggingarlist.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hagnyt_forrit_og_afbrigdi_af_sjalfkodara"></span>Hagnýt forrit og afbrigði af sjálfkóðara<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png" alt="" class="wp-image-1192" srcset="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>sjálfkóðari</strong>, lykilþáttur í vopnabúr djúpnáms knúið af gervigreind (AI), er taugakerfi sem er hannað til að umrita gögn í lægri víddar framsetningu og sundra þeim á þann hátt að viðeigandi endurbygging sé möguleg. Við skulum skoða þær <strong>hagnýt forrit</strong> og afbrigðin sem hafa komið fram á þessu heillandi sviði.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Hagnyt_forrit_sjalfvirkra_kodara-2"></span>Hagnýt forrit sjálfvirkra kóðara<span class="ez-toc-section-end"></span></h3>



<p>Sjálfkóðarar hafa ratað inn í fjöldann allan af forritum vegna getu þeirra til að læra skilvirka og þroskandi framsetningu gagna án eftirlits. Hér eru nokkur dæmi:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Viddarminnkun"></span>Víddarminnkun<span class="ez-toc-section-end"></span></h4>



<p>Eins og PCA (Principal Component Analysis), eru sjálfkóðarar oft notaðir fyrir <strong>víddarminnkun</strong>. Þessi tækni gerir það mögulegt að einfalda gagnavinnslu með því að fækka breytum til að taka tillit til á meðan þær varðveita flestar upplýsingarnar í upprunalegu gagnasafninu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Noise_Cancellation_denoising"></span>Noise Cancellation (denoising)<span class="ez-toc-section-end"></span></h4>



<p>Með getu þeirra til að læra að endurgera inntak úr gögnum sem hafa verið eytt að hluta eru sjálfkóðarar sérstaklega gagnlegir fyrir <strong>hávaðadeyfingu</strong>. Þeim tekst að þekkja og endurheimta gagnleg gögn þrátt fyrir truflun hávaða.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gagnathjoppun"></span>Gagnaþjöppun<span class="ez-toc-section-end"></span></h4>



<p>Með því að læra að umrita gögn í þéttara form er hægt að nota sjálfvirka kóðara fyrir <strong>gagnaþjöppun</strong>. Þó að þeir séu ekki enn notaðir mikið í þessum tilgangi í reynd, eru möguleikar þeirra verulegir, sérstaklega til að þjappa ákveðnum gagnategundum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gagnaoflun_og_utreikningur"></span>Gagnaöflun og útreikningur<span class="ez-toc-section-end"></span></h4>



<p>Autoencoders geta búið til ný gagnatilvik sem líkjast þjálfunargögnum þeirra. Þessa hæfileika er einnig hægt að nota til að <strong>álagningu</strong>, sem felur í sér að fylla út gögn sem vantar í gagnasafni.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Sjalfkodunarafbrigdi"></span>Sjálfkóðunarafbrigði<span class="ez-toc-section-end"></span></h3>



<p>Fyrir utan staðlaða sjálfkóðara hafa ýmis afbrigði verið þróuð til að laga sig að sérkennum gagna og verkefna sem krafist er. Hér eru nokkur athyglisverð afbrigði:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Variational_Autoencoders_VAE"></span>Variational Autoencoders (VAE)<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>Breytileg sjálfkóðunartæki</strong> (<strong>VAE</strong>) bæta við stochastic lagi sem gerir kleift að búa til gögn. VAE eru sérstaklega vinsæl við gerð efnis, svo sem mynda eða tónlistar, vegna þess að þeir gera það mögulegt að framleiða nýja og fjölbreytta þætti sem eru trúverðugir samkvæmt sömu fyrirmynd.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dreifdir_sjalfvirkir_kodarar"></span>Dreifðir sjálfvirkir kóðarar<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>dreifðir sjálfkóðarar</strong> fella inn refsingu sem setur takmarkaða virkni í földum hnútum. Þau eru áhrifarík við að uppgötva sérkenni gagna, sem gerir þau gagnleg fyrir <strong>flokkun</strong> og <strong>uppgötvun frávika</strong>.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Denoising_Autoencoders"></span>Denoising Autoencoders<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>óeðlilegir sjálfkóðarar</strong> eru hönnuð til að standast innleiðingu hávaða í inntaksgögnin. Þeir eru öflugir til að læra sterkar framsetningar og fyrir <strong>forvinnsla gagna</strong> áður en þú framkvæmir önnur vélnámsverkefni.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Radadar_sjalfvirkir_kodarar"></span>Raðaðar sjálfvirkir kóðarar<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>raðbundnir sjálfkóðarar</strong> vinna úr gögnum sem eru skipulögð í röð, svo sem texta eða tímaraðir. Þeir nota oft endurtekin net eins og LSTM (Long Short-Term Memory) til að umrita og afkóða upplýsingar með tímanum.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hvernig_a_ad_thjalfa_sjalfvirkan_kodara_og_koda_daemi"></span>Hvernig á að þjálfa sjálfvirkan kóðara og kóða dæmi<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png" alt="" class="wp-image-1193" srcset="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Þjálfun a <strong>sjálfkóðari</strong> er mikilvægt verkefni á sviði vélanáms fyrir víddarminnkun og fráviksgreiningu, meðal annarra forrita. Hér munum við sjá hvernig á að þjálfa slíkt líkan með Python og bókasafninu <strong>Keras</strong>, með kóðadæmum sem þú getur prófað og lagað að verkefnum þínum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Adferd_vid_ad_thjalfa_sjalfvirkan_kodara"></span>Aðferð við að þjálfa sjálfvirkan kóðara<span class="ez-toc-section-end"></span></h4>



<p>Til að þjálfa sjálfvirkan kóðara notar maður venjulega tapsmælikvarða, svo sem mean square error (MSE), sem mælir muninn á upprunalegu inntakinu og endurgerð þess. Markmið þjálfunar er að lágmarka þessa tapvirkni.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Daemi_um_koda_med_Keras"></span>Dæmi um kóða með Keras<span class="ez-toc-section-end"></span></h4>



<p>Hér er einfalt dæmi um að þjálfa sjálfvirkan kóðara með því að nota <strong>Keras</strong>:</p>



<pre class="wp-block-code"><code>

frá keras.layers import Input, Dense
frá keras.models import Model

# Inngangsstærð
# Stærð dulda rýmisins (eiginleikaframsetning)
encoding_dim = 32

# Skilgreining á kóðara
input_img = Input(shape=(input_dim,))
kóðuð = Þétt(encoding_dim, activation='relu')(input_img)

# Skilgreining á afkóðara
afkóðað = Þétt(input_dim, activation='sigmoid')(kóðað)

# Sjálfkóðunarlíkan
sjálfkóðari = Model(inntak_img, afkóðað)

# Líkanasöfnun
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Sjálfkóðunarþjálfun
autoencoder.fit(X_train,
                tímabil=50,
                lotusærð=256,
                shuffle=Satt,
                validation_data=(X_test, X_test))

</code></pre>



<p>Í þessu dæmi tákna „X_train“ og „X_test“ þjálfunar- og prófunargögnin. Athugaðu að sjálfkóðari er þjálfaður til að spá fyrir um eigin inntak „X_train“ sem úttak.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Abending_fyrir_goda_aefingu"></span>Ábending fyrir góða æfingu<span class="ez-toc-section-end"></span></h4>



<p></p>



<p>Notaðu tækni eins og <strong>krossfullgilding</strong>, þar <strong>batch normalization</strong> og <strong>svarhringingar</strong> af Keras getur einnig hjálpað til við að bæta afköst og stöðugleika sjálfkóðunardrifsins.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Forrit_sjalfvirkra_kodara"></span>Forrit sjálfvirkra kóðara<span class="ez-toc-section-end"></span></h4>



<p>Eftir þjálfun er hægt að nota sjálfkóðara til að:</p>



<ul class="wp-block-list">
<li>víddarminnkun,</li>



<li>uppgötvun fráviks,</li>



<li>eftirlitslaust nám á lýsingum sem eru gagnlegar fyrir önnur vélnámsverkefni.</li>
</ul>



<p>Að lokum, þjálfun sjálfkóðara er verkefni sem krefst skilnings á arkitektúr tauganeta og reynslu í fínstillingu hyperparameters. Hins vegar, einfaldleiki og sveigjanleiki sjálfkóðara gerir þá að dýrmætu tæki fyrir mörg gagnavinnsluvandamál.</p>



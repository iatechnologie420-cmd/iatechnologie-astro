---

title: "Hlutbundin forritun: hvað er það og til hvers er það?"
slug: "hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad"
excerpt: "Undirstöðuatriði hlutbundinnar forritunar Þarna Hlutbundin forritun (OOP) er forritunarhugmynd sem notar „hluti“ til að hanna tölvuforrit og forrit. Þessir hlutir tákna raunverulegar einingar og gera forriturum kleift að búa til sveigjanlegri, skalanlegri og viðhaldshæfari hugbúnað. Í þessari grein munum við kanna grunnhugtökin sem mynda grunninn að OOP. Útdráttur L&#8217;útdráttur er ferlið þar sem forritari felur [&hellip;]"
date: "2024-03-09T12:46:25"
featuredImage: "/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-3.png"
categories: ["taekni-og-stafraen-is", "tolvur-og-gogn-is"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Undirstoduatridi_hlutbundinnar_forritunar" >Undirstöðuatriði hlutbundinnar forritunar</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Utdrattur" >Útdráttur</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Encapsulation" >Encapsulation</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Arfleifd" >Arfleifð</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Fjolbreytni" >Fjölbreytni</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Flokkar_og_hlutir" >Flokkar og hlutir</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Smidir_og_eydingarmenn" >Smiðir og eyðingarmenn</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Adferdirnar" >Aðferðirnar</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Eiginleikar" >Eiginleikar</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Synileiki_Opinber_einkaadili_og_verndadur" >Sýnileiki: Opinber, einkaaðili og verndaður</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Samtok_sofnun_og_samsetning" >Samtök, söfnun og samsetning</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Hagur_og_hagnyt_notkun_OOP" >Hagur og hagnýt notkun OOP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Kostir_hlutbundinnar_forritunar" >Kostir hlutbundinnar forritunar</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Hagnyt_notkun_hlutbundinnar_forritunar" >Hagnýt notkun hlutbundinnar forritunar</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Samanburdur_vid_onnur_forritunarvidmid" >Samanburður við önnur forritunarviðmið</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-16" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Omissandi_forritun" >Ómissandi forritun</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Yfirlysandi_forritun" >Yfirlýsandi forritun</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Virk_forritun" >Virk forritun</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-19" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Hlutbundin_forritun_OOP" >Hlutbundin forritun (OOP)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/is/hlutbundin-forritun-hvad-er-thad-og-til-hvers-er-thad/#Mottaekileg_forritun" >Móttækileg forritun</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Undirstoduatridi_hlutbundinnar_forritunar"></span>Undirstöðuatriði hlutbundinnar forritunar<span class="ez-toc-section-end"></span></h2>



<p>Þarna <strong>Hlutbundin forritun</strong> (OOP) er forritunarhugmynd sem notar „hluti“ til að hanna tölvuforrit og forrit. Þessir hlutir tákna raunverulegar einingar og gera forriturum kleift að búa til sveigjanlegri, skalanlegri og viðhaldshæfari hugbúnað. Í þessari grein munum við kanna grunnhugtökin sem mynda grunninn að OOP.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="585" src="/images/blog/image-1024x585.png" alt="" class="wp-image-13812" srcset="/images/blog/image-1024x585.png 1024w, /images/blog/image-300x171.png 300w, /images/blog/image-150x86.png 150w, /images/blog/image-768x439.png 768w, /images/blog/image-1536x878.png 1536w, /images/blog/image.png 1792w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Utdrattur"></span>Útdráttur<span class="ez-toc-section-end"></span></h3>



<p>L&#8217;<strong>útdráttur</strong> er ferlið þar sem forritari felur allar óviðkomandi upplýsingar um hlut til að sýna notandanum aðeins mikilvæga eiginleika. Þetta gerir það einfaldara að skilja hvernig hlutir virka án þess að hafa áhyggjur af innra flókið þeirra.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Encapsulation"></span>Encapsulation<span class="ez-toc-section-end"></span></h4>



<p>L&#8217;<strong>hjúpun</strong> er tækni sem samanstendur af því að flokka gögn og aðferðir sem vinna með þau innan sömu einingarinnar, oft kallaður flokkur. Encapsulation verndar einnig gagnaheilleika með því að leyfa aðeins breytingar með skilgreindum aðferðum, sem kemur í veg fyrir beinan óviðkomandi aðgang.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Arfleifd"></span>Arfleifð<span class="ez-toc-section-end"></span></h4>



<p>L&#8217;<strong>arfleifð</strong> er eiginleiki OOP sem gerir þér kleift að búa til nýjan flokk sem byggir á núverandi bekk. Nýi flokkurinn, kallaður afleiddur flokkur, erfir eiginleika og aðferðir grunnklasans, sem gerir kleift að endurnýta kóða og búa til flokkastigveldi.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Fjolbreytni"></span>Fjölbreytni<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>fjölbreytni</strong> er hæfileiki aðferðar til að gera mismunandi aðgerðir eftir því hvaða hlut er kallað á. Það eru tvær megingerðir fjölbreytni: ofhleðslu fjölbreytni (nokkrar aðferðir deila sama nafni en með mismunandi breytum) og erfðafjölbreytni (afleiddur flokkur notar aðferð með sama nafni og aðferð flokksforeldris síns).</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Flokkar_og_hlutir"></span>Flokkar og hlutir<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>Flokkar</strong> eru líkön, eða teikningar, sem eru notuð til að búa til einstök tilvik sem kallast <strong>hlutir</strong>. Hver hlutur sem búinn er til úr flokki getur haft sín eigin gildi fyrir eiginleika flokksins, en deilir sömu aðferðum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Smidir_og_eydingarmenn"></span>Smiðir og eyðingarmenn<span class="ez-toc-section-end"></span></h4>



<p>A <strong>byggingaraðili</strong> er sérstök aðferð flokks sem er kölluð sjálfkrafa þegar hlutur þess flokks er búinn til. Það er almennt notað til að frumstilla eiginleika hlutarins. A <strong>eyðileggjandi</strong>, fyrir sitt leyti, er kallað þegar hlutur er við það að eyðast, sem gerir kleift að losa úthlutaðar auðlindir.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Adferdirnar"></span>Aðferðirnar<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>aðferðir</strong> eru aðgerðir skilgreindar inni í flokki sem lýsa hegðun eða aðgerðum sem hlutur getur framkvæmt. Hver aðferð getur unnið með innri eiginleika hlutarins til að framkvæma ákveðið verkefni.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Eiginleikar"></span>Eiginleikar<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>eiginleikar</strong> eru breytur sem eru skilgreindar inni í flokki og sem tákna ástand eða sérstaka eiginleika hlutar. Eigindir geta verið af mismunandi gagnagerð, svo sem tölur, strengi eða hluti af öðrum flokkum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Synileiki_Opinber_einkaadili_og_verndadur"></span>Sýnileiki: Opinber, einkaaðili og verndaður<span class="ez-toc-section-end"></span></h4>



<p><strong>Áhorfendur</strong>, <strong>Einkamál</strong> Og <strong>Verndaður</strong> eru sýnileikabreytingar sem stjórna aðgangi að eiginleikum og aðferðum flokks. Hægt er að nálgast opinbera meðlimi hvar sem er, aðeins er hægt að nálgast einkameðlimi í bekknum þar sem þeir eru skilgreindir og hægt er að nálgast verndaða meðlimi í bekknum þar sem þeir eru skilgreindir sem og afleiddir flokkar þeirra.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Samtok_sofnun_og_samsetning"></span>Samtök, söfnun og samsetning<span class="ez-toc-section-end"></span></h4>



<p>Í OOP, skilmálar <strong>félag</strong>, <strong>samansafn</strong> Og <strong>samsetningu</strong> lýst mismunandi leiðum sem hægt er að tengja hluti saman á. Tengsl er samband milli tveggja hluta sem eru óháðir hvor öðrum, samsöfnun er „heilhluti“ tengsl þar sem hlutar geta verið aðskildir frá heild, og samsetning er „heildar“ tengsl „þar sem hlutirnir geta ekki verið til án heill.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hagur_og_hagnyt_notkun_OOP"></span>Hagur og hagnýt notkun OOP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1.png" alt="" class="wp-image-1341" srcset="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1.png 1792w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-300x171.png 300w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-1024x585.png 1024w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-150x86.png 150w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-768x439.png 768w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kostir_hlutbundinnar_forritunar"></span>Kostir hlutbundinnar forritunar<span class="ez-toc-section-end"></span></h3>



<p>        OOP hefur marga kosti sem gera það að valinni nálgun við þróun flókins hugbúnaðar:</p>



<ul class="wp-block-list">
<li><strong>Hylki</strong>: Gerir þér kleift að hylja gögn og aðgerðir sem vinna með þau innan hluta og vernda þannig heilleika gagnanna.</li>



<li><strong>Útdráttur</strong>: Einfaldar þróun með því að leyfa notkun háþróaðra hugtaka án þess að þurfa djúpan skilning á innri starfsemi þeirra.</li>



<li><strong>Endurnotkun kóða</strong>: Hvetur til deilingar og notkunar á núverandi kóða sem endurnýtanlegum flokkum og dregur þannig úr þróunartíma og viðhaldskostnaði.</li>



<li><strong>Modularity</strong>: Stuðlar að skiptingu forritsins í sjálfstæða og skiptanlega hluta sem hægt er að þróa og prófa sjálfstætt.</li>



<li><strong>Fjölbreytni</strong>: Leyfir auðvelt að skipta um hluti í gegnum sameiginlegt viðmót, sem veitir mikinn sveigjanleika í forritun og kerfishönnun.</li>



<li><strong>Arfleifð</strong>: Veitir getu til að búa til afleidda flokka sem erfa eiginleika og aðferðir frá núverandi flokkum, sem auðveldar framlengingu og aðlögun.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hagnyt_notkun_hlutbundinnar_forritunar"></span>Hagnýt notkun hlutbundinnar forritunar<span class="ez-toc-section-end"></span></h4>



<p>        OOP er notað á mörgum sviðum og fyrir ýmsar gerðir af forritum. Hér eru nokkur áþreifanleg dæmi:</p>



<ul class="wp-block-list">
<li><strong>Þróun tölvuleikja</strong>: Hlutir geta táknað persónur, hindranir, power-ups osfrv., sem gerir það auðveldara að stjórna ástandi þeirra og hegðun.</li>



<li><strong>Grafísk notendaviðmót (GUI)</strong>: Hver viðmótsþáttur, eins og hnappar og valmyndir, er hlutur, sem gerir byggingu gagnvirkra viðmóta leiðandi.</li>



<li><strong>Gagnagrunnsstjórnunarkerfi</strong>: Einingum eins og töflum, færslum og fyrirspurnum er hægt að móta sem hluti til að auka skilvirkni og viðhald.</li>



<li><strong>vef þróun</strong>: OOP-undirstaða ramma, eins og <strong>Django</strong> fyrir Python eða <strong>Ruby on Rails</strong> fyrir Ruby, notaðu hluti til að tákna beiðnir, svör og aðra vefhluta.</li>



<li><strong>Farsímaforrit</strong>: Pallar eins og <strong>Android</strong> Og <strong>iOS</strong> nýta OOP líkanið til að meðhöndla atburði og meðhöndla notendaviðmótshluti.</li>



<li><strong>Hugbúnaður til að herma</strong>: Til að líkja eftir eðlisfræðilegum, efnahagslegum eða líffræðilegum kerfum gerir notkun hlutar það mögulegt að gera líkan af flóknu samspili milli íhluta kerfisins.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Samanburdur_vid_onnur_forritunarvidmid"></span>Samanburður við önnur forritunarviðmið<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2.png" alt="" class="wp-image-1342" srcset="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2.png 1792w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-300x171.png 300w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-1024x585.png 1024w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-150x86.png 150w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-768x439.png 768w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<figure class="wp-block-embed is-type-video is-provider-tiktok wp-block-embed-tiktok"><div class="wp-block-embed__wrapper">
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@louis_dhanis/video/7291716348722351392" data-video-id="7291716348722351392" data-embed-from="oembed" style="max-width:605px; min-width:325px;"> <section> <a target="_blank" title="@louis_dhanis" href="https://www.tiktok.com/@louis_dhanis?refer=embed" rel="noopener">@louis_dhanis</a> <p>C’est quoi la programmation orientée objet ? Comment ça marche ? C&#8217;est quoi la différence entre une voiture et une maison ? <a title="astucetech" target="_blank" href="https://www.tiktok.com/tag/astucetech?refer=embed" rel="noopener">#astucetech</a> <a title="louis_dhanis" target="_blank" href="https://www.tiktok.com/tag/louis_dhanis?refer=embed" rel="noopener">#louis_dhanis</a> <a title="apprendreautrement" target="_blank" href="https://www.tiktok.com/tag/apprendreautrement?refer=embed" rel="noopener">#apprendreautrement</a> <a title="apprendreacoder" target="_blank" href="https://www.tiktok.com/tag/apprendreacoder?refer=embed" rel="noopener">#apprendreacoder</a> <a title="devweb" target="_blank" href="https://www.tiktok.com/tag/devweb?refer=embed" rel="noopener">#devweb</a> <a title="entrepreneuriat" target="_blank" href="https://www.tiktok.com/tag/entrepreneuriat?refer=embed" rel="noopener">#entrepreneuriat</a> <a title="entrepreneurtech" target="_blank" href="https://www.tiktok.com/tag/entrepreneurtech?refer=embed" rel="noopener">#entrepreneurtech</a> <a title="developpement" target="_blank" href="https://www.tiktok.com/tag/developpement?refer=embed" rel="noopener">#developpement</a> <a title="poo" target="_blank" href="https://www.tiktok.com/tag/poo?refer=embed" rel="noopener">#POO</a> <a title="programmation" target="_blank" href="https://www.tiktok.com/tag/programmation?refer=embed" rel="noopener">#programmation</a></p> <a target="_blank" title="♬ son original - Louis Dhanis - Louis Dhanis" href="https://www.tiktok.com/music/son-original-Louis-Dhanis-7291716399008598816?refer=embed" rel="noopener">♬ son original &#8211; Louis Dhanis &#8211; Louis Dhanis</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Omissandi_forritun"></span>Ómissandi forritun<span class="ez-toc-section-end"></span></h3>



<p>Ómissandi forritun er elsta og einfaldasta hugmyndafræðin. Það felst í því að lýsa þeim skrefum sem tölvan þarf að fylgja til að ná niðurstöðu. C tungumálið er dæmigert dæmi um þessa hugmyndafræði.</p>



<p><strong>Kostir :</strong></p>



<ul class="wp-block-list">
<li>Nákvæm stjórn á flæði forrita og kerfisauðlindanotkun.</li>



<li>Hugmyndalega einfalt og auðskilið.</li>
</ul>



<p><strong>Ókostir:</strong></p>



<ul class="wp-block-list">
<li>Getur orðið mjög flókið fyrir stór forrit.</li>



<li>Skortur á sveigjanleika kóða og endurnýtanleika.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Yfirlysandi_forritun"></span>Yfirlýsandi forritun<span class="ez-toc-section-end"></span></h4>



<p>Ólíkt áríðandi forritun beinist yfirlýsandi forritun að því hver niðurstaðan ætti að vera án þess að lýsa sérstaklega hvernig á að ná henni. SQL og HTML eru dæmi um lýsandi tungumál.</p>



<p><strong>Kostir :</strong></p>



<ul class="wp-block-list">
<li>Einfaldleiki tjáningar á tilætluðum árangri.</li>



<li>Útdráttur á útfærsluupplýsingum, sem gerir oft kleift að hagræða betur af þýðanda eða túlk.</li>
</ul>



<p><strong>Ókostir:</strong></p>



<ul class="wp-block-list">
<li>Minni stjórn á því nákvæmlega ferli sem vélin fylgir.</li>



<li>Getur verið minna leiðandi fyrir þróunaraðila sem eru vanir að nota meira málsmeðferð.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Virk_forritun"></span>Virk forritun<span class="ez-toc-section-end"></span></h4>



<p>Virk forritun er undirmengi yfirlýsingarforritunar sem meðhöndlar útreikninga eins og mat á stærðfræðilegum föllum. Haskell og Scala eru tungumál sem styðja þessa hugmyndafræði.</p>



<p><strong>Kostir :</strong></p>



<ul class="wp-block-list">
<li>Auðveldar rökhugsun um kóðann og tryggir mikla mát.</li>



<li>Tilvalið fyrir samhliða forritun og dreifð kerfi vegna skorts á aukaverkunum.</li>
</ul>



<p><strong>Ókostir:</strong></p>



<ul class="wp-block-list">
<li>Getur verið brattur námsferill fyrir óvana forritara.</li>



<li>Frammistaða gæti verið minna fyrirsjáanleg vegna útdráttar á háu stigi.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hlutbundin_forritun_OOP"></span>Hlutbundin forritun (OOP)<span class="ez-toc-section-end"></span></h4>



<p>OOP er byggt á hugtakinu &#8220;hlutir&#8221;, sem eru dæmi um &#8220;flokka&#8221;. Hlutir innihalda bæði gögn og aðferðir. Java og Python eru tungumál sem fela í sér þessa hugmyndafræði.</p>



<p><strong>Kostir :</strong></p>



<ul class="wp-block-list">
<li>Eykur endurnýtanleika kóða og auðveldar viðhald.</li>



<li>Stuðlar að hjúpun og útdrætti gagna.</li>
</ul>



<p><strong>Ókostir:</strong></p>



<ul class="wp-block-list">
<li>Ofdráttur getur leitt til óþarfa flækjustigs.</li>



<li>Getur leitt til skertrar frammistöðu vegna viðbótarlaga af útdrætti.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mottaekileg_forritun"></span>Móttækileg forritun<span class="ez-toc-section-end"></span></h4>



<p>Reactive forritun er hugmyndafræði sem einbeitir sér að því að stjórna gagnaflæði og breiða út breytingar. Það er sérstaklega áhrifaríkt fyrir forrit með gagnvirkt notendaviðmót eða rauntímakerfi.</p>



<p><strong>Kostir :</strong></p>



<ul class="wp-block-list">
<li>Bætir stjórnun á flóknum ósamstilltum kerfum.</li>



<li>Stuðlar að læsilegri og minna villuhættulegum kóða í mjög gagnvirku samhengi.</li>
</ul>



<p><strong>Ókostir:</strong></p>



<ul class="wp-block-list">
<li>Krefst ítarlegs skilnings á móttækilegum hugtökum til að nota á áhrifaríkan hátt.</li>



<li>Stundum getur verið erfitt að kemba viðbragðsraðir.</li>
</ul>



<p>Að lokum er val á forritunarhugmynd oft háð eðli vandamálsins sem á að leysa, val þróunaraðila og frammistöðutakmörkunum kerfisins. Að skilja mismun þeirra og forrit getur hjálpað forriturum að velja réttu nálgunina fyrir verkefnið sitt og skrifa hreinni, viðhaldshæfari og skilvirkari kóða.</p>



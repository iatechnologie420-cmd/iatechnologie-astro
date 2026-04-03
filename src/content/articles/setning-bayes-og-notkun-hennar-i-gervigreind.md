---

title: "Setning Bayes og notkun hennar í gervigreind"
slug: "setning-bayes-og-notkun-hennar-i-gervigreind"
excerpt: "Inngangur að setningu Bayes THE setning Bayes er grundvallarformúla í líkindum og tölfræði sem lýsir uppfærslu á viðhorfum okkar í viðurvist nýrra upplýsinga. Þessi setning er nefnd til heiðurs séra Thomas Bayes og gegnir mikilvægu hlutverki á mörgum sviðum, allt frá vélanámi til ákvarðanatöku í óvissu. Kjarninn í setningu Bayes Hjarta setning Bayes eru skilyrtar [&hellip;]"
date: "2024-03-09T12:12:36"
categories: ["taekni-og-stafraen-is", "tolvur-og-gogn-is"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Probabilités S3 Probabilités Conditionnelles: le Théorème de Bayes #ep14" width="500" height="281" src="https://www.youtube.com/embed/cCQlN6FhHvo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Inngangur_ad_setningu_Bayes" >Inngangur að setningu Bayes</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Kjarninn_i_setningu_Bayes" >Kjarninn í setningu Bayes</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Beiting_a_setningu_Bayes" >Beiting á setningu Bayes</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Mikilvaegi_i_gervigreind_og_velanami" >Mikilvægi í gervigreind og vélanámi</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Grundvallaratridi_Bayesian_Inference" >Grundvallaratriði Bayesian Inference</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#setning_Bayes" >setning Bayes</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#A_priori_og_posterior_likur" >A priori og posterior líkur</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Sonnunargogn" >Sönnunargögn</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Bayesisk_alyktun_i_reynd" >Bayesísk ályktun í reynd</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-10" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Setning_Bayes_i_velraenum_reikniritum" >Setning Bayes í vélrænum reikniritum</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-11" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Beiting_setningar_Bayes_i_gervigreind" >Beiting setningar Bayes í gervigreind</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Mikilvaegi_Bayesisks_nams" >Mikilvægi Bayesísks náms</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Daemi_um_Bayesisk_reiknirit" >Dæmi um Bayesísk reiknirit</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/is/setning-bayes-og-notkun-hennar-i-gervigreind/#Setning_Bayes_i_framkvaemd" >Setning Bayes í framkvæmd</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Inngangur_ad_setningu_Bayes"></span>Inngangur að setningu Bayes<span class="ez-toc-section-end"></span></h2>



<p>THE <strong>setning Bayes</strong> er grundvallarformúla í líkindum og tölfræði sem lýsir uppfærslu á viðhorfum okkar í viðurvist nýrra upplýsinga. Þessi setning er nefnd til heiðurs séra Thomas Bayes og gegnir mikilvægu hlutverki á mörgum sviðum, allt frá vélanámi til ákvarðanatöku í óvissu.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kjarninn_i_setningu_Bayes"></span>Kjarninn í setningu Bayes<span class="ez-toc-section-end"></span></h3>



<p>Hjarta <strong>setning Bayes</strong> eru skilyrtar líkur. Í sinni einföldustu mynd lýsir það hvernig aftari líkur eru uppfærðar frá a priori líkum með því að taka tillit til líkinda á atburðinum sem sést. Með öðrum orðum, það gerir það mögulegt að endurskoða upphafslíkur byggðar á nýjum sönnunargögnum.</p>



<p>Það er venjulega táknað í formi eftirfarandi jöfnu:</p>



<p><strong>P(A|B) = (P(B|A) * P(A)) / P(B)</strong></p>



<p>Eða:</p>



<ul class="wp-block-list">
<li><strong>P(A|B)</strong> er líkurnar á atburði A gefnu B (aftari líkur)</li>



<li><strong>P(B|A)</strong> eru líkurnar á atburði B gefið A</li>



<li><strong>P(A)</strong> er upphafslíkur á atburði A (a priori líkur)</li>



<li><strong>P(B)</strong> er upphafslíkur á atburði B</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Beiting_a_setningu_Bayes"></span>Beiting á setningu Bayes<span class="ez-toc-section-end"></span></h4>



<p>Umsókn um <strong>setning Bayes</strong> getur komið fyrir í ýmsum hagnýtum aðstæðum, svo sem læknisfræðilegri greiningu, ruslpóstsíun eða tölfræðilegum ályktunum í vísindarannsóknum. Í læknisfræði, til dæmis, gerir setningin mögulegt að áætla líkurnar á því að sjúklingur sé með sjúkdóm út frá niðurstöðum prófs, vitandi líkurnar á því að þetta próf gefi sanna eða ranga jákvætt.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mikilvaegi_i_gervigreind_og_velanami"></span>Mikilvægi í gervigreind og vélanámi<span class="ez-toc-section-end"></span></h4>



<p>Í gervigreind (AI) og <strong>vélanám</strong>, setning Bayes er hornsteinn Bayesísks náms. Þessi námsrammi notar fyrri viðhorf og uppfærir þær með nýjum gögnum til að gera spár. Fyrir vikið geta líkön orðið nákvæmari eftir því sem þau fá viðbótargögn.</p>



<p>Í stuttu máli, the <strong>setning Bayes</strong> er öflugt tæki til að skilja skilyrtar líkur og til að betrumbæta skoðanir okkar með því að taka mið af nýjum upplýsingum. Stærðfræðilegur einfaldleiki þess er andstæður víðtækum merkingum og notkunarmöguleikum, sem gerir það að grundvallarviðfangsefni fyrir alla sem hafa áhuga á tölfræði, ákvarðanatöku og gervigreind.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Grundvallaratridi_Bayesian_Inference"></span>Grundvallaratriði Bayesian Inference<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA.png" alt="" class="wp-image-1314" srcset="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA.png 1792w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-300x171.png 300w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1024x585.png 1024w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-150x86.png 150w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-768x439.png 768w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>Bayesísk ályktun</strong> er grein tölfræði sem gefur fræðilegan ramma til að túlka atburði með tilliti til líkinda. Það er byggt á <strong>setning Bayes</strong>, sem er formúla til að uppfæra líkurnar á að atburður eigi sér stað í ljósi nýrra gagna. </p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="setning_Bayes"></span>setning Bayes<span class="ez-toc-section-end"></span></h3>



<p>Setning Bayes er burðarás Bayesískrar ályktunar. Stærðfræðilega er það orðað sem hér segir:</p>



<p><strong>P(H|E) = (P(E|H) * P(H)) / P(E)</strong></p>



<p>Eða:</p>



<ul class="wp-block-list">
<li><strong>P(H|E)</strong> er líkurnar á tilgátu H vitandi að atburður E hafi átt sér stað.</li>



<li><strong>P(E|H)</strong> er líkurnar á því að atburður E gerist ef tilgáta H er sönn.</li>



<li><strong>P(H)</strong> er a priori líkur á tilgátu H áður en gögnin E sjást.</li>



<li><strong>P(E)</strong> er fyrirfram líkur á atburði E.</li>
</ul>



<p>Þessi setning gerir okkur þannig kleift að uppfæra trú okkar hvað varðar líkur á tilgátunni H eftir að hafa orðið vör við atburðinn E.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="A_priori_og_posterior_likur"></span>A priori og posterior líkur<span class="ez-toc-section-end"></span></h4>



<p>Tvö lykilhugtök í Bayesískri ályktun eru hugmyndir um líkur <strong>a priori</strong> Og <strong>að aftan</strong> :</p>



<ul class="wp-block-list">
<li>Líkurnar <strong>a priori</strong>, táknað P(H), táknar það sem við vitum áður en tekið er tillit til nýju upplýsinganna.</li>



<li>Líkurnar <strong>að aftan</strong>, táknað P(H|E), táknar það sem við vitum eftir að hafa tekið tillit til nýju upplýsinganna.</li>
</ul>



<p>Bayesísk ályktun felur í sér að færa sig frá fyrri líkum yfir í aftari líkur með því að nota setningu Bayes.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Sonnunargogn"></span>Sönnunargögn<span class="ez-toc-section-end"></span></h4>



<p>Í setningu Bayes er P(E) oft kallaður þáttur af<strong>sönnunargögn</strong>. Það er hægt að líta á það sem mælikvarða á samrýmanleika gagna sem skoðaðir voru við allar mögulegar tilgátur. Í reynd virkar það sem eðlilegur þáttur við að uppfæra viðhorf okkar.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Bayesisk_alyktun_i_reynd"></span>Bayesísk ályktun í reynd<span class="ez-toc-section-end"></span></h4>



<p>Í reynd er Bayesian ályktun notuð á mörgum sviðum eins og vélanámi, tölfræðilegri gagnagreiningu, ákvarðanatöku í viðurvist óvissu osfrv. Sérstaklega leyfir það:</p>



<ul class="wp-block-list">
<li>Að þróa líkindaforspárlíkön.</li>



<li>Til að greina frávik eða ráða falin mynstur í flóknum gögnum.</li>



<li>Að taka ákvarðanir byggðar á ófullnægjandi eða óvissum gögnum.</li>
</ul>



<p>L&#8217;<strong>Bayesísk ályktun</strong> veitir öflugan ramma fyrir rökhugsun með óvissu og samþættingu nýrra upplýsinga. Umsóknir þess eru miklar og notkun þess á háþróuðum sviðum eins og<strong>gervigreind</strong> þar sem <strong>stór gögn</strong> vex stöðugt. Skilningur á grundvallarreglum hans er því nauðsynlegur fyrir þá sem vilja túlka heiminn í gegnum prisma líkinda.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Setning_Bayes_i_velraenum_reikniritum"></span>Setning Bayes í vélrænum reikniritum<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1.png" alt="" class="wp-image-1315" srcset="/images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1.png 1792w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-300x171.png 300w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-1024x585.png 1024w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-150x86.png 150w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-768x439.png 768w, /images/blog/Le-theoreme-de-Bayes-et-son-utilisation-en-IA-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Heimur gervigreindar (AI) er í stöðugri þróun og meðal grundvallarhugtakanna sem kynda undir þessari byltingu er setning Bayes. Þetta stærðfræðilega tól gegnir mikilvægu hlutverki í vélrænum reikniritum, sem gerir vélum kleift að taka upplýstar ákvarðanir byggðar á líkum.</p>



<p>THE <strong>setning Bayes</strong>, þróað af séra Thomas Bayes á 18. öld, er formúla sem lýsir skilyrtum líkum á atburði, byggt á fyrri þekkingu sem tengist þeim atburði. Formlega gerir það mögulegt að reikna út líkur (P(A|B)) á atburði A, vitandi að B er satt, með því að nota líkurnar á B vitandi að A er satt (P(B|A)), líkurnar af A ( P(A) ), og líkurnar á B ( P(B) ).</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Beiting_setningar_Bayes_i_gervigreind"></span>Beiting setningar Bayes í gervigreind<span class="ez-toc-section-end"></span></h3>



<p>Í samhengi við vélanám er setning Bayes beitt til að byggja upp líkindalíkön. Þessi líkön geta aðlagað spár sínar á grundvelli nýrra gagna sem veitt eru, sem gerir kleift að bæta stöðugt og betrumbæta frammistöðu. Þetta ferli er sérstaklega gagnlegt í flokkun, þar sem markmiðið er að úthluta merki fyrir tiltekið inntak byggt á einkennum sem mælst hefur.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Mikilvaegi_Bayesisks_nams"></span>Mikilvægi Bayesísks náms<span class="ez-toc-section-end"></span></h4>



<p>Einn helsti kosturinn við Bayesískt nám er hæfni þess til að takast á við óvissu og veita mælikvarða á sjálfstraust í spám. Þetta er grundvallaratriði á mikilvægum sviðum eins og læknisfræði eða fjármálum, þar sem hver spá getur haft mikil áhrif. Að auki veitir þessi nálgun ramma til að fella inn fyrri þekkingu og læra af litlu magni gagna.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Daemi_um_Bayesisk_reiknirit"></span>Dæmi um Bayesísk reiknirit<span class="ez-toc-section-end"></span></h4>



<p>Það eru nokkrir vélanámsreiknirit sem treysta á setningu Bayes, þar á meðal:</p>



<ul class="wp-block-list">
<li><strong>Barnlaus Bayes</strong>: Líkindaflokkari sem, þrátt fyrir „barnlaus“ heiti, er merkilegur fyrir einfaldleika og virkni, sérstaklega þegar líkur á eiginleikum eru óháðar.</li>



<li><strong>Bayesian Networks</strong>: Myndrænt líkan sem sýnir líkindatengsl milli mengis breyta og sem hægt er að nota til að spá, flokka og taka ákvarðanir.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Setning_Bayes_i_framkvaemd"></span>Setning Bayes í framkvæmd<span class="ez-toc-section-end"></span></h4>



<p>Til að sýna útfærslu á Bayesian-námi skaltu íhuga einfalt dæmi um forrit: ruslpóstsíun í tölvupósti. Að nota reiknirit <strong>Barnlaus Bayes</strong>, kerfi getur lært að greina lögmæt skilaboð frá ruslpósti með því að reikna út líkurnar á því að tölvupóstur sé ruslpóstur, byggt á tíðni ákveðinna leitarorða. </p>



<p>Eftir því sem kerfið fær nýjan tölvupóst aðlagar það líkur sínar og verður sífellt nákvæmari í flokkunum.</p>



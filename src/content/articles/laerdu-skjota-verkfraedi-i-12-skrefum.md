---
title: "Lærðu skjóta verkfræði: í 12 skrefum"
slug: "laerdu-skjota-verkfraedi-i-12-skrefum"
excerpt: "Kynning á skyndiverkfræði Hvað er prompt verkfræði? THE Hraðvirkt verkfræði er vaxandi svið sem leggur áherslu á að fínstilla leiðbeiningarnar eða skipanirnar sem við gefum gervigreindarkerfum (AI), sérstaklega þeim sem byggja á náttúrulegu tungumáli, eins og textaframleiðendum. Það er sérstaklega mikilvæg fræðigrein með komu tungumálavinnslulíkana eins og GPT-4 frá OpenAI. Hugmyndin er að læra að [&hellip;]"
date: "2024-03-09T12:51:05"
featuredImage: "/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-3.png"
categories: ["ai-thjalfun-og-grundvallaratridi-is"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Kynning_a_skyndiverkfraedi" >Kynning á skyndiverkfræði</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Hvad_er_prompt_verkfraedi" >Hvað er prompt verkfræði?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Hvers_vegna_er_skjot_verkfraedi_mikilvaeg" >Hvers vegna er skjót verkfræði mikilvæg?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Hvernig_Prompt_Engineering_virkar" >Hvernig Prompt Engineering virkar</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#God_astundun_og_taekni_i_hradvirkri_verkfraedi" >Góð ástundun og tækni í hraðvirkri verkfræði</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Grundvallarreglur_skjotrar_verkfraedi" >Grundvallarreglur skjótrar verkfræði</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Skilja_mikilvaegi_samhengis" >Skilja mikilvægi samhengis</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Skyrdu_tilgang_notenda" >Skýrðu tilgang notenda</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Skipuleggja_og_forgangsrada_upplysingum" >Skipuleggja og forgangsraða upplýsingum</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Val_um_tungumal_og_ordalag" >Val um tungumál og orðalag</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Itrekud_notkun_og_stodugar_umbaetur" >Ítrekuð notkun og stöðugar umbætur</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#Stjornun_a_ohefdbundnum_arangri" >Stjórnun á óhefðbundnum árangri</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/is/laerdu-skjota-verkfraedi-i-12-skrefum/#THekking_a_gervigreindarlikaninu_sem_notad_er" >Þekking á gervigreindarlíkaninu sem notað er</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kynning_a_skyndiverkfraedi"></span>Kynning á skyndiverkfræði<span class="ez-toc-section-end"></span></h2>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Hvad_er_prompt_verkfraedi"></span>Hvað er prompt verkfræði?<span class="ez-toc-section-end"></span></h3>



<p>    THE <strong>Hraðvirkt verkfræði</strong> er vaxandi svið sem leggur áherslu á að fínstilla leiðbeiningarnar eða skipanirnar sem við gefum gervigreindarkerfum (AI), sérstaklega þeim sem byggja á náttúrulegu tungumáli, eins og textaframleiðendum. Það er sérstaklega mikilvæg fræðigrein með komu tungumálavinnslulíkana eins og GPT-4 frá <strong>OpenAI</strong>. Hugmyndin er að læra að „tala“ á áhrifaríkan hátt við þessi gervigreind til að bæta gæði og mikilvægi svaranna sem fæst.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hvers_vegna_er_skjot_verkfraedi_mikilvaeg"></span>Hvers vegna er skjót verkfræði mikilvæg?<span class="ez-toc-section-end"></span></h4>



<p>Hlutverk <strong>Hraðvirkt verkfræði</strong> skiptir sköpum vegna þess að hvernig þú mótar skipun til gervigreindar getur árangurinn verið mjög mismunandi. Til dæmis gætu illa hönnuð leiðbeiningar framkallað ónákvæm svör eða svör sem ekki eru viðfangsefni, á meðan vel hönnuð boð geta bætt nákvæmni og mikilvægi upplýsinganna sem myndast. Hvetjandi verkfræðingar vinna að því að betrumbæta orðalag spurninga til að fá nákvæmar og gagnlegar niðurstöður.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Hvernig_Prompt_Engineering_virkar"></span>Hvernig Prompt Engineering virkar<span class="ez-toc-section-end"></span></h4>



<p> Ferlið við skyndiverkfræði felur í sér að skilja djúpt hvernig gervigreind líkön, svo sem taugakerfi, virka og nota þann skilning til að búa til leiðbeiningar sem nýta sér getu gervigreindar á meðan unnið er í kringum takmarkanir þess. Þetta getur krafist nokkurrar sköpunargáfu, mikillar tilrauna og nákvæmrar greiningar á niðurstöðunum til að betrumbæta leiðbeiningarnar ítrekað.</p>



<p>Listin að <strong>Hraðvirkt verkfræði</strong> táknar nauðsynlega færni fyrir alla sem leitast við að hafa áhrif á áhrifaríkan hátt við fullkomnustu gervigreindarkerfin. Að skilja og beita meginreglum skjótrar verkfræði getur til muna bætt gæði og skilvirkni þátttöku okkar í tækni sem byggir á gervigreind.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="God_astundun_og_taekni_i_hradvirkri_verkfraedi"></span>Góð ástundun og tækni í hraðvirkri verkfræði<span class="ez-toc-section-end"></span></h4>



<p>Listin að skjóta verkfræði fyrir efnis- og myndskapandi gervigreind, eins og OpenAI og MidJourney, krefst blöndu af tækni og bestu starfsvenjum til að ná gæða árangri. Hér eru nokkrar af þessum bestu starfsvenjum og aðferðum:</p>



<ol class="wp-block-list">
<li><strong>Notaðu dæmi:</strong> Með því að fella sýnishornsbeiðnir og -svörun inn í leiðbeiningarnar þínar getur það skilyrðað líkanið til að bregðast við á æskilegan hátt, með því að nota einn-skot eða fá-skot námstækni til að bæta nákvæmni svars líkansins.</li>



<li><strong>Gefðu gaum að vísbendingunum:</strong> Að innihalda vísbendingar í leiðbeiningunum þínum getur leiðbeint líkaninu til að búa til framleiðsla í takt við fyrirætlanir þínar. Þetta getur verið sérstaklega gagnlegt til að beina líkaninu í átt að æskilegri svörun.</li>



<li><strong>Prófaðu mismunandi fyrirkomulag:</strong> Röðin sem upplýsingar eru settar fram í hvetjunni getur haft áhrif á úttak líkansins. Það er gagnlegt að gera tilraunir með mismunandi fyrirkomulag leiðbeininga, aðalefni, dæmi og vísbendingar.</li>



<li><strong>Gefðu &#8220;úttak&#8221; til líkansins:</strong> Stundum getur líkanið átt í erfiðleikum með að klára verkefni nákvæmlega. Til að draga úr þessu, gefðu upp aðrar leiðir eða leiðbeiningar fyrir líkanið til að fylgja ef það finnur ekki fullnægjandi svar.</li>



<li><strong>Horfðu á lengdina:</strong> Tilvitnanir kunna að vera háðar stafatakmörkunum. Tilkynningar sem eru of langar geta verið erfiðar fyrir gervigreindarkerfi að vinna úr.</li>



<li><strong>Veldu orð þín vandlega:</strong> Árangursríkustu tilvitnanir nota skýrt, beint tungumál. Forðastu tvíræðni, litríkt mál, samlíkingar og slangur.</li>



<li><strong>Spyrðu opinna spurninga:</strong> Opnar spurningar veita meiri sveigjanleika í úttakinu. Til dæmis, hvetja til að lýsa flóknum þáttum er líklegri til að kalla fram ítarleg og yfirgripsmikil viðbrögð.</li>



<li><strong>Hafa samhengi:</strong> Vel hönnuð leiðbeiningar innihalda oft samhengi sem hjálpar gervigreindarkerfinu að sníða framleiðslu sína að fyrirhuguðum markhópi notandans.</li>



<li><strong>Stilltu úttakslengdarmarkmið eða takmörk:</strong> Þrátt fyrir að gervigreind sé hönnuð til að vera skapandi, þá er oft góð hugmynd að hafa hlífar fyrir þætti eins og úttakslengd.</li>



<li><strong>Forðastu misvísandi hugtök:</strong> Langar, flóknar ábendingar geta falið í sér óljós eða misvísandi hugtök. Gakktu úr skugga um að öll hugtök séu í samræmi.</li>



<li><strong>Notaðu greinarmerki til að skýra flóknar leiðbeiningar:</strong> Rétt eins og menn reiða sig á greinarmerki til að hjálpa til við að túlka texta, geta gervigreindartilmæli einnig notið góðs af skynsamlegri notkun kommu, gæsalappa og línuskila.</li>
</ol>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Grundvallarreglur_skjotrar_verkfraedi"></span>Grundvallarreglur skjótrar verkfræði<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering.png" alt="" class="wp-image-1714" srcset="/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering.png 1792w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-300x171.png 300w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-1024x585.png 1024w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-150x86.png 150w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-768x439.png 768w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Skilja_mikilvaegi_samhengis"></span>Skilja mikilvægi samhengis<span class="ez-toc-section-end"></span></h3>



<p>Nauðsynleg meginregla um <strong>skjót verkfræði</strong> er skilningur á því samhengi sem beiðni er sett fram í. Rétt eins og í mannlegu samtali hefur samhengi mikil áhrif á merkingu og mikilvægi svara. Þetta felur í sér að leiðbeiningar verða að vera hannaðar á þann hátt sem tekur mið af sérstöku umhverfi, markmiðum notanda og nákvæmu sviði umsóknar.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Skyrdu_tilgang_notenda"></span>Skýrðu tilgang notenda<span class="ez-toc-section-end"></span></h4>



<p>Skýr ásetning í boðun er lykilatriði til að fá viðeigandi svar frá gervigreindinni. Mikilvægt er að tilkynningin sé eins nákvæm og hægt er til að lágmarka tvíræðni. Stundum þýðir þetta að umorða eða bæta við upplýsingum sem leiða gervigreindina í átt að nákvæmari skilningi á því sem notandinn er að leita að.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Skipuleggja_og_forgangsrada_upplysingum"></span>Skipuleggja og forgangsraða upplýsingum<span class="ez-toc-section-end"></span></h4>



<p>Hvernig hvetja er byggð upp getur haft mikil áhrif á gæði svarsins sem þú færð. Þetta felur í sér að forgangsraða upplýsingum á rökréttan og samfelldan hátt þannig að gervigreindin geti unnið úr beiðninni á skilvirkan hátt, og að skipuleggja beiðnina þannig að mikilvægustu þættirnir séu dregnir fram og þannig leiðbeina gervigreindinni í átt að fullnægjandi viðbrögðum.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Val_um_tungumal_og_ordalag"></span>Val um tungumál og orðalag<span class="ez-toc-section-end"></span></h4>



<p>Orðin sem valin eru, tungumálastíll og heildarorðalag hvetjunnar gegna mikilvægu hlutverki í skyndiverkfræði. Skýrt, nákvæmt tungumál aðlagað að umræddu gervigreindarlíkani er nauðsynlegt. Til dæmis eru sumar gerðir móttækilegri fyrir náttúrulegu tungumáli, á meðan aðrar krefjast formlegrar eða tæknilegrar mótunar.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Itrekud_notkun_og_stodugar_umbaetur"></span>Ítrekuð notkun og stöðugar umbætur<span class="ez-toc-section-end"></span></h4>



<p>THE <strong>skjót verkfræði</strong> er oft endurtekið ferli. Það er ekki óalgengt að þurfa að stilla leiðbeiningarnar nokkrum sinnum áður en þú kemst að æskilegu svari. Að greina gervigreind viðbrögð og betrumbæta leiðbeiningar byggðar á þessum svörum er mikilvægur hluti af skyndiverkfræðiferlinu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Stjornun_a_ohefdbundnum_arangri"></span>Stjórnun á óhefðbundnum árangri<span class="ez-toc-section-end"></span></h4>



<p>Nauðsynlegt er að vita hvernig eigi að meðhöndla óvæntar eða óhefðbundnar niðurstöður, sem geta komið fram jafnvel með vel hönnuðum leiðbeiningum. Þetta felur í sér getu til að greina ástæður fyrir slíkum niðurstöðum og endurorða leiðbeiningar til að leiðrétta vandamálið.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="THekking_a_gervigreindarlikaninu_sem_notad_er"></span>Þekking á gervigreindarlíkaninu sem notað er<span class="ez-toc-section-end"></span></h4>



<p>Að lokum er ítarlegur skilningur á gervigreindarlíkaninu sem maður er að vinna með grundvallaratriði. Að þekkja styrkleika þess, takmarkanir og hvernig það vinnur úr leiðbeiningum er mikilvægt til að móta leiðbeiningar sem verða túlkaðar og framkvæmdar af gervigreindinni.</p>



<p>Þú munt því skilja að <strong>skjót verkfræði</strong> er sífellt mikilvægari færni eftir því sem gervigreind tækni verður flóknari og samþætt í daglegu lífi okkar. Svo byrjaðu að setja það á sinn stað eins fljótt og auðið er.</p>



---
title: "Forstå Turing-testen"
slug: "forsta-turing-testen"
excerpt: "Opprinnelsen og prinsippene til Turing-testen I verden av kunstig intelligens (AI) og databehandling inntar Turing-testen en fremtredende plass. Dette er en referansemetode utviklet for å evaluere en maskins evne til å imitere menneskelig intelligens. Opprinnelsen og prinsippene til denne revolusjonerende testen går tilbake til midten av 1900-tallet og er basert på komplekse filosofiske og beregningsmessige [&hellip;]"
date: "2024-03-09T12:57:25"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Bien-comprendre-le-test-de-Turing-3.png"
categories: ["ai-opplaering-og-grunnleggende-nb"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Comprendre le test de Turing facilement en 2 minutes" width="500" height="281" src="https://www.youtube.com/embed/XnFvfWWqosY?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/nb/forsta-turing-testen/#Opprinnelsen_og_prinsippene_til_Turing-testen" >Opprinnelsen og prinsippene til Turing-testen</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/nb/forsta-turing-testen/#Turing-testens_historie" >Turing-testens historie</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/nb/forsta-turing-testen/#Det_grunnleggende_prinsippet_for_Turing-testen" >Det grunnleggende prinsippet for Turing-testen</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/nb/forsta-turing-testen/#Gjennomforing_av_Turing-testen" >Gjennomføring av Turing-testen</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/nb/forsta-turing-testen/#Implikasjoner_og_problemer_med_Turing-testen" >Implikasjoner og problemer med Turing-testen</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/nb/forsta-turing-testen/#Kriteriene_for_en_vellykket_Turing-test" >Kriteriene for en vellykket Turing-test</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/nb/forsta-turing-testen/#Menneskelig_utskillelighetskriterium" >Menneskelig utskillelighetskriterium</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/nb/forsta-turing-testen/#Varighet_og_betingelser_for_testen" >Varighet og betingelser for testen</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/nb/forsta-turing-testen/#Evaluering_av_resultater_og_kontrovers" >Evaluering av resultater og kontrovers</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/nb/forsta-turing-testen/#Rollen_til_menneskelig_interaksjon" >Rollen til menneskelig interaksjon</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-11" href="/nb/forsta-turing-testen/#Utviklingen_av_Turing-testen_i_AI-tiden" >Utviklingen av Turing-testen i AI-tiden</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-12" href="/nb/forsta-turing-testen/#Den_originale_Turing-testen_og_dens_begrensninger" >Den originale Turing-testen og dens begrensninger</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/nb/forsta-turing-testen/#Fremskritt_innen_AI_og_utviklingen_av_Turing-testen" >Fremskritt innen AI og utviklingen av Turing-testen</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/nb/forsta-turing-testen/#Kompleksiteten_til_Turing-testen" >Kompleksiteten til Turing-testen</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/nb/forsta-turing-testen/#Turing-testens_fremtid" >Turing-testens fremtid</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Opprinnelsen_og_prinsippene_til_Turing-testen"></span>Opprinnelsen og prinsippene til Turing-testen<span class="ez-toc-section-end"></span></h2>



<p>I verden av kunstig intelligens (AI) og databehandling inntar Turing-testen en fremtredende plass. Dette er en referansemetode utviklet for å evaluere en maskins evne til å imitere menneskelig intelligens. Opprinnelsen og prinsippene til denne revolusjonerende testen går tilbake til midten av 1900-tallet og er basert på komplekse filosofiske og beregningsmessige konsepter.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Turing-testens_historie"></span>Turing-testens historie<span class="ez-toc-section-end"></span></h3>



<p>Turing-testen har fått navnet sitt fra oppfinneren, Alan Turing, en britisk matematiker regnet som en av pionerene innen informatikk. Han presenterte først denne testen i sin artikkel fra 1950 &#8220;Computing Machinery and Intelligence&#8221;, publisert i det britiske tidsskriftet Mind. Alan Turing utforsker spørsmålet om maskiner kan tenke og foreslår en metode for å evaluere kunstig intelligens.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Det_grunnleggende_prinsippet_for_Turing-testen"></span>Det grunnleggende prinsippet for Turing-testen<span class="ez-toc-section-end"></span></h4>



<p>Grunnprinsippet i Turing-testen er bemerkelsesverdig enkelt. Den er basert på et imitasjonsspill der et menneske, dommeren, har som oppgave å avgjøre om samtalepartneren er en maskin eller en annen menneskelig person. Dommeren kommuniserer med de to samtalepartnerne via en skjerm og et tastatur, noe som garanterer umuligheten av å stole på fysiske ledetråder for dommen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gjennomforing_av_Turing-testen"></span>Gjennomføring av Turing-testen<span class="ez-toc-section-end"></span></h4>



<p>Testen utføres som følger:<br>1. Dommeren stiller ulike spørsmål skriftlig.<br>2. Den menneskelige samtalepartneren og maskinen svarer også skriftlig.<br>3. Hvis dommeren ikke i tilstrekkelig grad kan skille maskinen fra mennesket, består maskinen testen.<br>Målet er å se om en maskin kan konkurrere med menneskelig intelligens til et nivå der responsene ikke kan skilles fra en mann eller kvinne.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Implikasjoner_og_problemer_med_Turing-testen"></span>Implikasjoner og problemer med Turing-testen<span class="ez-toc-section-end"></span></h4>



<p>Turing-testen har viktige filosofiske og tekniske implikasjoner. Det inviterer til refleksjon over tankens og bevissthetens natur og hva som utgjør sann intelligens. På et teknisk nivå har testen oppmuntret til betydelige fremskritt innen AI og naturlig språkbehandling. Systemer som IBM Watson eller stemmeassistenter som <strong>Siri</strong> av<strong>eple</strong>, <strong>Google Assistant</strong> Og <strong>Alexa</strong> av<strong>Amazon</strong> er moderne eksempler på innsats for å lage maskiner som potensielt kan bestå Turing-testen.</p>



<p>Turing-testen er fortsatt et tema for diskusjon og debatt, spesielt angående dens gyldighet og relevans i evaluering av kunstig intelligens. Mens noen hevder at testen kun måler samtalesimulator og ikke intelligens i seg selv, ser andre på det som en utfordring for fremtidig AI-utvikling.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Kriteriene_for_en_vellykket_Turing-test"></span>Kriteriene for en vellykket Turing-test<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Bien-comprendre-le-test-de-Turing.png" alt="" class="wp-image-806" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Bien-comprendre-le-test-de-Turing.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>En vellykket Turing-test er en måte å måle intelligensen til en maskin ved å vurdere dens evne til å imitere menneskelig atferd til det punktet hvor en menneskelig observatør ikke kan skille mellom svarene til maskinen og de til en virkelig person. Innenfor kunstig intelligens er den berømte Turing-testen, foreslått av Alan Turing i 1950, fortsatt en referanse i hjertet av mange diskusjoner om maskiners bevissthet og intelligens. Så hva er kriteriene som må oppfylles for at en Turing-test skal anses som vellykket?</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Menneskelig_utskillelighetskriterium"></span>Menneskelig utskillelighetskriterium<span class="ez-toc-section-end"></span></h3>



<p>Det sentrale målet med Turing-testen er å teste om en menneskelig avhører er i stand til å skille en maskin fra et menneske, ganske enkelt basert på deres svar på spørsmål eller utsagn. Hvis samtalepartneren ikke kan si med sikkerhet om svarene kommer fra et menneske eller en maskin, anses testen som bestått. Med dette i tankene må flere kriterier respekteres:</p>



<p>&#8211; <strong>Kvaliteten på svarene</strong> : De må være sammenhengende og virke naturlige, som om de kom fra et menneske.<br>&#8211; <strong>Mangfold i samtale</strong> : Maskinens evne til å delta i en lang rekke emner indikerer en form for forståelse eller tilpasning.<br>&#8211; <strong>Håndtere uklarheter</strong> : en maskin må kunne håndtere språkets finesser og nyanser, inkludert metaforer, humor og kulturelle referanser.<br>&#8211; <strong>Følelser og empati</strong>: Kunstig intelligens bør vise en form for empati eller passende følelsesmessig respons på situasjoner.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Varighet_og_betingelser_for_testen"></span>Varighet og betingelser for testen<span class="ez-toc-section-end"></span></h4>



<p>Det er ingen standardisert varighet for en Turing-test, men det er generelt akseptert at en lengre periode kan øke påliteligheten til de oppnådde resultatene. Følgende forhold er også viktige for en gyldig test:</p>



<p>&#8211; <strong>Total anonymitet</strong> : Avhøreren skal ikke ha noen visuelle eller hørbare ledetråder som kan hjelpe dem med å identifisere enheten bak svarene.<br>&#8211; <strong>Nøytralt kommunikasjonsgrensesnitt</strong> : Svar må overføres via tastatur og skjerm for å unngå diskriminering basert på stemme eller håndskrift.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Evaluering_av_resultater_og_kontrovers"></span>Evaluering av resultater og kontrovers<span class="ez-toc-section-end"></span></h4>



<p>Vurderinger må baseres på objektive kriterier, selv om den subjektive vurderingen til den menneskelige intervjueren spiller en sentral rolle i den endelige avgjørelsen. Følgende aspekter er avgjørende:<br>&#8211; <strong>Suksessstatistikk</strong> : prosentandelen av ganger dommere blir lurt er en viktig indikator.<br>&#8211; <strong>Bias kontroll</strong> : Spørsmålsskjevhet må minimeres ved en god vurderingsmetode for å sikre rettferdighet i testen.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Rollen_til_menneskelig_interaksjon"></span>Rollen til menneskelig interaksjon<span class="ez-toc-section-end"></span></h4>



<p>Interaksjoner under Turing-testen skal være naturlige og flytende, og etterligne flyten til en ekte menneskelig samtale. Følgende elementer bør tas i betraktning:<br>&#8211; <strong>Reaktivitet</strong> : Maskinen må svare på spørsmål i et tempo som ligner på en vanlig menneskelig samtale.<br>&#8211; <strong>Toveis interaksjon</strong> : Maskinen skal ikke bare svare på spørsmål, men også kunne stille spørsmål for å vise at den følger med og deltar aktivt i samtalen.</p>



<p>En vellykket Turing-test er ikke bare et spørsmål om å lure en samtalepartner én gang, men om å gjøre det konsekvent, under forskjellige forhold og med forskjellige dommere. Selv om denne testen er mye diskutert og noen ganger kritisert for sin mangel på presisjon på om en AI faktisk forstår eller er bevisst, er den fortsatt en interessant utfordring for AI-designere.<strong>AI</strong>. Dette er spesielt tilfellet for bedrifter i forkant av teknologisk innovasjon, som f.eks <strong>Google</strong> med sin assistent eller <strong>OpenAI</strong> med GPT-3 / GPT-4, som søker å skape stadig mer sofistikerte systemer. </p>



<p>Selv om ingen maskin ennå har bestått Turing-testen ved å imitere et menneske perfekt, presser fremskritt innen kunstig intelligens oss til hele tiden å revurdere grensene for hva en maskin kan utrette.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Utviklingen_av_Turing-testen_i_AI-tiden"></span>Utviklingen av Turing-testen i AI-tiden<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Bien-comprendre-le-test-de-Turing-2.png" alt="" class="wp-image-808" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Bien-comprendre-le-test-de-Turing-2.png 1792w, /images/blog/Bien-comprendre-le-test-de-Turing-2-300x171.png 300w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1024x585.png 1024w, /images/blog/Bien-comprendre-le-test-de-Turing-2-150x86.png 150w, /images/blog/Bien-comprendre-le-test-de-Turing-2-768x439.png 768w, /images/blog/Bien-comprendre-le-test-de-Turing-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Turing-testen, designet av Alan Turing på 1950-tallet, hadde som mål å vurdere en maskins evne til å imitere menneskelig atferd til det punktet at samtalepartneren ikke kan skille om dens korrespondent er en mann eller en maskin. I AI-tiden fortsetter Turing-testen å tjene som en målestokk for å måle utviklingen av kunstig intelligens, selv om den har blitt kritisert og redesignet på grunn av dramatiske teknologiske fremskritt.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Den_originale_Turing-testen_og_dens_begrensninger"></span>Den originale Turing-testen og dens begrensninger<span class="ez-toc-section-end"></span></h3>



<p>Opprinnelig er Turing-testen en test av tekstlig samtale mellom et menneske og en maskin. Målet er å finne ut om maskinen kan føre en samtale som ikke kan skilles fra et menneskes. Denne testen har imidlertid begrensninger. Det å bestå testen betyr faktisk ikke nødvendigvis at maskinen har ekte intelligens eller forståelse, men ganske enkelt at den kan overbevise et menneske om sin menneskelighet for en kort stund.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Fremskritt_innen_AI_og_utviklingen_av_Turing-testen"></span>Fremskritt innen AI og utviklingen av Turing-testen<span class="ez-toc-section-end"></span></h3>



<p>Med den raske utviklingen av kunstig intelligens er enkel tekstutveksling ikke lenger tilstrekkelig til å bedømme sofistikeringen til en AI. Nåværende systemer, som de som er utviklet av <strong>Google</strong> Eller <strong>OpenAI</strong>, er i stand til å føre komplekse samtaler, komponere musikk, generere realistiske bilder og til og med skrive sammenhengende tekster om en rekke emner.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Kompleksiteten_til_Turing-testen"></span>Kompleksiteten til Turing-testen<span class="ez-toc-section-end"></span></h3>



<p>For å tilpasse seg utviklingen av AI, foreslår forskere mer forseggjorte versjoner av Turing-testen. Disse nye versjonene kan innebære multimodal interaksjon med maskiner (tekst, bilde, lyd), kreativitetstester eller vurderinger av forståelse og sunn fornuft, for å presse grensene for kunstig intelligens langt utover enkel imitasjon.</p>



<p>Her er eksempler på situasjoner som representerer utviklingen av Turing-testen brukt på den moderne æraen av AI:</p>



<p>&#8211; Dybdesamtaler om spesifikke temaer<br>&#8211; Oppretting av originalt kunstnerisk innhold<br>&#8211; Reaksjoner på uventede hendelser eller ny informasjon<br>&#8211; Sanntidsinteraksjon med omgivelsene, for eksempel via roboter</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Turing-testens_fremtid"></span>Turing-testens fremtid<span class="ez-toc-section-end"></span></h2>



<p>Den opprinnelige ideen til Turing-testen utvikler seg nå til et bredere sett med vurderinger, ment å teste ikke bare evnen til å imitere, men også autonomien, læringen, kreativiteten og empatien til kunstig intelligens. Disse testene måler ikke lenger bare kvaliteten på imitasjon, men søker å vurdere i hvilken grad en AI kan betraktes som intelligent i henhold til stadig utviklende menneskelige kriterier.</p>



<p>Turing-testen fortsetter å utvikle seg sammen med utrolige fremskritt innen kunstig intelligens. Imidlertid forblir essensen den samme: søker å forstå hvor nær teknologi kan komme menneskelig intelligens og potensielt overgå den. </p>



<p>Det er i denne søken at hjertet av fascinasjonen for AI og dens fremtidige utvikling ligger.</p>



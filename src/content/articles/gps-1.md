---
title: "Како да најдете GPS координати (широчина и должина) на Google Maps?"
slug: "gps-1"
excerpt: "НА GPS (Global Positioning System) е технологија која стана суштинска во нашиот секојдневен живот. Користејќи сигнали пренесени од сателити, на ГПС систем ни овозможува точно да ја одредиме нашата позиција во форма на географски координати. Овие координати се претставени со два клучни елементи: на географска ширина и на географска должина. Во оваа статија, ќе го [&hellip;]"
date: "2024-03-09T12:03:47"
featuredImage: "/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-3.png"
categories: ["%d1%82%d0%b5%d1%85%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d1%98%d0%b0-%d0%b8-%d0%b4%d0%b8%d0%b3%d0%b8%d1%82%d0%b0%d0%bb%d0%bd%d0%b0-mk"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Implanter des points sur Google Earth à partir des coordonnées X et Y" width="500" height="281" src="https://www.youtube.com/embed/9ymcbTqEfNo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>    НА <strong>GPS</strong> (Global Positioning System) е технологија која стана суштинска во нашиот секојдневен живот. Користејќи сигнали пренесени од сателити, на <strong>ГПС систем</strong> ни овозможува точно да ја одредиме нашата позиција во форма на географски координати. </p>



<p>Овие координати се претставени со два клучни елементи: на <strong>географска ширина</strong> и на <strong>географска должина</strong>. Во оваа статија, ќе го истражиме светот на GPS координатите и ќе ја разбереме нивната суштинска улога во геолокацијата.</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-1" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%9A%D0%BE%D0%B8_%D1%81%D0%B5_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8%D1%82%D0%B5" >Кои се GPS координатите?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-2" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%9A%D0%BE%D1%80%D0%B8%D1%81%D0%BD%D0%BE%D1%81%D1%82%D0%B0_%D0%BD%D0%B0_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8%D1%82%D0%B5" >Корисноста на GPS координатите</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%9A%D0%B0%D0%BA%D0%BE_%D0%B4%D0%B0_%D0%BD%D0%B0%D1%98%D0%B4%D0%B5%D1%82%D0%B5_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8_%D0%BD%D0%B0_Google_Maps" >Како да најдете GPS координати на Google Maps</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%A1%D0%BE%D0%B2%D0%B5%D1%82_%D0%B7%D0%B0_%D0%B7%D0%B3%D0%BE%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D0%B0_%D1%82%D0%BE%D1%87%D0%BD%D0%BE%D1%81%D1%82" >Совет за зголемена точност</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%A7%D0%B8%D1%82%D0%B0%D1%98%D1%82%D0%B5_%D0%B8_%D1%80%D0%B0%D0%B7%D0%B1%D0%B5%D1%80%D0%B5%D1%82%D0%B5_%D0%B3%D0%B8_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8%D1%82%D0%B5" >Читајте и разберете ги GPS координатите</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%9A%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B5%D1%82%D0%B5_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8_%D0%BD%D0%B0_%E2%80%9E%D0%9A%D0%B0%D1%80%D1%82%D0%B8_%D0%BD%D0%B0_Google%E2%80%9C" >Користете GPS координати на „Карти на Google“.</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/mk/%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%bd%d0%b0%d1%98%d0%b4%d0%b5%d1%82%d0%b5-gps-%d0%ba%d0%be%d0%be%d1%80%d0%b4%d0%b8%d0%bd%d0%b0%d1%82%d0%b8-%d1%88%d0%b8%d1%80%d0%be%d1%87%d0%b8%d0%bd%d0%b0/#%D0%9F%D0%B8%D0%BD_%D0%B7%D0%B0_%D1%81%D0%BF%D0%BE%D0%B4%D0%B5%D0%BB%D1%83%D0%B2%D0%B0%D1%9A%D0%B5_%D0%B8_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8" >Пин за споделување и координати</a></li></ul></li></ul></nav></div>
<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D0%BE%D0%B8_%D1%81%D0%B5_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8%D1%82%D0%B5"></span>Кои се GPS координатите?<span class="ez-toc-section-end"></span></h3>



<p>    GPS координатите се референтни точки кои укажуваат на одредена локација на Земјата. Таму <strong>географска ширина</strong> го мери растојанието северно или југ од екваторот и варира помеѓу -90 степени (на Јужниот пол) и +90 степени (на Северниот Пол). Таму <strong>географска должина</strong>, од своја страна, го мери растојанието источно или западно од меридијанот Гринич и варира помеѓу -180 и +180 степени. Тоа е комбинацијата на овие две мерења што овозможува да се одреди прецизна географска точка.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D0%BE%D1%80%D0%B8%D1%81%D0%BD%D0%BE%D1%81%D1%82%D0%B0_%D0%BD%D0%B0_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8%D1%82%D0%B5"></span>Корисноста на GPS координатите<span class="ez-toc-section-end"></span></h4>



<p>    Точноста што ја нудат GPS координатите има многу практични примени во нашиот секојдневен живот. Тие се користат за навигација, овозможувајќи им на корисниците да го најдат патот до дестинацијата или да следат рута кога патуваат со автомобил, велосипед или пеш преку паметни телефони и интегрирани системи за навигација. Тие се исто така клучни за операциите за пребарување и спасување, што овозможува прецизно да се лоцираат изгубените или вознемирените луѓе.</p>



<p>Во науката и истражувањето, GPS координатите играат важна улога во студиите како што се следење тектонски движења, следење диви животни и многу повеќе. Конечно, тие се суштински елемент за сектори како што се прецизно земјоделство, географирање и услуги за испорака.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D0%B0%D0%BA%D0%BE_%D0%B4%D0%B0_%D0%BD%D0%B0%D1%98%D0%B4%D0%B5%D1%82%D0%B5_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8_%D0%BD%D0%B0_Google_Maps"></span>Како да најдете GPS координати на Google Maps<span class="ez-toc-section-end"></span></h4>



<p>    За да ја пронајдете вашата географска ширина и должина на <strong>Гугл мапи</strong>, постојат неколку едноставни чекори што треба да се следат:</p>



<ol class="wp-block-list">
<li>Отвори <strong>Гугл мапи</strong> во вашиот веб-прелистувач или на вашата мобилна апликација.</li>



<li>Кликнете со десното копче на точката од интерес на мапата (или допрете и задржете на мобилен телефон).</li>



<li>Во менито што се појавува, кликнете &#8220;Кои се координатите?&#8221; или директно ќе ги видите координатите прикажани во мал скокачки прозорец.</li>



<li>Копирајте ги GPS координатите кои се претставени како два броја (на пример, 48,8566° N, 2,3522° E за локацијата на Париз).</li>
</ol>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A1%D0%BE%D0%B2%D0%B5%D1%82_%D0%B7%D0%B0_%D0%B7%D0%B3%D0%BE%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D0%B0_%D1%82%D0%BE%D1%87%D0%BD%D0%BE%D1%81%D1%82"></span>Совет за зголемена точност<span class="ez-toc-section-end"></span></h4>



<p>За уште поголема прецизност, откако ќе кликнете со десното копче на саканата локација, можете да го усовршите изборот со малку поместување на покажувачот пред да изберете „Повеќе информации за оваа локација“. Ова може да биде корисно кога се наоѓаат координати за многу специфична локација, како што е влезот во зграда или точка од природен интерес.</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-.png" alt="" class="wp-image-1613" srcset="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-.png 1792w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--300x171.png 300w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--1024x585.png 1024w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--150x86.png 150w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--768x439.png 768w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps--1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A7%D0%B8%D1%82%D0%B0%D1%98%D1%82%D0%B5_%D0%B8_%D1%80%D0%B0%D0%B7%D0%B1%D0%B5%D1%80%D0%B5%D1%82%D0%B5_%D0%B3%D0%B8_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8%D1%82%D0%B5"></span>Читајте и разберете ги GPS координатите<span class="ez-toc-section-end"></span></h3>



<p>ГПС координатите обично се во форма на два броја што ја претставуваат географската ширина и должина. Разбирањето како да се читаат овие бројки е од суштинско значење за правилно толкување на координатите.</p>



<ul class="wp-block-list">
<li><strong>Географска ширина:</strong> тоа е мерењето во степени што го покажува растојанието северно или југ од екваторот, кое варира од -90° до +90°.</li>



<li><strong>Географска должина:</strong> тоа е мерењето во степени што го означува растојанието источно или западно од меридијанот Гринич, кое варира од -180° до +180°.</li>
</ul>



<p>            На <strong>Гугл мапи</strong>, координатите обично се прикажуваат во децимална форма. На пример, Ајфеловата кула во Париз има приближни координати на <strong>Географска ширина: 48,8584</strong> И <strong>Географска должина: 2,2945</strong>.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B5%D1%82%D0%B5_GPS_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8_%D0%BD%D0%B0_%E2%80%9E%D0%9A%D0%B0%D1%80%D1%82%D0%B8_%D0%BD%D0%B0_Google%E2%80%9C"></span>Користете GPS координати на „Карти на Google“.<span class="ez-toc-section-end"></span></h4>



<p>Откако ќе ги имате GPS координатите на местото што го сакате, можете лесно да го лоцирате <strong>Гугл мапи</strong>. Еве како:</p>



<ol class="wp-block-list">
<li>Се вратат во <strong>Гугл мапи</strong>.</li>



<li>Во лентата за пребарување, напишете ги координатите што ги добивте, а потоа притиснете Enter или кликнете на копчето за пребарување.</li>



<li><strong>Гугл мапи</strong> ќе ве однесе директно до точната локација што одговара на внесените координати.</li>
</ol>



<p>            Овој метод е особено корисен за навигација до локации кои не се вообичаени, за кои традиционалните адреси не се доволни.</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2.png" alt="" class="wp-image-1615" srcset="/images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2.png 1792w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-300x171.png 300w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-1024x585.png 1024w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-150x86.png 150w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-768x439.png 768w, /images/blog/Comment-Trouver-les-Coordonnees-GPS-Latitude-et-Longitude-sur-Google-Maps-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9F%D0%B8%D0%BD_%D0%B7%D0%B0_%D1%81%D0%BF%D0%BE%D0%B4%D0%B5%D0%BB%D1%83%D0%B2%D0%B0%D1%9A%D0%B5_%D0%B8_%D0%BA%D0%BE%D0%BE%D1%80%D0%B4%D0%B8%D0%BD%D0%B0%D1%82%D0%B8"></span>Пин за споделување и координати<span class="ez-toc-section-end"></span></h4>



<p>        По наоѓање или внесување на координати, <strong>Гугл мапи</strong> обезбедува и опција за споделување на оваа информација или обележување со игла за идна референца. Еве како да го направите тоа:</p>



<ol class="wp-block-list">
<li>Откако ќе ги имате деталите за контакт, користете го вграденото копче за споделување за да ги испратите информациите преку е-пошта, порака или на социјалните медиуми.</li>



<li>За да ја прикачите локацијата, кликнете на иконата за игла веднаш до деталите за контакт за да биде додадена во „Вашите места“ за лесен пристап подоцна.</li>
</ol>



<p>            Дали да споделите место за состаноци, за урбекс, лов на богатство или едноставно за работа или за слободни активности, знајте како да најдете и читате GPS координати на <strong>Гугл мапи</strong> е практична вештина. Само следете ги чекорите споменати погоре и ќе можете прецизно да лоцирате која било точка на Земјата.</p>



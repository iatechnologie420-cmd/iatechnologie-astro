---
title: "د اعتراض پر بنسټ پروګرامونه: دا څه شی دی او د څه لپاره دی؟"
slug: "%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c"
excerpt: "د آبجیکٹ اورینټ پروګرام کولو اساسات هلته د آبجیکٹ اورینټ پروګرام کول (OOP) د پروګرام کولو تمثیل دی چې د کمپیوټر غوښتنلیکونو او پروګرامونو ډیزاین کولو لپاره &#8220;شیان&#8221; کاروي. دا توکي د ریښتیني نړۍ نهادونو استازیتوب کوي او پراختیا کونکو ته اجازه ورکوي چې ډیر انعطاف وړ ، د توزیع وړ ، او ساتلو وړ [&hellip;]"
date: "2024-03-09T12:48:52"
featuredImage: "/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-3.png"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps", "%da%a9%d9%85%d9%be%db%8c%d9%88%d9%bc%d8%b1%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d9%bc%d8%a7-ps"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AF_%D8%A2%D8%A8%D8%AC%DB%8C%DA%A9%D9%B9_%D8%A7%D9%88%D8%B1%DB%8C%D9%86%D9%BC_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85_%DA%A9%D9%88%D9%84%D9%88_%D8%A7%D8%B3%D8%A7%D8%B3%D8%A7%D8%AA" >د آبجیکٹ اورینټ پروګرام کولو اساسات</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AE%D9%84%D8%A7%D8%B5%D9%88%D9%86" >خلاصون</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#encapsulation" >encapsulation</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%85%DB%8C%D8%B1%D8%A7%D8%AB" >میراث</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%BE%D9%88%D9%84%DB%8C%D9%85%D9%88%D8%B1%D9%81%DB%8C%D8%B2%D9%85" >پولیمورفیزم</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%BC%D9%88%D9%84%DA%AB%D9%8A_%D8%A7%D9%88_%D8%AA%D9%88%DA%A9%D9%8A" >ټولګي او توکي</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AC%D9%88%DA%93%D9%88%D9%86%DA%A9%D9%8A_%D8%A7%D9%88_%D9%88%DB%8C%D8%AC%D8%A7%DA%93%D9%88%D9%86%DA%A9%D9%8A" >جوړونکي او ویجاړونکي</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%85%DB%8C%D8%AA%D9%88%D8%AF%D9%88%D9%86%D9%87" >میتودونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%B5%D9%81%D8%AA%D9%88%D9%86%D9%87" >صفتونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%84%DB%8C%D8%AF%D9%84%D9%88%D8%B1%DB%8C_%D8%B9%D8%A7%D9%85%D9%87%D8%8C_%D8%B4%D8%AE%D8%B5%D9%8A_%D8%A7%D9%88_%D8%AE%D9%88%D9%86%D8%AF%D9%8A" >لیدلوری: عامه، شخصي او خوندي</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%BC%D9%88%D9%84%D9%86%D9%87%D8%8C_%D9%85%D8%AC%D9%85%D9%88%D8%B9%D9%87_%D8%A7%D9%88_%D8%AA%D8%B1%DA%A9%DB%8C%D8%A8" >ټولنه، مجموعه او ترکیب</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AF_OOP_%DA%AB%D9%BC%DB%90_%D8%A7%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87" >د OOP ګټې او عملي غوښتنلیکونه</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AF_%D8%A2%D8%A8%D8%AC%DB%8C%DA%A9%D9%B9_%D8%A7%D9%88%D8%B1%DB%8C%D9%86%D9%BC_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85_%DA%A9%D9%88%D9%84%D9%88_%DA%AB%D9%BC%DB%90" >د آبجیکٹ اورینټ پروګرام کولو ګټې</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AF_%D8%A7%D8%B9%D8%AA%D8%B1%D8%A7%D8%B6_%D9%BE%D8%B1_%D8%A8%D9%86%D8%B3%D9%BC_%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87_%DA%A9%D9%88%D9%84%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87" >د اعتراض پر بنسټ برنامه کولو عملي غوښتنلیکونه</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AF_%D9%86%D9%88%D8%B1%D9%88_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%D9%88%D9%86%D9%88_%D8%AA%D9%85%D8%AB%DB%8C%D9%84%D9%88%D9%86%D9%88_%D8%B3%D8%B1%D9%87_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84" >د نورو پروګرامونو تمثیلونو سره پرتله کول</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-16" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D9%84%D8%A7%D8%B2%D9%85%D9%8A_%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87_%DA%A9%D9%88%D9%84" >لازمي برنامه کول</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%A7%D8%B9%D9%84%D8%A7%D9%86%D8%A7%D8%AA%D9%8A_%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87_%DA%A9%D9%88%D9%84" >اعلاناتي برنامه کول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%DA%A9%D8%A7%D8%B1%D9%8A_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%D9%88%D9%86%D9%87" >کاري پروګرامونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-19" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%D8%AF_%D8%A2%D8%A8%D8%AC%DB%8C%DA%A9%D9%B9_%D8%A7%D9%88%D8%B1%DB%8C%D9%86%D9%BC%DA%89_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%DB%8C%D9%86%DA%AB_OOP" >د آبجیکٹ اورینټډ پروګرامینګ (OOP)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/ps/%d8%af-%d8%a7%d8%b9%d8%aa%d8%b1%d8%a7%d8%b6-%d9%be%d8%b1-%d8%a8%d9%86%d8%b3%d9%bc-%d9%be%d8%b1%d9%88%da%ab%d8%b1%d8%a7%d9%85%d9%88%d9%86%d9%87-%d8%af%d8%a7-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c/#%DA%81%D9%88%D8%A7%D8%A8_%D9%88%D8%B1%DA%A9%D9%88%D9%88%D9%86%DA%A9%D9%8A_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%D9%88%D9%86%D9%87" >ځواب ورکوونکي پروګرامونه</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A2%D8%A8%D8%AC%DB%8C%DA%A9%D9%B9_%D8%A7%D9%88%D8%B1%DB%8C%D9%86%D9%BC_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85_%DA%A9%D9%88%D9%84%D9%88_%D8%A7%D8%B3%D8%A7%D8%B3%D8%A7%D8%AA"></span>د آبجیکٹ اورینټ پروګرام کولو اساسات<span class="ez-toc-section-end"></span></h2>



<p>هلته <strong>د آبجیکٹ اورینټ پروګرام کول</strong> (OOP) د پروګرام کولو تمثیل دی چې د کمپیوټر غوښتنلیکونو او پروګرامونو ډیزاین کولو لپاره &#8220;شیان&#8221; کاروي. دا توکي د ریښتیني نړۍ نهادونو استازیتوب کوي او پراختیا کونکو ته اجازه ورکوي چې ډیر انعطاف وړ ، د توزیع وړ ، او ساتلو وړ سافټویر رامینځته کړي. په دې مقاله کې، موږ به هغه بنسټیز مفکورې وپلټئ چې د OOP بنسټ جوړوي.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="585" src="/images/blog/image-1024x585.png" alt="" class="wp-image-13812" srcset="/images/blog/image-1024x585.png 1024w, /images/blog/image-300x171.png 300w, /images/blog/image-150x86.png 150w, /images/blog/image-768x439.png 768w, /images/blog/image-1536x878.png 1536w, /images/blog/image.png 1792w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AE%D9%84%D8%A7%D8%B5%D9%88%D9%86"></span>خلاصون<span class="ez-toc-section-end"></span></h3>



<p>L&#8217;<strong>خلاصون</strong> هغه پروسه ده چې له مخې یې یو پروګرامر د یو څیز ټول غیر اړونده توضیحات پټوي ترڅو کارونکي ته یوازې مهمې ځانګړتیاوې وښیې. دا دا اسانه کوي چې پوه شي چې څیزونه پرته له دې چې د دوی د داخلي پیچلتیا په اړه اندیښنه وکړي څنګه کار کوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="encapsulation"></span>encapsulation<span class="ez-toc-section-end"></span></h4>



<p>L&#8217;<strong>encapsulation</strong> یو تخنیک دی چې د ګروپ کولو ډاټا او هغه میتودونه لري چې په ورته واحد کې یې اداره کوي، ډیری وختونه د ټولګي په نوم یادیږي. Encapsulation یوازې د ټاکل شوي میتودونو له لارې د ترمیم کولو اجازه ورکولو سره د معلوماتو بشپړتیا ساتي ، د مستقیم غیر مجاز لاسرسي مخه نیسي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%85%DB%8C%D8%B1%D8%A7%D8%AB"></span>میراث<span class="ez-toc-section-end"></span></h4>



<p>L&#8217;<strong>میراث</strong> د OOP ځانګړتیا ده چې تاسو ته اجازه درکوي د موجوده ټولګي پراساس یو نوی ټولګي رامینځته کړئ. نوې ټولګي چې د اخستل شوي ټولګي په نوم یادیږي، د اساس ټولګي ځانګړتیاوې او میتودونه په میراث پاتې دي، د کوډ بیا کارولو او د ټولګي درجه بندي رامینځته کولو ته اجازه ورکوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BE%D9%88%D9%84%DB%8C%D9%85%D9%88%D8%B1%D9%81%DB%8C%D8%B2%D9%85"></span>پولیمورفیزم<span class="ez-toc-section-end"></span></h4>



<p>د <strong>پولیمورفیزم</strong> د یو میتود وړتیا ده چې مختلف عملونه ترسره کړي د هغه څیز پورې اړه لري چې ورته ویل کیږي. د پولیمورفیزم دوه اصلي ډولونه شتون لري: د ډیر بار کولو پولیمورفیزم (ډیری میتودونه ورته نوم لري مګر د مختلف پیرامیټونو سره) او د میراث پولیمورفیزم (یو اخستل شوی ټولګی د ورته نوم سره میتود کاروي لکه د خپل ټولګي والدین میتود).</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BC%D9%88%D9%84%DA%AB%D9%8A_%D8%A7%D9%88_%D8%AA%D9%88%DA%A9%D9%8A"></span>ټولګي او توکي<span class="ez-toc-section-end"></span></h4>



<p>د <strong>ټولګي</strong> ماډلونه، یا بلوپرینټ دي، چې د انفرادي مثالونو جوړولو لپاره کارول کیږي چې په نوم یادیږي <strong>توکي</strong>. د ټولګي څخه جوړ شوی هر څیز کولی شي د ټولګي د ځانګړتیاو لپاره خپل ارزښت ولري، مګر ورته میتودونه شریکوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AC%D9%88%DA%93%D9%88%D9%86%DA%A9%D9%8A_%D8%A7%D9%88_%D9%88%DB%8C%D8%AC%D8%A7%DA%93%D9%88%D9%86%DA%A9%D9%8A"></span>جوړونکي او ویجاړونکي<span class="ez-toc-section-end"></span></h4>



<p>الف <strong>جوړونکی</strong> د ټولګي یو ځانګړی میتود دی چې په اتوماتيک ډول ویل کیږي کله چې د دې ټولګي اعتراض رامینځته شي. دا عموما د اعتراض د ځانګړتیاوو د پیل کولو لپاره کارول کیږي. الف <strong>ویجاړونکی</strong>د هغې برخې لپاره، هغه وخت ویل کیږي کله چې یو شی د ویجاړیدو په حال کې وي، چې تخصیص شوي سرچینې خوشې کولو ته اجازه ورکوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%85%DB%8C%D8%AA%D9%88%D8%AF%D9%88%D9%86%D9%87"></span>میتودونه<span class="ez-toc-section-end"></span></h4>



<p>د <strong>میتودونه</strong> هغه دندې دي چې د ټولګي دننه تعریف شوي چې چلند یا کړنې تشریح کوي چې یو شی یې ترسره کولی شي. هره طریقه کولی شي د یو ځانګړي کار ترسره کولو لپاره د اعتراض داخلي ځانګړتیاو سره کار وکړي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%B5%D9%81%D8%AA%D9%88%D9%86%D9%87"></span>صفتونه<span class="ez-toc-section-end"></span></h4>



<p>د <strong>صفات</strong> هغه متغیرونه دي چې د ټولګي دننه تعریف شوي او د یو څیز حالت یا ځانګړي ځانګړتیاوې استازیتوب کوي. ځانګړتیاوې کیدای شي د مختلف ډیټا ډولونو څخه وي، لکه شمیرې، تارونه، یا د نورو ټولګیو توکي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%84%DB%8C%D8%AF%D9%84%D9%88%D8%B1%DB%8C_%D8%B9%D8%A7%D9%85%D9%87%D8%8C_%D8%B4%D8%AE%D8%B5%D9%8A_%D8%A7%D9%88_%D8%AE%D9%88%D9%86%D8%AF%D9%8A"></span>لیدلوری: عامه، شخصي او خوندي<span class="ez-toc-section-end"></span></h4>



<p><strong>اوریدونکي</strong>, <strong>شخصي</strong> او <strong>ساتل شوی</strong> د لید بدلون کونکي دي چې د ټولګي ځانګړتیاو او میتودونو ته لاسرسی کنټرولوي. عامه غړو ته له هر ځای څخه لاسرسی کیدی شي ، خصوصي غړي یوازې په ټولګي کې لاسرسی کیدی شي چیرې چې دوی تعریف شوي ، او خوندي غړي په ټولګي کې لاسرسی کیدی شي چیرې چې دوی تعریف شوي او همدارنګه د دوی ترلاسه شوي ټولګي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BC%D9%88%D9%84%D9%86%D9%87%D8%8C_%D9%85%D8%AC%D9%85%D9%88%D8%B9%D9%87_%D8%A7%D9%88_%D8%AA%D8%B1%DA%A9%DB%8C%D8%A8"></span>ټولنه، مجموعه او ترکیب<span class="ez-toc-section-end"></span></h4>



<p>په OOP کې، شرایط <strong>ټولنه</strong>, <strong>مجموعه</strong> او <strong>ترکیب</strong> هغه مختلفې لارې تشریح کړئ چې په کوم کې شیان یو بل سره تړل کیدی شي. انجمن د دوو شیانو تر منځ اړیکه ده چې له یو بل څخه خپلواکه وي، مجموعه د &#8220;ټولې برخې&#8221; اړیکه ده چیرې چې برخې له ټول څخه جلا شتون لري، او ترکیب د &#8220;ټولې برخې&#8221; اړیکه ده چیرې چې برخې پرته له شتون څخه شتون نلري. ټول</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_OOP_%DA%AB%D9%BC%DB%90_%D8%A7%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87"></span>د OOP ګټې او عملي غوښتنلیکونه<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1.png" alt="" class="wp-image-1341" srcset="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1.png 1792w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-300x171.png 300w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-1024x585.png 1024w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-150x86.png 150w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-768x439.png 768w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A2%D8%A8%D8%AC%DB%8C%DA%A9%D9%B9_%D8%A7%D9%88%D8%B1%DB%8C%D9%86%D9%BC_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85_%DA%A9%D9%88%D9%84%D9%88_%DA%AB%D9%BC%DB%90"></span>د آبجیکٹ اورینټ پروګرام کولو ګټې<span class="ez-toc-section-end"></span></h3>



<p>        OOP ډیری ګټې لري چې دا د پیچلي سافټویر پراختیا لپاره غوره طریقه جوړوي:</p>



<ul class="wp-block-list">
<li><strong>کیپسول</strong>: تاسو ته اجازه درکوي ډاټا او هغه دندې چې دا په شیانو کې مینځ ته راوړي، په دې توګه د معلوماتو بشپړتیا خوندي کوي.</li>



<li><strong>خلاصون</strong>: پرته له دې چې د دوی د داخلي کارونو ژورې پوهې ته اړتیا ولري د لوړې کچې مفکورو کارولو ته اجازه ورکولو سره پراختیا ساده کوي.</li>



<li><strong>کوډ بیا کارول</strong>: د بیا کارونې وړ ټولګیو په توګه د موجوده کوډ شریکول او کارول هڅوي، په دې توګه د پراختیا وخت او د ساتنې لګښتونه کموي.</li>



<li><strong>انډول</strong>: د برنامه په خپلواکه او د تبادلې وړ برخو ویشل خوښوي کوم چې په خپلواکه توګه پراختیا او ازمول کیدی شي.</li>



<li><strong>پولیمورفیزم</strong>: شیانو ته اجازه ورکوي چې په اسانۍ سره د یو عام انٹرفیس له لارې تبادله شي، د پروګرام کولو او سیسټم ډیزاین کې لوی انعطاف چمتو کوي.</li>



<li><strong>میراث</strong>: د اخذ شوي ټولګیو رامینځته کولو وړتیا چمتو کوي چې د موجوده ټولګیو څخه ملکیتونه او میتودونه میراث کوي ، تمدید او دودیز کولو اسانتیا.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%B9%D8%AA%D8%B1%D8%A7%D8%B6_%D9%BE%D8%B1_%D8%A8%D9%86%D8%B3%D9%BC_%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87_%DA%A9%D9%88%D9%84%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87"></span>د اعتراض پر بنسټ برنامه کولو عملي غوښتنلیکونه<span class="ez-toc-section-end"></span></h4>



<p>        OOP په ډیری برخو کې او د غوښتنلیکونو مختلف ډولونو لپاره کارول کیږي. دلته ځینې کنکریټ مثالونه دي:</p>



<ul class="wp-block-list">
<li><strong>د ویډیو لوبې پراختیا</strong>: څیزونه کولی شي د کرکټرونو، خنډونو، ځواک پورته کولو او داسې نور استازیتوب وکړي، د دوی د حالتونو او چلندونو اداره کول اسانه کوي.</li>



<li><strong>د ګرافیکي کارن انٹرفیس (GUI)</strong>: د انٹرفیس هر عنصر، لکه تڼۍ او مینو، یو څیز دی، چې د متقابل انٹرفیس جوړول ډیر هوښیار کوي.</li>



<li><strong>د ډیټابیس مدیریت سیسټمونه</strong>: ادارې لکه میزونه، ریکارډونه، او پوښتنې کولی شي د شیانو په توګه ماډل شي ترڅو موثریت او ساتنه زیاته کړي.</li>



<li><strong>د ویب پراختیا</strong>: د OOP پر بنسټ چوکاټونه، لکه <strong>جینګو</strong> د Python یا لپاره <strong>روبي په ریلونو کې</strong> د روبي لپاره، د غوښتنو، ځوابونو، او نورو ویب اجزاوو استازیتوب کولو لپاره شیان وکاروئ.</li>



<li><strong>د موبایل ایپس</strong>: پلیټ فارمونه لکه <strong>Android</strong> او <strong>iOS</strong> د پیښو اداره کولو او د کارن انٹرفیس اجزاو مینځلو لپاره د OOP ماډل څخه ګټه پورته کړئ.</li>



<li><strong>د سمولو سافټویر</strong>: د فزیکي، اقتصادي یا بیولوژیکي سیسټمونو انډول کولو لپاره، د شیانو کارول د سیسټم د اجزاوو ترمنځ د پیچلو تعاملاتو ماډل کول ممکنه کوي.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%86%D9%88%D8%B1%D9%88_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%D9%88%D9%86%D9%88_%D8%AA%D9%85%D8%AB%DB%8C%D9%84%D9%88%D9%86%D9%88_%D8%B3%D8%B1%D9%87_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84"></span>د نورو پروګرامونو تمثیلونو سره پرتله کول<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2.png" alt="" class="wp-image-1342" srcset="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2.png 1792w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-300x171.png 300w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-1024x585.png 1024w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-150x86.png 150w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-768x439.png 768w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<figure class="wp-block-embed is-type-video is-provider-tiktok wp-block-embed-tiktok"><div class="wp-block-embed__wrapper">
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@louis_dhanis/video/7291716348722351392" data-video-id="7291716348722351392" data-embed-from="oembed" style="max-width:605px; min-width:325px;"> <section> <a target="_blank" title="@louis_dhanis" href="https://www.tiktok.com/@louis_dhanis?refer=embed" rel="noopener">@louis_dhanis</a> <p>C’est quoi la programmation orientée objet ? Comment ça marche ? C&#8217;est quoi la différence entre une voiture et une maison ? <a title="astucetech" target="_blank" href="https://www.tiktok.com/tag/astucetech?refer=embed" rel="noopener">#astucetech</a> <a title="louis_dhanis" target="_blank" href="https://www.tiktok.com/tag/louis_dhanis?refer=embed" rel="noopener">#louis_dhanis</a> <a title="apprendreautrement" target="_blank" href="https://www.tiktok.com/tag/apprendreautrement?refer=embed" rel="noopener">#apprendreautrement</a> <a title="apprendreacoder" target="_blank" href="https://www.tiktok.com/tag/apprendreacoder?refer=embed" rel="noopener">#apprendreacoder</a> <a title="devweb" target="_blank" href="https://www.tiktok.com/tag/devweb?refer=embed" rel="noopener">#devweb</a> <a title="entrepreneuriat" target="_blank" href="https://www.tiktok.com/tag/entrepreneuriat?refer=embed" rel="noopener">#entrepreneuriat</a> <a title="entrepreneurtech" target="_blank" href="https://www.tiktok.com/tag/entrepreneurtech?refer=embed" rel="noopener">#entrepreneurtech</a> <a title="developpement" target="_blank" href="https://www.tiktok.com/tag/developpement?refer=embed" rel="noopener">#developpement</a> <a title="poo" target="_blank" href="https://www.tiktok.com/tag/poo?refer=embed" rel="noopener">#POO</a> <a title="programmation" target="_blank" href="https://www.tiktok.com/tag/programmation?refer=embed" rel="noopener">#programmation</a></p> <a target="_blank" title="♬ son original - Louis Dhanis - Louis Dhanis" href="https://www.tiktok.com/music/son-original-Louis-Dhanis-7291716399008598816?refer=embed" rel="noopener">♬ son original &#8211; Louis Dhanis &#8211; Louis Dhanis</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D9%84%D8%A7%D8%B2%D9%85%D9%8A_%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87_%DA%A9%D9%88%D9%84"></span>لازمي برنامه کول<span class="ez-toc-section-end"></span></h3>



<p>لازمي برنامه کول ترټولو زوړ او خورا مستقیم تمثیل دی. دا د هغه ګامونو تشریح کولو څخه جوړه ده چې کمپیوټر باید د پایلې ترلاسه کولو لپاره تعقیب کړي. د C ژبه د دې تمثیل یوه ځانګړې بیلګه ده.</p>



<p><strong>ګټې:</strong></p>



<ul class="wp-block-list">
<li>د برنامه جریان او د سیسټم سرچینې کارولو باندې دقیق کنټرول.</li>



<li>د مفهوم له پلوه ساده او د پوهیدو لپاره مستقیم.</li>
</ul>



<p><strong>زیانونه:</strong></p>



<ul class="wp-block-list">
<li>د لوی برنامو لپاره خورا پیچلي کیدی شي.</li>



<li>د کوډ انعطاف او بیا کارونې نشتوالی.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%A7%D8%B9%D9%84%D8%A7%D9%86%D8%A7%D8%AA%D9%8A_%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87_%DA%A9%D9%88%D9%84"></span>اعلاناتي برنامه کول<span class="ez-toc-section-end"></span></h4>



<p>د لازمي برنامه کولو برخلاف ، اعلاناتي برنامه پدې تمرکز کوي چې پایله باید څه وي پرته له دې چې په روښانه ډول تشریح کړي چې څنګه یې ترلاسه کړي. SQL او HTML د اعلاناتي ژبو مثالونه دي.</p>



<p><strong>ګټې:</strong></p>



<ul class="wp-block-list">
<li>د مطلوب پایلې د بیان ساده کول.</li>



<li>د تطبیق توضیحاتو خلاصول، کوم چې ډیری وختونه د تالیف کونکي یا ژباړونکي لخوا غوره اصلاح کولو ته اجازه ورکوي.</li>
</ul>



<p><strong>زیانونه:</strong></p>



<ul class="wp-block-list">
<li>په دقیقه پروسه باندې لږ کنټرول چې ماشین یې تعقیبوي.</li>



<li>کیدای شي د پرمختلونکو لپاره لږ هوښیار وي چې ډیر طرزالعمل ته کار کوي.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%DA%A9%D8%A7%D8%B1%D9%8A_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%D9%88%D9%86%D9%87"></span>کاري پروګرامونه<span class="ez-toc-section-end"></span></h4>



<p>فنکشنل برنامه د اعلاناتي برنامو یوه فرعي سیټ ده چې د محاسبې سره چلند کوي لکه د ریاضيکي دندو ارزونه. هاسکل او سکالا هغه ژبې دي چې د دې تمثیل ملاتړ کوي.</p>



<p><strong>ګټې:</strong></p>



<ul class="wp-block-list">
<li>په کوډ کې استدلال اسانه کوي او عالي ماډلیت تضمینوي.</li>



<li>د اړخیزو تاثیراتو نشتوالي له امله د موازي برنامو او توزیع شوي سیسټمونو لپاره مثالی.</li>
</ul>



<p><strong>زیانونه:</strong></p>



<ul class="wp-block-list">
<li>کیدای شي د ناپیژندل شویو پراختیا کونکو لپاره د زده کړې سخته وکر وړاندې کړي.</li>



<li>فعالیت ممکن د لوړې کچې خلاصون له امله لږ وړاندوینه شي.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A2%D8%A8%D8%AC%DB%8C%DA%A9%D9%B9_%D8%A7%D9%88%D8%B1%DB%8C%D9%86%D9%BC%DA%89_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%DB%8C%D9%86%DA%AB_OOP"></span>د آبجیکٹ اورینټډ پروګرامینګ (OOP)<span class="ez-toc-section-end"></span></h4>



<p>OOP د &#8220;شیانو&#8221; مفهوم پر بنسټ والړ دی، کوم چې د &#8220;ټولګیو&#8221; مثالونه دي. توکي دواړه ډاټا او میتودونه لري. جاوا او پیتون هغه ژبې دي چې دا تمثیل جذبوي.</p>



<p><strong>ګټې:</strong></p>



<ul class="wp-block-list">
<li>د کوډ بیا کارونې وړتیا زیاتوي او ساتنه یې اسانه کوي.</li>



<li>د ډیټا انکیپسولیشن او خلاصون ته وده ورکوي.</li>
</ul>



<p><strong>زیانونه:</strong></p>



<ul class="wp-block-list">
<li>ډیر خلاصول کولی شي د غیر ضروري پیچلتیا لامل شي.</li>



<li>د خلاصون اضافي پرتونو له امله د فعالیت کمیدو لامل کیدی شي.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%DA%81%D9%88%D8%A7%D8%A8_%D9%88%D8%B1%DA%A9%D9%88%D9%88%D9%86%DA%A9%D9%8A_%D9%BE%D8%B1%D9%88%DA%AB%D8%B1%D8%A7%D9%85%D9%88%D9%86%D9%87"></span>ځواب ورکوونکي پروګرامونه<span class="ez-toc-section-end"></span></h4>



<p>عکس العمل برنامه کول یو تمثیل دی چې د معلوماتو جریان اداره کولو او د بدلونونو تبلیغ کولو تمرکز کوي. دا په ځانګړي ډول د متقابل کارونکي انٹرفیسونو یا ریښتیني وخت سیسټمونو سره غوښتنلیکونو لپاره مؤثره دی.</p>



<p><strong>ګټې:</strong></p>



<ul class="wp-block-list">
<li>د پیچلي غیر متمرکز سیسټمونو مدیریت ته وده ورکوي.</li>



<li>په خورا متقابل شرایطو کې د لوستلو وړ او لږ خطا کونکي کوډ ته وده ورکوي.</li>
</ul>



<p><strong>زیانونه:</strong></p>



<ul class="wp-block-list">
<li>د مؤثره کارولو لپاره د ځواب ویونکي مفاهیمو بشپړ پوهاوي ته اړتیا لري.</li>



<li>د عکس العمل ترتیبونه ځینې وختونه د ډیبګ کولو لپاره ستونزمن وي.</li>
</ul>



<p>په پایله کې، د پروګرام کولو تمثیل انتخاب اکثرا د ستونزې په نوعیت پورې اړه لري چې حل کیږي، د پراختیا کونکي غوره توب او د سیسټم فعالیت محدودیتونه. د دوی د توپیرونو او غوښتنلیکونو پوهیدل کولی شي له پراختیا کونکو سره مرسته وکړي چې د دوی پروژې لپاره سم چلند غوره کړي او پاک ، ډیر ساتلو وړ او ډیر موثر کوډ ولیکئ.</p>



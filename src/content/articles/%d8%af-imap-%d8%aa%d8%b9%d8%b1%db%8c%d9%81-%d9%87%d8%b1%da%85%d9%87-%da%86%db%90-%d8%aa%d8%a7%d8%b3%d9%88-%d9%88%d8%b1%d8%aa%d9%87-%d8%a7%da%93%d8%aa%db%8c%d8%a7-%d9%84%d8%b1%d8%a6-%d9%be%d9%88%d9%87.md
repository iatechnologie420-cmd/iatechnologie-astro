---
title: "د IMAP تعریف: هرڅه چې تاسو ورته اړتیا لرئ پوه شئ"
slug: "%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87"
excerpt: "د IMAP پیژندنه د انټرنیټ پیغام لاسرسي پروتوکول (IMAP) د مخابراتو معیار دی چې کاروونکو ته اجازه ورکوي چې خپل بریښنالیکونه په مستقیم ډول د بریښنالیک سرورونو کې ترلاسه او اداره کړي ، کوم چې د دودیز چلند څخه توپیر لري چیرې چې بریښنالیکونه ځایی بریښنالیک پیرودونکي ته ډاونلوډ کیږي. دا ډیری عملي ګټې راوړي [&hellip;]"
date: "2024-03-09T12:13:24"
featuredImage: "/images/blog/Tout-savoir-sur-le-protocole-IMAP-3.png"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps", "%d8%b2%db%8c%d8%b1%d8%a8%d9%86%d8%a7%d9%88%db%90-%d8%a7%d9%88-%d8%b4%d8%a8%da%a9%db%90-ps"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="What is SMTP - Simple Mail Transfer Protocol" width="500" height="375" src="https://www.youtube.com/embed/PJo5yOtu7o8?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_IMAP_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87" >د IMAP پیژندنه</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#IMAP_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A" >IMAP څنګه کار کوي</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_IMAP_%DA%AB%D9%BC%DB%90" >د IMAP ګټې</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#IMAP_vs_POP3" >IMAP vs. POP3</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_IMAP_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D9%8A_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7%D9%88%DB%90" >د IMAP ځانګړي ځانګړتیاوې</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_IMAP_%D8%A7%D9%88_%D9%86%D9%88%D8%B1%D9%88_%D8%A8%D8%B1%DB%8C%DA%9A%D9%86%D8%A7%D9%84%DB%8C%DA%A9_%D9%BE%D8%B1%D9%88%D8%AA%D9%88%DA%A9%D9%88%D9%84%D9%88%D9%86%D9%88_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84" >د IMAP او نورو بریښنالیک پروتوکولونو ترمنځ پرتله کول</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_%D8%A8%D8%B1%DB%8C%DA%9A%D9%86%D8%A7%D9%84%DB%8C%DA%A9_%D9%BE%D8%B1%D9%88%D8%AA%D9%88%DA%A9%D9%88%D9%84%D9%88%D9%86%D9%88_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87" >د بریښنالیک پروتوکولونو پیژندنه</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#POP3_%D8%AA%D8%B1%D9%BC%D9%88%D9%84%D9%88_%D8%B2%D9%88%DA%93_%D9%BE%D8%B1%D9%88%D8%AA%D9%88%DA%A9%D9%88%D9%84" >POP3: ترټولو زوړ پروتوکول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#SMTP_%D8%AF_%D8%A8%D8%B1%DB%8C%DA%9A%D9%86%D8%A7%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%88_%D9%84%DB%8C%DA%96%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%A7%DA%93%DB%8C%D9%86" >SMTP: د بریښنالیکونو لیږلو لپاره اړین</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84" >د ځانګړتیا پرتله کول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_%D8%A7%DA%93%D8%AA%DB%8C%D8%A7%D9%88%D9%88_%D8%B3%D8%B1%D9%87_%D8%B3%D9%85_%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8" >د اړتیاوو سره سم انتخاب</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_IMAP_%DA%A9%D8%A7%D8%B1%D9%88%D9%84_%D8%AA%D9%86%D8%B8%DB%8C%D9%85_%D8%A7%D9%88_%D8%A7%D8%B5%D9%84%D8%A7%D8%AD_%DA%A9%D9%88%D9%84" >د IMAP کارول تنظیم او اصلاح کول</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%A8%D9%86%D8%B3%D9%BC%DB%8C%D8%B2_IMAP_%D8%AA%D8%B1%D8%AA%DB%8C%D8%A8%D8%A7%D8%AA" >بنسټیز IMAP ترتیبات</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%B3%D8%AA%D8%A7%D8%B3%D9%88_%D8%AF_IMAP_%DA%A9%D8%A7%D8%B1%D9%88%D9%84_%D8%A7%D8%B5%D9%84%D8%A7%D8%AD_%DA%A9%D9%88%D9%84" >ستاسو د IMAP کارول اصلاح کول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/ps/%d8%af-imap-%d8%aa%d8%b9%d8%b1%db%8c%d9%81-%d9%87%d8%b1%da%85%d9%87-%da%86%db%90-%d8%aa%d8%a7%d8%b3%d9%88-%d9%88%d8%b1%d8%aa%d9%87-%d8%a7%da%93%d8%aa%db%8c%d8%a7-%d9%84%d8%b1%d8%a6-%d9%be%d9%88%d9%87/#%D8%AF_IMAP_%D8%B3%D8%B1%D9%87_%D8%A7%D9%85%D9%86%DB%8C%D8%AA%D9%8A_%DA%A9%DA%93%D9%86%DB%90" >د IMAP سره امنیتي کړنې</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_IMAP_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87"></span>د IMAP پیژندنه<span class="ez-toc-section-end"></span></h2>



<p>د انټرنیټ پیغام لاسرسي پروتوکول (IMAP) د مخابراتو معیار دی چې کاروونکو ته اجازه ورکوي چې خپل بریښنالیکونه په مستقیم ډول د بریښنالیک سرورونو کې ترلاسه او اداره کړي ، کوم چې د دودیز چلند څخه توپیر لري چیرې چې بریښنالیکونه ځایی بریښنالیک پیرودونکي ته ډاونلوډ کیږي. دا ډیری عملي ګټې راوړي ، په ځانګړي توګه په داسې نړۍ کې چیرې چې موږ له ډیری وسیلو څخه زموږ بریښنالیکونو ته لاسرسی لرو. په دې مقاله کې، موږ به وګورو چې IMAP څنګه کار کوي، د هغې ګټې، او دا څنګه د نورو پروتوکولونو لکه POP3 سره پرتله کوي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="IMAP_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A"></span>IMAP څنګه کار کوي<span class="ez-toc-section-end"></span></h3>



<p>د <strong>IMAP</strong> یو پروتوکول دی چې په 143 بندر کې یا په 993 بندر کې د خوندي نسخې لپاره کار کوي <strong>IMAPS</strong>. کله چې یو کاروونکی خپل ان باکس د IMAP په کارولو سره ګوري، دوی ټول مینځپانګه نه ډاونلوډ کوي. پرځای یې، بریښنالیک په سرور کې ساتل کیږي، او د بریښنالیک مراجع یو مخکتنه ښکاره کوي. دا کارونکي ته اجازه ورکوي چې خپل بریښنالیکونه په مستقیم سرور کې تنظیم، فلټر او لټون وکړي. کله چې بریښنالیک خلاص شي ، یوازې بیا د هغې مینځپانګه ډاونلوډ کیږي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_IMAP_%DA%AB%D9%BC%DB%90"></span>د IMAP ګټې<span class="ez-toc-section-end"></span></h4>



<p>د کارولو <strong>IMAP</strong> ډیری کلیدي ګټې وړاندې کوي:</p>



<ul class="wp-block-list">
<li><strong>د وسیلو ترمنځ همغږي کول</strong>: په یوه وسیله د بریښنالیک ایډیټ کول به دا په ټولو همغږي وسیلو کې ترمیم کړي.</li>



<li><strong>د آنلاین بریښنالیک مدیریت</strong>: د ډاونلوډ کولو پرته د بریښنالیکونو لوستلو او اداره کولو وړتیا د وخت او ذخیره کولو ځای خوندي کوي.</li>



<li><strong>انعطاف</strong>: تاسو ته اجازه درکوي چې خپل بریښنالیک فولډرونه سمبال کړئ او د هر IMAP پیرودونکي انٹرفیس څخه یې تنظیم کړئ.</li>



<li><strong>غښتلیتوب</strong>: بریښنالیکونه حتی د لوستلو وروسته په سرور کې زیرمه شوي ، کوم چې د ځایی وسیلې له لاسه ورکولو یا ماتیدو په صورت کې اضافي امنیت چمتو کوي.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="IMAP_vs_POP3"></span>IMAP vs. POP3<span class="ez-toc-section-end"></span></h4>



<p><strong>IMAP</strong> اکثرا سره پرتله کیږي <strong>POP3</strong> (د پوست دفتر پروتوکول نسخه 3)، د بریښنالیکونو ترلاسه کولو لپاره بل پروتوکول. اصلي توپیر دا دی چې POP3 د کارونکي وسیلې ته بریښنالیکونه ډاونلوډ کوي او په ډیفالټ ډول یې له سرور څخه حذف کوي. دا پدې مانا ده چې پیغامونه یوازې په یوه وسیله لوستل کیدی شي، کوم چې زموږ د څو وسیلو شرایطو کې لږ عملي دی. سربیره پردې، د POP3 سره، د بریښنالیکونو فایلول او تنظیم باید په هر وسیله تکرار شي، پداسې حال کې چې د IMAP سره، دا عملیات نړیوال دي او په ټولو وسیلو کې منعکس کیږي.</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-savoir-sur-le-protocole-IMAP.png" alt="" class="wp-image-1376" srcset="/images/blog/Tout-savoir-sur-le-protocole-IMAP.png 1792w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-300x171.png 300w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1024x585.png 1024w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-150x86.png 150w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-768x439.png 768w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_IMAP_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D9%8A_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7%D9%88%DB%90"></span>د IMAP ځانګړي ځانګړتیاوې<span class="ez-toc-section-end"></span></h4>



<p>                    دلته ځینې ځانګړتیاوې دي چې د IMAP پروتوکول جلا کوي:</p>



<ul class="wp-block-list">
<li><strong>څو فولډرونه:</strong> تاسو کولی شئ په میل سرور کې ډیری فولډرونه جوړ کړئ ترڅو خپل پیغامونه تنظیم کړئ.</li>



<li><strong>همغږي کول:</strong> د همغږي کولو له لارې، د بریښنالیک پیرودونکي هغه څه منعکس کوي چې په سرور کې دي. که تاسو په خپل تلیفون کې یو پیغام حذف کړئ، دا به ستاسو په ډیسټاپ پیرودونکي کې هم ورک شي.</li>



<li><strong>د پیغام وضعیت مدیریت:</strong> پیغامونه د وروسته تعقیب لپاره لوستل شوي، نه لوستل شوي، حذف شوي، یا ځنډول شوي په توګه نښه کیدی شي.</li>



<li><strong>څیړنه:</strong> IMAP په مستقیم ډول په سرور کې د پیغامونو پیچلي لټون ته اجازه ورکوي پرته له دې چې په محلي ډول د پیغامونو ډاونلوډ ته اړتیا ولري.</li>



<li><strong>فلټر کول:</strong> دا ممکنه ده چې پیغامونه مستقیم په سرور کې فلټر کړئ، د بریښنالیک غوره مدیریت ته اجازه ورکوي.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_IMAP_%D8%A7%D9%88_%D9%86%D9%88%D8%B1%D9%88_%D8%A8%D8%B1%DB%8C%DA%9A%D9%86%D8%A7%D9%84%DB%8C%DA%A9_%D9%BE%D8%B1%D9%88%D8%AA%D9%88%DA%A9%D9%88%D9%84%D9%88%D9%86%D9%88_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84"></span>د IMAP او نورو بریښنالیک پروتوکولونو ترمنځ پرتله کول<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-savoir-sur-le-protocole-IMAP-1.png" alt="" class="wp-image-1377" srcset="/images/blog/Tout-savoir-sur-le-protocole-IMAP-1.png 1792w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-300x171.png 300w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-1024x585.png 1024w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-150x86.png 150w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-768x439.png 768w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A8%D8%B1%DB%8C%DA%9A%D9%86%D8%A7%D9%84%DB%8C%DA%A9_%D9%BE%D8%B1%D9%88%D8%AA%D9%88%DA%A9%D9%88%D9%84%D9%88%D9%86%D9%88_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87"></span>د بریښنالیک پروتوکولونو پیژندنه<span class="ez-toc-section-end"></span></h3>



<p>                د پرتله کولو دمخه <strong>IMAP</strong> (د انټرنیټ پیغام لاسرسي پروتوکول) د نورو پروتوکولونو سره، دا مهمه ده چې پوه شئ چې د پیغام رسولو پروتوکولونه څه دي. دا معیارونه دي چې کاروونکو ته اجازه ورکوي چې د میل سرورونو شبکو کې بریښنالیکونه ترلاسه او واستوي. هر پروتوکول خپل ځانګړتیاوې، ګټې او زیانونه لري، دا په ګوته کوي چې پیغامونه څنګه ساتل کیږي، اداره کیږي او لاسرسی لري.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="POP3_%D8%AA%D8%B1%D9%BC%D9%88%D9%84%D9%88_%D8%B2%D9%88%DA%93_%D9%BE%D8%B1%D9%88%D8%AA%D9%88%DA%A9%D9%88%D9%84"></span>POP3: ترټولو زوړ پروتوکول<span class="ez-toc-section-end"></span></h4>



<p>                د <strong>POP3</strong> (د پوست دفتر پروتوکول نسخه 3) یو زوړ پروتوکول دی چې د سرور څخه د کارونکي محلي وسیلې ته د بریښنالیکونو ډاونلوډ کولو تمرکز کوي. یوځل ډاونلوډ شوی ، بریښنالیکونه عموما نور د سرور له لارې د لاسرسي وړ ندي. دا د هغه کارونکي لپاره محدود کیدی شي څوک چې غواړي د ډیری وسیلو څخه خپل بریښنالیکونو ته لاسرسی ومومي ، مګر دا د دوی بریښنالیکونو آفلاین لیدو وړتیا وړاندیز کوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="SMTP_%D8%AF_%D8%A8%D8%B1%DB%8C%DA%9A%D9%86%D8%A7%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%88_%D9%84%DB%8C%DA%96%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%A7%DA%93%DB%8C%D9%86"></span>SMTP: د بریښنالیکونو لیږلو لپاره اړین<span class="ez-toc-section-end"></span></h4>



<p>                <strong>SMTP</strong> (د ساده میل لیږد پروتوکول) د بریښنالیکونو لیږلو لپاره معیاري پروتوکول دی. دا په ترکیب کې کارول کیږي <strong>IMAP</strong> یا <strong>POP3</strong>، کوم چې د پیغامونو استقبال اداره کوي. <strong>SMTP</strong> د بریښنالیکونو لیږلو لپاره اړین دی، مګر په مختلفو وسیلو کې د پیغامونو ترلاسه کولو یا همغږي کولو اداره نه کوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84"></span>د ځانګړتیا پرتله کول<span class="ez-toc-section-end"></span></h4>



<figure class="wp-block-table"><table><tbody><tr><td>پروتوکول</td><td>تفصیل</td><td>بریښنالیکونو ته لاسرسی</td><td>د څو وسیلو مدیریت</td><td>آفلاین</td></tr><tr><td><strong>IMAP</strong></td><td>په سرور کې پرمختللي بریښنالیک مدیریت.</td><td>هرچیرې، تر هغه چې انټرنیټ سره وصل وي.</td><td>هو، د ریښتیني وخت همغږي.</td><td>یوازې لوستل، زیرمه شوي.</td></tr><tr><td><strong>POP3</strong></td><td>وسیله ته د بریښنالیکونو ډاونلوډ کول.</td><td>یوازې په ډاونلوډ شوي وسیله کې.</td><td>نه، نه همغږي.</td><td>هو، بشپړ لاسرسی.</td></tr><tr><td><strong>SMTP</strong></td><td>د بریښنالیک پیرودونکي څخه بریښنالیکونه لیږل.</td><td>د تطبیق وړ نه دی، یوازې پروتوکول لیږل.</td><td>کاروړی نه دی.</td><td>کاروړی نه دی.</td></tr></tbody></table></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%DA%93%D8%AA%DB%8C%D8%A7%D9%88%D9%88_%D8%B3%D8%B1%D9%87_%D8%B3%D9%85_%D8%A7%D9%86%D8%AA%D8%AE%D8%A7%D8%A8"></span>د اړتیاوو سره سم انتخاب<span class="ez-toc-section-end"></span></h4>



<p>                تر منځ انتخاب <strong>IMAP</strong> او نور پروتوکولونه لکه <strong>POP3</strong> او <strong>SMTP</strong> د کارونکي اړتیاو پورې اړه لري. که په لاره کې لاسرسی او د څو وسیلو مدیریت اړین وي، <strong>IMAP</strong> یو مثالی حل دی. د هغو کسانو لپاره چې په یوه وسیله د دوی بریښنالیکونو ساده ترلاسه کول غوره کوي، <strong>POP3</strong> کیدای شي کافي وي. په پای کې، <strong>SMTP</strong> د بریښنالیکونو لیږلو لپاره به تل اړین وي، پرته له دې چې د استقبال پروتوکول غوره کړي.</p>



<p>                په پرتله، <strong>IMAP</strong> انعطاف او اسانتیا چمتو کوي چې نور پروتوکولونه نشي کولی د کاروونکو لپاره مطابقت ولري چې د مختلف وسیلو څخه خپل بریښنالیک ته دوامداره لاسرسي ته اړتیا لري. په هرصورت، هر پروتوکول د شخصي یا مسلکي اړتیاو پر بنسټ خپل اهمیت او ګټورتیا لري. د دې توپیرونو پوهیدل د خورا مناسب بریښنالیک ترتیب غوره کولو لپاره اړین دي.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_IMAP_%DA%A9%D8%A7%D8%B1%D9%88%D9%84_%D8%AA%D9%86%D8%B8%DB%8C%D9%85_%D8%A7%D9%88_%D8%A7%D8%B5%D9%84%D8%A7%D8%AD_%DA%A9%D9%88%D9%84"></span>د IMAP کارول تنظیم او اصلاح کول<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-savoir-sur-le-protocole-IMAP-2.png" alt="" class="wp-image-1378" srcset="/images/blog/Tout-savoir-sur-le-protocole-IMAP-2.png 1792w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-300x171.png 300w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-1024x585.png 1024w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-150x86.png 150w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-768x439.png 768w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<figure class="wp-block-embed is-type-video is-provider-tiktok wp-block-embed-tiktok"><div class="wp-block-embed__wrapper">
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@formip/video/7295627671319383328" data-video-id="7295627671319383328" data-embed-from="oembed" style="max-width:605px; min-width:325px;"> <section> <a target="_blank" title="@formip" href="https://www.tiktok.com/@formip?refer=embed" rel="noopener">@formip</a> <p>Mister IMAP : Le DJ des E-mails 🎧📧 PART 2 <a title="misterimap" target="_blank" href="https://www.tiktok.com/tag/misterimap?refer=embed" rel="noopener">#MisterIMAP</a>E-mailsSynchronisésDJDesE-mails<a title="portiervip" target="_blank" href="https://www.tiktok.com/tag/portiervip?refer=embed" rel="noopener">#PortierVIP</a>BibliothécaireE-mails<a title="sécuritéimap" target="_blank" href="https://www.tiktok.com/tag/s%C3%A9curit%C3%A9imap?refer=embed" rel="noopener">#SécuritéIMAP</a>ChefOrchestreE-mails<a title="messagerienumérique" target="_blank" href="https://www.tiktok.com/tag/messagerienum%C3%A9rique?refer=embed" rel="noopener">#MessagerieNumérique</a><a title="mozartmessagerie" target="_blank" href="https://www.tiktok.com/tag/mozartmessagerie?refer=embed" rel="noopener">#MozartMessagerie</a><a title="playlistimap" target="_blank" href="https://www.tiktok.com/tag/playlistimap?refer=embed" rel="noopener">#PlaylistIMAP</a></p> <a target="_blank" title="♬ son original - Formip - Formip" href="https://www.tiktok.com/music/son-original-Formip-7295627771307395873?refer=embed" rel="noopener">♬ son original &#8211; Formip &#8211; Formip</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%A8%D9%86%D8%B3%D9%BC%DB%8C%D8%B2_IMAP_%D8%AA%D8%B1%D8%AA%DB%8C%D8%A8%D8%A7%D8%AA"></span>بنسټیز IMAP ترتیبات<span class="ez-toc-section-end"></span></h3>



<p>ستاسو د بریښنالیک پیرودونکي کې IMAP تنظیم کولو لپاره ، تاسو به لاندې معلوماتو ته اړتیا ولرئ:</p>



<ul class="wp-block-list">
<li>کارن نوم: ستاسو بشپړ بریښنالیک آدرس</li>



<li>پاسورډ: هغه پټنوم چې ستاسو د بریښنالیک آدرس سره تړاو لري</li>



<li>IMAP سرور: ستاسو د بریښنالیک کوربه لخوا چمتو شوی د IMAP سرور پته</li>



<li>IMAP پورټ: عموما 993 د خوندي پیوستون لپاره (SSL)</li>
</ul>



<p>یوځل چې دا معلومات ستاسو د بریښنالیک پیرودونکي تنظیماتو کې داخل شي ، تاسو به خپلو پیغامونو ته لاسرسی ومومئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%B3%D8%AA%D8%A7%D8%B3%D9%88_%D8%AF_IMAP_%DA%A9%D8%A7%D8%B1%D9%88%D9%84_%D8%A7%D8%B5%D9%84%D8%A7%D8%AD_%DA%A9%D9%88%D9%84"></span>ستاسو د IMAP کارول اصلاح کول<span class="ez-toc-section-end"></span></h4>



<p>د ښه تجربې لپاره، دلته د اصلاح کولو ځینې لارښوونې دي:</p>



<ul class="wp-block-list">
<li><strong>همغږي شوي فولډرې:</strong> دا اکثرا ممکنه ده چې انتخاب کړئ کوم فولډر چې تاسو یې همغږي کول غواړئ. یوازې هغه غوره کړئ چې تاسو یې په منظم ډول ګورئ ترڅو د ذخیره کولو ځای او ډیټا خوندي کړئ.</li>



<li><strong>د بریښنالیک مدیریت:</strong> د خپل پیرودونکي لخوا وړاندیز شوي ځانګړتیاو څخه ګټه واخلئ ترڅو خپل بریښنالیکونه په مؤثره توګه تنظیم کړئ. د فلټرونو کارول، سمارټ فولډرونه او د ترتیب کولو مقررات کولی شي ستاسو د تولید وړتیا ډیره کړي.</li>



<li><strong>همغږي اندازه:</strong> ځینې ​​​​پیرودونکي تاسو ته اجازه درکوي چې د ډیټا مقدار محدود کړي ترڅو همغږي شي (د مثال په توګه ، یوازې د تیرو 30 ورځو څخه بریښنالیکونه). دا کولی شي همغږي ګړندي کړي او د بینډ ویت کارول کم کړي.</li>



<li><strong>د غیر استعمال شوي وسایلو نښلول:</strong> د غیر ضروري همغږي کولو او احتمالي امنیتي سرغړونو څخه مخنیوي لپاره ، ډاډ ترلاسه کړئ چې هغه وسایل منقط کړئ چې تاسو نور نه کاروئ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_IMAP_%D8%B3%D8%B1%D9%87_%D8%A7%D9%85%D9%86%DB%8C%D8%AA%D9%8A_%DA%A9%DA%93%D9%86%DB%90"></span>د IMAP سره امنیتي کړنې<span class="ez-toc-section-end"></span></h4>



<p>امنیت یو اړین اړخ دی کله چې د مخابراتو پروتوکولونه لکه IMAP کاروي. دلته ځینې غوره تمرینونه دي:</p>



<ul class="wp-block-list">
<li><strong>کوډ شوي اړیکې وکاروئ:</strong> تل د خوندي IMAP پورټ (SSL/TLS) څخه کار واخلئ ترڅو ستاسو د بریښنالیک پیرودونکي او سرور ترمینځ تبادله شوي ډیټا کوډ کړئ.</li>



<li><strong>قوي پاسورډونه:</strong> ډاډ ترلاسه کړئ چې ستاسو د بریښنالیک پاسورډ قوي او ځانګړی دی ترڅو د غیر مجاز لاسرسي مخه ونیسي.</li>



<li><strong>دوه مرحلې تایید:</strong> که ستاسو چمتو کونکی دې ته اجازه ورکړي، د امنیت اضافي پرت اضافه کولو لپاره دوه مرحلې تایید فعال کړئ.</li>
</ul>



<p>د کارولو ترتیب او اصلاح کول<strong>IMAP</strong> د اسانه او خوندي بریښنالیک تجربې څخه خوند اخیستو لپاره اړین دي. د پورته لارښوونو په تعقیب سره، تاسو کولی شئ خپل محصول ښه کړئ پداسې حال کې چې ستاسو ډاټا خوندي وساتئ. همدارنګه په یاد ولرئ چې په منظم ډول خپل بریښنالیک پیرودونکي تازه کړئ او د ډیجیټل امنیت غوره کړنو په اړه خبر اوسئ.</p>



---
title: "یو اتوماتیک کوډر څه شی دی؟ وروستی لارښود!"
slug: "article-126"
excerpt: "Autoencoders، یا اتوماتیک کوډر په انګلیسي کې، ځان د ماشین زده کړې او مصنوعي استخباراتو په برخه کې د ځواکمن وسیلو په توګه موقعیت لري. دا ځانګړي عصبي شبکې د ابعاد کمولو ، بې تفاوتۍ کشف ، د معلوماتو له مینځه وړلو او نور ډیر څه لپاره کارول کیږي. دا مقاله د دې زړه راښکونکي [&hellip;]"
date: "2024-03-09T12:07:24"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps", "%da%a9%d9%85%d9%be%db%8c%d9%88%d9%bc%d8%b1%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d9%bc%d8%a7-ps"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tracking Corn &amp; Weed with Yolov5 and Auto Encoder - Tracker" width="500" height="281" src="https://www.youtube.com/embed/8-jWgsGWaR0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>Autoencoders، یا <em>اتوماتیک کوډر</em> په انګلیسي کې، ځان د ماشین زده کړې او مصنوعي استخباراتو په برخه کې د ځواکمن وسیلو په توګه موقعیت لري. دا ځانګړي عصبي شبکې د ابعاد کمولو ، بې تفاوتۍ کشف ، د معلوماتو له مینځه وړلو او نور ډیر څه لپاره کارول کیږي. دا مقاله د دې زړه راښکونکي ټیکنالوژۍ پیژندنه وړاندې کوي، د هغې کاري اصول، د هغې غوښتنلیکونه او په څیړنه او صنعت کې د هغې مخ پر ودې اهمیت په ګوته کوي.</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%DA%85%D9%87_%D8%B4%DB%8C_%D8%AF%DB%8C%D8%9F" >اتوماتیک کوډر څه شی دی؟</a></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-2" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A%D8%9F" >اتوماتیک کوډر څنګه کار کوي؟</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-3" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87" >د اتوماتیک کوډرونو عملي غوښتنلیکونه</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-4" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84%D8%8C_%D8%AE%D9%86%DA%89_%D8%A7%D9%88_%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84" >اتوماتیک کوډر: کوډ کول، خنډ او کوډ کول</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84" >کوډ کول</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AE%D9%86%DA%89" >خنډ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84-2" >کوډ کول</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87_%D8%A7%D9%88_%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%88_%D8%AA%D8%BA%DB%8C%D8%B1%D8%A7%D8%AA" >عملي غوښتنلیکونه او د اتوماتیک کوډرونو تغیرات</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87-2" >د اتوماتیک کوډرونو عملي غوښتنلیکونه</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%A7%D8%A8%D8%B9%D8%A7%D8%AF_%DA%A9%D9%85%D9%88%D9%84" >د ابعاد کمول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%B4%D9%88%D8%B1_%D9%84%D8%BA%D9%88%D9%87_%DA%A9%D9%88%D9%84_%D9%85%D9%86%DA%81%D9%87_%D9%88%DA%93%D9%84" >د شور لغوه کول (منځه وړل)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA%D9%88_%DA%A9%D9%85%D9%BE%D8%B1%DB%8C%D8%B4%D9%86" >د معلوماتو کمپریشن</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA%D9%88_%D8%AA%D9%88%D9%84%DB%8C%D8%AF_%D8%A7%D9%88_%D8%AA%D9%88%D8%B1_%D9%84%DA%AB%D9%88%D9%84" >د معلوماتو تولید او تور لګول</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_Autoencoder_%DA%89%D9%88%D9%84%D9%88%D9%86%D9%87" >د Autoencoder ډولونه</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AA%D8%BA%DB%8C%D8%B1%D8%A7%D8%AA%D9%8A_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_VAE" >تغیراتي اتوماتیک کوډر (VAE)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%B3%D9%BE%D8%A7%D8%B1%D8%B3_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%87" >سپارس اتوماتیک کوډرونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_Autoencoders_%D9%84%D9%87_%D9%85%DB%8C%D9%86%DA%81%D9%87_%D9%88%DA%93%D9%84" >د Autoencoders له مینځه وړل</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AA%D8%B3%D9%84%D8%B3%D9%84%D9%8A_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1" >تسلسلي اتوماتیک کوډر</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-19" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%D8%A7%D9%88_%DA%A9%D9%88%DA%89_%D9%85%D8%AB%D8%A7%D9%84%D9%88%D9%86%D9%88_%D8%B1%D9%88%D8%B2%D9%84%D9%88_%DA%85%D8%B1%D9%86%DA%AB%D9%88%D8%A7%D9%84%DB%8C" >د اتوماتیک کوډر او کوډ مثالونو روزلو څرنګوالی</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%D8%AF_%D8%B1%D9%88%D8%B2%D9%86%DB%90_%D9%BE%D8%B1%D9%88%D8%B3%D9%87" >د اتوماتیک کوډر د روزنې پروسه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-21" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%DA%A9%DB%8C%D8%B1%D8%A7_%D8%B3%D8%B1%D9%87_%DA%A9%D9%88%DA%89_%D9%85%D8%AB%D8%A7%D9%84" >د کیرا سره کوډ مثال</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-22" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%DA%9A%D9%87_%D8%AA%D9%85%D8%B1%DB%8C%D9%86_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D9%84%D8%A7%D8%B1%DA%9A%D9%88%D9%88%D9%86%D9%87" >د ښه تمرین لپاره لارښوونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-23" href="/ps/%db%8c%d9%88-%d8%a7%d8%aa%d9%88%d9%85%d8%a7%d8%aa%db%8c%da%a9-%da%a9%d9%88%da%89%d8%b1-%da%85%d9%87-%d8%b4%db%8c-%d8%af%db%8c%d8%9f-%d9%88%d8%b1%d9%88%d8%b3%d8%aa%db%8c-%d9%84%d8%a7%d8%b1%da%9a%d9%88/#%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D9%88%D9%86%D9%88_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87" >د اتوماتیک کوډونو غوښتنلیکونه</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%DA%85%D9%87_%D8%B4%DB%8C_%D8%AF%DB%8C%D8%9F"></span>اتوماتیک کوډر څه شی دی؟<span class="ez-toc-section-end"></span></h2>



<p>الف <strong>اتوماتیک کوډر</strong> یو ډول مصنوعي عصبي شبکه ده چې د غیر څارل شوي زده کړې لپاره کارول کیږي. د اتوماتیک کوډر اصلي هدف دا دی چې د ان پټ ډیټا سیټ یو کمپیکٹ نمایش (کوډینګ) تولید کړي او بیا د دې نمایش څخه ډاټا بیا تنظیم کړي. نظر دا دی چې د ډیټا خورا مهم اړخونه ونیسي، ډیری وختونه د ابعاد کمولو لپاره. د آټوینکوډر جوړښت عموما د دوو اصلي برخو څخه جوړ شوی دی:</p>



<ul class="wp-block-list">
<li><strong>کوډ کوونکی</strong> ((<em>کوډ</em>): د شبکې دا لومړۍ برخه په کمه بڼه کې د ان پټ ډیټا کمپریشن مسؤلیت لري.</li>



<li><strong>ډیکوډر</strong> ((<em>ډیکوډ</em>) دویمه برخه کمپریس شوي کوډونه ترلاسه کوي او د اصلي معلوماتو بیا رغولو هڅه کوي.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A%D8%9F"></span>اتوماتیک کوډر څنګه کار کوي؟<span class="ez-toc-section-end"></span></h2>



<p>د اتوماتیک کوډر عملیات په څو مرحلو کې تشریح کیدی شي:</p>



<ol class="wp-block-list">
<li>شبکه د ان پټ په توګه معلومات ترلاسه کوي.</li>



<li>کوډ کوونکی ډیټا په فیچر ویکتور کې فشاروي، چې کوډ یا پټ ځای نومیږي.</li>



<li>کوډ کونکی دا ویکتور اخلي او هڅه کوي چې لومړني معلومات بیا تنظیم کړي.</li>



<li>د بیارغونې کیفیت د ضایع فعالیت په کارولو سره اندازه کیږي، کوم چې د اصلي آخذو او بیارغول شوي محصول ترمنځ توپیر ارزوي.</li>



<li>شبکه خپل وزن د بیک پروپیګیشن الګوریتم له لارې تنظیموي ترڅو د دې ضایع فعالیت کم کړي.</li>
</ol>



<p>د دې تکراري پروسې له لارې، اوټوینکوډر د بیارغونې پروسې په جریان کې د خورا مهم ځانګړتیاو په ساتلو ټینګار سره د معلوماتو مؤثره نمایش زده کوي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87"></span>د اتوماتیک کوډرونو عملي غوښتنلیکونه<span class="ez-toc-section-end"></span></h3>



<p>اتوماتیک کوډرونه خورا متقابل دي او په ډیری برخو کې پلي کیدی شي:</p>



<ul class="wp-block-list">
<li><strong>د ابعاد کمول</strong>: د PCA په څیر (د اصلي اجزاو تحلیل)، مګر د غیر خطي ظرفیت سره.</li>



<li><strong>له منځه وړل</strong>: دوی کولی شي په ډیټا کې &#8220;شور&#8221; له پامه غورځول زده کړي.</li>



<li><strong>د معلوماتو کمپریشن</strong>: دوی کولی شي کوډونه زده کړي چې د دودیز کمپریشن میتودونو څخه ډیر اغیزمن دي.</li>



<li><strong>د معلوماتو تولید</strong>: د پټ ځای په نیولو سره، دوی د نوي ډیټا مثالونو رامینځته کولو ته اجازه ورکوي چې د اصلي ننوتلو سره ورته وي.</li>



<li><strong>د بې نظمۍ کشف</strong>: Autoencoders کولی شي د ډیټا په موندلو کې مرسته وکړي چې د زده شوي توزیع سره سم نه وي.</li>
</ul>



<p>په لنډه توګه، د ډیټا معنی لرونکي ځانګړتیاو موندلو او تعریف کولو لپاره د اتوماتیک کوډرانو وړتیا دوی ته د AI د هر کارګر په وسیلې کې لازمي وسیله ګرځوي.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84%D8%8C_%D8%AE%D9%86%DA%89_%D8%A7%D9%88_%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84"></span>اتوماتیک کوډر: کوډ کول، خنډ او کوډ کول<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png" alt="" class="wp-image-1191" srcset="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84"></span>کوډ کول<span class="ez-toc-section-end"></span></h3>



<p>کوډ کول، یا د کوډ کولو مرحله، د ان پټ ډیټا بدلول شامل دي چې په کمپریس شوي نمایش کې شامل دي. لومړني معلومات، چې کیدای شي لوی وي، د آټوینکوډر شبکې ته ورکول کیږي. د شبکې پرتونه به په تدریجي ډول د ډیټا ابعاد کم کړي، اړین معلومات په کوچني نمایش ځای کې فشاروي. د شبکې هره طبقه د نیورونونو څخه جوړه شوې ده چې غیر خطي بدلونونه پلي کوي، د بیلګې په توګه، د فعال کولو افعال لکه ReLU یا Sigmoid کارول، ترڅو د ډیټا نوي استازیتوب ته ورسیږي کوم چې اړین معلومات ساتي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AE%D9%86%DA%89"></span>خنډ<span class="ez-toc-section-end"></span></h4>



<p>خنډ د اوټوینکوډر مرکزي برخه ده چیرې چې د معلوماتو نمایش خپل ټیټ ابعاد ته رسي ، چې کوډ هم ورته ویل کیږي. دا دا کمپریس شوی نمایش دی چې د ان پټ ډیټا خورا مهم ځانګړتیاوې ساتي. خنډ د فلټر په توګه کار کوي اوټوینکوډر دې ته اړ کوي چې د معلوماتو کمولو لپاره مؤثره لاره زده کړي. دا د ډیټا کمپریشن ډول سره پرتله کیدی شي ، مګر چیرې چې کمپریشن د معیاري الګوریتمونو لخوا تعریف شوي پرځای د ډیټا څخه په اوتومات ډول زده کیږي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%DA%A9%D9%88%DA%89_%DA%A9%D9%88%D9%84-2"></span>کوډ کول<span class="ez-toc-section-end"></span></h4>



<p>د کوډ کولو مرحله د کوډ کولو لپاره همغږي مرحله ده، چیرې چې کمپریس شوی نمایش د محصول په لور بیا رغول کیږي چې هدف یې د اصلي ان پټ سره د امکان تر حده وفادار وي. د خنډ نمایش څخه پیل کول، عصبي شبکه به په تدریجي ډول د معلوماتو ابعاد زیات کړي. دا د کوډ کولو برعکس پروسه ده: پرله پسې پرتونه د کم شوي نمایش څخه لومړني ځانګړتیاوې بیا رغوي. که چیرې کوډ کول اغیزمن وي، د آټوینکوډر محصول باید د اصلي معلوماتو سره نږدې نږدې وي.</p>



<p>په غیر څارل شوي زده کړې کې، اتوماتیک کوډر په ځانګړې توګه د معلوماتو د اصلي جوړښت د پوهیدو لپاره ګټور دي. د دې شبکو اغیزمنتوب د دوی د وړتیا له لارې نه اندازه کیږي چې په بشپړ ډول د معلوماتو بیا تولید کړي، بلکه د دوی د وړتیا له لارې چې په کوډ کې د ډیټا خورا مهم او اړونده صفات نیول کیږي. دا کوډ بیا په ډیرو پیچلو جوړښتونو کې د نورو عصبي شبکو لپاره د ابعاد کمولو ، لید لید ، یا حتی دمخه پروسس کولو لپاره کارول کیدی شي.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87_%D8%A7%D9%88_%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%88_%D8%AA%D8%BA%DB%8C%D8%B1%D8%A7%D8%AA"></span>عملي غوښتنلیکونه او د اتوماتیک کوډرونو تغیرات<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png" alt="" class="wp-image-1192" srcset="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>اتوماتیک کوډر</strong>، د مصنوعي استخباراتو (AI) لخوا پرمخ وړل شوي د ژورې زده کړې آرسنال کې کلیدي برخه ، یو عصبي شبکه ده چې ډیټا په ټیټ ابعاد نمایش کې کوډ کولو لپاره ډیزاین شوې او په داسې ډول تخریب کوي چې اړونده بیارغونه ممکنه وي. راځئ چې دوی معاینه کړو <strong>عملي غوښتنلیکونه</strong> او هغه ډولونه چې په دې زړه پورې ساحه کې راڅرګند شوي دي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%88_%D8%B9%D9%85%D9%84%D9%8A_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87-2"></span>د اتوماتیک کوډرونو عملي غوښتنلیکونه<span class="ez-toc-section-end"></span></h3>



<p>اوټوینکوډرانو د څارنې پرته د معلوماتو مؤثره او معنی لرونکي نمایشونو زده کولو وړتیا له امله ډیری غوښتنلیکونو ته لاره موندلې. دلته ځینې مثالونه دي:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%A8%D8%B9%D8%A7%D8%AF_%DA%A9%D9%85%D9%88%D9%84"></span>د ابعاد کمول<span class="ez-toc-section-end"></span></h4>



<p>د PCA (د اصلي اجزاو تحلیل) په څیر، اتوماتیک کوډرونه په مکرر ډول کارول کیږي <strong>د ابعاد کمول</strong>. دا تخنیک دا ممکنه کوي چې د متغیرونو شمیر کمولو سره د معلوماتو پروسس ساده کړي پداسې حال کې چې په اصلي ډیټاسیټ کې موجود ډیری معلومات خوندي کوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%B4%D9%88%D8%B1_%D9%84%D8%BA%D9%88%D9%87_%DA%A9%D9%88%D9%84_%D9%85%D9%86%DA%81%D9%87_%D9%88%DA%93%D9%84"></span>د شور لغوه کول (منځه وړل)<span class="ez-toc-section-end"></span></h4>



<p>د دوی د وړتیا سره چې د جزوي ویجاړ شوي ډیټا څخه د ان پټ بیارغونې زده کړه وکړي ، اوټوینکوډر په ځانګړي توګه د دې لپاره ګټور دي <strong>شور لغوه کول</strong>. دوی د شور مداخلې سره سره د ګټورو معلوماتو پیژندلو او بحالولو اداره کوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA%D9%88_%DA%A9%D9%85%D9%BE%D8%B1%DB%8C%D8%B4%D9%86"></span>د معلوماتو کمپریشن<span class="ez-toc-section-end"></span></h4>



<p>د ډیټا انکوډ کولو زده کولو سره په ډیر کمپیکٹ فارم کې ، اوټوینکوډر د دې لپاره کارول کیدی شي <strong>د معلوماتو کمپریشن</strong>. که څه هم دوی لاهم په پراخه کچه په عمل کې د دې هدف لپاره ندي کارول شوي ، د دوی احتمال د پام وړ دی ، په ځانګړي توګه د ځانګړو ډیټا ډولونو فشارولو لپاره.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA%D9%88_%D8%AA%D9%88%D9%84%DB%8C%D8%AF_%D8%A7%D9%88_%D8%AA%D9%88%D8%B1_%D9%84%DA%AB%D9%88%D9%84"></span>د معلوماتو تولید او تور لګول<span class="ez-toc-section-end"></span></h4>



<p>Autoencoders د دې وړتیا لري چې نوي ډیټا مثالونه رامینځته کړي چې د دوی د روزنې ډیټا سره ورته وي. دا وړتیا هم کارول کیدی شي <strong>تورول</strong>، کوم چې په ډیټاسیټ کې د ورک شوي ډیټا ډکول شامل دي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_Autoencoder_%DA%89%D9%88%D9%84%D9%88%D9%86%D9%87"></span>د Autoencoder ډولونه<span class="ez-toc-section-end"></span></h3>



<p>د معیاري آټوینکوډر هاخوا ، مختلف ډولونه رامینځته شوي ترڅو د ډیټا ځانګړتیاو او اړینو دندو سره تطابق وکړي. دلته ځینې د پام وړ توپیرونه دي:</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AA%D8%BA%DB%8C%D8%B1%D8%A7%D8%AA%D9%8A_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_VAE"></span>تغیراتي اتوماتیک کوډر (VAE)<span class="ez-toc-section-end"></span></h4>



<p>د <strong>تغیراتي اتوماتیک کوډر</strong> ((<strong>VAE</strong>) د سټوچاسټیک پرت اضافه کړئ کوم چې د معلوماتو تولید ته اجازه ورکوي. VAEs په ځانګړي ډول د مینځپانګې په نسل کې مشهور دي ، لکه عکسونه یا میوزیک ، ځکه چې دوی دا امکان رامینځته کوي چې نوي او مختلف عناصر تولید کړي چې د ورته ماډل سره سم د منلو وړ وي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%B3%D9%BE%D8%A7%D8%B1%D8%B3_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1%D9%88%D9%86%D9%87"></span>سپارس اتوماتیک کوډرونه<span class="ez-toc-section-end"></span></h4>



<p>د <strong>لږ اوټکوډر</strong> یو جزا شامل کړئ چې په پټو نوډونو کې محدود فعالیت وضع کوي. دوی د ډیټا د ځانګړو ځانګړتیاو په موندلو کې اغیزمن دي، کوم چې د دوی لپاره ګټور کوي <strong>طبقه بندي</strong> او د <strong>بې نظمۍ کشف</strong>.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_Autoencoders_%D9%84%D9%87_%D9%85%DB%8C%D9%86%DA%81%D9%87_%D9%88%DA%93%D9%84"></span>د Autoencoders له مینځه وړل<span class="ez-toc-section-end"></span></h4>



<p>د <strong>غیر نورمال شوي اتوماتیک کوډر</strong> د ان پټ ډیټا کې د شور معرفي کولو مقاومت لپاره ډیزاین شوي. دوی د قوي نمایندګیو زده کولو لپاره ځواکمن دي او د دې لپاره <strong>د معلوماتو دمخه پروسس کول</strong> مخکې له دې چې د ماشین زده کړې نورې دندې ترسره کړئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AA%D8%B3%D9%84%D8%B3%D9%84%D9%8A_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1"></span>تسلسلي اتوماتیک کوډر<span class="ez-toc-section-end"></span></h4>



<p>د <strong>ترتیبي اتوماتیک کوډرونه</strong> د پروسس ډاټا په ترتیبونو کې تنظیم شوي، لکه متن یا د وخت لړۍ. دوی ډیری وختونه تکراري شبکې کاروي لکه LSTM (اوږدې لنډ مهاله حافظه) د وخت په تیریدو سره معلومات کوډ او کوډ کولو لپاره.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%D8%A7%D9%88_%DA%A9%D9%88%DA%89_%D9%85%D8%AB%D8%A7%D9%84%D9%88%D9%86%D9%88_%D8%B1%D9%88%D8%B2%D9%84%D9%88_%DA%85%D8%B1%D9%86%DA%AB%D9%88%D8%A7%D9%84%DB%8C"></span>د اتوماتیک کوډر او کوډ مثالونو روزلو څرنګوالی<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png" alt="" class="wp-image-1193" srcset="/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>د روزنې <strong>اتوماتیک کوډر</strong> د نورو غوښتنلیکونو په مینځ کې د ابعاد کمولو او بې نظمۍ موندلو لپاره د ماشین زده کړې په برخه کې لازمي دنده ده. دلته به وګورو چې څنګه د Python او کتابتون په کارولو سره دا ډول ماډل وروزو <strong>کیراس</strong>، د کوډ مثالونو سره چې تاسو کولی شئ ازموینه وکړئ او خپلو پروژو سره موافقت وکړئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D8%B1_%D8%AF_%D8%B1%D9%88%D8%B2%D9%86%DB%90_%D9%BE%D8%B1%D9%88%D8%B3%D9%87"></span>د اتوماتیک کوډر د روزنې پروسه<span class="ez-toc-section-end"></span></h4>



<p>د اتوماتیک کوډر روزلو لپاره، یو څوک عموما د ضایع میټریک کاروي، لکه د منځنۍ مربع غلطی (MSE)، کوم چې د اصلي ان پټ او بیا رغونې ترمنځ توپیر اندازه کوي. د روزنې هدف د دې ضایع فعالیت کمول دي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%DA%A9%DB%8C%D8%B1%D8%A7_%D8%B3%D8%B1%D9%87_%DA%A9%D9%88%DA%89_%D9%85%D8%AB%D8%A7%D9%84"></span>د کیرا سره کوډ مثال<span class="ez-toc-section-end"></span></h4>



<p>دلته د اتوماتیک کوډر کارولو روزنې یوه ساده بیلګه ده <strong>کیراس</strong>:</p>



<pre class="wp-block-code"><code>

د keras.layers څخه د انپټ واردول، ډینس
د keras.models واردولو ماډل څخه

# د ننوتلو اندازه
# د پټ ځای ابعاد (د فیچر نمایش)
encoding_dim = 32

# د کوډر تعریف
input_img = ننوت(شکل=(input_dim،))
کوډ شوی = ډنډ (کوډینګ_ډیم، فعالول = 'relu') (input_img)

# د کوډر تعریف
ډیکوډ شوی = ډنډ(input_dim، فعالول = 'sigmoid') (کوډ شوی)

# د اتوماتیک کوډر ماډل
autoencoder = ماډل (input_img، کوډ شوی)

# ماډل تالیف
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# د اتوماتیک کوډر روزنه
autoencoder.fit(X_train,
                دورې = 50،
                بیچ_سایز = 256،
                شفل = ریښتیا،
                د اعتبار_ډاټا=(X_test, X_test))

</code></pre>



<p>په دې مثال کې، `X_train` او `X_test` د روزنې او ازموینې ډاټا استازیتوب کوي. په یاد ولرئ چې اتوماتیک کوډر روزل شوی ترڅو د خپل ان پټ &#8216;X_train&#8217; د محصول په توګه وړاندوینه وکړي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%DA%9A%D9%87_%D8%AA%D9%85%D8%B1%DB%8C%D9%86_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D9%84%D8%A7%D8%B1%DA%9A%D9%88%D9%88%D9%86%D9%87"></span>د ښه تمرین لپاره لارښوونه<span class="ez-toc-section-end"></span></h4>



<p></p>



<p>لکه تخنیکونه وکاروئ <strong>کراس تایید</strong>، هلته <strong>بسته نورمال کول</strong> او د <strong>کال بیکونه</strong> د کیراس کولی شي د آټوینکوډر ډرایو فعالیت او ثبات ښه کولو کې هم مرسته وکړي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9_%DA%A9%D9%88%DA%89%D9%88%D9%86%D9%88_%D8%BA%D9%88%DA%9A%D8%AA%D9%86%D9%84%DB%8C%DA%A9%D9%88%D9%86%D9%87"></span>د اتوماتیک کوډونو غوښتنلیکونه<span class="ez-toc-section-end"></span></h4>



<p>د روزنې وروسته، اتوماتیک کوډر کارول کیدی شي:</p>



<ul class="wp-block-list">
<li>د ابعاد کمول</li>



<li>د بې نظمۍ کشف</li>



<li>د تشریح کونکو غیر څارل شوي زده کړه د ماشین زده کړې نورو دندو لپاره ګټوره ده.</li>
</ul>



<p>د پای ته رسولو لپاره، د آټوینکوډر روزنه یوه دنده ده چې د عصبي شبکې جوړښتونو پوهه او د ښه ټونینګ هایپر پارامیټرونو کې تجربې ته اړتیا لري. په هرصورت، د اتوماتیک کوډرونو سادگي او انعطاف دوی د ډیری ډیټا پروسس کولو ستونزو لپاره ارزښتناکه وسیله جوړوي.</p>



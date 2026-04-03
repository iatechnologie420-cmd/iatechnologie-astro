---

title: "د انسان ماشین انٹرفیس: HMIs څه دي؟"
slug: "hmis"
excerpt: "د انسان ماشین انٹرفیس تعریف د انسان ماشین انٹرفیس ټولو وسیلو او وسیلو ته اشاره کوي چې پلي شوي ترڅو د انسان کارونکي او کمپیوټر سیسټم ترمینځ اغیزمن تعامل فعال کړي. دا د سکرینونو بصري ډیزاین څخه نیولې تر وسیلو لکه کیبورډ ، ماوس او حتی ټچ او غږ انٹرفیس پورې هرڅه پوښي. د HMI [&hellip;]"
date: "2024-03-09T12:21:58"
featuredImage: "/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-3.png"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps", "%d8%af-%d8%a7%d8%ba%d9%88%d8%b3%d8%aa%d9%84%d9%88-%d9%88%da%93-%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-iot-ps"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="03 Interface Homme Machine" width="500" height="375" src="https://www.youtube.com/embed/v4pMXQVU0i8?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86_%D9%85%D8%A7%D8%B4%DB%8C%D9%86_%D8%A7%D9%86%D9%B9%D8%B1%D9%81%DB%8C%D8%B3_%D8%AA%D8%B9%D8%B1%DB%8C%D9%81" >د انسان ماشین انٹرفیس تعریف</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE%D9%8A_%D8%AA%D8%AD%D9%88%D9%84" >د HMI تاریخي تحول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-3" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%DA%89%DB%8C%D8%B2%D8%A7%DB%8C%D9%86_%D8%A7%D8%B5%D9%88%D9%84" >د HMI ډیزاین اصول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-4" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D9%BE%D9%87_HCI_%DA%A9%DB%90_%D8%A7%D8%B1%D9%88%D8%A7%D9%BE%D9%88%D9%87%D9%86%D9%87" >په HCI کې ارواپوهنه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%D8%A7%D9%88%D8%B3%D9%86%D9%8A_%D8%A7%D9%88_%D8%B1%D8%A7%D8%AA%D9%84%D9%88%D9%86%DA%A9%D9%8A_%D8%B1%D8%AC%D8%AD%D8%A7%D9%86%D8%A7%D8%AA" >د HMI اوسني او راتلونکي رجحانات</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D9%BE%D9%87_HMI_%DA%A9%DB%90_%D9%84%D8%A7%D8%B3%D8%B1%D8%B3%DB%8C_%D8%A7%D9%88_%D9%BC%D9%88%D9%84_%D8%B4%D9%85%D9%88%D9%84%D9%87" >په HMI کې لاسرسی او ټول شموله</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%D8%A7%D8%BA%DB%8C%D8%B2%D9%85%D9%86%D8%AA%D9%88%D8%A8_%D8%A7%D9%86%D8%AF%D8%A7%D8%B2%D9%87_%DA%A9%D9%88%D9%84" >د HMI اغیزمنتوب اندازه کول</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_%D8%A7%D8%BA%DB%8C%D8%B2%D9%85%D9%86_HMI_%DA%89%DB%8C%D8%B2%D8%A7%DB%8C%D9%86_%DA%A9%D9%88%D9%84%D9%88_%D8%A7%D8%B5%D9%88%D9%84" >د اغیزمن HMI ډیزاین کولو اصول</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D9%88%D8%B6%D8%A7%D8%AD%D8%AA_%D8%A7%D9%88_%D8%B3%D8%A7%D8%AF%DA%AF%D9%8A" >وضاحت او سادگي</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AA%D8%B3%D9%84%D8%B3%D9%84" >تسلسل</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_%D8%BA%D8%A8%D8%B1%DA%AB%D9%88%D9%86_%D8%A7%D9%88_%D8%BA%D8%A8%D8%B1%DA%AB%D9%88%D9%86_%D9%88%D8%AE%D8%AA" >د غبرګون او غبرګون وخت</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D9%84%D8%A7%D8%B3%D8%B1%D8%B3%DB%8C" >لاسرسی</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_%D8%A7%D8%B3%D8%AA%D8%B9%D9%85%D8%A7%D9%84_%D8%A7%D9%86%D8%B9%D8%B7%D8%A7%D9%81_%D8%A7%D9%88_%D9%85%D9%88%D8%AB%D8%B1%DB%8C%D8%AA" >د استعمال انعطاف او موثریت</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_%D8%AA%DB%90%D8%B1%D9%88%D8%AA%D9%86%DB%90_%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA" >د تېروتنې مدیریت</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D9%BE%D9%87_HMI_%DA%A9%DB%90_%D8%A7%D9%88%D8%B3%D9%86%D9%8A_%D8%B1%D8%AC%D8%AD%D8%A7%D9%86%D8%A7%D8%AA_%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86_%D9%85%D8%A7%D8%B4%DB%8C%D9%86_%D8%A7%D9%86%D9%B9%D8%B1%D9%81%DB%8C%D8%B3" >په HMI کې اوسني رجحانات (د انسان ماشین انٹرفیس)</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-16" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%D8%A7%D9%88%D8%B3%D9%86%D9%8A_%D8%B1%D8%AC%D8%AD%D8%A7%D9%86%D8%A7%D8%AA" >د HMI اوسني رجحانات</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%D9%BE%D9%87_%D8%AA%DA%A9%D8%A7%D9%85%D9%84_%DA%A9%DB%90_%D8%AF_UX_%D8%A7%D9%87%D9%85%DB%8C%D8%AA" >د HMI په تکامل کې د UX اهمیت</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_HMI_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%B1%D8%A7%D8%AA%D9%84%D9%88%D9%86%DA%A9%DB%8C_%D9%84%DB%8C%D8%AF" >د HMI لپاره راتلونکی لید</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-19" href="/ps/%d8%af-%d8%a7%d9%86%d8%b3%d8%a7%d9%86-%d9%85%d8%a7%d8%b4%db%8c%d9%86-%d8%a7%d9%86%d9%b9%d8%b1%d9%81%db%8c%d8%b3-hmis-%da%85%d9%87-%d8%af%d9%8a%d8%9f/#%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86_%D8%A7%D9%88_%D9%85%D8%A7%D8%B4%DB%8C%D9%86_%D8%AA%D8%B9%D8%A7%D9%85%D9%84_%D8%B1%D8%A7%D8%AA%D9%84%D9%88%D9%86%DA%A9%DB%8C" >د انسان او ماشین تعامل راتلونکی</a></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86_%D9%85%D8%A7%D8%B4%DB%8C%D9%86_%D8%A7%D9%86%D9%B9%D8%B1%D9%81%DB%8C%D8%B3_%D8%AA%D8%B9%D8%B1%DB%8C%D9%81"></span>د انسان ماشین انٹرفیس تعریف<span class="ez-toc-section-end"></span></h2>



<p>د انسان ماشین انٹرفیس ټولو وسیلو او وسیلو ته اشاره کوي چې پلي شوي ترڅو د انسان کارونکي او کمپیوټر سیسټم ترمینځ اغیزمن تعامل فعال کړي. دا د سکرینونو بصري ډیزاین څخه نیولې تر وسیلو لکه کیبورډ ، ماوس او حتی ټچ او غږ انٹرفیس پورې هرڅه پوښي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE%D9%8A_%D8%AA%D8%AD%D9%88%D9%84"></span>د HMI تاریخي تحول<span class="ez-toc-section-end"></span></h3>



<p>HMIs د کمپیوټینګ له راتګ راهیسې د پام وړ پرمختګ کړی دی. په پیل کې لومړني او د کمانډ لینونو باندې متمرکز شوي، دوی د ګرافیکي کاروونکي انٹرفیس (GUI) ظاهري بڼه سره بدل شوي، د کمپیوټر کارول خورا ډیر رواني دي. نن ورځ، HMIs د ټیکنالوژیو څخه کار اخلي لکه <strong>لمس کول</strong>د غږ پیژندنه، یا حتی وده شوي یا مجازی واقعیت تعاملات.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%DA%89%DB%8C%D8%B2%D8%A7%DB%8C%D9%86_%D8%A7%D8%B5%D9%88%D9%84"></span>د HMI ډیزاین اصول<span class="ez-toc-section-end"></span></h3>



<p>د دې لپاره چې یو انٹرفیس اغیزمن وي، دا باید د ډیزاین کلیدي اصولو ته غاړه کیږدي. سادگي، دوام، روښانتیا، ځواب ویونکي او د کاروونکي اړتیاوو اټکل اړین دي. یو ښه HMI باید کارونکي ته اجازه ورکړي چې د لږترلږه هڅې او ګډوډي سره دندې ترسره کړي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BE%D9%87_HCI_%DA%A9%DB%90_%D8%A7%D8%B1%D9%88%D8%A7%D9%BE%D9%88%D9%87%D9%86%D9%87"></span>په HCI کې ارواپوهنه<span class="ez-toc-section-end"></span></h3>



<p>د HMIs په ډیزاین کې د کاروونکو ادراکي پروسو پوهیدل خورا مهم دي. ادراکي ارګونومیک هڅه کوي د انسان دماغ لخوا د معلوماتو پروسس کولو ظرفیتونو او محدودیتونو سره سم انٹرفیسونه غوره کړي. رنګونه، شکلونه، حرکتونه یا غږ فیډبیک باید د مثال په توګه، د دوی د رواني اغیزو سره سم ډیزاین شي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%D8%A7%D9%88%D8%B3%D9%86%D9%8A_%D8%A7%D9%88_%D8%B1%D8%A7%D8%AA%D9%84%D9%88%D9%86%DA%A9%D9%8A_%D8%B1%D8%AC%D8%AD%D8%A7%D9%86%D8%A7%D8%AA"></span>د HMI اوسني او راتلونکي رجحانات<span class="ez-toc-section-end"></span></h3>



<p>د ظهور سره<strong>مصنوعي استخبارات</strong> او لوی معلومات (<strong>لوی معلومات</strong>)، HMIs په تخصص کې لاس ته راځي. موږ د تصمیم نیولو لپاره د ډیټا لید په کارولو سره د هوښیار شخصي معاونینو ، پرمختللي وړاندیز سیسټمونو او حتی متقابل ډشبورډونو څرګندیدو شاهدان یو.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BE%D9%87_HMI_%DA%A9%DB%90_%D9%84%D8%A7%D8%B3%D8%B1%D8%B3%DB%8C_%D8%A7%D9%88_%D9%BC%D9%88%D9%84_%D8%B4%D9%85%D9%88%D9%84%D9%87"></span>په HMI کې لاسرسی او ټول شموله<span class="ez-toc-section-end"></span></h3>



<p>یو HMI باید ټولو ته د لاسرسي وړ وي ، مختلف فزیکي یا ادراکي معلولیت په پام کې نیولو سره. دا پدې مانا ده چې د ټول شموله ډیزاین لپاره ځینې معیارونو او سپارښتنو ته غاړه ایښودل، نو هر کارونکی کولی شي د دوی وړتیاو ته په پام سره د سیسټمونو سره اړیکه ونیسي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%D8%A7%D8%BA%DB%8C%D8%B2%D9%85%D9%86%D8%AA%D9%88%D8%A8_%D8%A7%D9%86%D8%AF%D8%A7%D8%B2%D9%87_%DA%A9%D9%88%D9%84"></span>د HMI اغیزمنتوب اندازه کول<span class="ez-toc-section-end"></span></h3>



<p>د HMI د اغیزمنتیا ارزولو لپاره، میتودونه لکه د کارونې ازموینې، سروې، او د کارونې ډاټا تحلیلونه کارول کیږي. دا میتودونه د رګونو ټکو پیژندلو او د کارونکي تجربه ښه کولو کې مرسته کوي.</p>



<p>د انسان ماشین انٹرفیس د انسانانو او پرمختللي ټیکنالوژۍ ترمینځ اړین پل استازیتوب کوي. په دوامداره توګه وده کوي، HMIs به بدلون ته دوام ورکړي، داسې ښکاري چې لا نور ډیر هوښیار، هوښیار او تطابق کیږي. د کیفیت ډیزاین ډاډمن کول د سبا ټیکنالوژیو منلو او اغیزمنتوب لپاره اړین دي.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%BA%DB%8C%D8%B2%D9%85%D9%86_HMI_%DA%89%DB%8C%D8%B2%D8%A7%DB%8C%D9%86_%DA%A9%D9%88%D9%84%D9%88_%D8%A7%D8%B5%D9%88%D9%84"></span>د اغیزمن HMI ډیزاین کولو اصول<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM.png" alt="" class="wp-image-1178" srcset="/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM.png 1792w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-300x171.png 300w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1024x585.png 1024w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-150x86.png 150w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-768x439.png 768w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>د انسان ماشین انٹرفیس، یا HMI، د کارونکي او سیسټم ترمنځ په تعامل کې مهم رول لوبوي. دا اړینه ده چې ډیزاینران ښه تعریف شوي اصول تعقیب کړي ترڅو د خوښې، رواني او ګټور کاروونکي تجربه یقیني کړي. </p>



<p>دلته هغه مهم اصول دي چې باید په پام کې ونیول شي کله چې د اغیزمن HMI ډیزاین کول.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D9%88%D8%B6%D8%A7%D8%AD%D8%AA_%D8%A7%D9%88_%D8%B3%D8%A7%D8%AF%DA%AF%D9%8A"></span>وضاحت او سادگي<span class="ez-toc-section-end"></span></h3>



<p>HMI باید روښانه او د پوهیدو لپاره اسانه وي. هرڅومره چې دا ډیر هوښیار وي ، نو د کارونکي لږ روزنه یا ملاتړ ته اړتیا وي.</p>



<p>د روښانتیا او سادگي لپاره کلیدي لارښوونې:</p>



<ul class="wp-block-list">
<li>د ادراکي اوورلوډ څخه مخنیوي لپاره د اختیارونو شمیر کم کړئ.</li>



<li>ښکاره شبیهونه او لیبلونه وکاروئ.</li>



<li>د څو درجې نیویګیشن پرځای مستقیم عملونو ته غاړه کیږدئ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AA%D8%B3%D9%84%D8%B3%D9%84"></span>تسلسل<span class="ez-toc-section-end"></span></h4>



<p>د HMI ډیزاین کې دوام ډاډ ورکوي چې کاروونکي به د یوې برخې څخه بلې برخې ته د تګ پرمهال بې هوښه نشي. پیژندل شوي یا تکراري عناصر د ګړندي زده کړې او غوره حافظې ته اجازه ورکوي.</p>



<p>د ثبات د یقیني کولو لپاره ځینې سپارښتنې:</p>



<ul class="wp-block-list">
<li>یونیفورم بڼه وساتئ (فونټونه، رنګونه، تڼۍ).</li>



<li>د انٹرفیس کړنې او عکس العملونه معیاري کړئ.</li>



<li>ډاډ ترلاسه کړئ چې ورته عملیات د ورته ځوابونو پایله لري.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%BA%D8%A8%D8%B1%DA%AB%D9%88%D9%86_%D8%A7%D9%88_%D8%BA%D8%A8%D8%B1%DA%AB%D9%88%D9%86_%D9%88%D8%AE%D8%AA"></span>د غبرګون او غبرګون وخت<span class="ez-toc-section-end"></span></h4>



<p>یو ځواب ویونکی سیسټم کارونکي ته د کنټرول او اعتبار احساس ورکوي. د انٹرفیس غبرګون وخت باید ګړندی وي ، یا لږترلږه د وړاندوینې وړ وي ، ترڅو د کارونکي مایوسي مخه ونیسي.</p>



<p>د HMI ځواب ویلو ښه کولو لپاره لارښوونې:</p>



<ul class="wp-block-list">
<li>د پروسس کولو وخت ګړندي کولو لپاره کوډ غوره کړئ.</li>



<li>د هر کارونکي عمل وروسته سمدستي فیډبیک چمتو کړئ.</li>



<li>د پرمختګ بارونو یا متحرکاتو په کارولو سره عملیاتي حالت په ګوته کړئ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D9%84%D8%A7%D8%B3%D8%B1%D8%B3%DB%8C"></span>لاسرسی<span class="ez-toc-section-end"></span></h4>



<p>انٹرفیس باید هرچا ته د لاسرسي وړ وي ، پرته لدې چې د دوی عمر ، مهارتونه یا فزیکي وضعیت په پام کې ونیول شي. پدې کې د معلولیت لرونکو کاروونکو حساب اخیستل شامل دي.</p>



<p>د لاسرسي وړ HMI لپاره لارښوونې:</p>



<ul class="wp-block-list">
<li>د غیر متني منځپانګو لپاره متني بدیلونه وړاندې کړئ.</li>



<li>د ضعیفانو لپاره د ښه رنګ برعکس ډاډ ترلاسه کړئ.</li>



<li>د کیبورډ نیویګیشن ځانګړتیاوې پلي کړئ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D8%B3%D8%AA%D8%B9%D9%85%D8%A7%D9%84_%D8%A7%D9%86%D8%B9%D8%B7%D8%A7%D9%81_%D8%A7%D9%88_%D9%85%D9%88%D8%AB%D8%B1%DB%8C%D8%AA"></span>د استعمال انعطاف او موثریت<span class="ez-toc-section-end"></span></h4>



<p>یو انعطاف وړ HMI کاروونکو ته اجازه ورکوي چې د دندو سرته رسولو مختلف لارو تجربه کړي ، ډیری وختونه د لوی عملیاتي موثریت لامل کیږي.</p>



<p>څنګه خپل HMI انعطاف وړ کړئ:</p>



<ul class="wp-block-list">
<li>د بریښنا کاروونکو لپاره د کیبورډ شارټ کټ چمتو کړئ.</li>



<li>د عادي کارونو تنظیم کول فعال کړئ.</li>



<li>خپل انٹرفیس د کارونکي کاري فلو سره تطابق کړئ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%AA%DB%90%D8%B1%D9%88%D8%AA%D9%86%DB%90_%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA"></span>د تېروتنې مدیریت<span class="ez-toc-section-end"></span></h4>



<p>HMI باید د تېروتنې په مخنیوي کې مرسته وکړي مخکې له دې چې دوی پیښ شي، او په اسانۍ سره د دوی د سمولو کې مرسته وکړي.</p>



<p>د خطا د سمبالولو لپاره اړین ټکي:</p>



<ul class="wp-block-list">
<li>د انٹرفیس عناصر ډیزاین کړئ چې د خطا خطر کموي.</li>



<li>واضح او جوړونکي خطا پیغامونه چمتو کړئ.</li>



<li>د اسانه درملنې لپاره &#8220;Undo&#8221; او &#8220;Redo&#8221; فعالیت شامل کړئ.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BE%D9%87_HMI_%DA%A9%DB%90_%D8%A7%D9%88%D8%B3%D9%86%D9%8A_%D8%B1%D8%AC%D8%AD%D8%A7%D9%86%D8%A7%D8%AA_%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86_%D9%85%D8%A7%D8%B4%DB%8C%D9%86_%D8%A7%D9%86%D9%B9%D8%B1%D9%81%DB%8C%D8%B3"></span>په HMI کې اوسني رجحانات (د انسان ماشین انٹرفیس)<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1.png" alt="" class="wp-image-1179" srcset="/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1.png 1792w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1-300x171.png 300w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1-1024x585.png 1024w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1-150x86.png 150w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1-768x439.png 768w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%D8%A7%D9%88%D8%B3%D9%86%D9%8A_%D8%B1%D8%AC%D8%AD%D8%A7%D9%86%D8%A7%D8%AA"></span>د HMI اوسني رجحانات<span class="ez-toc-section-end"></span></h3>



<p>عصري HMIs د دودیزو ان پټ وسیلو څخه لیرې دي او د طبیعي او رواني تعاملاتو په لور حرکت کوي. غوره رجحانات شامل دي:</p>



<p><strong>1. زیات شوی حقیقت او مجازی حقیقت: </strong>د عمیق تجربو وړاندیز کول، دا ټیکنالوژي په ژوره توګه هغه طریقه بدلوي چې موږ د ډیجیټل معلوماتو سره تعامل کوو. د VR هیډسیټ په څیر وسایلو سره (<strong>مجازی حقیقت</strong>) او AR شیشې (<strong>وده شوی حقیقت</strong>)، د حقیقي او مجازی ترمنځ سرحدونه په زیاتیدونکي توګه تیاره کیږي.</p>



<p><strong>2. د اشارې کنټرول:</strong> سیسټمونه لکه <strong>LeapMotion</strong> یا <strong>Kinect</strong> پرته له مستقیم فزیکي تماس څخه د طبیعي لاس یا بدن اشارو له لارې د انٹرفیسونو کنټرول امکان څرګند کړ.</p>



<p><strong>3. مصنوعي ذهانت:</strong> د AI ادغام سره، HMIs د شرایطو درک کولو وړتیا لري، د کاروونکو اړتیاوو وړاندوینه کوي او د انفرادي غوره توبونو سره سمون لري.</p>



<p><strong>4. غږیز حکم:</strong> د متقابل عمل وسیلې په توګه د غږ کارول د شخصي معاونینو څخه مننه معمول ګرځیدلی لکه <strong>سری</strong>, <strong>د ګوګل مرستیال</strong>، او <strong>الیکسا</strong>. د غږ پیژندنه د وسیلو سره د طبیعي اړیکو لپاره اجازه ورکوي.</p>



<p><strong>5. مستقیم عصبي انٹرفیس:</strong> د HMI څیړنې په سر کې ، دا انٹرفیسونه د دماغ او کمپیوټر ترمینځ مستقیم ارتباط رامینځته کول دي ، د فزیکي پردیو اړتیا له مینځه وړل.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%D9%BE%D9%87_%D8%AA%DA%A9%D8%A7%D9%85%D9%84_%DA%A9%DB%90_%D8%AF_UX_%D8%A7%D9%87%D9%85%DB%8C%D8%AA"></span>د HMI په تکامل کې د UX اهمیت<span class="ez-toc-section-end"></span></h4>



<p>د کارونکي متمرکز ډیزاین (<strong>د UX ډیزاین</strong>) د HMI په تکامل کې مهم رول لوبوي، چې موخه یې د امکان تر حده خوندور او اغیزمن تعامل کول دي. د UX ډیزاین د انٹرفیسونو رامینځته کولو لپاره د کارونکي احساسات ، لیدونه او ځوابونه په پام کې نیسي چې نه یوازې فعال وي بلکه د کارولو لپاره هم خوندور وي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HMI_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%B1%D8%A7%D8%AA%D9%84%D9%88%D9%86%DA%A9%DB%8C_%D9%84%DB%8C%D8%AF"></span>د HMI لپاره راتلونکی لید<span class="ez-toc-section-end"></span></h4>



<p>د HMI راتلونکی داسې ښکاري چې د مصنوعي استخباراتو د تل لوی ادغام او په متقابل عمل کې د ډوبیدو او طبیعي کیدو لپاره دوامداره لټون لخوا نښه کیږي. بې له شکه چې ننګونې به د ټیکنالوژیو په پراختیا کې وي چې ټول شموله او ټولو ته د لاسرسي وړ وي ، پداسې حال کې چې د کاروونکو محرمیت او امنیت ساتي.</p>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2.png" alt="" class="wp-image-1180" srcset="/images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2.png 1792w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2-300x171.png 300w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2-1024x585.png 1024w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2-150x86.png 150w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2-768x439.png 768w, /images/blog/Interface-Homme-Machine-tout-savoir-sur-les-IHM-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<figure class="wp-block-embed is-type-video is-provider-tiktok wp-block-embed-tiktok"><div class="wp-block-embed__wrapper">
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@lucienprof/video/7276471705206361376" data-video-id="7276471705206361376" data-embed-from="oembed" style="max-width:605px; min-width:325px;"> <section> <a target="_blank" title="@lucienprof" href="https://www.tiktok.com/@lucienprof?refer=embed" rel="noopener">@lucienprof</a> <p>Interface Homme-machine <a title="prof" target="_blank" href="https://www.tiktok.com/tag/prof?refer=embed" rel="noopener">#prof</a> <a title="profparticulier" target="_blank" href="https://www.tiktok.com/tag/profparticulier?refer=embed" rel="noopener">#profparticulier</a> <a title="coursparticulier" target="_blank" href="https://www.tiktok.com/tag/coursparticulier?refer=embed" rel="noopener">#coursparticulier</a> <a title="coursparticuliers" target="_blank" href="https://www.tiktok.com/tag/coursparticuliers?refer=embed" rel="noopener">#coursparticuliers</a> <a title="science" target="_blank" href="https://www.tiktok.com/tag/science?refer=embed" rel="noopener">#science</a> <a title="nsi" target="_blank" href="https://www.tiktok.com/tag/nsi?refer=embed" rel="noopener">#nsi</a> <a title="informatique" target="_blank" href="https://www.tiktok.com/tag/informatique?refer=embed" rel="noopener">#informatique</a> <a title="réussir" target="_blank" href="https://www.tiktok.com/tag/r%C3%A9ussir?refer=embed" rel="noopener">#réussir</a> </p> <a target="_blank" title="♬ son original - LucienProf®" href="https://www.tiktok.com/music/son-original-7276471722507815712?refer=embed" rel="noopener">♬ son original &#8211; LucienProf®</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%A7%D9%86%D8%B3%D8%A7%D9%86_%D8%A7%D9%88_%D9%85%D8%A7%D8%B4%DB%8C%D9%86_%D8%AA%D8%B9%D8%A7%D9%85%D9%84_%D8%B1%D8%A7%D8%AA%D9%84%D9%88%D9%86%DA%A9%DB%8C"></span>د انسان او ماشین تعامل راتلونکی<span class="ez-toc-section-end"></span></h3>



<p>د انسان &#8211; ماشین تعامل راتلونکی ژمنه کوي چې حتی ډیر مدغم او هوښیار وي. دلته د انعکاس او پرمختګ لپاره ځینې لارې شتون لري:</p>



<ol class="wp-block-list">
<li>د پرمختګ <strong>مصنوعي استخبارات</strong> څوک کولی شي د کارونکي اړتیاوې اټکل کړي او د ځوابونو مطابق ځواب ورکړي.</li>



<li>د ظهور <strong>زیات شوي واقعیتونه</strong> او <strong>مجازی</strong> کوم چې د نوي کاروونکو تجربو لپاره عمیق چاپیریال رامینځته کوي.</li>



<li>د ادغام <strong>د اشارې کنټرولونه</strong> او لخوا <strong>وینا</strong>، د ماشینونو کارول حتی طبیعي او هوښیارتیا رامینځته کوي.</li>



<li>د مغز ماشین انٹرفیس (BMIs) رامینځته کول چې د انسان فکر او کمپیوټر ترمینځ مستقیم تعامل ته اجازه ورکوي ، د مخابراتو سرعت او موثریت له مخې د حیرانتیا امکانات خلاصوي.</li>
</ol>



<p>شرکتونه لکه <strong>اپل</strong>, <strong>Google</strong> او <strong>مایکروسافټ</strong> د هغه څه حدودو ته دوام ورکړئ چې ممکن وي، د وسایلو ډیزاین کول چې زموږ د ورځني فعالیتونو او د فکر کولو لارو سره ډیر تړلي وي.</p>



---

title: "د ګوګل مورپیون لوبه: دا څنګه لوبیږو او مصنوعي استخباراتو ته ماتې ورکړو؟"
slug: "article-2"
excerpt: "د ګوګل د ټیک-ټو لوبې قواعد د لوبې هدف د مورپیون لوبه، چې د Tic-tac-toe په نوم هم یادیږي، یوه ستراتیژي لوبه ده چې په 3&#215;3 گرډ کې لوبیږي. موخه دا ده چې درې ورته سمبولونه (کراس یا دایره) په افقی، عمودی یا اختصاصی توګه ستاسو د مخالف په وړاندې قطار کړئ. چمتو کول د [&hellip;]"
date: "2024-03-09T12:44:07"
featuredImage: "/images/blog/Jeu-de-Morpion-de-Google-Comment-y-jouer-et-battre-lintelligence-artificielle-.png"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%D8%AF_%DA%AB%D9%88%DA%AB%D9%84_%D8%AF_%D9%BC%DB%8C%DA%A9-%D9%BC%D9%88_%D9%84%D9%88%D8%A8%DB%90_%D9%82%D9%88%D8%A7%D8%B9%D8%AF" >د ګوګل د ټیک-ټو لوبې قواعد</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-2" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%D8%AF_%D9%84%D9%88%D8%A8%DB%90_%D9%87%D8%AF%D9%81" >د لوبې هدف</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%DA%86%D9%85%D8%AA%D9%88_%DA%A9%D9%88%D9%84" >چمتو کول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%D8%AF_%D9%84%D9%88%D8%A8%DB%90_%D9%BE%D8%B1%D9%85%D8%AE%D8%AA%DA%AB" >د لوبې پرمختګ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%D8%AF_%DA%AB%D9%BC%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%AA%D8%AE%D9%86%DB%8C%DA%A9%D9%88%D9%86%D9%87" >د ګټلو لپاره تخنیکونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%D8%A7%D8%B6%D8%A7%D9%81%D9%8A_%D9%84%D8%A7%D8%B1%DA%9A%D9%88%D9%88%D9%86%DB%90" >اضافي لارښوونې</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-7" href="/ps/%d8%af-%da%ab%d9%88%da%ab%d9%84-%d9%85%d9%88%d8%b1%d9%be%db%8c%d9%88%d9%86-%d9%84%d9%88%d8%a8%d9%87-%d8%af%d8%a7-%da%85%d9%86%da%ab%d9%87-%d9%84%d9%88%d8%a8%db%8c%da%96%d9%88-%d8%a7%d9%88-%d9%85/#%D8%AF_%D9%BC%DB%8C%DA%A9-%D9%BC%DB%8C%DA%A9-%D9%BC%D9%88_%D9%84%D9%88%D8%A8%DB%90_%D9%85%D8%B5%D9%86%D9%88%D8%B9%D9%8A_%D8%A7%D8%B3%D8%AA%D8%AE%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA%D9%88_%D8%AA%D9%87_%D9%85%D8%A7%D8%AA%DB%90_%D9%88%D8%B1%DA%A9%D9%88%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%AF_%D8%B3%D8%AA%D8%B1%D8%A7%D8%AA%DB%8C%DA%98%DB%8C%D9%88_%D9%84%D9%86%DA%89%DB%8C%D8%B2" >د ټیک-ټیک-ټو لوبې مصنوعي استخباراتو ته ماتې ورکولو لپاره د ستراتیژیو لنډیز</a></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%DA%AB%D9%88%DA%AB%D9%84_%D8%AF_%D9%BC%DB%8C%DA%A9-%D9%BC%D9%88_%D9%84%D9%88%D8%A8%DB%90_%D9%82%D9%88%D8%A7%D8%B9%D8%AF"></span>د ګوګل د ټیک-ټو لوبې قواعد<span class="ez-toc-section-end"></span></h2>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%84%D9%88%D8%A8%DB%90_%D9%87%D8%AF%D9%81"></span>د لوبې هدف<span class="ez-toc-section-end"></span></h4>



<p>د مورپیون لوبه، چې د Tic-tac-toe په نوم هم یادیږي، یوه ستراتیژي لوبه ده چې په 3&#215;3 گرډ کې لوبیږي. موخه دا ده چې درې ورته سمبولونه (کراس یا دایره) په افقی، عمودی یا اختصاصی توګه ستاسو د مخالف په وړاندې قطار کړئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%DA%86%D9%85%D8%AA%D9%88_%DA%A9%D9%88%D9%84"></span>چمتو کول<span class="ez-toc-section-end"></span></h4>



<p>د ګوګل ټیک پیر لوبه آنلاین شتون لري او په مختلف وسیلو کې لوبیدلی شي ، پشمول سمارټ فونونه ، ټابلیټونه یا کمپیوټرونه. د پیل کولو لپاره، په ساده ډول د ګوګل ویب پاڼې ته لاړ شئ او د لټون بار کې د &#8220;ټیک پیر لوبې&#8221; لټون وکړئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%84%D9%88%D8%A8%DB%90_%D9%BE%D8%B1%D9%85%D8%AE%D8%AA%DA%AB"></span>د لوبې پرمختګ<span class="ez-toc-section-end"></span></h4>



<p>یوځل د لوبې پا pageه کې ، تاسو کولی شئ د مصنوعي استخباراتو پروړاندې لوبه وکړئ ، چې د ګوګل AI په نوم هم پیژندل کیږي ، یا د بل لوبغاړي پروړاندې. که تاسو د ګوګل AI پروړاندې لوبې کول غوره کوئ ، تاسو کولی شئ د مشکل کچه غوره کړئ: اسانه ، متوسط ​​​​یا سخت.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%DA%AB%D9%BC%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%AA%D8%AE%D9%86%DB%8C%DA%A9%D9%88%D9%86%D9%87"></span>د ګټلو لپاره تخنیکونه<span class="ez-toc-section-end"></span></h4>



<p>&#8211; د گرډ د مرکز په نیولو سره پیل کړئ: له مرکز څخه پیل کولو سره ، تاسو د ګټلو چانس ډیروئ ، ځکه چې دا مربع د ډیری احتمالي سمونونو لپاره د پیل ټکی دی.</p>



<p>&#8211; د مخالف حرکتونه بند کړئ: د خپل مخالف حرکتونو ته پام وکړئ او هڅه وکړئ چې په ستراتیژیکو ځایونو کې ستاسو سمبولونو په ځای کولو سره د دوی احتمالي لاین اپونه بند کړئ.</p>



<p>&#8211; د راتلونکو حرکتونو اټکل وکړئ: هڅه وکړئ د خپل مخالف حرکتونو وړاندوینه وکړئ او خپل سمبولونه ځای په ځای کړئ ترڅو د دوی ستراتیژیو سره مقابله وکړئ.</p>



<p>&#8211; په خپل چلند کې انعطاف منونکی اوسئ: ځان په یوه واحد ستراتیژۍ کې مه بندوئ ، د خپل مخالف حرکتونو پراساس تاکتیکونو بدلولو ته چمتو اوسئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%A7%D8%B6%D8%A7%D9%81%D9%8A_%D9%84%D8%A7%D8%B1%DA%9A%D9%88%D9%88%D9%86%DB%90"></span>اضافي لارښوونې<span class="ez-toc-section-end"></span></h4>



<p>&#8211; د &#8220;اسانه&#8221; کچه کم مه ګڼئ: حتی که تاسو تجربه لرونکی لوبغاړی یاست ، د &#8220;اسانه&#8221; کچه د نوي ستراتیژیو ازموینې یا ستاسو د لوبې اصلاح کولو لپاره ښه تمرین کیدی شي.</p>



<p>&#8211; ساتیري وکړئ: د ټیک پیر لوبه یوه ساده او ساتیري لوبه ده چې په چټکۍ سره لوبیدلی شي. د ساتیرۍ لپاره د هرې لوبې څخه ګټه واخلئ او خپل مهارتونه ښه کړئ.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%BC%DB%8C%DA%A9-%D9%BC%DB%8C%DA%A9-%D9%BC%D9%88_%D9%84%D9%88%D8%A8%DB%90_%D9%85%D8%B5%D9%86%D9%88%D8%B9%D9%8A_%D8%A7%D8%B3%D8%AA%D8%AE%D8%A8%D8%A7%D8%B1%D8%A7%D8%AA%D9%88_%D8%AA%D9%87_%D9%85%D8%A7%D8%AA%DB%90_%D9%88%D8%B1%DA%A9%D9%88%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%AF_%D8%B3%D8%AA%D8%B1%D8%A7%D8%AA%DB%8C%DA%98%DB%8C%D9%88_%D9%84%D9%86%DA%89%DB%8C%D8%B2"></span>د ټیک-ټیک-ټو لوبې مصنوعي استخباراتو ته ماتې ورکولو لپاره د ستراتیژیو لنډیز<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tuto pour jouer au morpion sur Google" width="500" height="281" src="https://www.youtube.com/embed/CbG0dxF02Uw?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p><br><strong>1. د لوبې په اصولو پوهیدل:</strong><br>مخکې له دې چې د AI ماتولو لپاره ستراتیژۍ جوړ کړئ، دا اړینه ده چې د ټیک پیر لوبې قواعدو باندې پوه شئ. ډاډ ترلاسه کړئ چې تاسو موخې، اجازه شوي عملونه او د بریا معیارونه پیژنئ. دا به تاسو ته اجازه درکړي چې د لوبې په اوږدو کې باخبره پریکړې وکړئ.</p>



<p><strong>2. د AI چلند وګورئ:</strong><br>د AI وهلو لپاره یو له لومړیو ګامونو څخه دی چې دا په دقت سره مشاهده کړي. هغه حرکتونه یاد کړئ چې هغه یې کوي، هغه نمونې چې هغه یې تعقیبوي، او کومې تېروتنې چې هغه یې کوي. دا به تاسو ته د هغه ستراتیژیو په اړه نښې درکړي چې هغه یې کاروي او تاسو سره به د دوی سره د مبارزې لپاره د لارو موندلو کې مرسته وکړي.</p>



<p><strong>3. غیر متوقع نمونې رامینځته کړئ:</strong><br>یوځل چې تاسو د AI عملونو نمونو باندې پوه شئ ، تاسو کولی شئ د غیر متوقع نمونو په رامینځته کولو سره خپلې ګټې وکاروئ. د مثال په توګه، که چیرې AI د افقی حرکتونو سره مینه ولري، نو هڅه وکړئ چې دا عمودی یا اختریز حرکتونه جوړ کړئ. دا کولی شي د هغه ستراتیژی ګډوډ کړي او هغه ته سخت وخت ورکړي.</p>



<p><strong>4. د AI بریا فرصتونه بند کړئ:</strong><br>د AI وهلو لپاره یو له مهمو ستراتیژیو څخه د ګټلو فرصتونو مخه نیول دي. که تاسو وګورئ چې AI د یو قطار، کالم، یا ډیګونال بشپړولو په اړه دی، خپل سمبول په یوه بکس کې ځای پرځای کړئ چې دا د دې کولو مخه نیسي. دا کولی شي هغه دې ته اړ کړي چې خپل اختیارونه بیا ارزونه وکړي او لږ وړاندوینې وړ چلند وکړي.</p>



<p><strong>5. د راتلونکي AI حرکتونو اټکل وکړئ:</strong><br>د AI ماتولو لپاره، دا مهمه ده چې د دې راتلونکي حرکتونو اټکل وکړئ. د لوبې موقعیتونه تحلیل کړئ او د وړاندوینې کولو هڅه وکړئ چیرې چې AI ممکن خپل راتلونکی سمبول ځای په ځای کړي. دا به تاسو ته اجازه درکړي په مؤثره توګه د دوی ستراتیژیانې بندې کړئ او د کلیدي چوکیو په نیولو سره ګټه ترلاسه کړئ.</p>



<p><strong>6. له خپلو تېروتنو ګټه پورته کړئ:</strong><br>که څه هم AIs عموما خورا وړ دي، دوی ځینې وختونه غلطي کولی شي. که تاسو کومه تېروتنه وینئ، نو له دې فرصت څخه ګټه واخلئ چې مقابله وکړئ او ګټه ترلاسه کړئ. د مثال په توګه ، که AI ستاسو د راتلونکي ګټونکي لاین بندول هیر کړي ، نو دا فرصت واخلئ چې دا بشپړ کړئ او لوبه وګټئ.</p>



<p>د دې ستراتیژیو په تعقیب، تاسو به د ټیک پیر په لوبه کې د مصنوعي استخباراتو وهلو امکانات زیات کړئ. په هرصورت، په یاد ولرئ چې AIs کولی شي د دوی له غلطیو څخه هم زده کړي او تطبیق کړي، نو دا مهمه ده چې د لوبې په اوږدو کې ستاسو ستراتیژیو ته وده ورکولو او پاکولو ته دوام ورکړئ.</p>



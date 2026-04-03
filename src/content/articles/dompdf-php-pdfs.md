---
title: "Dompdf: په PHP کې په زړه پورې PDFs څنګه رامینځته کړئ؟"
slug: "dompdf-php-pdfs"
excerpt: "د Dompdf پیژندنه Dompdf د PHP کتابتون دی چې تاسو ته اجازه درکوي د HTML مینځپانګې څخه پی ډی ایف فایلونه رامینځته کړئ. دا حل په PDF بڼه کې د راپورونو، رسیدونو یا کوم بل سند جوړولو لپاره خورا ګټور دی. پدې مقاله کې ، موږ به د Dompdf لومړني ځانګړتیاوې ومومئ او زده کړو [&hellip;]"
date: "2024-03-09T12:42:44"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps", "%da%a9%d9%85%d9%be%db%8c%d9%88%d9%bc%d8%b1%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d9%bc%d8%a7-ps"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%AF_Dompdf_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87" >د Dompdf پیژندنه</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%B4%D8%B1%D8%B7%D9%88%D9%86%D9%87" >شرطونه</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%AF_Dompdf_%D9%86%D8%B5%D8%A8_%DA%A9%D9%88%D9%84" >د Dompdf نصب کول</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%B2%D9%85%D8%A7_%D9%84%D9%88%D9%85%DA%93%DB%8C_PDF_%D8%B3%D9%86%D8%AF_%D8%AF_Dompdf_%D8%B3%D8%B1%D9%87" >زما لومړی PDF سند د Dompdf سره</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D9%BE%D9%87_%D9%BE%DB%8C_%D8%A7%DB%8C%DA%86_%D9%BE%DB%8C_%DA%A9%DB%90_%D8%AF_%DA%9A%DA%A9%D9%84%D9%8A_%D9%BE%DB%8C_%DA%89%DB%8C_%D8%A7%DB%8C%D9%81_%D8%B1%D8%A7%D9%85%DB%8C%D9%86%DA%81%D8%AA%D9%87_%DA%A9%D9%88%D9%84" >په پی ایچ پی کې د ښکلي پی ډی ایف رامینځته کول</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%AF_Dompdf_%D9%86%D8%B5%D8%A8%D9%88%D9%84%D9%88_%D8%A7%D9%88_%DA%A9%D8%A7%D8%B1%D9%88%D9%84%D9%88_%D8%A8%D9%84%D9%87_%D8%B7%D8%B1%DB%8C%D9%82%D9%87" >د Dompdf نصبولو او کارولو بله طریقه</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%AF_HTML_%D9%BC%DB%8C%D9%85%D9%BE%D9%84%DB%8C%D9%BC_%DA%85%D8%AE%D9%87_%D8%AF_%D9%BE%DB%8C_%DA%89%DB%8C_%D8%A7%DB%8C%D9%81_%D8%B1%D8%A7%D9%85%DB%8C%D9%86%DA%81%D8%AA%D9%87_%DA%A9%D9%88%D9%84" >د HTML ټیمپلیټ څخه د پی ډی ایف رامینځته کول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%AF_%D8%B9%DA%A9%D8%B3%D9%88%D9%86%D9%88_%D8%A7%D9%88_%D9%81%D9%88%D9%86%D9%BC%D9%88%D9%86%D9%88_%D8%A7%D8%AF%D8%A7%D8%B1%D9%87_%DA%A9%D9%88%D9%84" >د عکسونو او فونټونو اداره کول</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ps/dompdf-%d9%be%d9%87-php-%da%a9%db%90-%d9%be%d9%87-%d8%b2%da%93%d9%87-%d9%be%d9%88%d8%b1%db%90-pdfs-%da%85%d9%86%da%ab%d9%87-%d8%b1%d8%a7%d9%85%db%8c%d9%86%da%81%d8%aa%d9%87-%da%a9%da%93%d8%a6%d8%9f/#%D8%AF_%D8%B1%DB%8C%D9%86%DA%89%DB%8C%D9%86%DA%AB_%D8%A7%D8%B5%D9%84%D8%A7%D8%AD_%DA%A9%D9%88%D9%84_%D8%A7%D9%88_%D8%AF_Dompdf_%D9%85%D8%B3%D9%84%D9%88_%D8%AD%D9%84_%DA%A9%D9%88%D9%84" >د رینډینګ اصلاح کول او د Dompdf مسلو حل کول</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_Dompdf_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87"></span>د Dompdf پیژندنه<span class="ez-toc-section-end"></span></h2>



<p>Dompdf د PHP کتابتون دی چې تاسو ته اجازه درکوي د HTML مینځپانګې څخه پی ډی ایف فایلونه رامینځته کړئ. دا حل په PDF بڼه کې د راپورونو، رسیدونو یا کوم بل سند جوړولو لپاره خورا ګټور دی. پدې مقاله کې ، موږ به د Dompdf لومړني ځانګړتیاوې ومومئ او زده کړو چې څنګه د ښکلي او فعال PDFs رامینځته کولو لپاره دا وکاروو.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%B4%D8%B1%D8%B7%D9%88%D9%86%D9%87"></span>شرطونه<span class="ez-toc-section-end"></span></h3>



<p>د Dompdf نصبولو دمخه، ډاډ ترلاسه کړئ چې تاسو لاندې لرئ:</p>



<ul class="wp-block-list">
<li><strong>پی ایچ پی:</strong> Dompdf PHP>= 5.4 ته اړتیا لري. دا د PHP د 7.x نسخو سره مطابقت لري.</li>



<li><strong>د پی ایچ پی توسیع:</strong> ډاډ ترلاسه کړئ چې تاسو لاندې پی ایچ پی توسیعونه فعال کړي دي: mbstring، DOM او GD. دا توسیعونه د Dompdf د سم فعالیت لپاره اړین دي.</li>



<li><strong>کمپوز:</strong> Dompdf د کمپوزر له لارې ویشل شوی، کوم چې د پی ایچ پی لپاره د انحصار مدیر دی. ډاډ ترلاسه کړئ چې تاسو په خپل سیسټم کې کمپوزر نصب کړی.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_Dompdf_%D9%86%D8%B5%D8%A8_%DA%A9%D9%88%D9%84"></span>د Dompdf نصب کول<span class="ez-toc-section-end"></span></h4>



<p>د Dompdf نصبولو لپاره، لاندې مرحلې تعقیب کړئ:</p>



<ol class="wp-block-list">
<li><strong>د PHP نوې پروژه جوړه کړئ:</strong> که تاسو لا دمخه موجوده پروژه نلرئ، د خپلې خوښې بنسټیز جوړښت په کارولو سره یوه نوې جوړه کړئ.</li>



<li><strong>د کمپوزر له لارې د Dompdf انحصار اضافه کړئ:</strong> کنسول خلاص کړئ او خپل د پروژې لارښود ته لاړشئ. خپلې پروژې ته د Dompdf اضافه کولو لپاره لاندې کمانډ چل کړئ:     <pre><code>کمپوزر dompdf/dompdf ته اړتیا لري</code></pre>     دا کمانډ به په اوتومات ډول د دې انحصارونو سره Dompdf ډاونلوډ او نصب کړي.</li>



<li><strong>په خپل غوښتنلیک کې Dompdf وکاروئ:</strong> تاسو اوس کولی شئ په خپله پروژه کې Dompdf وکاروئ. د Dompdf سره د پی ډی ایف فایلونو جوړولو لپاره ډیری لارې شتون لري، مګر دلته د پیل کولو لپاره یو بنسټیز مثال دی:
<pre><code>// د کمپوزر آٹولوډر شامل کړئ
'vendor/autoload.php' ته اړتیا لري؛

// یو نوی Dompdf څیز جوړ کړئ
$dompdf = نوی Dompdf();

// د فایل یا تار څخه HTML مینځپانګه پورته کړئ
$html = '<h1><span class="ez-toc-section" id="%D8%B2%D9%85%D8%A7_%D9%84%D9%88%D9%85%DA%93%DB%8C_PDF_%D8%B3%D9%86%D8%AF_%D8%AF_Dompdf_%D8%B3%D8%B1%D9%87"></span>زما لومړی PDF سند د Dompdf سره<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// د PDF سند وړاندې کړئ
$dompdf->render();

// محصول ته د PDF سند واستوئ
$dompdf->stream('document.pdf');</code></pre>
    دا مثال د سرلیک سره یو نوی PDF سند رامینځته کوي او د &#8220;document.pdf&#8221; فایل په توګه اپلوډ کوي. تاسو کولی شئ د خپلو اړتیاو سره سم د HTML مینځپانګه تنظیم کړئ.</li>
</ol>



<p>اوس چې تاسو Dompdf نصب کړی، تاسو کولی شئ په خپلو ویب غوښتنلیکونو کې د ښکلي او فعال PDF فایلونو تولید پیل کړئ. Dompdf د PDF رینډینګ دودیز کولو لپاره ډیری پرمختللي ب featuresې وړاندې کوي ، لکه د عکسونو اداره کول ، دودیز فونټونه او CSS سټایلونه.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D9%BE%D9%87_%D9%BE%DB%8C_%D8%A7%DB%8C%DA%86_%D9%BE%DB%8C_%DA%A9%DB%90_%D8%AF_%DA%9A%DA%A9%D9%84%D9%8A_%D9%BE%DB%8C_%DA%89%DB%8C_%D8%A7%DB%8C%D9%81_%D8%B1%D8%A7%D9%85%DB%8C%D9%86%DA%81%D8%AA%D9%87_%DA%A9%D9%88%D9%84"></span>په پی ایچ پی کې د ښکلي پی ډی ایف رامینځته کول<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_Dompdf_%D9%86%D8%B5%D8%A8%D9%88%D9%84%D9%88_%D8%A7%D9%88_%DA%A9%D8%A7%D8%B1%D9%88%D9%84%D9%88_%D8%A8%D9%84%D9%87_%D8%B7%D8%B1%DB%8C%D9%82%D9%87"></span>د Dompdf نصبولو او کارولو بله طریقه<span class="ez-toc-section-end"></span></h3>



<p>دلته د تعقیب لپاره ګامونه دي:<br>1. د رسمي ویب پاڼې څخه د Dompdf وروستۍ نسخه ډاونلوډ کړئ.<br>2. ډاونلوډ شوي فایلونه راوباسئ او په خپل PHP پروژه کې یې ځای په ځای کړئ.<br>3. د Dompdfautoload.php فایل شامل کړئ ترڅو کتابتون ستاسو په پی ایچ پی سکریپټ کې پورته کړي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HTML_%D9%BC%DB%8C%D9%85%D9%BE%D9%84%DB%8C%D9%BC_%DA%85%D8%AE%D9%87_%D8%AF_%D9%BE%DB%8C_%DA%89%DB%8C_%D8%A7%DB%8C%D9%81_%D8%B1%D8%A7%D9%85%DB%8C%D9%86%DA%81%D8%AA%D9%87_%DA%A9%D9%88%D9%84"></span>د HTML ټیمپلیټ څخه د پی ډی ایف رامینځته کول<span class="ez-toc-section-end"></span></h4>



<p>اوس چې موږ Dompdf نصب کړی، موږ به وګورو چې څنګه د HTML ټیمپلیټ په کارولو سره پی ډی ایف جوړ کړو. دا ګامونه تعقیب کړئ:</p>



<p>1. یو HTML فایل جوړ کړئ چې هغه جوړښت او ترتیب ولري چې تاسو یې د PDF لپاره غواړئ.<br>2. د خپل سند د سټایل کولو لپاره د CSS ځانګړتیاوې وکاروئ، د ځانګړتیاوو په کارولو سره لکه د فونټ کورنۍ، د فونټ اندازه، سرحد، او نور.<br>3. د Dompdf ځانګړي ټګونو په کارولو سره متحرک معلومات شامل کړئ، لکه &#8220;{{نوم}}&#8221; یا &#8220;{{address}}&#8221;.<br>4. د هغه HTML ټیمپلیټ په کارولو سره چې تاسو یې رامینځته کړی د PDF تولید لپاره د Dompdf ټولګي وکاروئ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%B9%DA%A9%D8%B3%D9%88%D9%86%D9%88_%D8%A7%D9%88_%D9%81%D9%88%D9%86%D9%BC%D9%88%D9%86%D9%88_%D8%A7%D8%AF%D8%A7%D8%B1%D9%87_%DA%A9%D9%88%D9%84"></span>د عکسونو او فونټونو اداره کول<span class="ez-toc-section-end"></span></h4>



<p>کله چې ښکلي پی ډی ایف رامینځته کړئ ، نو ډیری وختونه اړین دي چې عکسونه پکې شامل کړئ یا ځانګړي فونټونه وکاروئ. دلته د Dompdf سره دا څنګه ترسره کول دي:</p>



<p>1. د ټګ په کارولو سره په خپل HTML ټیمپلیټ کې عکسونه شامل کړئ <img decoding="async" src="chemin_vers_image">.<br>2. مهرباني وکړئ په یاد ولرئ چې Dompdf ټول فونټونه په ډیفالټ کې نه شاملوي. تاسو کولی شئ په خپل CSS کې د @font-face په کارولو سره دودیز فونټونه اضافه کړئ یا د Dompdf لخوا چمتو شوي فونټونو په کارولو سره.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D8%B1%DB%8C%D9%86%DA%89%DB%8C%D9%86%DA%AB_%D8%A7%D8%B5%D9%84%D8%A7%D8%AD_%DA%A9%D9%88%D9%84_%D8%A7%D9%88_%D8%AF_Dompdf_%D9%85%D8%B3%D9%84%D9%88_%D8%AD%D9%84_%DA%A9%D9%88%D9%84"></span>د رینډینګ اصلاح کول او د Dompdf مسلو حل کول<span class="ez-toc-section-end"></span></h4>



<p>ځینې ​​​​وختونه تاسو ممکن د خپل پی ډی ایف وړاندې کولو یا فایلونو رامینځته کولو کې ستونزې سره مخ شئ. دلته د دوی د حل لپاره ځینې لارښوونې دي:</p>



<p>1. وګورئ چې ستاسو د HTML ټیمپلیټ په سمه توګه جوړ شوی او اعتبار لري.<br>2. ډاډ ترلاسه کړئ چې ټولې بهرنۍ سرچینې (انځورونه، فونټونه، او نور) د سرور څخه د لاسرسي وړ دي.<br>3. د Dompdf ډیبګ حالت په فعالولو او د ښودل شوي غلطیو په چک کولو سره خپل کوډ ډیبګ کړئ.<br>4. د عامو تشکیلاتو او مسلو په اړه د نورو معلوماتو لپاره د Dompdf اسناد وګورئ.</p>



<p>د Dompdf په کارولو سره، تاسو کولی شئ د مسلکي او ښه فارمیټ شوي PDF سندونو په وړاندې کولو سره د کاروونکي ښه تجربه چمتو کړئ. که چیرې راپورونه، رسیدونه یا د اسنادو نور ډولونه تولید کړي، Dompdf یو معتبر او پیاوړی انتخاب دی.</p>



<p>په پایله کې، د Dompdf نصب کول ګړندي او اسانه دي د کمپوزر څخه مننه. یوځل نصب شوی ، تاسو کولی شئ د خپل ویب غوښتنلیک اړتیاو پوره کولو لپاره د لوړ کیفیت پی ډی ایف فایلونو رامینځته کول پیل کړئ. د دې د ځانګړتیاوو او شته دودیز کولو اختیارونو په اړه د نورو معلوماتو لپاره د رسمي Dompdf اسنادو کتل مه هیروئ.</p>



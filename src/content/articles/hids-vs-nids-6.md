---

title: "HIDS vs NIDS: توپیرونه او کارول"
slug: "hids-vs-nids-6"
excerpt: "د مداخلې د کشف سیسټمونو پیژندنه: HIDS او NIDS د معلوماتو سیسټم امنیت د ټولو اندازو سوداګرۍ او سازمانونو لپاره مرکزي اندیښنه ده. د مخ په زیاتیدونکي ګواښونو او د سایبر بریدونو پیچلتیا سره مخ دي، دا اړینه ده چې اغیزمن دفاعي میکانیزمونه ځای په ځای کړي. د دې په منځ کې، د د نفوذ [&hellip;]"
date: "2024-03-09T11:58:42"
featuredImage: "/images/blog/HIDS-vs-NIDS-differences-et-utilisation-3.png"
categories: ["%d9%bc%db%8c%da%a9%d9%86%d8%a7%d9%84%d9%88%da%98%d9%8a-%d8%a7%d9%88-%da%89%db%8c%d8%ac%db%8c%d9%bc%d9%84-ps", "%d8%b2%db%8c%d8%b1%d8%a8%d9%86%d8%a7%d9%88%db%90-%d8%a7%d9%88-%d8%b4%d8%a8%da%a9%db%90-ps"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Network Based IDS (NIDS)" width="500" height="281" src="https://www.youtube.com/embed/sjnJrc_iNho?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_%D9%85%D8%AF%D8%A7%D8%AE%D9%84%DB%90_%D8%AF_%DA%A9%D8%B4%D9%81_%D8%B3%DB%8C%D8%B3%D9%BC%D9%85%D9%88%D9%86%D9%88_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87_HIDS_%D8%A7%D9%88_NIDS" >د مداخلې د کشف سیسټمونو پیژندنه: HIDS او NIDS</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#HIDS_%D8%AF_%DA%A9%D9%88%D8%B1%D8%A8%D9%87_%D9%BE%D8%B1_%D8%A8%D9%86%D8%B3%D9%BC_%D8%AF_%D9%85%D8%AF%D8%A7%D8%AE%D9%84%DB%90_%DA%A9%D8%B4%D9%81_%D8%B3%DB%8C%D8%B3%D9%BC%D9%85_%DA%85%D9%87_%D8%B4%DB%8C_%D8%AF%DB%8C%D8%9F" >HIDS (د کوربه پر بنسټ د مداخلې کشف سیسټم) څه شی دی؟</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#NIDS_%D8%AF_%D8%B4%D8%A8%DA%A9%DB%90_%D9%BE%D8%B1_%D8%A8%D9%86%D8%B3%D9%BC_%D8%AF_%D9%86%D9%81%D9%88%D8%B0_%DA%A9%D8%B4%D9%81_%D8%B3%DB%8C%D8%B3%D9%BC%D9%85_%DA%85%D9%87_%D8%B4%DB%8C_%D8%AF%DB%8C%D8%9F" >NIDS (د شبکې پر بنسټ د نفوذ کشف سیسټم) څه شی دی؟</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84" >د HIDS او NIDS ترمنځ پرتله کول</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%D9%BE%D9%88%D9%87%DB%8C%D8%AF%D9%84_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7%D9%88%DB%90_%D8%A7%D9%88_%DA%AB%D9%BC%DB%90" >د HIDS پوهیدل: ځانګړتیاوې او ګټې</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7%D9%88%DB%90" >د HIDS ځانګړتیاوې</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%DA%AB%D9%BC%DB%90" >د HIDS ګټې</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#NIDS_%D8%AA%D8%B4%D8%B1%DB%8C%D8%AD_%DA%A9%DA%93%D9%87_%D8%AF%D8%A7_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A_%D8%A7%D9%88_%DA%AB%D9%BC%DB%90" >NIDS تشریح کړه: دا څنګه کار کوي او ګټې</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#NIDS_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A" >NIDS څنګه کار کوي</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-10" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_NIDS_%DA%AB%D9%BC%DB%90" >د NIDS ګټې</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_NIDS_%D8%BA%D9%88%D8%B1%D9%87_%DA%A9%D9%88%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D9%86%D8%B8%D8%B1%D9%88%D9%86%D9%87" >د NIDS غوره کولو لپاره نظرونه</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D8%BA%D9%88%D8%B1%D9%87_%DA%A9%D9%88%D9%84_%D8%AF_%D9%BE%D8%B1%DB%8C%DA%A9%DA%93%DB%90_%D9%85%D8%B9%DB%8C%D8%A7%D8%B1%D9%88%D9%86%D9%87_%D8%A7%D9%88_%D8%AF_%DA%A9%D8%A7%D8%B1%D9%88%D9%84%D9%88_%D8%B4%D8%B1%D8%A7%DB%8C%D8%B7" >د HIDS او NIDS ترمنځ غوره کول: د پریکړې معیارونه او د کارولو شرایط</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D8%AF_%D8%BA%D9%88%D8%B1%D9%87_%DA%A9%D9%88%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%AF_%D9%BE%D8%B1%DB%8C%DA%A9%DA%93%DB%90_%D9%85%D8%B9%DB%8C%D8%A7%D8%B1%D9%88%D9%86%D9%87" >د HIDS او NIDS ترمنځ د غوره کولو لپاره د پریکړې معیارونه</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/ps/hids-vs-nids-%d8%aa%d9%88%d9%be%db%8c%d8%b1%d9%88%d9%86%d9%87-%d8%a7%d9%88-%da%a9%d8%a7%d8%b1%d9%88%d9%84/#%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%DA%A9%D8%A7%D8%B1%D9%88%D9%84%D9%88_%D8%B4%D8%B1%D8%A7%DB%8C%D8%B7" >د HIDS او NIDS کارولو شرایط</a></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_%D9%85%D8%AF%D8%A7%D8%AE%D9%84%DB%90_%D8%AF_%DA%A9%D8%B4%D9%81_%D8%B3%DB%8C%D8%B3%D9%BC%D9%85%D9%88%D9%86%D9%88_%D9%BE%DB%8C%DA%98%D9%86%D8%AF%D9%86%D9%87_HIDS_%D8%A7%D9%88_NIDS"></span>د مداخلې د کشف سیسټمونو پیژندنه: HIDS او NIDS<span class="ez-toc-section-end"></span></h2>



<p>د معلوماتو سیسټم امنیت د ټولو اندازو سوداګرۍ او سازمانونو لپاره مرکزي اندیښنه ده. د مخ په زیاتیدونکي ګواښونو او د سایبر بریدونو پیچلتیا سره مخ دي، دا اړینه ده چې اغیزمن دفاعي میکانیزمونه ځای په ځای کړي. د دې په منځ کې، د <strong>د نفوذ کشف سیسټمونه</strong> ((<strong>IDS</strong>) د کمپیوټري شبکو په څارنې او د مشکوکو فعالیتونو په کشفولو کې مهم رول لوبوي. په ځانګړې توګه، د <strong>کوربه د ننوتلو کشف سیسټمونه</strong> ((<strong>HIDS</strong>) او د <strong>د شبکې د نفوذ کشف سیسټمونه</strong> ((<strong>NESTS</strong>) دوه بشپړونکي ډولونه دي چې د محافظت اضافي پرت چمتو کوي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="HIDS_%D8%AF_%DA%A9%D9%88%D8%B1%D8%A8%D9%87_%D9%BE%D8%B1_%D8%A8%D9%86%D8%B3%D9%BC_%D8%AF_%D9%85%D8%AF%D8%A7%D8%AE%D9%84%DB%90_%DA%A9%D8%B4%D9%81_%D8%B3%DB%8C%D8%B3%D9%BC%D9%85_%DA%85%D9%87_%D8%B4%DB%8C_%D8%AF%DB%8C%D8%9F"></span>HIDS (د کوربه پر بنسټ د مداخلې کشف سیسټم) څه شی دی؟<span class="ez-toc-section-end"></span></h3>



<p>الف <strong>HIDS</strong> سافټویر دی چې په انفرادي کمپیوټر یا کوربه کې نصب شوی. دا هغه سیسټم څاري چې په کوم کې دا د شکمنو فعالیتونو لپاره نصب شوی او دا پیښې مدیر یا د مرکزي امنیت پیښې مدیریت (SIEM) سیسټم ته راپور ورکوي. HIDS د ممکنه مداخلو موندلو لپاره د سیسټم فایلونه، د چلولو پروسې، د فعالیت لاګ، او د فایل سیسټم بشپړتیا تحلیلوي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="NIDS_%D8%AF_%D8%B4%D8%A8%DA%A9%DB%90_%D9%BE%D8%B1_%D8%A8%D9%86%D8%B3%D9%BC_%D8%AF_%D9%86%D9%81%D9%88%D8%B0_%DA%A9%D8%B4%D9%81_%D8%B3%DB%8C%D8%B3%D9%BC%D9%85_%DA%85%D9%87_%D8%B4%DB%8C_%D8%AF%DB%8C%D8%9F"></span>NIDS (د شبکې پر بنسټ د نفوذ کشف سیسټم) څه شی دی؟<span class="ez-toc-section-end"></span></h4>



<p>په مقابل کې، a <strong>NESTS</strong> د شبکې په کچه موقعیت لري ترڅو د سویچ کولو او روټینګ سیسټمونو څخه تیریدونکي ترافیک څارنه وکړي. دا د هغو بریدونو د کشف کولو توان لري چې د شبکې زیربنا په نښه کوي، لکه د خدماتو توزیع شوي انکار (DDoS)، د پورټ سکین، یا د غیرعادلانه چلند نور ډولونه چې د شبکې څخه تیریږي.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D9%BE%D8%B1%D8%AA%D9%84%D9%87_%DA%A9%D9%88%D9%84"></span>د HIDS او NIDS ترمنځ پرتله کول<span class="ez-toc-section-end"></span></h4>



<p>کله چې د مداخلې کشف سیسټم غوره کولو خبره راځي، نو دا اړینه ده چې د HIDS او NIDS ترمنځ توپیرونه پوه شي ترڅو معلومه کړي چې کوم یو به د سازمان ځانګړي چاپیریال سره مناسب وي.</p>



<figure class="wp-block-table"><table><thead><tr><th>معیارونه</th><th>HIDS</th><th>NESTS</th></tr></thead><tbody><tr><td>موقعیت ورکول</td><td>په انفرادي کوربه کې نصب شوی</td><td>د شبکې زیربنا کې پلي شوي</td></tr><tr><td>فعالیت کول</td><td>محلي فایلونه او پروسې څاري</td><td>د شبکې ترافیک څارنه کوي</td></tr><tr><td>د بریدونو ډول معلوم شو</td><td>د فایل ترمیم، روټکیټونه، او نور.</td><td>د پورټ سکین، DDoS، او نور.</td></tr><tr><td>ساحه</td><td>د کوربه ماشین پورې محدود</td><td>ټولې شبکې ته غزول شوي</td></tr><tr><td>فعالیت</td><td>کیدای شي د کوربه بار لخوا اغیزمن شي</td><td>د شبکې ترافیک حجم پورې اړه لري</td></tr></tbody></table></figure>



<p>په مؤثره توګه یوځای کولو سره <strong>HIDS</strong> او <strong>NESTS</strong>، سوداګرۍ کولی شي د امنیت له هولیسټیک لید څخه ګټه پورته کړي او د ناوړه فعالیت ښه کشف یقیني کړي.</p>



<p>د HIDS او NIDS پلي کول د سایبر ګواښونو سره د مبارزې په برخه کې د یوې فعالې ستراتیژۍ استازیتوب کوي. هر سازمان باید د دې اړین مداخلې کشف سیسټمونو سره یوځای کولو سره د غوره امنیت زیربنا رامینځته کولو لپاره خپلې ځانګړي اړتیاوې و ارزوي. د هوښیار پاتې کیدو او د سمو وسیلو سره د ځان سمبالولو سره ، دا ممکنه ده چې د مداخلې پروړاندې ډیجیټل سرچینې د پام وړ خوندي کړئ.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%D9%BE%D9%88%D9%87%DB%8C%D8%AF%D9%84_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7%D9%88%DB%90_%D8%A7%D9%88_%DA%AB%D9%BC%DB%90"></span>د HIDS پوهیدل: ځانګړتیاوې او ګټې<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="/images/blog/HIDS-vs-NIDS-differences-et-utilisation.png" alt="" class="wp-image-1641" srcset="/images/blog/HIDS-vs-NIDS-differences-et-utilisation.png 1792w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-300x171.png 300w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1024x585.png 1024w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-150x86.png 150w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-768x439.png 768w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%DA%81%D8%A7%D9%86%DA%AB%DA%93%D8%AA%DB%8C%D8%A7%D9%88%DB%90"></span>د HIDS ځانګړتیاوې<span class="ez-toc-section-end"></span></h3>



<p>        د <strong>برخی</strong> د HIDS کلیدي ځانګړتیاو کې ترتیب او د فایل پلټنه، د فایل بشپړتیا څارنه، د ناوړه چلند نمونې پیژندنه، او د لاګ مدیریت شامل دي. د HIDS سیسټمونه هم کولی شي په فعاله توګه د ارتباطاتو په بندولو یا د لاسرسي حقونو بدلولو سره عمل وکړي کله چې شکمن فعالیت کشف شي. HIDS اکثرا د NIDS سربیره د IT د لا پراخه امنیت پوښښ لپاره کارول کیږي.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%DA%AB%D9%BC%DB%90"></span>د HIDS ګټې<span class="ez-toc-section-end"></span></h3>



<p>        د HIDS کارول ډیری وړاندیز کوي <strong>ګټې</strong>. لومړی، د کوربه سیسټمونو دقیقه څارنه اجازه ورکوي چې د مداخلو ښه کشف کشف کړي چې ممکن د NIDS لخوا له لاسه ورکړل شوي وي. دوی په ځانګړي ډول د سیسټم مهم فایلونو کې د غیرقانوني بدلونونو او محلي استحصال هڅو په ګوته کولو کې اغیزمن دي. بله ګټه دا ده چې HIDS خپل تاثیر ساتي حتی کله چې د شبکې ترافیک کوډ شوی وي ، کوم چې تل د NIDS سره قضیه نده. برسیره پردې، HIDS کولی شي د تطبیق وړ امنیتي پالیسیو او مقرراتو سره د موافقت په یقیني کولو کې مرسته وکړي.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="NIDS_%D8%AA%D8%B4%D8%B1%DB%8C%D8%AD_%DA%A9%DA%93%D9%87_%D8%AF%D8%A7_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A_%D8%A7%D9%88_%DA%AB%D9%BC%DB%90"></span>NIDS تشریح کړه: دا څنګه کار کوي او ګټې<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-1.png" alt="" class="wp-image-1642" srcset="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-1.png 1792w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-300x171.png 300w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-1024x585.png 1024w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-150x86.png 150w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-768x439.png 768w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="NIDS_%DA%85%D9%86%DA%AB%D9%87_%DA%A9%D8%A7%D8%B1_%DA%A9%D9%88%D9%8A"></span>NIDS څنګه کار کوي<span class="ez-toc-section-end"></span></h3>



<p>د عملیاتو <strong>NESTS</strong> په څو مهمو مرحلو ویشل کیدی شي:</p>



<ul class="wp-block-list">
<li><strong>د معلوماتو راټولول</strong> : NIDS په ریښتیني وخت کې د شبکې ترافیک نظارت کوي د پاکټونو چوس کولو سره چې په ټوله شبکه کې سفر کوي.</li>



<li><strong>د ترافیک تحلیل</strong> : راټول شوي معلومات د مختلفو میتودونو په کارولو سره تحلیل کیږي لکه د لاسلیک معاینه، هیوریسټیک تحلیل یا د چلند تحلیل.</li>



<li><strong>الارمونه او خبرتیاوې</strong> : کله چې شکمن فعالیت وموندل شي، NIDS الارم غږوي او د شبکې مدیرانو ته خبرتیا لیږي.</li>



<li><strong>ادغام او غبرګون</strong> : ځینې NIDS کولی شي د نورو امنیتي سیسټمونو سره مدغم شي ترڅو د کشف شوي ګواښ لپاره اتوماتیک ځواب تنظیم کړي.</li>
</ul>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_NIDS_%DA%AB%D9%BC%DB%90"></span>د NIDS ګټې<span class="ez-toc-section-end"></span></h3>



<p>د تطبیق <strong>NESTS</strong> د کارپوریټ شبکې دننه ډیری د پام وړ ګټې وړاندې کوي:</p>



<ul class="wp-block-list">
<li><strong>د ریښتیني وخت خبرتیاوې</strong> : مدیرانو ته اجازه ورکوي چې سمدستي د احتمالي ګواښونو څخه خبر شي ترڅو سمدستي غبرګون وښيي.</li>



<li><strong>د نفوذ مخنیوی</strong> : په چټکۍ سره د غیر معمولي فعالیتونو په موندلو سره، NIDS د پام وړ زیان رسولو دمخه د نفوذ مخنیوي کې مرسته کوي.</li>



<li><strong>د ترافیک پوهه</strong> : په شبکه کې څه پیښیږي ښه لید وړاندې کوي، کوم چې د امنیت مدیریت لپاره اړین دی.</li>



<li><strong>تنظیمي مطابقت</strong> : په ځینو مواردو کې، د NIDS کارول د سایبر امنیت مختلف معیارونو او مقرراتو اړتیاو پوره کولو کې مرسته کوي.</li>



<li><strong>د پیښې اسناد</strong> : د دې وړتیا وړاندې کوي چې امنیتي پیښې د وروستیو تحلیلونو او احتمالي قانوني شواهدو لپاره ثبت کړي.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_NIDS_%D8%BA%D9%88%D8%B1%D9%87_%DA%A9%D9%88%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D9%86%D8%B8%D8%B1%D9%88%D9%86%D9%87"></span>د NIDS غوره کولو لپاره نظرونه<span class="ez-toc-section-end"></span></h4>



<p>سم یو غوره کړئ <strong>NESTS</strong> د شرکت ځانګړي اړتیاو ژور تحلیل ته اړتیا لري. دلته ځینې مهم نظرونه شتون لري:</p>



<ul class="wp-block-list">
<li><strong>د شبکې مطابقت</strong> : ډاډ ترلاسه کړئ چې NIDS کولی شي پرته له موجوده شبکې زیربنا سره یوځای شي.</li>



<li><strong>د کشف وړتیاوې</strong> : د NIDS لاسلیکونو او د کشف میتودونو اغیزمنتوب ارزونه او د ګواښونو سره د پرمختګ لپاره د دوی وړتیا.</li>



<li><strong>فعالیت</strong> : NIDS باید د پام وړ ځنډ معرفي کولو پرته د شبکې ترافیک حجم اداره کولو وړ وي.</li>



<li><strong>د مدیریت اسانتیا</strong> : د NIDS انٹرفیس باید د کاروونکي دوستانه وي ترڅو د خبرتیاو اسانه او مؤثره مدیریت ته اجازه ورکړي.</li>



<li></li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D8%BA%D9%88%D8%B1%D9%87_%DA%A9%D9%88%D9%84_%D8%AF_%D9%BE%D8%B1%DB%8C%DA%A9%DA%93%DB%90_%D9%85%D8%B9%DB%8C%D8%A7%D8%B1%D9%88%D9%86%D9%87_%D8%A7%D9%88_%D8%AF_%DA%A9%D8%A7%D8%B1%D9%88%D9%84%D9%88_%D8%B4%D8%B1%D8%A7%DB%8C%D8%B7"></span>د HIDS او NIDS ترمنځ غوره کول: د پریکړې معیارونه او د کارولو شرایط<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-2.png" alt="" class="wp-image-1643" srcset="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-2.png 1792w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-300x171.png 300w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-1024x585.png 1024w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-150x86.png 150w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-768x439.png 768w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%D8%AA%D8%B1%D9%85%D9%86%DA%81_%D8%AF_%D8%BA%D9%88%D8%B1%D9%87_%DA%A9%D9%88%D9%84%D9%88_%D9%84%D9%BE%D8%A7%D8%B1%D9%87_%D8%AF_%D9%BE%D8%B1%DB%8C%DA%A9%DA%93%DB%90_%D9%85%D8%B9%DB%8C%D8%A7%D8%B1%D9%88%D9%86%D9%87"></span>د HIDS او NIDS ترمنځ د غوره کولو لپاره د پریکړې معیارونه<span class="ez-toc-section-end"></span></h3>



<p>د HIDS یا NIDS سیسټم تر مینځ انتخاب به په ډیری فکتورونو پورې اړه ولري:</p>



<ul class="wp-block-list">
<li><strong>د څارنې کچه</strong> : HIDS د انفرادي سیسټمونو د څارنې لپاره ډیر مناسب دی، پداسې حال کې چې NIDS د شبکې چاپیریال لپاره ډیزاین شوی.</li>



<li><strong>د ساتنې لپاره د معلوماتو ډولونه</strong> : که تاسو اړتیا لرئ چې په ځانګړي سرورونو کې زیرمه شوي مهم معلومات خوندي کړئ، HIDS ممکن ډیر اړونده وي. د معلوماتو لیږد خوندي کولو لپاره، NIDS غوره دی.</li>



<li><strong>د سیسټم فعالیت</strong> : HIDS کولی شي په کوربه کې د سیسټم ډیرې سرچینې مصرف کړي چې دا یې ساتنه کوي، پداسې حال کې چې NIDS عموما د شبکې څارنې لپاره وقف سرچینو ته اړتیا لري.</li>



<li><strong>د ځای پرځای کولو پیچلتیا</strong> : د HIDS نصب کول د NIDS د تنظیم کولو په پرتله لږ پیچلي کیدی شي کوم چې ډیر ځانګړي شبکې ترتیب ته اړتیا لري.</li>
</ul>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D8%AF_HIDS_%D8%A7%D9%88_NIDS_%DA%A9%D8%A7%D8%B1%D9%88%D9%84%D9%88_%D8%B4%D8%B1%D8%A7%DB%8C%D8%B7"></span>د HIDS او NIDS کارولو شرایط<span class="ez-toc-section-end"></span></h3>



<p>د HIDS یا NIDS کارولو پریکړه اکثرا د کارولو شرایطو پورې اړه لري:</p>



<ul class="wp-block-list">
<li>د ډیری لیرې پرتو نقطو سره د سوداګرۍ لپاره، په هر وسیله کې د HIDS کارول نږدې څارنه چمتو کوي.</li>



<li>هغه سازمانونه چې لوی، متفاوت شبکې لري ممکن د دوی شبکې فعالیتونو کې د نړیوال لید لپاره NIDS خوښ کړي.</li>



<li>د معلوماتو مرکزونه، چیرې چې د سرور فعالیت او بشپړتیا مهم دي، کولی شي د هر سرور په اساس د HIDS پلي کولو څخه ګټه پورته کړي.</li>
</ul>



<p>د HIDS او NIDS ترمنځ انتخاب باید دقیق وي، د امنیتي اهدافو، د معلوماتي ټیکنالوژۍ جوړښت او د سازمان عملیاتي شرایطو سره سمون ولري. HIDS به د سیسټم په کچه د مفصلې څارنې لپاره غوره وي، پداسې حال کې چې NIDS به د شبکې په کچه د څارنې اړتیاوو ته ښه خدمت وکړي. د دواړو ترکیب ځینې وختونه د سایبر امنیت ګواښونو پروړاندې غوره دفاع کیدی شي.</p>



<p>په یاد ولرئ چې ځینې عرضه کونکي د هایبرډ حلونه وړاندیز کوي، د دواړو سیسټمونو وړتیاوې یوځای کوي، لکه <strong>سیمانټیک</strong>, <strong>McAfee</strong>، یا <strong>نارې وهل</strong>. د وروستي انتخاب کولو دمخه د خپلو اړتیاو ارزولو لپاره وخت ونیسئ.</p>



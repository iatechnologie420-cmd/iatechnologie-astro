---
title: "Dompdf: PHP ಯಲ್ಲಿ ಸೊಗಸಾದ PDF ಗಳನ್ನು ಹೇಗೆ ರಚಿಸುವುದು?"
slug: "dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97"
excerpt: "Dompdf ಗೆ ಪರಿಚಯ Dompdf ಎನ್ನುವುದು PHP ಲೈಬ್ರರಿಯಾಗಿದ್ದು ಅದು HTML ವಿಷಯದಿಂದ PDF ಫೈಲ್‌ಗಳನ್ನು ರಚಿಸಲು ನಿಮಗೆ ಅನುಮತಿಸುತ್ತದೆ. ವರದಿಗಳು, ಇನ್‌ವಾಯ್ಸ್‌ಗಳು ಅಥವಾ ಯಾವುದೇ ಇತರ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು PDF ಸ್ವರೂಪದಲ್ಲಿ ರಚಿಸಲು ಈ ಪರಿಹಾರವು ತುಂಬಾ ಉಪಯುಕ್ತವಾಗಿದೆ. ಈ ಲೇಖನದಲ್ಲಿ, ನಾವು Dompdf ನ ಮೂಲ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕಂಡುಕೊಳ್ಳುತ್ತೇವೆ ಮತ್ತು ಸೊಗಸಾದ ಮತ್ತು ಕ್ರಿಯಾತ್ಮಕ PDF ಗಳನ್ನು ರಚಿಸಲು ಅದನ್ನು ಹೇಗೆ ಬಳಸಬೇಕೆಂದು ಕಲಿಯುತ್ತೇವೆ. ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸುವ ಮೊದಲು, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು [&hellip;]"
date: "2024-03-09T12:41:13"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%e0%b2%95%e0%b2%82%e0%b2%aa%e0%b3%8d%e0%b2%af%e0%b3%82%e0%b2%9f%e0%b2%bf%e0%b2%82%e0%b2%97%e0%b3%8d-%e0%b2%ae%e0%b2%a4%e0%b3%8d%e0%b2%a4%e0%b3%81-%e0%b2%a1%e0%b3%87%e0%b2%9f%e0%b2%be-kn", "%e0%b2%a4%e0%b2%82%e0%b2%a4%e0%b3%8d%e0%b2%b0%e0%b2%9c%e0%b3%8d%e0%b2%9e%e0%b2%be%e0%b2%a8-%e0%b2%ae%e0%b2%a4%e0%b3%8d%e0%b2%a4%e0%b3%81-%e0%b2%a1%e0%b2%bf%e0%b2%9c%e0%b2%bf%e0%b2%9f%e0%b2%b2%e0%b3%8d"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#Dompdf_%E0%B2%97%E0%B3%86_%E0%B2%AA%E0%B2%B0%E0%B2%BF%E0%B2%9A%E0%B2%AF" >Dompdf ಗೆ ಪರಿಚಯ</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#%E0%B2%AA%E0%B3%82%E0%B2%B0%E0%B3%8D%E0%B2%B5%E0%B2%BE%E0%B2%AA%E0%B3%87%E0%B2%95%E0%B3%8D%E0%B2%B7%E0%B2%BF%E0%B2%A4%E0%B2%97%E0%B2%B3%E0%B3%81" >ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#Dompdf_%E0%B2%B8%E0%B3%8D%E0%B2%A5%E0%B2%BE%E0%B2%AA%E0%B2%A8%E0%B3%86" >Dompdf ಸ್ಥಾಪನೆ</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#Domdf_%E0%B2%A8%E0%B3%8A%E0%B2%82%E0%B2%A6%E0%B2%BF%E0%B2%97%E0%B3%86_%E0%B2%A8%E0%B2%A8%E0%B3%8D%E0%B2%A8_%E0%B2%AE%E0%B3%8A%E0%B2%A6%E0%B2%B2_PDF_%E0%B2%A1%E0%B2%BE%E0%B2%95%E0%B3%8D%E0%B2%AF%E0%B3%81%E0%B2%AE%E0%B3%86%E0%B2%82%E0%B2%9F%E0%B3%8D" >Domdf ನೊಂದಿಗೆ ನನ್ನ ಮೊದಲ PDF ಡಾಕ್ಯುಮೆಂಟ್</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#PHP_%E0%B2%A8%E0%B2%B2%E0%B3%8D%E0%B2%B2%E0%B2%BF_%E0%B2%B8%E0%B3%8A%E0%B2%97%E0%B2%B8%E0%B2%BE%E0%B2%A6_PDF_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B0%E0%B2%9A%E0%B2%BF%E0%B2%B8%E0%B2%B2%E0%B2%BE%E0%B2%97%E0%B3%81%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B2%BF%E0%B2%A6%E0%B3%86" >PHP ನಲ್ಲಿ ಸೊಗಸಾದ PDF ಅನ್ನು ರಚಿಸಲಾಗುತ್ತಿದೆ</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#Dompdf_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B8%E0%B3%8D%E0%B2%A5%E0%B2%BE%E0%B2%AA%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5_%E0%B2%AE%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B3%81_%E0%B2%AC%E0%B2%B3%E0%B2%B8%E0%B3%81%E0%B2%B5_%E0%B2%87%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%8A%E0%B2%82%E0%B2%A6%E0%B3%81_%E0%B2%B5%E0%B2%BF%E0%B2%A7%E0%B2%BE%E0%B2%A8" >Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸುವ ಮತ್ತು ಬಳಸುವ ಇನ್ನೊಂದು ವಿಧಾನ</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#HTML_%E0%B2%9F%E0%B3%86%E0%B2%82%E0%B2%AA%E0%B3%8D%E0%B2%B2%E0%B3%87%E0%B2%9F%E0%B3%8D%E2%80%8C%E0%B2%A8%E0%B2%BF%E0%B2%82%E0%B2%A6_PDF_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B0%E0%B2%9A%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81" >HTML ಟೆಂಪ್ಲೇಟ್‌ನಿಂದ PDF ಅನ್ನು ರಚಿಸುವುದು</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#%E0%B2%9A%E0%B2%BF%E0%B2%A4%E0%B3%8D%E0%B2%B0%E0%B2%97%E0%B2%B3%E0%B3%81_%E0%B2%AE%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B3%81_%E0%B2%AB%E0%B2%BE%E0%B2%82%E0%B2%9F%E0%B3%8D%E2%80%8C%E0%B2%97%E0%B2%B3%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%A8%E0%B2%BF%E0%B2%B0%E0%B3%8D%E0%B2%B5%E0%B2%B9%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81" >ಚಿತ್ರಗಳು ಮತ್ತು ಫಾಂಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/kn/dompdf-php-%e0%b2%af%e0%b2%b2%e0%b3%8d%e0%b2%b2%e0%b2%bf-%e0%b2%b8%e0%b3%8a%e0%b2%97%e0%b2%b8%e0%b2%be%e0%b2%a6-pdf-%e0%b2%97%e0%b2%b3%e0%b2%a8%e0%b3%8d%e0%b2%a8%e0%b3%81-%e0%b2%b9%e0%b3%87%e0%b2%97/#%E0%B2%B0%E0%B3%86%E0%B2%82%E0%B2%A1%E0%B2%B0%E0%B2%BF%E0%B2%82%E0%B2%97%E0%B3%8D_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%89%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B2%AE%E0%B2%97%E0%B3%8A%E0%B2%B3%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81_%E0%B2%AE%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B3%81_Dompdf_%E0%B2%B8%E0%B2%AE%E0%B2%B8%E0%B3%8D%E0%B2%AF%E0%B3%86%E0%B2%97%E0%B2%B3%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B8%E0%B2%B0%E0%B2%BF%E0%B2%AA%E0%B2%A1%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81" >ರೆಂಡರಿಂಗ್ ಅನ್ನು ಉತ್ತಮಗೊಳಿಸುವುದು ಮತ್ತು Dompdf ಸಮಸ್ಯೆಗಳನ್ನು ಸರಿಪಡಿಸುವುದು</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_%E0%B2%97%E0%B3%86_%E0%B2%AA%E0%B2%B0%E0%B2%BF%E0%B2%9A%E0%B2%AF"></span>Dompdf ಗೆ ಪರಿಚಯ<span class="ez-toc-section-end"></span></h2>



<p>Dompdf ಎನ್ನುವುದು PHP ಲೈಬ್ರರಿಯಾಗಿದ್ದು ಅದು HTML ವಿಷಯದಿಂದ PDF ಫೈಲ್‌ಗಳನ್ನು ರಚಿಸಲು ನಿಮಗೆ ಅನುಮತಿಸುತ್ತದೆ. ವರದಿಗಳು, ಇನ್‌ವಾಯ್ಸ್‌ಗಳು ಅಥವಾ ಯಾವುದೇ ಇತರ ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು PDF ಸ್ವರೂಪದಲ್ಲಿ ರಚಿಸಲು ಈ ಪರಿಹಾರವು ತುಂಬಾ ಉಪಯುಕ್ತವಾಗಿದೆ. ಈ ಲೇಖನದಲ್ಲಿ, ನಾವು Dompdf ನ ಮೂಲ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕಂಡುಕೊಳ್ಳುತ್ತೇವೆ ಮತ್ತು ಸೊಗಸಾದ ಮತ್ತು ಕ್ರಿಯಾತ್ಮಕ PDF ಗಳನ್ನು ರಚಿಸಲು ಅದನ್ನು ಹೇಗೆ ಬಳಸಬೇಕೆಂದು ಕಲಿಯುತ್ತೇವೆ.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E0%B2%AA%E0%B3%82%E0%B2%B0%E0%B3%8D%E0%B2%B5%E0%B2%BE%E0%B2%AA%E0%B3%87%E0%B2%95%E0%B3%8D%E0%B2%B7%E0%B2%BF%E0%B2%A4%E0%B2%97%E0%B2%B3%E0%B3%81"></span>ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು<span class="ez-toc-section-end"></span></h3>



<p>Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸುವ ಮೊದಲು, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಹೊಂದಿರುವಿರಾ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf ಗೆ PHP >= 5.4 ಅಗತ್ಯವಿದೆ. ಇದು PHP ಯ 7.x ಆವೃತ್ತಿಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ.</li>



<li><strong>PHP ವಿಸ್ತರಣೆಗಳು:</strong> ನೀವು ಈ ಕೆಳಗಿನ PHP ವಿಸ್ತರಣೆಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿದ್ದೀರಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ: mbstring, DOM ಮತ್ತು GD. Dompdf ನ ಸರಿಯಾದ ಕಾರ್ಯನಿರ್ವಹಣೆಗೆ ಈ ವಿಸ್ತರಣೆಗಳು ಅತ್ಯಗತ್ಯ.</li>



<li><strong>ರಚಿಸಿ:</strong> Dompdf ಅನ್ನು ಸಂಯೋಜಕ ಮೂಲಕ ವಿತರಿಸಲಾಗುತ್ತದೆ, ಇದು PHP ಗಾಗಿ ಅವಲಂಬಿತ ವ್ಯವಸ್ಥಾಪಕವಾಗಿದೆ. ನಿಮ್ಮ ಸಿಸ್ಟಂನಲ್ಲಿ ನೀವು ಸಂಯೋಜಕವನ್ನು ಸ್ಥಾಪಿಸಿದ್ದೀರಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_%E0%B2%B8%E0%B3%8D%E0%B2%A5%E0%B2%BE%E0%B2%AA%E0%B2%A8%E0%B3%86"></span>Dompdf ಸ್ಥಾಪನೆ<span class="ez-toc-section-end"></span></h4>



<p>Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸಲು, ಈ ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:</p>



<ol class="wp-block-list">
<li><strong>ಹೊಸ PHP ಯೋಜನೆಯನ್ನು ರಚಿಸಿ:</strong> ನೀವು ಈಗಾಗಲೇ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಯೋಜನೆಯನ್ನು ಹೊಂದಿಲ್ಲದಿದ್ದರೆ, ನಿಮ್ಮ ಆಯ್ಕೆಯ ಮೂಲ ರಚನೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಹೊಸದನ್ನು ರಚಿಸಿ.</li>



<li><strong>ಸಂಯೋಜಕ ಮೂಲಕ Dompdf ಅವಲಂಬನೆಯನ್ನು ಸೇರಿಸಿ:</strong> ಕನ್ಸೋಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಡೈರೆಕ್ಟರಿಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ. ನಿಮ್ಮ ಯೋಜನೆಗೆ Dompdf ಅನ್ನು ಸೇರಿಸಲು ಈ ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಲಾಯಿಸಿ:     <pre><code>ಸಂಯೋಜಕರಿಗೆ dompdf/dompdf ಅಗತ್ಯವಿದೆ</code></pre>     ಈ ಆಜ್ಞೆಯು ಅದರ ಅವಲಂಬನೆಗಳೊಂದಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ Dompdf ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡುತ್ತದೆ ಮತ್ತು ಸ್ಥಾಪಿಸುತ್ತದೆ.</li>



<li><strong>ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ Dompdf ಬಳಸಿ:</strong> ನೀವು ಈಗ ನಿಮ್ಮ ಯೋಜನೆಯಲ್ಲಿ Dompdf ಅನ್ನು ಬಳಸಬಹುದು. Dompdf ನೊಂದಿಗೆ PDF ಫೈಲ್‌ಗಳನ್ನು ರಚಿಸಲು ಹಲವು ಮಾರ್ಗಗಳಿವೆ, ಆದರೆ ನೀವು ಪ್ರಾರಂಭಿಸಲು ಮೂಲ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:
<pre><code>// ಸಂಯೋಜಕ ಆಟೋಲೋಡರ್ ಅನ್ನು ಸೇರಿಸಿ
'vendor/autoload.php' ಅಗತ್ಯವಿದೆ;

// ಹೊಸ Dompdf ವಸ್ತುವನ್ನು ರಚಿಸಿ
$dompdf = ಹೊಸ Dompdf();

// ಫೈಲ್ ಅಥವಾ ಸ್ಟ್ರಿಂಗ್‌ನಿಂದ HTML ವಿಷಯವನ್ನು ಲೋಡ್ ಮಾಡಿ
$html = '<h1><span class="ez-toc-section" id="Domdf_%E0%B2%A8%E0%B3%8A%E0%B2%82%E0%B2%A6%E0%B2%BF%E0%B2%97%E0%B3%86_%E0%B2%A8%E0%B2%A8%E0%B3%8D%E0%B2%A8_%E0%B2%AE%E0%B3%8A%E0%B2%A6%E0%B2%B2_PDF_%E0%B2%A1%E0%B2%BE%E0%B2%95%E0%B3%8D%E0%B2%AF%E0%B3%81%E0%B2%AE%E0%B3%86%E0%B2%82%E0%B2%9F%E0%B3%8D"></span>Domdf ನೊಂದಿಗೆ ನನ್ನ ಮೊದಲ PDF ಡಾಕ್ಯುಮೆಂಟ್<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// PDF ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ನಿರೂಪಿಸಿ
$dompdf->ರೆಂಡರ್();

// ಔಟ್‌ಪುಟ್‌ಗೆ PDF ಡಾಕ್ಯುಮೆಂಟ್ ಕಳುಹಿಸಿ
$dompdf->ಸ್ಟ್ರೀಮ್('document.pdf');</code></pre>
    ಈ ಉದಾಹರಣೆಯು ಶೀರ್ಷಿಕೆಯೊಂದಿಗೆ ಹೊಸ PDF ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ ಮತ್ತು ಅದನ್ನು &#8220;document.pdf&#8221; ಫೈಲ್ ಆಗಿ ಅಪ್‌ಲೋಡ್ ಮಾಡುತ್ತದೆ. ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ನೀವು HTML ವಿಷಯವನ್ನು ಗ್ರಾಹಕೀಯಗೊಳಿಸಬಹುದು.</li>
</ol>



<p>ಈಗ ನೀವು Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸಿರುವಿರಿ, ನಿಮ್ಮ ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಸೊಗಸಾದ ಮತ್ತು ಕ್ರಿಯಾತ್ಮಕ PDF ಫೈಲ್‌ಗಳನ್ನು ರಚಿಸಲು ನೀವು ಪ್ರಾರಂಭಿಸಬಹುದು. ಚಿತ್ರಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು, ಕಸ್ಟಮ್ ಫಾಂಟ್‌ಗಳು ಮತ್ತು CSS ಶೈಲಿಗಳಂತಹ PDF ರೆಂಡರಿಂಗ್ ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಲು Dompdf ಹಲವು ಸುಧಾರಿತ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ನೀಡುತ್ತದೆ.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="PHP_%E0%B2%A8%E0%B2%B2%E0%B3%8D%E0%B2%B2%E0%B2%BF_%E0%B2%B8%E0%B3%8A%E0%B2%97%E0%B2%B8%E0%B2%BE%E0%B2%A6_PDF_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B0%E0%B2%9A%E0%B2%BF%E0%B2%B8%E0%B2%B2%E0%B2%BE%E0%B2%97%E0%B3%81%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B2%BF%E0%B2%A6%E0%B3%86"></span>PHP ನಲ್ಲಿ ಸೊಗಸಾದ PDF ಅನ್ನು ರಚಿಸಲಾಗುತ್ತಿದೆ<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B8%E0%B3%8D%E0%B2%A5%E0%B2%BE%E0%B2%AA%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5_%E0%B2%AE%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B3%81_%E0%B2%AC%E0%B2%B3%E0%B2%B8%E0%B3%81%E0%B2%B5_%E0%B2%87%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%8A%E0%B2%82%E0%B2%A6%E0%B3%81_%E0%B2%B5%E0%B2%BF%E0%B2%A7%E0%B2%BE%E0%B2%A8"></span>Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸುವ ಮತ್ತು ಬಳಸುವ ಇನ್ನೊಂದು ವಿಧಾನ<span class="ez-toc-section-end"></span></h3>



<p>ಅನುಸರಿಸಬೇಕಾದ ಹಂತಗಳು ಇಲ್ಲಿವೆ:<br>1. ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್‌ನಿಂದ Dompdf ನ ಇತ್ತೀಚಿನ ಆವೃತ್ತಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.<br>2. ಡೌನ್‌ಲೋಡ್ ಮಾಡಿದ ಫೈಲ್‌ಗಳನ್ನು ಹೊರತೆಗೆಯಿರಿ ಮತ್ತು ಅವುಗಳನ್ನು ನಿಮ್ಮ PHP ಯೋಜನೆಯಲ್ಲಿ ಇರಿಸಿ.<br>3. ನಿಮ್ಮ PHP ಸ್ಕ್ರಿಪ್ಟ್‌ಗೆ ಲೈಬ್ರರಿಯನ್ನು ಲೋಡ್ ಮಾಡಲು Dompdfautoload.php ಫೈಲ್ ಅನ್ನು ಸೇರಿಸಿ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="HTML_%E0%B2%9F%E0%B3%86%E0%B2%82%E0%B2%AA%E0%B3%8D%E0%B2%B2%E0%B3%87%E0%B2%9F%E0%B3%8D%E2%80%8C%E0%B2%A8%E0%B2%BF%E0%B2%82%E0%B2%A6_PDF_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B0%E0%B2%9A%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81"></span>HTML ಟೆಂಪ್ಲೇಟ್‌ನಿಂದ PDF ಅನ್ನು ರಚಿಸುವುದು<span class="ez-toc-section-end"></span></h4>



<p>ಈಗ ನಾವು Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸಿದ್ದೇವೆ, HTML ಟೆಂಪ್ಲೇಟ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು PDF ಅನ್ನು ಹೇಗೆ ರಚಿಸುವುದು ಎಂದು ನಾವು ನೋಡುತ್ತೇವೆ. ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:</p>



<p>1. ನಿಮ್ಮ PDF ಗಾಗಿ ನಿಮಗೆ ಬೇಕಾದ ರಚನೆ ಮತ್ತು ವಿನ್ಯಾಸವನ್ನು ಹೊಂದಿರುವ HTML ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ.<br>2. ಫಾಂಟ್-ಕುಟುಂಬ, ಫಾಂಟ್-ಗಾತ್ರ, ಗಡಿ, ಇತ್ಯಾದಿ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಶೈಲಿ ಮಾಡಲು CSS ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಬಳಸಿ.<br>3. &#8220;{{name}}&#8221; ಅಥವಾ &#8220;{{address}}&#8221; ನಂತಹ Dompdf-ನಿರ್ದಿಷ್ಟ ಟ್ಯಾಗ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಡೈನಾಮಿಕ್ ಡೇಟಾವನ್ನು ಸೇರಿಸಿ.<br>4. ನೀವು ರಚಿಸಿದ HTML ಟೆಂಪ್ಲೇಟ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು PDF ಅನ್ನು ರಚಿಸಲು Dompdf ವರ್ಗವನ್ನು ಬಳಸಿ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%B2%9A%E0%B2%BF%E0%B2%A4%E0%B3%8D%E0%B2%B0%E0%B2%97%E0%B2%B3%E0%B3%81_%E0%B2%AE%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B3%81_%E0%B2%AB%E0%B2%BE%E0%B2%82%E0%B2%9F%E0%B3%8D%E2%80%8C%E0%B2%97%E0%B2%B3%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%A8%E0%B2%BF%E0%B2%B0%E0%B3%8D%E0%B2%B5%E0%B2%B9%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81"></span>ಚಿತ್ರಗಳು ಮತ್ತು ಫಾಂಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು<span class="ez-toc-section-end"></span></h4>



<p>ಸೊಗಸಾದ PDF ಗಳನ್ನು ರಚಿಸುವಾಗ, ಚಿತ್ರಗಳನ್ನು ಸೇರಿಸುವುದು ಅಥವಾ ನಿರ್ದಿಷ್ಟ ಫಾಂಟ್‌ಗಳನ್ನು ಬಳಸುವುದು ಅಗತ್ಯವಾಗಿರುತ್ತದೆ. Dompdf ನೊಂದಿಗೆ ಇದನ್ನು ಹೇಗೆ ಮಾಡುವುದು ಎಂಬುದು ಇಲ್ಲಿದೆ:</p>



<p>1. ಟ್ಯಾಗ್ ಬಳಸಿ ನಿಮ್ಮ HTML ಟೆಂಪ್ಲೇಟ್‌ನಲ್ಲಿ ಚಿತ್ರಗಳನ್ನು ಸೇರಿಸಿ <img decoding="async" src="chemin_vers_image">.<br>2. Dompdf ಪೂರ್ವನಿಯೋಜಿತವಾಗಿ ಎಲ್ಲಾ ಫಾಂಟ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿಲ್ಲ ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ನಿಮ್ಮ CSS ನಲ್ಲಿ @font-face ಬಳಸಿ ಅಥವಾ Dompdf ಒದಗಿಸಿದ ಫಾಂಟ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ನೀವು ಕಸ್ಟಮ್ ಫಾಂಟ್‌ಗಳನ್ನು ಸೇರಿಸಬಹುದು.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%B2%B0%E0%B3%86%E0%B2%82%E0%B2%A1%E0%B2%B0%E0%B2%BF%E0%B2%82%E0%B2%97%E0%B3%8D_%E0%B2%85%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%89%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B2%AE%E0%B2%97%E0%B3%8A%E0%B2%B3%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81_%E0%B2%AE%E0%B2%A4%E0%B3%8D%E0%B2%A4%E0%B3%81_Dompdf_%E0%B2%B8%E0%B2%AE%E0%B2%B8%E0%B3%8D%E0%B2%AF%E0%B3%86%E0%B2%97%E0%B2%B3%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B3%81_%E0%B2%B8%E0%B2%B0%E0%B2%BF%E0%B2%AA%E0%B2%A1%E0%B2%BF%E0%B2%B8%E0%B3%81%E0%B2%B5%E0%B3%81%E0%B2%A6%E0%B3%81"></span>ರೆಂಡರಿಂಗ್ ಅನ್ನು ಉತ್ತಮಗೊಳಿಸುವುದು ಮತ್ತು Dompdf ಸಮಸ್ಯೆಗಳನ್ನು ಸರಿಪಡಿಸುವುದು<span class="ez-toc-section-end"></span></h4>



<p>ಕೆಲವೊಮ್ಮೆ ನಿಮ್ಮ PDF ಅನ್ನು ರೆಂಡರ್ ಮಾಡುವಲ್ಲಿ ಅಥವಾ ಫೈಲ್‌ಗಳನ್ನು ರಚಿಸುವಲ್ಲಿ ನೀವು ಸಮಸ್ಯೆಗಳನ್ನು ಎದುರಿಸಬಹುದು. ಅವುಗಳನ್ನು ಪರಿಹರಿಸಲು ಕೆಲವು ಸಲಹೆಗಳು ಇಲ್ಲಿವೆ:</p>



<p>1. ನಿಮ್ಮ HTML ಟೆಂಪ್ಲೇಟ್ ಅನ್ನು ಸರಿಯಾಗಿ ನಿರ್ಮಿಸಲಾಗಿದೆಯೇ ಮತ್ತು ಮಾನ್ಯವಾಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.<br>2. ಎಲ್ಲಾ ಬಾಹ್ಯ ಸಂಪನ್ಮೂಲಗಳನ್ನು (ಚಿತ್ರಗಳು, ಫಾಂಟ್‌ಗಳು, ಇತ್ಯಾದಿ) ಸರ್ವರ್‌ನಿಂದ ಪ್ರವೇಶಿಸಬಹುದೆಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.<br>3. Dompdf ಡೀಬಗ್ ಮೋಡ್ ಅನ್ನು ಸಕ್ರಿಯಗೊಳಿಸುವ ಮೂಲಕ ಮತ್ತು ಪ್ರದರ್ಶಿಸಲಾದ ದೋಷಗಳನ್ನು ಪರಿಶೀಲಿಸುವ ಮೂಲಕ ನಿಮ್ಮ ಕೋಡ್ ಅನ್ನು ಡೀಬಗ್ ಮಾಡಿ.<br>4. ಸಾಮಾನ್ಯ ಕಾನ್ಫಿಗರೇಶನ್‌ಗಳು ಮತ್ತು ಸಮಸ್ಯೆಗಳ ಕುರಿತು ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ Dompdf ದಸ್ತಾವೇಜನ್ನು ನೋಡಿ.</p>



<p>Dompdf ಅನ್ನು ಬಳಸಿಕೊಂಡು, ವೃತ್ತಿಪರ ಮತ್ತು ಉತ್ತಮವಾಗಿ ಫಾರ್ಮ್ಯಾಟ್ ಮಾಡಲಾದ PDF ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ತಲುಪಿಸುವ ಮೂಲಕ ನೀವು ವರ್ಧಿತ ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಒದಗಿಸಬಹುದು. ವರದಿಗಳು, ಇನ್‌ವಾಯ್ಸ್‌ಗಳು ಅಥವಾ ಇತರ ರೀತಿಯ ದಾಖಲೆಗಳನ್ನು ರಚಿಸುತ್ತಿರಲಿ, Dompdf ಒಂದು ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ಶಕ್ತಿಯುತ ಆಯ್ಕೆಯಾಗಿದೆ.</p>



<p>ಕೊನೆಯಲ್ಲಿ, Dompdf ಅನ್ನು ಸ್ಥಾಪಿಸುವುದು ತ್ವರಿತ ಮತ್ತು ಸುಲಭವಾಗಿದೆ ಸಂಯೋಜಕರಿಗೆ ಧನ್ಯವಾದಗಳು. ಒಮ್ಮೆ ಸ್ಥಾಪಿಸಿದ ನಂತರ, ನಿಮ್ಮ ವೆಬ್ ಅಪ್ಲಿಕೇಶನ್ ಅಗತ್ಯಗಳನ್ನು ಪೂರೈಸಲು ನೀವು ಉತ್ತಮ ಗುಣಮಟ್ಟದ PDF ಫೈಲ್‌ಗಳನ್ನು ರಚಿಸಲು ಪ್ರಾರಂಭಿಸಬಹುದು. ಅದರ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಲಭ್ಯವಿರುವ ಗ್ರಾಹಕೀಕರಣ ಆಯ್ಕೆಗಳ ಕುರಿತು ಇನ್ನಷ್ಟು ತಿಳಿದುಕೊಳ್ಳಲು ಅಧಿಕೃತ Dompdf ದಸ್ತಾವೇಜನ್ನು ಪರೀಕ್ಷಿಸಲು ಮರೆಯಬೇಡಿ.</p>



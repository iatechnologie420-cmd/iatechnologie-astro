---
title: "AlphaGo ທຽບກັບ Leedsol: AI ຍອດຢ້ຽມເອົາຊະນະ Go master"
slug: "alphago-leedsol-ai"
excerpt: "ການປະທະກັນປະຫວັດສາດ: ປັນຍາປະດິດທ້າທາຍເຈົ້າຂອງ Go ໂລກຂອງ Go ໄດ້ຖືກຄອບງໍາໃນປະຫວັດສາດໂດຍແມ່ບົດຂອງມະນຸດ, ຈົນກ່ວາເຫດການທີ່ສໍາຄັນທີ່ສັ່ນສະເທືອນ paradigms. ປັນຍາປະດິດ, ເຄື່ອງມືນີ້ຖືກພັດທະນາໂດຍຄວາມສະຫຼາດຂອງມະນຸດ, ໄດ້ເອົາສິ່ງທ້າທາຍໃນການຕໍ່ສູ້ກັບຫນຶ່ງໃນເກມຍຸດທະສາດທີ່ສັບສົນທີ່ສຸດໃນປະຫວັດສາດ. ການປະທະກັນຄັ້ງປະຫວັດສາດນີ້ລະຫວ່າງວົງຈອນຢ່າງມີເຫດຜົນຂອງຊຸບເປີຄອມພີວເຕີແລະຈິດໃຈຍຸດທະສາດຂອງແຊ້ມໂລກ Go ເປັນຈຸດປ່ຽນຂອງການຮັບຮູ້ຄວາມສາມາດທາງດ້ານສະຕິປັນຍາຂອງ AI. ອາລຸນຂອງຍຸກໃໝ່: AlphaGo ທຽບກັບ Lee Sedol ບາງທີຜົນໄດ້ຮັບທີ່ຫນ້າປະທັບໃຈທີ່ສຸດຂອງການປະທະກັນລະຫວ່າງຜູ້ຊາຍແລະເຄື່ອງຈັກນີ້ແມ່ນເກມ 2016 ທີ່ໄດ້ເຫັນ. AlphaGo, ພັດທະນາໂດຍ DeepMind, ສາຂາ Google, ແລະ Lee Sedol, ຫນຶ່ງໃນຜູ້ນ Go ທີ່ຍິ່ງໃຫຍ່ທີ່ສຸດໃນໂລກ. AlphaGo ຊະນະ 4 ໃນ 5 ການແຂ່ງຂັນ, ພິສູດວ່າປັນຍາປະດິດບໍ່ພຽງແຕ່ສາມາດສ້າງເກມທີ່ຮູ້ຈັກສໍາລັບຄວາມສັບສົນແລະຄວາມເລິກຂອງມັນເທົ່ານັ້ນ, ແຕ່ຍັງປະຕິບັດໄດ້ດີກວ່ານາຍໃຫຍ່ຂອງມະນຸດໃນມັນ. AI ຮຽນຮູ້ວິທີຫຼິ້ນ Go ການຮຽນຮູ້ AI ເພື່ອເປັນຕົ້ນສະບັບ Go ແມ່ນຂະບວນການທີ່ໜ້າສົນໃຈ ແລະສັບສົນ. AlphaGo ໄດ້ໃຊ້ການປະສົມປະສານຂອງການຮຽນຮູ້ແບບຄວບຄຸມຈາກເກມ Go ທີ່ມະນຸດຫຼິ້ນ [&hellip;]"
date: "2024-03-09T12:54:57"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-3.png"
categories: ["%e0%ba%81%e0%ba%b2%e0%ba%99%e0%ba%9d%e0%ba%b6%e0%ba%81%e0%ba%ad%e0%ba%bb%e0%ba%9a%e0%ba%ae%e0%ba%bb%e0%ba%a1-ai-%e0%bb%81%e0%ba%a5%e0%ba%b0%e0%ba%9e%e0%ba%b7%e0%bb%89%e0%ba%99%e0%ba%96%e0%ba%b2"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="AlphaGo Triomphe : Lee Sedol Battu par l&#039;IA!" width="500" height="281" src="https://www.youtube.com/embed/KJ1Me8vHlYY?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%9B%E0%BA%B0%E0%BA%97%E0%BA%B0%E0%BA%81%E0%BA%B1%E0%BA%99%E0%BA%9B%E0%BA%B0%E0%BA%AB%E0%BA%A7%E0%BA%B1%E0%BA%94%E0%BA%AA%E0%BA%B2%E0%BA%94_%E0%BA%9B%E0%BA%B1%E0%BA%99%E0%BA%8D%E0%BA%B2%E0%BA%9B%E0%BA%B0%E0%BA%94%E0%BA%B4%E0%BA%94%E0%BA%97%E0%BB%89%E0%BA%B2%E0%BA%97%E0%BA%B2%E0%BA%8D%E0%BB%80%E0%BA%88%E0%BA%BB%E0%BB%89%E0%BA%B2%E0%BA%82%E0%BA%AD%E0%BA%87_Go" >ການປະທະກັນປະຫວັດສາດ: ປັນຍາປະດິດທ້າທາຍເຈົ້າຂອງ Go</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%AD%E0%BA%B2%E0%BA%A5%E0%BA%B8%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%8D%E0%BA%B8%E0%BA%81%E0%BB%83%E0%BB%9D%E0%BB%88_AlphaGo_%E0%BA%97%E0%BA%BD%E0%BA%9A%E0%BA%81%E0%BA%B1%E0%BA%9A_Lee_Sedol" >ອາລຸນຂອງຍຸກໃໝ່: AlphaGo ທຽບກັບ Lee Sedol</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#AI_%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BA%A7%E0%BA%B4%E0%BA%97%E0%BA%B5%E0%BA%AB%E0%BA%BC%E0%BA%B4%E0%BB%89%E0%BA%99_Go" >AI ຮຽນຮູ້ວິທີຫຼິ້ນ Go</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%95%E0%BA%BB%E0%BA%81%E2%80%8B%E0%BA%88%E0%BA%B2%E0%BA%81%E2%80%8B%E0%BA%81%E0%BA%B2%E0%BA%99%E2%80%8B%E0%BA%9B%E0%BA%B0%E2%80%8B%E0%BA%97%E0%BA%B0%E2%80%8B%E0%BA%81%E0%BA%B1%E0%BA%99%E2%80%8B%E0%BA%94%E0%BA%B1%E0%BB%88%E0%BA%87%E2%80%8B%E0%BA%81%E0%BB%88%E0%BA%B2%E0%BA%A7" >ຕົກ​ຈາກ​ການ​ປະ​ທະ​ກັນ​ດັ່ງ​ກ່າວ</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BB%80%E0%BA%9E%E0%BA%B5%E0%BB%88%E0%BA%A1%E0%BA%82%E0%BA%B6%E0%BB%89%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87_Super_AI_Intelligence_%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AB%E0%BA%BC%E0%BA%B4%E0%BB%89%E0%BA%99%E0%BB%81%E0%BA%99%E0%BA%A7%E0%BB%83%E0%BA%94" >ການເພີ່ມຂຶ້ນຂອງ Super AI: Intelligence ຮຽນຮູ້ການຫຼິ້ນແນວໃດ?</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%82%E0%BA%B1%E0%BB%89%E0%BA%99%E0%BA%95%E0%BA%AD%E0%BA%99%E0%BA%97%E0%BB%8D%E0%BA%B2%E0%BA%AD%E0%BA%B4%E0%BA%94%E0%BA%82%E0%BA%AD%E0%BA%87_AI_%E0%BB%83%E0%BA%99%E0%BB%82%E0%BA%A5%E0%BA%81%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BB%80%E0%BA%81%E0%BA%A1" >ຂັ້ນຕອນທໍາອິດຂອງ AI ໃນໂລກຂອງເກມ</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BB%80%E0%BA%84%E0%BA%B7%E0%BB%88%E0%BA%AD%E0%BA%87%E0%BA%88%E0%BA%B1%E0%BA%81%E0%BB%80%E0%BA%81%E0%BA%A1_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BA%82%E0%BA%B1%E0%BB%89%E0%BA%99%E0%BA%95%E0%BB%88%E0%BA%B3%E0%BA%AA%E0%BA%B8%E0%BA%94" >ເຄື່ອງຈັກເກມ ແລະຂັ້ນຕ່ຳສຸດ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%8D%E0%BA%B8%E0%BA%81%E0%BA%82%E0%BA%AD%E0%BA%87_Super_AI_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%9B%E0%BA%B0%E0%BA%95%E0%BA%B4%E0%BA%A7%E0%BA%B1%E0%BA%94%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BA%97%E0%BA%B5%E0%BB%88%E0%BB%80%E0%BA%A5%E0%BA%B4%E0%BA%81%E0%BB%80%E0%BA%8A%E0%BA%B4%E0%BB%88%E0%BA%87" >ຍຸກຂອງ Super AI ແລະການປະຕິວັດການຮຽນຮູ້ທີ່ເລິກເຊິ່ງ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%88%E0%BA%B2%E0%BA%81_intuition_%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%A1%E0%BA%B0%E0%BA%99%E0%BA%B8%E0%BA%94%E0%BA%81%E0%BA%B1%E0%BA%9A%E0%BA%8D%E0%BA%B8%E0%BA%94%E0%BA%97%E0%BA%B0%E0%BA%AA%E0%BA%B2%E0%BA%94_AI" >ຈາກ intuition ຂອງມະນຸດກັບຍຸດທະສາດ AI</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-10" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#The_Duel_at_the_Summit_%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%A7%E0%BA%B4%E0%BB%80%E0%BA%84%E0%BA%B2%E0%BA%B0%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%97%E0%BA%B5%E0%BB%88%E0%BA%AA%E0%BA%B1%E0%BB%88%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BB%80%E0%BA%97%E0%BA%B7%E0%BA%AD%E0%BA%99%E0%BB%82%E0%BA%A5%E0%BA%81%E0%BA%82%E0%BA%AD%E0%BA%87_Go" >The Duel at the Summit: ການວິເຄາະເກມທີ່ສັ່ນສະເທືອນໂລກຂອງ Go</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-11" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BB%80%E0%BA%9B%E0%BA%B1%E0%BA%99%E0%BA%AA%E0%BA%B1%E0%BA%94%E0%BA%95%E0%BA%B9%E0%BA%81%E0%BA%B1%E0%BA%99%E0%BA%97%E0%BA%B2%E0%BA%87%E0%BA%9B%E0%BA%B0%E0%BA%AB%E0%BA%A7%E0%BA%B1%E0%BA%94%E0%BA%AA%E0%BA%B2%E0%BA%94_AlphaGo_%E0%BA%97%E0%BA%BD%E0%BA%9A%E0%BA%81%E0%BA%B1%E0%BA%9A_Lee_Sedol" >ການເປັນສັດຕູກັນທາງປະຫວັດສາດ: AlphaGo ທຽບກັບ Lee Sedol</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%81%E0%BA%B0%E0%BA%81%E0%BA%BD%E0%BA%A1%E0%BA%AA%E0%BB%8D%E0%BA%B2%E0%BA%A5%E0%BA%B1%E0%BA%9A_AlphaGo_Beyond_Classic_Programming" >ການກະກຽມສໍາລັບ AlphaGo: Beyond Classic Programming</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#Clash_of_the_Titans_%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%AD%E0%BB%89%E0%BA%B2%E0%BA%87%E0%BA%AD%E0%BA%B5%E0%BA%87" >Clash of the Titans: ເກມອ້າງອີງ</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-14" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%AD%E0%BA%B0%E0%BA%99%E0%BA%B2%E0%BA%84%E0%BA%BB%E0%BA%94%E0%BA%82%E0%BA%AD%E0%BA%87_Go_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%8D%E0%BA%B8%E0%BA%94%E0%BA%97%E0%BA%B0%E0%BA%AA%E0%BA%B2%E0%BA%94_%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BA%97%E0%BB%89%E0%BA%AD%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BB%84%E0%BA%8A%E0%BA%8A%E0%BA%B0%E0%BA%99%E0%BA%B0%E0%BA%82%E0%BA%AD%E0%BA%87_Super_AI" >ອະນາຄົດຂອງ Go ແລະເກມຍຸດທະສາດ: ຜົນສະທ້ອນຂອງໄຊຊະນະຂອງ Super AI</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-15" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BB%80%E0%BA%AA%E0%BA%B5%E0%BA%A1_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BA%97%E0%BB%89%E0%BA%AD%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%A1%E0%BA%B1%E0%BA%99" >ການຮຽນຮູ້ເສີມ ແລະຜົນສະທ້ອນຂອງມັນ</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%AD%E0%BA%B0%E0%BA%99%E0%BA%B2%E0%BA%84%E0%BA%BB%E0%BA%94%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BB%81%E0%BA%82%E0%BB%88%E0%BA%87%E0%BA%82%E0%BA%B1%E0%BA%99%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%8D%E0%BA%B8%E0%BA%94%E0%BA%97%E0%BA%B0%E0%BA%AA%E0%BA%B2%E0%BA%94" >ອະນາຄົດຂອງການແຂ່ງຂັນເກມຍຸດທະສາດ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%81%E0%BA%B0%E0%BA%97%E0%BA%BB%E0%BA%9A%E0%BA%95%E0%BB%8D%E0%BB%88%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AD%E0%BA%AD%E0%BA%81%E0%BB%81%E0%BA%9A%E0%BA%9A%E0%BB%80%E0%BA%81%E0%BA%A1" >ຜົນກະທົບຕໍ່ການອອກແບບເກມ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/lo/alphago-%e0%ba%97%e0%ba%bd%e0%ba%9a%e0%ba%81%e0%ba%b1%e0%ba%9a-leedsol-ai-%e0%ba%8d%e0%ba%ad%e0%ba%94%e0%ba%a2%e0%bb%89%e0%ba%bd%e0%ba%a1%e0%bb%80%e0%ba%ad%e0%ba%bb%e0%ba%b2%e0%ba%8a%e0%ba%b0/#%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BA%97%E0%BB%89%E0%BA%AD%E0%BA%99%E0%BA%95%E0%BB%8D%E0%BB%88%E0%BA%AA%E0%BA%B1%E0%BA%87%E0%BA%84%E0%BA%BB%E0%BA%A1%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BB%80%E0%BA%81%E0%BA%A1" >ຜົນສະທ້ອນຕໍ່ສັງຄົມຂອງເກມ</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%9B%E0%BA%B0%E0%BA%97%E0%BA%B0%E0%BA%81%E0%BA%B1%E0%BA%99%E0%BA%9B%E0%BA%B0%E0%BA%AB%E0%BA%A7%E0%BA%B1%E0%BA%94%E0%BA%AA%E0%BA%B2%E0%BA%94_%E0%BA%9B%E0%BA%B1%E0%BA%99%E0%BA%8D%E0%BA%B2%E0%BA%9B%E0%BA%B0%E0%BA%94%E0%BA%B4%E0%BA%94%E0%BA%97%E0%BB%89%E0%BA%B2%E0%BA%97%E0%BA%B2%E0%BA%8D%E0%BB%80%E0%BA%88%E0%BA%BB%E0%BB%89%E0%BA%B2%E0%BA%82%E0%BA%AD%E0%BA%87_Go"></span>ການປະທະກັນປະຫວັດສາດ: ປັນຍາປະດິດທ້າທາຍເຈົ້າຂອງ Go<span class="ez-toc-section-end"></span></h2>



<p>ໂລກຂອງ Go ໄດ້ຖືກຄອບງໍາໃນປະຫວັດສາດໂດຍແມ່ບົດຂອງມະນຸດ, ຈົນກ່ວາເຫດການທີ່ສໍາຄັນທີ່ສັ່ນສະເທືອນ paradigms. ປັນຍາປະດິດ, ເຄື່ອງມືນີ້ຖືກພັດທະນາໂດຍຄວາມສະຫຼາດຂອງມະນຸດ, ໄດ້ເອົາສິ່ງທ້າທາຍໃນການຕໍ່ສູ້ກັບຫນຶ່ງໃນເກມຍຸດທະສາດທີ່ສັບສົນທີ່ສຸດໃນປະຫວັດສາດ. ການປະທະກັນຄັ້ງປະຫວັດສາດນີ້ລະຫວ່າງວົງຈອນຢ່າງມີເຫດຜົນຂອງຊຸບເປີຄອມພີວເຕີແລະຈິດໃຈຍຸດທະສາດຂອງແຊ້ມໂລກ Go ເປັນຈຸດປ່ຽນຂອງການຮັບຮູ້ຄວາມສາມາດທາງດ້ານສະຕິປັນຍາຂອງ AI.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%AD%E0%BA%B2%E0%BA%A5%E0%BA%B8%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%8D%E0%BA%B8%E0%BA%81%E0%BB%83%E0%BB%9D%E0%BB%88_AlphaGo_%E0%BA%97%E0%BA%BD%E0%BA%9A%E0%BA%81%E0%BA%B1%E0%BA%9A_Lee_Sedol"></span>ອາລຸນຂອງຍຸກໃໝ່: AlphaGo ທຽບກັບ Lee Sedol<span class="ez-toc-section-end"></span></h3>



<p>ບາງທີຜົນໄດ້ຮັບທີ່ຫນ້າປະທັບໃຈທີ່ສຸດຂອງການປະທະກັນລະຫວ່າງຜູ້ຊາຍແລະເຄື່ອງຈັກນີ້ແມ່ນເກມ 2016 ທີ່ໄດ້ເຫັນ. <strong>AlphaGo</strong>, ພັດທະນາໂດຍ <strong>DeepMind</strong>, ສາຂາ <strong>Google</strong>, ແລະ Lee Sedol, ຫນຶ່ງໃນຜູ້ນ Go ທີ່ຍິ່ງໃຫຍ່ທີ່ສຸດໃນໂລກ. AlphaGo ຊະນະ 4 ໃນ 5 ການແຂ່ງຂັນ, ພິສູດວ່າປັນຍາປະດິດບໍ່ພຽງແຕ່ສາມາດສ້າງເກມທີ່ຮູ້ຈັກສໍາລັບຄວາມສັບສົນແລະຄວາມເລິກຂອງມັນເທົ່ານັ້ນ, ແຕ່ຍັງປະຕິບັດໄດ້ດີກວ່ານາຍໃຫຍ່ຂອງມະນຸດໃນມັນ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="AI_%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BA%A7%E0%BA%B4%E0%BA%97%E0%BA%B5%E0%BA%AB%E0%BA%BC%E0%BA%B4%E0%BB%89%E0%BA%99_Go"></span>AI ຮຽນຮູ້ວິທີຫຼິ້ນ Go<span class="ez-toc-section-end"></span></h4>



<p>ການຮຽນຮູ້ AI ເພື່ອເປັນຕົ້ນສະບັບ Go ແມ່ນຂະບວນການທີ່ໜ້າສົນໃຈ ແລະສັບສົນ. <strong>AlphaGo</strong> ໄດ້ໃຊ້ການປະສົມປະສານຂອງການຮຽນຮູ້ແບບຄວບຄຸມຈາກເກມ Go ທີ່ມະນຸດຫຼິ້ນ ແລະການຮຽນຮູ້ເສີມ, ເຊິ່ງເຮັດໃຫ້ມັນຫຼິ້ນກັບຕົວມັນເອງ ແລະຮຽນຮູ້ຈາກຄວາມຜິດພາດຂອງຕົນເອງ. ນີ້, ບວກໃສ່ກັບເຄືອຂ່າຍ neural ຢ່າງກວ້າງຂວາງແລະຂັ້ນຕອນວິທີການຄົ້ນຫາຕົ້ນໄມ້ເກມຂັ້ນສູງ, ອະນຸຍາດໃຫ້ AI ເກີນຄວາມສາມາດຂອງມະນຸດໃນເກມນີ້.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%95%E0%BA%BB%E0%BA%81%E2%80%8B%E0%BA%88%E0%BA%B2%E0%BA%81%E2%80%8B%E0%BA%81%E0%BA%B2%E0%BA%99%E2%80%8B%E0%BA%9B%E0%BA%B0%E2%80%8B%E0%BA%97%E0%BA%B0%E2%80%8B%E0%BA%81%E0%BA%B1%E0%BA%99%E2%80%8B%E0%BA%94%E0%BA%B1%E0%BB%88%E0%BA%87%E2%80%8B%E0%BA%81%E0%BB%88%E0%BA%B2%E0%BA%A7"></span>ຕົກ​ຈາກ​ການ​ປະ​ທະ​ກັນ​ດັ່ງ​ກ່າວ<span class="ez-toc-section-end"></span></h4>



<p>ນອກເຫນືອໄປຈາກລັກສະນະທີ່ຫນ້າປະທັບໃຈຂອງການປະເຊີນຫນ້ານີ້, ຜົນສະທ້ອນຍັງດີເກີນຂອບເຂດທີ່ງ່າຍດາຍຂອງເກມ Go. ພວກເຂົາເຈົ້າໄດ້ສ້າງທັດສະນະໃຫມ່ກ່ຽວກັບອະນາຄົດຂອງປັນຍາປະດິດໃນດ້ານຕ່າງໆ, ເຊັ່ນ: ຢາປົວພະຍາດ, ການເງິນ, ຫຼືແມ້ກະທັ້ງການແກ້ໄຂບັນຫາທີ່ສັບສົນ. . ໄຊຊະນະຂອງ<strong>AlphaGo</strong> ຍັງໄດ້ກະຕຸ້ນການຄົ້ນຄວ້າໃນ AI, ຊຸກຍູ້ໃຫ້ມີຈໍານວນການປະດິດສ້າງແລະການນໍາໃຊ້ເຕັກໂນໂລຢີເຫຼົ່ານີ້ເພີ່ມຂຶ້ນ.</p>



<p>ການປະທະກັນຄັ້ງປະຫວັດສາດນີ້ບໍ່ພຽງແຕ່ເປັນຈຸດປ່ຽນຂອງໂລກຂອງ Go, ແຕ່ຍັງຢູ່ໃນທັດສະນະທົ່ວໂລກກ່ຽວກັບສິ່ງທີ່ປັນຍາປະດິດສາມາດບັນລຸໄດ້. ນີ້ສ້າງຄໍາຖາມພື້ນຖານກ່ຽວກັບລັກສະນະຂອງປັນຍາ, ການຮຽນຮູ້ແລະຄວາມສາມາດໃນອະນາຄົດຂອງ AI ໃນສັງຄົມຂອງພວກເຮົາ.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BB%80%E0%BA%9E%E0%BA%B5%E0%BB%88%E0%BA%A1%E0%BA%82%E0%BA%B6%E0%BB%89%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87_Super_AI_Intelligence_%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AB%E0%BA%BC%E0%BA%B4%E0%BB%89%E0%BA%99%E0%BB%81%E0%BA%99%E0%BA%A7%E0%BB%83%E0%BA%94"></span>ການເພີ່ມຂຶ້ນຂອງ Super AI: Intelligence ຮຽນຮູ້ການຫຼິ້ນແນວໃດ?<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA.png" alt="" class="wp-image-811" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA.png 1792w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-300x171.png 300w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1024x585.png 1024w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-150x86.png 150w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-768x439.png 768w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>ປັນຍາທຽມໄດ້ມີຄວາມຄືບໜ້າຢ່າງຫຼວງຫຼາຍໃນທົດສະວັດທີ່ຜ່ານມາ, ໂດຍສະເພາະໃນດ້ານເກມ. ຈາກເກມກະດານແບບດັ້ງເດີມໄປສູ່ໂລກສະເໝືອນທີ່ສັບສົນ, AIs ບໍ່ພຽງແຕ່ໄດ້ຮຽນຮູ້ທີ່ຈະຫລິ້ນເທົ່ານັ້ນ, ແຕ່ໄດ້ກາຍເປັນຄູ່ຕໍ່ສູ້ທີ່ເປັນຕາຢ້ານ, ສາມາດທ້າທາຍ ແລະເອົາຊະນະແຊ້ມມະນຸດໄດ້. ການເພີ່ມຂຶ້ນຂອງປັນຍາປະດິດເຫຼົ່ານີ້ເປັນສັນຍາລັກຂອງການປະສົມປະສານຂອງຄວາມກ້າວຫນ້າທາງດ້ານຄອມພິວເຕີ້ແລະມັນສະຫມອງຫຼາຍ. ມາເບິ່ງວິທີການທີ່ປັນຍາປະດິດໄດ້ຮຽນຮູ້ກົດລະບຽບຂອງການແຂ່ງຂັນຫຼິ້ນແລະກາຍເປັນ Super AI ໃນສະຫນາມກິລາ.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%82%E0%BA%B1%E0%BB%89%E0%BA%99%E0%BA%95%E0%BA%AD%E0%BA%99%E0%BA%97%E0%BB%8D%E0%BA%B2%E0%BA%AD%E0%BA%B4%E0%BA%94%E0%BA%82%E0%BA%AD%E0%BA%87_AI_%E0%BB%83%E0%BA%99%E0%BB%82%E0%BA%A5%E0%BA%81%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BB%80%E0%BA%81%E0%BA%A1"></span>ຂັ້ນຕອນທໍາອິດຂອງ AI ໃນໂລກຂອງເກມ<span class="ez-toc-section-end"></span></h3>



<p>ປະຫວັດຂອງປັນຍາປະດິດໃນເກມມີມາຕັ້ງແຕ່ຄອມພິວເຕີທຳອິດ ແລະ ຄວາມພະຍາຍາມທີ່ຈະຫຼິ້ນໝາກຮຸກ. ໃນຕົ້ນຊຸມປີ 1950, ໂຄງການຄ້າຍຄືໂຄງການທີ່ພັດທະນາໂດຍ Claude Shannon ໄດ້ວາງພື້ນຖານສໍາລັບການຄິດສູດການຄິດໄລ່ໃນເກມຍຸດທະສາດ. ຢ່າງໃດກໍ່ຕາມ, ລະບົບເຫຼົ່ານີ້ຖືກຈໍາກັດໃນແງ່ຂອງຄວາມສາມາດໃນການປຸງແຕ່ງແລະບໍ່ສາມາດແຂ່ງຂັນຢ່າງແທ້ຈິງກັບຜູ້ຫຼິ້ນຂອງມະນຸດ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BB%80%E0%BA%84%E0%BA%B7%E0%BB%88%E0%BA%AD%E0%BA%87%E0%BA%88%E0%BA%B1%E0%BA%81%E0%BB%80%E0%BA%81%E0%BA%A1_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BA%82%E0%BA%B1%E0%BB%89%E0%BA%99%E0%BA%95%E0%BB%88%E0%BA%B3%E0%BA%AA%E0%BA%B8%E0%BA%94"></span>ເຄື່ອງຈັກເກມ ແລະຂັ້ນຕ່ຳສຸດ<span class="ez-toc-section-end"></span></h4>



<p>ເຄື່ອງຈັກເກມ, ການໃຊ້ສູດການຄິດໄລ່ຂັ້ນຕ່ຳສຸດເພື່ອຄາດການເຄື່ອນທີ່ໃນອະນາຄົດ, ໄດ້ກາຍເປັນອົງປະກອບມາດຕະຖານຂອງ AIs ທີ່ມີຄວາມສາມາດໃນການຫຼິ້ນເກມແບບ chessboard. ສູດການຄິດໄລ່ເຫຼົ່ານີ້ປະຕິບັດການວິເຄາະການຄາດຄະເນໃນລະດັບຄວາມເລິກຫຼາຍ, ການປະເມີນການເຄື່ອນໄຫວທີ່ດີທີ່ສຸດແລະຮ້າຍແຮງທີ່ສຸດທີ່ເປັນໄປໄດ້ເພື່ອເພີ່ມປະສິດທິພາບຍຸດທະສາດທີ່ຈະປະຕິບັດຕາມ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%8D%E0%BA%B8%E0%BA%81%E0%BA%82%E0%BA%AD%E0%BA%87_Super_AI_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%9B%E0%BA%B0%E0%BA%95%E0%BA%B4%E0%BA%A7%E0%BA%B1%E0%BA%94%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BA%97%E0%BA%B5%E0%BB%88%E0%BB%80%E0%BA%A5%E0%BA%B4%E0%BA%81%E0%BB%80%E0%BA%8A%E0%BA%B4%E0%BB%88%E0%BA%87"></span>ຍຸກຂອງ Super AI ແລະການປະຕິວັດການຮຽນຮູ້ທີ່ເລິກເຊິ່ງ<span class="ez-toc-section-end"></span></h4>



<p>ຈຸດຫັນປ່ຽນອັນໃຫຍ່ຫຼວງມາພ້ອມກັບການມາເຖິງຂອງການຮຽນຮູ້ເລິກເຊິ່ງ ແລະເຄືອຂ່າຍ neural, ເຊິ່ງເຮັດໃຫ້ມັນເປັນໄປໄດ້ທີ່ຈະສ້າງ AIs ທົ່ວໄປຫຼາຍຂື້ນທີ່ສາມາດຮຽນຮູ້ເກມຕ່າງໆໄດ້ຢ່າງມີປະສິດທິພາບທີ່ຫນ້າປະຫລາດໃຈ. ລະບົບເຊັ່ນ <strong>AlphaGo</strong> ຂອງ <strong>DeepMind</strong>, ຂໍຂອບໃຈກັບສະຖາປັດຕະຍະກໍາເຄືອຂ່າຍ neural ຂອງເຂົາເຈົ້າແລະການຮຽນຮູ້ການເສີມສ້າງ, ໄດ້ບັນລຸຜົນຂອງການຕີແຊ້ມໃນເກມ Go, ພາກສະຫນາມທີ່ intuition ຂອງມະນຸດຖືວ່າເປັນສິ່ງຈໍາເປັນ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%88%E0%BA%B2%E0%BA%81_intuition_%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%A1%E0%BA%B0%E0%BA%99%E0%BA%B8%E0%BA%94%E0%BA%81%E0%BA%B1%E0%BA%9A%E0%BA%8D%E0%BA%B8%E0%BA%94%E0%BA%97%E0%BA%B0%E0%BA%AA%E0%BA%B2%E0%BA%94_AI"></span>ຈາກ intuition ຂອງມະນຸດກັບຍຸດທະສາດ AI<span class="ez-toc-section-end"></span></h4>



<p>ນອກຈາກນີ້, ການນໍາແນວຄວາມຄິດຂອງ intuition ເຂົ້າໄປໃນປັນຍາປະດິດແມ່ນການຕັດສິນໃຈ. AI ໄດ້ເລີ່ມຕົ້ນທີ່ຈະ &#8216;ເຂົ້າໃຈ&#8217; ຮູບແບບທີ່ຊັບຊ້ອນແລະຍຸດທະສາດໂດຍບໍ່ມີການວາງແຜນຢ່າງຈະແຈ້ງເພື່ອເຮັດແນວນັ້ນ. ນາງໄດ້ພັດທະນາຮູບແບບການຫຼີ້ນແບບປະດິດສ້າງ, ເຊິ່ງບໍ່ເຄີຍຮູ້ຈັກມາກ່ອນ, ພິສູດຄວາມສາມາດໃນການປະດິດສ້າງແລະພັດທະນາຢ່າງເປັນເອກະລາດ.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="The_Duel_at_the_Summit_%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%A7%E0%BA%B4%E0%BB%80%E0%BA%84%E0%BA%B2%E0%BA%B0%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%97%E0%BA%B5%E0%BB%88%E0%BA%AA%E0%BA%B1%E0%BB%88%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BB%80%E0%BA%97%E0%BA%B7%E0%BA%AD%E0%BA%99%E0%BB%82%E0%BA%A5%E0%BA%81%E0%BA%82%E0%BA%AD%E0%BA%87_Go"></span>The Duel at the Summit: ການວິເຄາະເກມທີ່ສັ່ນສະເທືອນໂລກຂອງ Go<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1.png" alt="" class="wp-image-812" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1.png 1792w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1-300x171.png 300w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1-1024x585.png 1024w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1-150x86.png 150w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1-768x439.png 768w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>ການພົບກັນລະຫວ່າງປັນຍາປະດິດ <strong>AlphaGo</strong> ແລະຜູ້ຫຼິ້ນ Go ມືອາຊີບເກົາຫຼີໃຕ້, Lee Sedol, ເປັນຈຸດປ່ຽນທາງປະຫວັດສາດໃນພາກສະຫນາມຂອງປັນຍາປະດິດແລະເກມຍຸດທະສາດບັນພະບຸລຸດຂອງ Go. ການປະເຊີນຫນ້າກັບ epic ນີ້, ເຊິ່ງໄດ້ຈັດຂຶ້ນໃນເດືອນມີນາ 2016, ໄດ້ມີຜົນກະທົບທົ່ວໂລກ, ເປັນພະຍານເຖິງຄວາມປະທັບໃຈ. ຄວາມຄືບຫນ້າຂອງເຄື່ອງຈັກໃນຄວາມສາມາດຂອງເຂົາເຈົ້າກັບຕົ້ນສະບັບເກມໃນເມື່ອກ່ອນຖືວ່າເປັນການຮັກສາປັນຍາຂອງມະນຸດ. ເບິ່ງລາຍລະອຽດໃນສ່ວນນີ້ທີ່ສັ່ນສະເທືອນທັງໂລກຂອງ Go ແລະເຕັກໂນໂລຢີ.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BB%80%E0%BA%9B%E0%BA%B1%E0%BA%99%E0%BA%AA%E0%BA%B1%E0%BA%94%E0%BA%95%E0%BA%B9%E0%BA%81%E0%BA%B1%E0%BA%99%E0%BA%97%E0%BA%B2%E0%BA%87%E0%BA%9B%E0%BA%B0%E0%BA%AB%E0%BA%A7%E0%BA%B1%E0%BA%94%E0%BA%AA%E0%BA%B2%E0%BA%94_AlphaGo_%E0%BA%97%E0%BA%BD%E0%BA%9A%E0%BA%81%E0%BA%B1%E0%BA%9A_Lee_Sedol"></span>ການເປັນສັດຕູກັນທາງປະຫວັດສາດ: AlphaGo ທຽບກັບ Lee Sedol<span class="ez-toc-section-end"></span></h3>



<p>Lee Sedol, ມັກຈະອ້າງເຖິງບັນດາຜູ້ຫຼິ້ນ Go ໃນຍຸກປະຈຸບັນທີ່ຍິ່ງໃຫຍ່ທີ່ສຸດ, ໄດ້ປະເຊີນຫນ້າກັບ opponent ຂອງລັກສະນະທີ່ແຕກຕ່າງກັນທັງຫມົດ: <strong>AlphaGo</strong>, ພັດທະນາໂດຍ <strong>DeepMind</strong>, ບໍລິສັດຍ່ອຍຂອງ Google ທີ່ຊ່ຽວຊານໃນ AI. AlphaGo ເປັນໂປຣແກມຄອມພິວເຕີອັດສະລິຍະປັນຍາປະດິດ ເຊິ່ງເປົ້າໝາຍແມ່ນເພື່ອຈຳລອງຄວາມສາມາດໃນການຕັດສິນໃຈຂອງມະນຸດໃນຄວາມສັບສົນຂອງເກມ Go.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%81%E0%BA%B0%E0%BA%81%E0%BA%BD%E0%BA%A1%E0%BA%AA%E0%BB%8D%E0%BA%B2%E0%BA%A5%E0%BA%B1%E0%BA%9A_AlphaGo_Beyond_Classic_Programming"></span>ການກະກຽມສໍາລັບ AlphaGo: Beyond Classic Programming<span class="ez-toc-section-end"></span></h4>



<p>ການ​ກະ​ກຽມ​ຂອງ​<strong>AlphaGo</strong> ສໍາລັບການແຂ່ງຂັນນີ້ແມ່ນບໍ່ສາມາດປຽບທຽບກັບວິທີການຄລາສສິກຂອງບັນດາໂຄງການຄອມພິວເຕີ. ແທນທີ່ຈະອີງໃສ່ພຽງແຕ່ການເຄື່ອນໄຫວການຂຽນໂປລແກລມໂດຍອີງໃສ່ຫລາຍພັນເກມທີ່ບັນທຶກໄວ້, AlphaGo ໃຊ້ເຕັກນິກການຮຽນຮູ້ເລິກແລະເຄືອຂ່າຍ neural ເພື່ອປັບປຸງທັກສະຂອງມັນຢ່າງຕໍ່ເນື່ອງໂດຍການຫຼີ້ນກັບຕົວເອງແລະການຮຽນຮູ້ຂອງແຕ່ລະພາກສ່ວນ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Clash_of_the_Titans_%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%AD%E0%BB%89%E0%BA%B2%E0%BA%87%E0%BA%AD%E0%BA%B5%E0%BA%87"></span>Clash of the Titans: ເກມອ້າງອີງ<span class="ez-toc-section-end"></span></h4>



<p>ເກມທີ່ຈັດຂຶ້ນໃນວັນທີ 9 ມີນາ 2016 ເປັນເກມທໍາອິດຂອງຊຸດຂອງຫ້າ. AlphaGo ໄດ້ເຮັດໃຫ້ໂລກທັງຫມົດແປກໃຈໂດຍການຊະນະການປະເຊີນຫນ້າຄັ້ງທໍາອິດນີ້. ຫຼາຍກວ່າໄຊຊະນະ, ມັນແມ່ນການສະແດງຄວາມສາມາດໃນການຈັບຄູ່ແລະລື່ນກາຍປັນຍາຍຸດທະສາດຂອງມະນຸດ.</p>



<figure class="wp-block-table"><table><tbody><tr><td>ຮອບ</td><td>ເຫດການ</td></tr><tr><td>ເລີ່ມເກມ</td><td>AlphaGo ເປີດເກມທີ່ມີການເຄື່ອນໄຫວທີ່ບໍ່ທໍາມະດາ</td></tr><tr><td>ກາງເກມ</td><td>ຍ້າຍ 37, AlphaGo ປະຫລາດໃຈກັບຍຸດທະສາດນະວັດກໍາ</td></tr><tr><td>ສິ້ນສຸດເກມ</td><td>Lee Sedol ຍອມຈຳນົນ ຫຼັງຈາກການຕໍ່ສູ້ຢ່າງດຸເດືອດ</td></tr></tbody></table><figcaption class="wp-element-caption">ຕາຕະລາງສະຫຼຸບຂອງເກມ AI vs Go champion<br> </figcaption></figure>



<p>ການເຄື່ອນໄຫວຂອງ AlphaGo 37 ແມ່ນໂດດເດັ່ນໂດຍສະເພາະ; ຜູ້ຊ່ຽວຊານໄດ້ກ່າວເຖິງການເຄື່ອນໄຫວ &#8220;ຈາກກາລັກຊີອື່ນ&#8221;, ທີ່ບໍ່ຄາດຄິດຢ່າງສົມບູນສໍາລັບຜູ້ຊ່ຽວຊານດ້ານ Go.<strong>AlphaGo</strong> ອີງໃສ່ການຮຽນຮູ້ເລິກ.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%AD%E0%BA%B0%E0%BA%99%E0%BA%B2%E0%BA%84%E0%BA%BB%E0%BA%94%E0%BA%82%E0%BA%AD%E0%BA%87_Go_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%8D%E0%BA%B8%E0%BA%94%E0%BA%97%E0%BA%B0%E0%BA%AA%E0%BA%B2%E0%BA%94_%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BA%97%E0%BB%89%E0%BA%AD%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BB%84%E0%BA%8A%E0%BA%8A%E0%BA%B0%E0%BA%99%E0%BA%B0%E0%BA%82%E0%BA%AD%E0%BA%87_Super_AI"></span>ອະນາຄົດຂອງ Go ແລະເກມຍຸດທະສາດ: ຜົນສະທ້ອນຂອງໄຊຊະນະຂອງ Super AI<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2.png" alt="" class="wp-image-813" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2.png 1792w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2-300x171.png 300w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2-1024x585.png 1024w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2-150x86.png 150w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2-768x439.png 768w, /images/blog/Le-champion-mondial-du-jeu-de-go-vaincu-par-une-super-IA-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>ອະນາຄົດຂອງ Go, ເປັນເກມກະດານບັນພະບຸລຸດທີ່ຮູ້ຈັກກັບຄວາມຊັບຊ້ອນທາງດ້ານຍຸດທະສາດ, ໄດ້ຖືກປ່ຽນແປງຢ່າງໃຫຍ່ຫຼວງ ຫຼັງຈາກໄດ້ຮັບໄຊຊະນະຢ່າງລົ້ນເຫຼືອຂອງ Artificial Super Intelligence (AI) ຕໍ່ກັບຜູ້ຫຼິ້ນມະນຸດທີ່ດີທີ່ສຸດໃນໂລກ. ເຫດການທີ່ໂດດເດັ່ນແມ່ນໄຊຊະນະຂອງ AI <strong>AlphaGo</strong> ຂອງ <strong>DeepMind</strong> ຕໍ່ກັບແຊ້ມໂລກ Lee Sedol ໃນປີ 2016. ການສະແດງທີ່ຫນ້າປະທັບໃຈນີ້ບໍ່ພຽງແຕ່ພິສູດຄວາມສາມາດພິເສດຂອງ AI ໃນເກມຍຸດທະສາດ, ແຕ່ຍັງໄດ້ປູທາງໃຫ້ຄວາມຄິດເລິກເຊິ່ງກ່ຽວກັບອະນາຄົດຂອງຄວາມບັນເທີງທາງປັນຍາເຫຼົ່ານີ້. ໃຫ້ກວດເບິ່ງຜົນກະທົບຂອງຄວາມກ້າວຫນ້າທາງດ້ານເຕັກໂນໂລຢີນີ້.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AE%E0%BA%BD%E0%BA%99%E0%BA%AE%E0%BA%B9%E0%BB%89%E0%BB%80%E0%BA%AA%E0%BA%B5%E0%BA%A1_%E0%BB%81%E0%BA%A5%E0%BA%B0%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BA%97%E0%BB%89%E0%BA%AD%E0%BA%99%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%A1%E0%BA%B1%E0%BA%99"></span>ການຮຽນຮູ້ເສີມ ແລະຜົນສະທ້ອນຂອງມັນ<span class="ez-toc-section-end"></span></h3>



<p>ໄຊຊະນະຂອງ<strong>AlphaGo</strong> ເປັນໄປໄດ້ໂດຍຜ່ານການຮຽນຮູ້ເສີມ, ເຕັກນິກ AI ທີ່ຕົວແທນຮຽນຮູ້ທີ່ຈະຕັດສິນໃຈທີ່ດີທີ່ສຸດໂດຍການປະຕິບັດທີ່ເພີ່ມລາງວັນສະສົມ. ຜົນສະທ້ອນແມ່ນກວ້າງຂວາງ:</p>



<ul class="wp-block-list">
<li><strong>ປັບປຸງສູດການຄິດໄລ່</strong> : ໂຄງການ AI ຈະສືບຕໍ່ປັບປຸງ, ເຮັດໃຫ້ເກມຂອງ Go, ເຊັ່ນດຽວກັນກັບເກມຍຸດທະສາດອື່ນໆ, ການແຂ່ງຂັນກັບປັນຍາປະດິດເພີ່ມຂຶ້ນ.</li>



<li><strong>ການປັບແຕ່ງການອອກກຳລັງກາຍ</strong> : AIs ສາມາດເປັນຄູຝຶກສອນສ່ວນບຸກຄົນໃຫ້ກັບຜູ້ຫຼິ້ນ, ປັບຕົວເຂົ້າກັບທັກສະ ແລະຮູບແບບການຫຼິ້ນຂອງເຂົາເຈົ້າ.</li>



<li><strong>ນະວັດຕະກໍາ tactical</strong> : AIs ສາມາດເປີດເຜີຍຍຸດທະສາດ ແລະຍຸດທະວິທີໃໝ່ໆທີ່ມະນຸດບໍ່ເຄີຍສຳຫຼວດມາກ່ອນ, ດັ່ງນັ້ນຈຶ່ງມີສ່ວນຮ່ວມໃນການວິວັດທະນາການຂອງເກມເອງ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%AD%E0%BA%B0%E0%BA%99%E0%BA%B2%E0%BA%84%E0%BA%BB%E0%BA%94%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BB%81%E0%BA%82%E0%BB%88%E0%BA%87%E0%BA%82%E0%BA%B1%E0%BA%99%E0%BB%80%E0%BA%81%E0%BA%A1%E0%BA%8D%E0%BA%B8%E0%BA%94%E0%BA%97%E0%BA%B0%E0%BA%AA%E0%BA%B2%E0%BA%94"></span>ອະນາຄົດຂອງການແຂ່ງຂັນເກມຍຸດທະສາດ<span class="ez-toc-section-end"></span></h4>



<p>ໄຊຊະນະຂອງ AI ໃນເກມຍຸດທະສາດຮຽກຮ້ອງຄວາມສົນໃຈຂອງການແຂ່ງຂັນແບບດັ້ງເດີມ. ນີ້ແມ່ນບາງເສັ້ນທາງທີ່ເປັນໄປໄດ້ສໍາລັບອະນາຄົດ:</p>



<ul class="wp-block-list">
<li><strong>ມະນຸດກັບການແຂ່ງຂັນ AI</strong> : ການຈັບຄູ່ທີ່ມະນຸດປະເຊີນກັບ AI ສາມາດກາຍເປັນມາດຕະຖານໃຫມ່, ດຶງດູດຄວາມສົນໃຈກັບວິທີທີ່ມະນຸດປັບຕົວແລະປະຕິກິລິຍາກັບຍຸດທະສາດ AI.</li>



<li><strong>ການ​ພັດ​ທະ​ນາ​ຮູບ​ແບບ​ການ​ແຂ່ງ​ຂັນ​</strong> : ການແນະນໍາປະເພດແຍກຕ່າງຫາກສໍາລັບ AIs ແລະມະນຸດ, ຫຼືການສ້າງການແຂ່ງຂັນແບບປະສົມເພື່ອປະເມີນການຮ່ວມມືລະຫວ່າງມະນຸດແລະ AI.</li>



<li>ການສຶກສາ ແລະການຝຶກອົບຮົມຂອງຜູ້ຫຼິ້ນສາມາດແຍກອອກຈາກເຄື່ອງມືປັນຍາປະດິດ, ການປ່ຽນແປງວິທີການຮຽນຮູ້ຂອງນັກຍຸດທະສາດໃນມື້ອື່ນ Go ແລະເກມທີ່ຄ້າຍຄືກັນອື່ນໆ.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%81%E0%BA%B0%E0%BA%97%E0%BA%BB%E0%BA%9A%E0%BA%95%E0%BB%8D%E0%BB%88%E0%BA%81%E0%BA%B2%E0%BA%99%E0%BA%AD%E0%BA%AD%E0%BA%81%E0%BB%81%E0%BA%9A%E0%BA%9A%E0%BB%80%E0%BA%81%E0%BA%A1"></span>ຜົນກະທົບຕໍ່ການອອກແບບເກມ<span class="ez-toc-section-end"></span></h4>



<p>ຄວາມສຳເລັດຂອງ AI ໃນເກມຍຸດທະສາດຍັງມີອິດທິພົນຕໍ່ວິທີທີ່ເກມຖືກອອກແບບ ແລະຫຼິ້ນ:</p>



<figure class="wp-block-table"><table><tbody><tr><td>ຮູບລັກສະນະ</td><td>ຜົນກະທົບ</td></tr><tr><td>ຄວາມ​ສັບ​ສົນ​ຂອງ​ເກມ​</td><td>ເກມອາດຈະສັບສົນຂຶ້ນເພື່ອສະຫນອງສິ່ງທ້າທາຍໃຫມ່ສໍາລັບ AI ແລະເຮັດໃຫ້ຜູ້ຫຼິ້ນຂອງມະນຸດມີຄວາມສົນໃຈ.</td></tr><tr><td>ການປັບແຕ່ງສ່ວນຕົວ</td><td>ເກມສາມາດສະຫນອງການປັບແຕ່ງທີ່ເລິກເຊິ່ງເຮັດໃຫ້ AIs ສາມາດສ້າງປະສົບການທີ່ເປັນເອກະລັກສໍາລັບຜູ້ຫຼິ້ນແຕ່ລະຄົນ.</td></tr></tbody></table></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E0%BA%9C%E0%BA%BB%E0%BA%99%E0%BA%AA%E0%BA%B0%E0%BA%97%E0%BB%89%E0%BA%AD%E0%BA%99%E0%BA%95%E0%BB%8D%E0%BB%88%E0%BA%AA%E0%BA%B1%E0%BA%87%E0%BA%84%E0%BA%BB%E0%BA%A1%E0%BA%82%E0%BA%AD%E0%BA%87%E0%BB%80%E0%BA%81%E0%BA%A1"></span>ຜົນສະທ້ອນຕໍ່ສັງຄົມຂອງເກມ<span class="ez-toc-section-end"></span></h4>



<p>ສຸດທ້າຍ, ມັນເປັນສິ່ງຈໍາເປັນທີ່ຈະພິຈາລະນາຜົນກະທົບທາງສັງຄົມຂອງຄວາມກ້າວຫນ້ານີ້. ເກມຍັງເປັນວິທີການສ້າງຄວາມສໍາພັນ, ພັດທະນາຈິດໃຈການແຂ່ງຂັນແລະມີຄວາມມ່ວນ. ການໃສ່ AI ເຂົ້າໄປໃນກອບນີ້ສາມາດ:</p>



<ul class="wp-block-list">
<li>ປ່ຽນວິທີທີ່ຊຸມຊົນເກມມີປະຕິສຳພັນ ແລະພົບປະກັນ.</li>



<li>ແນະນໍາອົງປະກອບຂອງການຮ່ວມມືລະຫວ່າງມະນຸດກັບ AI, ດັ່ງນັ້ນການເພີ່ມລະດັບການຫຼິ້ນ ແລະປະສົບການລວມ.</li>
</ul>



<p>ໄຊຊະນະຂອງ <strong>AlphaGo</strong> ຂອງ <strong>DeepMind</strong> ບໍ່ພຽງແຕ່ໄດ້ປະຕິວັດເກມ Go ເທົ່ານັ້ນ, ແຕ່ມັນຍັງຊີ້ໃຫ້ເຫັນເຖິງທ່າແຮງຂອງ AIs ພິເສດໃນເກມຍຸດທະສາດ ແລະ ສະເໜີໃຫ້ເຫັນຜົນສະທ້ອນຫຼາຍຢ່າງຕໍ່ກັບອະນາຄົດຂອງກິດຈະກໍາທາງປັນຍາເຫຼົ່ານີ້. ການສືບຕໍ່ປະດິດສ້າງໃນ AI ສັນຍາວ່າຈະຫັນປ່ຽນບໍ່ພຽງແຕ່ວິທີການທີ່ພວກເຮົາຫຼິ້ນ, ແຕ່ຍັງວິທີການທີ່ພວກເຮົາຄິດກ່ຽວກັບຍຸດທະສາດໂດຍທົ່ວໄປ.</p>



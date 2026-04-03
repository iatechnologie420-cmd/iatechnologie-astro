---

title: "Изучите оперативное проектирование: за 12 шагов"
slug: "article-76"
excerpt: "Введение в оперативный инжиниринг Что такое оперативный инжиниринг? ТО Оперативное проектирование — это новая область, которая фокусируется на оптимизации подсказок или команд, которые мы отдаем системам искусственного интеллекта (ИИ), особенно тем, которые основаны на естественном языке, например, генераторам текста. Это особенно важная дисциплина с появлением таких моделей обработки языка, как GPT-4. ОпенАИ. Идея состоит в [&hellip;]"
date: "2024-03-09T12:53:21"
featuredImage: "/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-3.png"
categories: ["%d0%be%d0%b1%d1%83%d1%87%d0%b5%d0%bd%d0%b8%d0%b5-%d0%b8-%d0%be%d1%81%d0%bd%d0%be%d0%b2%d1%8b-%d0%b8%d1%81%d0%ba%d1%83%d1%81%d1%81%d1%82%d0%b2%d0%b5%d0%bd%d0%bd%d0%be%d0%b3%d0%be-%d0%b8%d0%bd%d1%82"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B6%D0%B8%D0%BD%D0%B8%D1%80%D0%B8%D0%BD%D0%B3" >Введение в оперативный инжиниринг</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%A7%D1%82%D0%BE_%D1%82%D0%B0%D0%BA%D0%BE%D0%B5_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B6%D0%B8%D0%BD%D0%B8%D1%80%D0%B8%D0%BD%D0%B3" >Что такое оперативный инжиниринг?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83_%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5" >Почему важно оперативное проектирование?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%9A%D0%B0%D0%BA_%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82_%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F" >Как работает Оперативная инженерия</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0_%D0%B8_%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" >Передовая практика и техника оперативного проектирования</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%A4%D1%83%D0%BD%D0%B4%D0%B0%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F" >Фундаментальные принципы оперативного проектирования</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%9F%D0%BE%D0%B9%D0%BC%D0%B8%D1%82%D0%B5_%D0%B7%D0%BD%D0%B0%D1%87%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C_%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0" >Поймите значимость контекста</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%A3%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D1%82%D0%B5_%D0%BD%D0%B0%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F" >Уточните намерение пользователя</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B8_%D0%BF%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8" >Структурирование и приоритезация информации</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%92%D1%8B%D0%B1%D0%BE%D1%80_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_%D0%B8_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8" >Выбор языка и формулировки</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%98%D1%82%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B8_%D0%BF%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%BD%D0%BE%D0%B5_%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B5%D0%BD%D0%B8%D0%B5" >Итеративное использование и постоянное улучшение</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B0%D1%82%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%BC%D0%B8_%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B0%D0%BC%D0%B8" >Управление атипичными результатами</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/ru/%d0%b8%d0%b7%d1%83%d1%87%d0%b8%d1%82%d0%b5-%d0%be%d0%bf%d0%b5%d1%80%d0%b0%d1%82%d0%b8%d0%b2%d0%bd%d0%be%d0%b5-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d0%bd%d0%b8%d0%b5/#%D0%97%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D0%BE%D0%B9_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8_%D0%98%D0%98" >Знание используемой модели ИИ</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B6%D0%B8%D0%BD%D0%B8%D1%80%D0%B8%D0%BD%D0%B3"></span>Введение в оперативный инжиниринг<span class="ez-toc-section-end"></span></h2>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A7%D1%82%D0%BE_%D1%82%D0%B0%D0%BA%D0%BE%D0%B5_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B6%D0%B8%D0%BD%D0%B8%D1%80%D0%B8%D0%BD%D0%B3"></span>Что такое оперативный инжиниринг?<span class="ez-toc-section-end"></span></h3>



<p>    ТО <strong>Оперативное проектирование</strong> — это новая область, которая фокусируется на оптимизации подсказок или команд, которые мы отдаем системам искусственного интеллекта (ИИ), особенно тем, которые основаны на естественном языке, например, генераторам текста. Это особенно важная дисциплина с появлением таких моделей обработки языка, как GPT-4. <strong>ОпенАИ</strong>. Идея состоит в том, чтобы научиться эффективно «разговаривать» с этими ИИ, чтобы улучшить качество и актуальность получаемых ответов.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9F%D0%BE%D1%87%D0%B5%D0%BC%D1%83_%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5"></span>Почему важно оперативное проектирование?<span class="ez-toc-section-end"></span></h4>



<p>Роль <strong>Оперативное проектирование</strong> имеет решающее значение, потому что то, как вы формулируете команду ИИ, может сильно варьировать результаты. Например, плохо продуманные подсказки могут привести к неточным ответам или ответам не по теме, тогда как хорошо продуманные подсказки могут повысить точность и актуальность генерируемой информации. Оперативные инженерные эксперты работают над уточнением формулировок вопросов для получения точных и полезных результатов.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D0%B0%D0%BA_%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82_%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F_%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F"></span>Как работает Оперативная инженерия<span class="ez-toc-section-end"></span></h4>



<p> Процесс разработки подсказок предполагает глубокое понимание того, как работают модели ИИ, такие как нейронные сети, и использование этого понимания для разработки подсказок, которые используют преимущества возможностей ИИ и одновременно обходят его ограничения. Это может потребовать некоторой креативности, большого количества экспериментов и тщательного анализа результатов для итеративного уточнения подсказок.</p>



<p>Искусство <strong>Оперативное проектирование</strong> представляет собой важный навык для любого, кто стремится эффективно взаимодействовать с самыми передовыми системами искусственного интеллекта. Понимание и применение принципов оперативного проектирования может значительно улучшить качество и эффективность нашего взаимодействия с технологиями на основе искусственного интеллекта.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0_%D0%B8_%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></span>Передовая практика и техника оперативного проектирования<span class="ez-toc-section-end"></span></h4>



<p>Искусство оперативной разработки ИИ, генерирующих контент и изображения, таких как OpenAI и MidJourney, требует сочетания методов и лучших практик для достижения качественных результатов. Вот некоторые из этих лучших практик и методов:</p>



<ol class="wp-block-list">
<li><strong>Используя примеры:</strong> Включение образцов запросов и ответов в ваши подсказки может привести к тому, что модель будет реагировать желаемым образом, используя методы однократного или малократного обучения для повышения точности ответа модели.</li>



<li><strong>Обратите внимание на подсказки:</strong> Включение подсказок в подсказку может помочь модели генерировать выходные данные, соответствующие вашим намерениям. Это может быть особенно полезно для направления модели на желаемый ответ.</li>



<li><strong>Протестируйте различные варианты:</strong> Порядок представления информации в подсказке может влиять на выходные данные модели. Полезно поэкспериментировать с различным расположением инструкций, основного содержания, примеров и подсказок.</li>



<li><strong>Предоставьте «выход» модели:</strong> Иногда у модели могут возникнуть трудности с точным выполнением задачи. Чтобы смягчить это, предоставьте альтернативные пути или инструкции, которым модель должна следовать, если она не может найти удовлетворительный ответ.</li>



<li><strong>Следите за длиной:</strong> В подсказках могут быть ограничения на количество символов. Слишком длинные запросы могут быть трудными для обработки системами искусственного интеллекта.</li>



<li><strong>Тщательно подбирайте слова:</strong> Наиболее эффективные подсказки используют ясный и прямой язык. Избегайте двусмысленности, красочного языка, метафор и сленга.</li>



<li><strong>Задавайте открытые вопросы:</strong> Открытые вопросы обеспечивают большую гибкость в результатах. Например, запрос на описание сложных факторов с большей вероятностью вызовет подробный и исчерпывающий ответ.</li>



<li><strong>Включить контекст:</strong> Хорошо продуманные подсказки часто включают контекст, который помогает системе ИИ адаптировать вывод к целевой аудитории пользователя.</li>



<li><strong>Установите цели или ограничения длины вывода:</strong> Хотя ИИ создан для творчества, зачастую полезно предусмотреть ограничения по таким факторам, как длина вывода.</li>



<li><strong>Избегайте противоречивых терминов:</strong> Длинные и сложные подсказки могут включать неоднозначные или противоречивые термины. Убедитесь, что все условия совпадают.</li>



<li><strong>Используйте знаки препинания, чтобы уточнить сложные подсказки:</strong> Точно так же, как люди полагаются на пунктуацию при интерпретации текста, подсказки ИИ также могут выиграть от разумного использования запятых, кавычек и разрывов строк.</li>
</ol>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A4%D1%83%D0%BD%D0%B4%D0%B0%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F"></span>Фундаментальные принципы оперативного проектирования<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering.png" alt="" class="wp-image-1714" srcset="/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering.png 1792w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-300x171.png 300w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-1024x585.png 1024w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-150x86.png 150w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-768x439.png 768w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9F%D0%BE%D0%B9%D0%BC%D0%B8%D1%82%D0%B5_%D0%B7%D0%BD%D0%B0%D1%87%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C_%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%B0"></span>Поймите значимость контекста<span class="ez-toc-section-end"></span></h3>



<p>Важнейший принцип <strong>оперативное проектирование</strong> это понимание контекста, в котором сделан запрос. Как и в человеческом разговоре, контекст сильно влияет на смысл и актуальность ответов. Это означает, что подсказки должны быть разработаны таким образом, чтобы учитывать конкретную среду, цели пользователя и точную область применения.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A3%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D1%82%D0%B5_%D0%BD%D0%B0%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F"></span>Уточните намерение пользователя<span class="ez-toc-section-end"></span></h4>



<p>Ясность намерений в подсказке имеет решающее значение для получения соответствующего ответа от ИИ. Важно, чтобы подсказка была как можно более точной, чтобы свести к минимуму двусмысленность. Иногда это означает перефразирование или добавление деталей, которые направляют ИИ к более точному пониманию того, что ищет пользователь.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B8_%D0%BF%D1%80%D0%B8%D0%BE%D1%80%D0%B8%D1%82%D0%B5%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8"></span>Структурирование и приоритезация информации<span class="ez-toc-section-end"></span></h4>



<p>То, как структурировано приглашение, может оказать огромное влияние на качество получаемого ответа. Это включает в себя определение приоритетности информации логическим и последовательным образом, чтобы ИИ мог эффективно обрабатывать запрос, и структурирование запроса так, чтобы наиболее важные элементы были выделены, тем самым направляя ИИ к адекватному ответу.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%92%D1%8B%D0%B1%D0%BE%D1%80_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_%D0%B8_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8"></span>Выбор языка и формулировки<span class="ez-toc-section-end"></span></h4>



<p>Выбранные слова, стиль языка и общая формулировка подсказки играют важную роль в разработке подсказки. Четкий и точный язык, адаптированный к рассматриваемой модели ИИ, имеет важное значение. Например, некоторые модели более чувствительны к естественному языку, тогда как другие требуют более формальной или технической формулировки.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%98%D1%82%D0%B5%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B8_%D0%BF%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%BD%D0%BE%D0%B5_%D1%83%D0%BB%D1%83%D1%87%D1%88%D0%B5%D0%BD%D0%B8%D0%B5"></span>Итеративное использование и постоянное улучшение<span class="ez-toc-section-end"></span></h4>



<p>ТО <strong>оперативное проектирование</strong> часто является итеративным процессом. Нередко приходится несколько раз корректировать подсказки, прежде чем получить желаемый ответ. Анализ ответов ИИ и уточнение подсказок на основе этих ответов — важная часть процесса разработки подсказок.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B0%D1%82%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%BC%D0%B8_%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B0%D0%BC%D0%B8"></span>Управление атипичными результатами<span class="ez-toc-section-end"></span></h4>



<p>Очень важно знать, как обрабатывать неожиданные или нетипичные результаты, которые могут возникнуть даже при хорошо продуманной подсказке. Это включает в себя возможность диагностировать причины таких результатов и перефразировать подсказки для устранения проблемы.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%97%D0%BD%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D0%BE%D0%B9_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D0%B8_%D0%98%D0%98"></span>Знание используемой модели ИИ<span class="ez-toc-section-end"></span></h4>



<p>Наконец, фундаментальное значение имеет глубокое понимание модели ИИ, с которой вы работаете. Знание его сильных сторон, ограничений и того, как он обрабатывает подсказки, имеет решающее значение для формулирования подсказок, которые будут эффективно интерпретироваться и выполняться ИИ.</p>



<p>Таким образом, вы поймете, что <strong>оперативное проектирование</strong> становится все более важным навыком по мере того, как технологии искусственного интеллекта становятся все более сложными и интегрированы в нашу повседневную жизнь. Поэтому начните устанавливать его как можно быстрее.</p>



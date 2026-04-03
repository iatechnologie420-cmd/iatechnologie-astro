---

title: "Dompdf: Како да креирате елегантни PDF-датотеки во PHP?"
slug: "dompdf-pdf"
excerpt: "Вовед во Dompdf Dompdf е PHP библиотека која ви овозможува да генерирате PDF датотеки од HTML содржина. Ова решение е многу корисно за генерирање извештаи, фактури или кој било друг документ во PDF формат. Во оваа статија, ќе ги откриеме основните карактеристики на Dompdf и ќе научиме како да го користиме за да креираме елегантни [&hellip;]"
date: "2024-03-09T12:41:57"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%d0%bf%d1%80%d0%b5%d1%81%d0%bc%d0%b5%d1%82%d1%83%d0%b2%d0%b0%d1%9a%d0%b5-%d0%b8-%d0%bf%d0%be%d0%b4%d0%b0%d1%82%d0%be%d1%86%d0%b8-mk", "%d1%82%d0%b5%d1%85%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d1%98%d0%b0-%d0%b8-%d0%b4%d0%b8%d0%b3%d0%b8%d1%82%d0%b0%d0%bb%d0%bd%d0%b0-mk"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%92%D0%BE%D0%B2%D0%B5%D0%B4_%D0%B2%D0%BE_Dompdf" >Вовед во Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%9F%D1%80%D0%B5%D0%B4%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8" >Предуслови</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%98%D0%BD%D1%81%D1%82%D0%B0%D0%BB%D0%B0%D1%86%D0%B8%D1%98%D0%B0_%D0%BD%D0%B0_Dompdf" >Инсталација на Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%9C%D0%BE%D1%98%D0%BE%D1%82_%D0%BF%D1%80%D0%B2_PDF_%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D1%81%D0%BE_Dompdf" >Мојот прв PDF документ со Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%9A%D1%80%D0%B5%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%BD%D0%B0_%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BD_PDF_%D0%B2%D0%BE_PHP" >Креирање на елегантен PDF во PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%94%D1%80%D1%83%D0%B3_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4_%D0%B7%D0%B0_%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BB%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%B8_%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B5%D1%9A%D0%B5_%D0%BD%D0%B0_Dompdf" >Друг метод за инсталирање и користење на Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%9A%D1%80%D0%B5%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_PDF_%D0%BE%D0%B4_HTML_%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD" >Креирање PDF од HTML шаблон</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D1%83%D0%B2%D0%B0%D1%9A%D0%B5_%D1%81%D0%BE_%D1%81%D0%BB%D0%B8%D0%BA%D0%B8_%D0%B8_%D1%84%D0%BE%D0%BD%D1%82%D0%BE%D0%B2%D0%B8" >Управување со слики и фонтови</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/mk/dompdf-%d0%ba%d0%b0%d0%ba%d0%be-%d0%b4%d0%b0-%d0%ba%d1%80%d0%b5%d0%b8%d1%80%d0%b0%d1%82%d0%b5-%d0%b5%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d0%b8-pdf-%d0%b4%d0%b0%d1%82%d0%be%d1%82%d0%b5%d0%ba/#%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%BD%D0%B0_%D1%80%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%B8_%D0%BF%D0%BE%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0_%D0%BD%D0%B0_%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B8_%D1%81%D0%BE_Dompdf" >Оптимизирање на рендерирање и поправка на проблеми со Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D0%92%D0%BE%D0%B2%D0%B5%D0%B4_%D0%B2%D0%BE_Dompdf"></span>Вовед во Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf е PHP библиотека која ви овозможува да генерирате PDF датотеки од HTML содржина. Ова решение е многу корисно за генерирање извештаи, фактури или кој било друг документ во PDF формат. Во оваа статија, ќе ги откриеме основните карактеристики на Dompdf и ќе научиме како да го користиме за да креираме елегантни и функционални PDF-датотеки.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9F%D1%80%D0%B5%D0%B4%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8"></span>Предуслови<span class="ez-toc-section-end"></span></h3>



<p>Пред да го инсталирате Dompdf, проверете дали го имате следново:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf бара PHP >= 5.4. Компатибилен е со верзиите 7.x на PHP.</li>



<li><strong>PHP екстензии:</strong> Проверете дали сте ги овозможиле следните PHP екстензии: mbstring, DOM и GD. Овие екстензии се неопходни за правилно функционирање на Dompdf.</li>



<li><strong>Состави:</strong> Dompdf се дистрибуира преку Composer, кој е менаџер за зависност за PHP. Проверете дали имате инсталирано Composer на вашиот систем.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%98%D0%BD%D1%81%D1%82%D0%B0%D0%BB%D0%B0%D1%86%D0%B8%D1%98%D0%B0_%D0%BD%D0%B0_Dompdf"></span>Инсталација на Dompdf<span class="ez-toc-section-end"></span></h4>



<p>За да инсталирате Dompdf, следете ги следниве чекори:</p>



<ol class="wp-block-list">
<li><strong>Создадете нов PHP проект:</strong> Ако веќе немате постоечки проект, креирајте нов користејќи ја основната структура по ваш избор.</li>



<li><strong>Додајте ја зависноста од Dompdf преку Composer:</strong> Отворете конзола и одете до директориумот на вашиот проект. Извршете ја следнава команда за да додадете Dompdf во вашиот проект:     <pre><code>композитор бара dompdf/dompdf</code></pre>     Оваа команда автоматски ќе го преземе и инсталира Dompdf заедно со неговите зависности.</li>



<li><strong>Користете Dompdf во вашата апликација:</strong> Сега можете да го користите Dompdf во вашиот проект. Постојат многу начини да креирате PDF-датотеки со Dompdf, но еве основен пример за да започнете:
<pre><code>// Вклучете го автоматскиот вчитувач на Композиторот
бара 'продавач/автоматско вчитување.php';

// Креирај нов објект Dompdf
$dompdf = нов Dompdf();

// Вчитај HTML содржина од датотека или низа
$html = '<h1><span class="ez-toc-section" id="%D0%9C%D0%BE%D1%98%D0%BE%D1%82_%D0%BF%D1%80%D0%B2_PDF_%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D1%81%D0%BE_Dompdf"></span>Мојот прв PDF документ со Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Рендерирајте го документот PDF
$dompdf->render();

// Испрати PDF документ на излез
$dompdf->stream('document.pdf');</code></pre>
    Овој пример создава нов PDF документ со наслов и го поставува како датотека „document.pdf“. Можете да ја прилагодите содржината на HTML според вашите потреби.</li>
</ol>



<p>Сега кога го имате инсталирано Dompdf, можете да започнете да генерирате елегантни и функционални PDF-датотеки во вашите веб-апликации. Dompdf нуди многу напредни функции за приспособување на рендерирање на PDF, како што се управување со слики, сопствени фонтови и CSS стилови.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D1%80%D0%B5%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%BD%D0%B0_%D0%B5%D0%BB%D0%B5%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BD_PDF_%D0%B2%D0%BE_PHP"></span>Креирање на елегантен PDF во PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%94%D1%80%D1%83%D0%B3_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4_%D0%B7%D0%B0_%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BB%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%B8_%D0%BA%D0%BE%D1%80%D0%B8%D1%81%D1%82%D0%B5%D1%9A%D0%B5_%D0%BD%D0%B0_Dompdf"></span>Друг метод за инсталирање и користење на Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Еве ги чекорите што треба да ги следите:<br>1. Преземете ја најновата верзија на Dompdf од официјалната веб-страница.<br>2. Извлечете ги преземените датотеки и ставете ги во вашиот PHP проект.<br>3. Вклучете ја датотеката Dompdfautoload.php за да ја вчитате библиотеката во вашата PHP скрипта.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9A%D1%80%D0%B5%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_PDF_%D0%BE%D0%B4_HTML_%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD"></span>Креирање PDF од HTML шаблон<span class="ez-toc-section-end"></span></h4>



<p>Сега кога го инсталиравме Dompdf, ќе видиме како да креираме PDF користејќи HTML шаблон. Следете ги овие чекори:</p>



<p>1. Направете HTML-датотека што ги содржи структурата и распоредот што ги сакате за вашиот PDF.<br>2. Користете CSS карактеристики за стилизирање на вашиот документ, користејќи својства како фонт-семејство, големина на фонт, граница итн.<br>3. Вклучете динамички податоци користејќи ознаки специфични за Dompdf, како што се „{{име}}“ или „{{адреса}}“.<br>4. Користете ја класата Dompdf за да генерирате PDF користејќи го HTML шаблонот што сте го создале.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D1%83%D0%B2%D0%B0%D1%9A%D0%B5_%D1%81%D0%BE_%D1%81%D0%BB%D0%B8%D0%BA%D0%B8_%D0%B8_%D1%84%D0%BE%D0%BD%D1%82%D0%BE%D0%B2%D0%B8"></span>Управување со слики и фонтови<span class="ez-toc-section-end"></span></h4>



<p>Кога креирате стилски PDF-датотеки, често е неопходно да се вклучат слики или да се користат специфични фонтови. Еве како да го направите тоа со Dompdf:</p>



<p>1. Вклучете слики во вашиот HTML шаблон користејќи ја ознаката <img decoding="async" src="chemin_vers_image">.<br>2. Имајте предвид дека Dompdf стандардно не ги вклучува сите фонтови. Можете да додавате сопствени фонтови користејќи @font-face во вашиот CSS или користејќи фонтови обезбедени од Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%BD%D0%B0_%D1%80%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D0%B8%D1%80%D0%B0%D1%9A%D0%B5_%D0%B8_%D0%BF%D0%BE%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0_%D0%BD%D0%B0_%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B8_%D1%81%D0%BE_Dompdf"></span>Оптимизирање на рендерирање и поправка на проблеми со Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Понекогаш може да наидете на проблеми со рендерирање на вашиот PDF или генерирање на датотеки. Еве неколку совети за нивно решавање:</p>



<p>1. Проверете дали вашиот HTML шаблон е правилно конструиран и валиден.<br>2. Проверете дали сите надворешни ресурси (слики, фонтови, итн.) се достапни од серверот.<br>3. Дебагирајте го вашиот код со активирање на режимот за отстранување грешки Dompdf и проверка на прикажаните грешки.<br>4. Видете ја документацијата Dompdf за повеќе информации за вообичаените конфигурации и проблеми.</p>



<p>Користејќи го Dompdf, можете да обезбедите подобрено корисничко искуство со доставување професионални и добро форматирани PDF документи. Без разлика дали генерира извештаи, фактури или други видови документи, Dompdf е сигурен и моќен избор.</p>



<p>Како заклучок, инсталирањето на Dompdf е брзо и лесно благодарение на Composer. Откако ќе се инсталира, можете да започнете да создавате висококвалитетни PDF-датотеки за да ги задоволите потребите на вашите веб-апликации. Не заборавајте да ја проверите официјалната документација на Dompdf за да дознаете повеќе за неговите карактеристики и достапните опции за прилагодување.</p>



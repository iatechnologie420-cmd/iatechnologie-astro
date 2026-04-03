---

title: "Dompdf: Как создать элегантные PDF-файлы на PHP?"
slug: "dompdf-pdf-php"
excerpt: "Введение в Домpdf Dompdf — это библиотека PHP, которая позволяет создавать PDF-файлы из HTML-контента. Это решение очень полезно для создания отчетов, счетов-фактур или любого другого документа в формате PDF. В этой статье мы познакомимся с основными функциями Dompdf и узнаем, как использовать его для создания элегантных и функциональных PDF-файлов. Предварительные условия Перед установкой Dompdf убедитесь, [&hellip;]"
date: "2024-03-09T12:43:15"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%d0%b2%d1%8b%d1%87%d0%b8%d1%81%d0%bb%d0%b5%d0%bd%d0%b8%d1%8f-%d0%b8-%d0%b4%d0%b0%d0%bd%d0%bd%d1%8b%d0%b5-ru", "%d1%82%d0%b5%d1%85%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d0%b8-%d0%b8-%d1%86%d0%b8%d1%84%d1%80%d0%be%d0%b2%d1%8b%d0%b5-%d1%82%d0%b5%d1%85%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d0%b8-ru"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D0%94%D0%BE%D0%BCpdf" >Введение в Домpdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%9F%D1%80%D0%B5%D0%B4%D0%B2%D0%B0%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F" >Предварительные условия</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_%D0%94%D0%BE%D0%BC%D0%9F%D0%94%D0%A4" >Установка ДомПДФ</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%9C%D0%BE%D0%B9_%D0%BF%D0%B5%D1%80%D0%B2%D1%8B%D0%B9_PDF-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D1%81_%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E_Dompdf" >Мой первый PDF-документ с помощью Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D1%8D%D0%BB%D0%B5%D0%B3%D0%B0%D0%BD%D1%82%D0%BD%D0%BE%D0%B3%D0%BE_PDF-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0_%D0%BD%D0%B0_PHP" >Создание элегантного PDF-файла на PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%95%D1%89%D0%B5_%D0%BE%D0%B4%D0%B8%D0%BD_%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1_%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8_%D0%B8_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_Dompdf" >Еще один способ установки и использования Dompdf.</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_PDF-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0_%D0%B8%D0%B7_HTML-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B0" >Создание PDF-файла из HTML-шаблона</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%D0%BC%D0%B8_%D0%B8_%D1%88%D1%80%D0%B8%D1%84%D1%82%D0%B0%D0%BC%D0%B8" >Управление изображениями и шрифтами</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ru/dompdf-%d0%ba%d0%b0%d0%ba-%d1%81%d0%be%d0%b7%d0%b4%d0%b0%d1%82%d1%8c-%d1%8d%d0%bb%d0%b5%d0%b3%d0%b0%d0%bd%d1%82%d0%bd%d1%8b%d0%b5-pdf-%d1%84%d0%b0%d0%b9%d0%bb%d1%8b-%d0%bd%d0%b0-php/#%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D0%B8%D0%BD%D0%B3%D0%B0_%D0%B8_%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC_%D1%81_Dompdf" >Оптимизация рендеринга и исправление проблем с Dompdf.</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2_%D0%94%D0%BE%D0%BCpdf"></span>Введение в Домpdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf — это библиотека PHP, которая позволяет создавать PDF-файлы из HTML-контента. Это решение очень полезно для создания отчетов, счетов-фактур или любого другого документа в формате PDF. В этой статье мы познакомимся с основными функциями Dompdf и узнаем, как использовать его для создания элегантных и функциональных PDF-файлов.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9F%D1%80%D0%B5%D0%B4%D0%B2%D0%B0%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5_%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F"></span>Предварительные условия<span class="ez-toc-section-end"></span></h3>



<p>Перед установкой Dompdf убедитесь, что у вас есть следующее:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf требует PHP >= 5.4. Он совместим с версиями PHP 7.x.</li>



<li><strong>Расширения PHP:</strong> Убедитесь, что вы включили следующие расширения PHP: mbstring, DOM и GD. Эти расширения необходимы для правильного функционирования Dompdf.</li>



<li><strong>Составить:</strong> Dompdf распространяется через Composer, который является менеджером зависимостей для PHP. Убедитесь, что в вашей системе установлен Composer.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0_%D0%94%D0%BE%D0%BC%D0%9F%D0%94%D0%A4"></span>Установка ДомПДФ<span class="ez-toc-section-end"></span></h4>



<p>Чтобы установить Dompdf, выполните следующие действия:</p>



<ol class="wp-block-list">
<li><strong>Создайте новый проект PHP:</strong> Если у вас еще нет существующего проекта, создайте новый, используя базовую структуру по вашему выбору.</li>



<li><strong>Добавьте зависимость Dompdf через Composer:</strong> Откройте консоль и перейдите в каталог вашего проекта. Запустите следующую команду, чтобы добавить Dompdf в ваш проект:     <pre><code>композитору требуется dompdf/dompdf</code></pre>     Эта команда автоматически загрузит и установит Dompdf вместе со всеми его зависимостями.</li>



<li><strong>Используйте Dompdf в своем приложении:</strong> Теперь вы можете использовать Dompdf в своем проекте. Существует множество способов создания PDF-файлов с помощью Dompdf, но вот базовый пример, который поможет вам начать:
<pre><code>// Включаем автозагрузчик Composer
требуется «vendor/autoload.php»;

// Создаем новый объект Dompdf
$dompdf = новый Dompdf();

// Загружаем HTML-контент из файла или строки
$html = '<h1><span class="ez-toc-section" id="%D0%9C%D0%BE%D0%B9_%D0%BF%D0%B5%D1%80%D0%B2%D1%8B%D0%B9_PDF-%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82_%D1%81_%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E_Dompdf"></span>Мой первый PDF-документ с помощью Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Отображение PDF-документа
$dompdf->рендер();

// Отправляем PDF-документ на вывод
$dompdf->stream('document.pdf');</code></pre>
    В этом примере создается новый PDF-документ с заголовком и загружается как файл «document.pdf». Вы можете настроить содержимое HTML в соответствии со своими потребностями.</li>
</ol>



<p>Теперь, когда у вас установлен Dompdf, вы можете начать создавать элегантные и функциональные PDF-файлы в своих веб-приложениях. Dompdf предлагает множество расширенных функций для настройки рендеринга PDF, таких как управление изображениями, пользовательскими шрифтами и стилями CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D1%8D%D0%BB%D0%B5%D0%B3%D0%B0%D0%BD%D1%82%D0%BD%D0%BE%D0%B3%D0%BE_PDF-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0_%D0%BD%D0%B0_PHP"></span>Создание элегантного PDF-файла на PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%D0%95%D1%89%D0%B5_%D0%BE%D0%B4%D0%B8%D0%BD_%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1_%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8_%D0%B8_%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F_Dompdf"></span>Еще один способ установки и использования Dompdf.<span class="ez-toc-section-end"></span></h3>



<p>Вот шаги, которые необходимо выполнить:<br>1. Загрузите последнюю версию Dompdf с официального сайта.<br>2. Извлеките загруженные файлы и поместите их в свой проект PHP.<br>3. Включите файл Dompdfautoload.php, чтобы загрузить библиотеку в ваш PHP-скрипт.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_PDF-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0_%D0%B8%D0%B7_HTML-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%B0"></span>Создание PDF-файла из HTML-шаблона<span class="ez-toc-section-end"></span></h4>



<p>Теперь, когда мы установили Dompdf, мы увидим, как создать PDF-файл с использованием шаблона HTML. Следуй этим шагам:</p>



<p>1. Создайте HTML-файл, содержащий нужную структуру и макет вашего PDF-файла.<br>2. Используйте функции CSS для стилизации вашего документа, используя такие свойства, как семейство шрифтов, размер шрифта, граница и т. д.<br>3. Включите динамические данные, используя теги, специфичные для Dompdf, такие как «{{name}}» или «{{address}}».<br>4. Используйте класс Dompdf для создания PDF-файла с использованием созданного вами шаблона HTML.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%A3%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%D0%BC%D0%B8_%D0%B8_%D1%88%D1%80%D0%B8%D1%84%D1%82%D0%B0%D0%BC%D0%B8"></span>Управление изображениями и шрифтами<span class="ez-toc-section-end"></span></h4>



<p>При создании элегантных PDF-файлов часто необходимо включать изображения или использовать определенные шрифты. Вот как это сделать с помощью Dompdf:</p>



<p>1. Включите изображения в свой HTML-шаблон, используя тег <img decoding="async" src="chemin_vers_image">.<br>2. Обратите внимание, что Dompdf по умолчанию включает не все шрифты. Вы можете добавить собственные шрифты, используя @font-face в своем CSS или используя шрифты, предоставленные Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%D0%9E%D0%BF%D1%82%D0%B8%D0%BC%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F_%D1%80%D0%B5%D0%BD%D0%B4%D0%B5%D1%80%D0%B8%D0%BD%D0%B3%D0%B0_%D0%B8_%D0%B8%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC_%D1%81_Dompdf"></span>Оптимизация рендеринга и исправление проблем с Dompdf.<span class="ez-toc-section-end"></span></h4>



<p>Иногда вы можете столкнуться с проблемами при рендеринге PDF-файла или создании файлов. Вот несколько советов по их решению:</p>



<p>1. Убедитесь, что ваш HTML-шаблон правильно построен и действителен.<br>2. Убедитесь, что все внешние ресурсы (изображения, шрифты и т. д.) доступны с сервера.<br>3. Выполните отладку кода, активировав режим отладки Dompdf и проверив отображаемые ошибки.<br>4. Дополнительную информацию об распространенных конфигурациях и проблемах см. в документации Dompdf.</p>



<p>Используя Dompdf, вы можете повысить удобство работы пользователей, предоставляя профессиональные и хорошо отформатированные PDF-документы. Независимо от того, создаете ли вы отчеты, счета-фактуры или другие типы документов, Dompdf — надежный и мощный выбор.</p>



<p>В заключение, установка Dompdf происходит быстро и легко благодаря Composer. После установки вы можете начать создавать высококачественные PDF-файлы для удовлетворения потребностей вашего веб-приложения. Не забудьте ознакомиться с официальной документацией Dompdf, чтобы узнать больше о его функциях и доступных вариантах настройки.</p>



---
title: "Dompdf：如何用 PHP 创建优雅的 PDF？"
slug: "dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2"
excerpt: "Dompdf简介 Dompdf 是一个 PHP 库，允许您从 HTML 内容生成 PDF 文件。该解决方案对于生成 PDF 格式的报告、发票或任何其他文档非常有用。在本文中，我们将了解 Dompdf 的基本功能，并学习如何使用它创建优雅且实用的 PDF。 先决条件 在安装 Dompdf 之前，请确保您具备以下条件： Dompdf安装 要安装 Dompdf，请按照以下步骤操作： 现在您已经安装了 Dompdf，您可以开始在 Web 应用程序中生成优雅且实用的 PDF 文件。 Dompdf 提供了许多用于自定义 PDF 渲染的高级功能，例如管理图像、自定义字体和 CSS 样式。 用 PHP 创建优雅的 PDF 安装和使用Dompdf的另一种方法 以下是要遵循的步骤：1.从官网下载最新版本的Dompdf。2. 解压下载的文件并将其放入您的 PHP 项目中。3. 包含 Dompdfautoload.php 文件以将该库加载到 PHP 脚本中。 从 HTML 模板创建 PDF 现在我们已经安装了 Dompdf，我们将了解如何使用 HTML 模板创建 [&hellip;]"
date: "2024-03-09T12:44:11"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%e7%a7%91%e6%8a%80%e4%b8%8e%e6%95%b0%e5%ad%97-zh-tw", "%e8%ae%a1%e7%ae%97%e4%b8%8e%e6%95%b0%e6%8d%ae-zh-tw"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#Dompdf%E7%AE%80%E4%BB%8B" >Dompdf简介</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E5%85%88%E5%86%B3%E6%9D%A1%E4%BB%B6" >先决条件</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#Dompdf%E5%AE%89%E8%A3%85" >Dompdf安装</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E6%88%91%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%BD%BF%E7%94%A8_Dompdf_%E7%9A%84_PDF_%E6%96%87%E6%A1%A3" >我的第一个使用 Dompdf 的 PDF 文档</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E7%94%A8_PHP_%E5%88%9B%E5%BB%BA%E4%BC%98%E9%9B%85%E7%9A%84_PDF" >用 PHP 创建优雅的 PDF</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8Dompdf%E7%9A%84%E5%8F%A6%E4%B8%80%E7%A7%8D%E6%96%B9%E6%B3%95" >安装和使用Dompdf的另一种方法</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E4%BB%8E_HTML_%E6%A8%A1%E6%9D%BF%E5%88%9B%E5%BB%BA_PDF" >从 HTML 模板创建 PDF</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E7%AE%A1%E7%90%86%E5%9B%BE%E5%83%8F%E5%92%8C%E5%AD%97%E4%BD%93" >管理图像和字体</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/zh-tw/dompdf%ef%bc%9a%e5%a6%82%e4%bd%95%e7%94%a8-php-%e5%88%9b%e5%bb%ba%e4%bc%98%e9%9b%85%e7%9a%84-pdf%ef%bc%9f-2/#%E4%BC%98%E5%8C%96%E6%B8%B2%E6%9F%93%E5%B9%B6%E4%BF%AE%E5%A4%8D_Dompdf_%E9%97%AE%E9%A2%98" >优化渲染并修复 Dompdf 问题</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf%E7%AE%80%E4%BB%8B"></span>Dompdf简介<span class="ez-toc-section-end"></span></h2>



<p>Dompdf 是一个 PHP 库，允许您从 HTML 内容生成 PDF 文件。该解决方案对于生成 PDF 格式的报告、发票或任何其他文档非常有用。在本文中，我们将了解 Dompdf 的基本功能，并学习如何使用它创建优雅且实用的 PDF。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E5%85%88%E5%86%B3%E6%9D%A1%E4%BB%B6"></span>先决条件<span class="ez-toc-section-end"></span></h3>



<p>在安装 Dompdf 之前，请确保您具备以下条件：</p>



<ul class="wp-block-list">
<li><strong>PHP：</strong> Dompdf 需要 PHP >= 5.4。它与 PHP 7.x 版本兼容。</li>



<li><strong>PHP 扩展：</strong> 确保您已启用以下 PHP 扩展：mbstring、DOM 和 GD。这些扩展对于 Dompdf 的正常运行至关重要。</li>



<li><strong>撰写：</strong> Dompdf 通过 Composer 分发，Composer 是 PHP 的依赖管理器。确保您的系统上安装了 Composer。</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf%E5%AE%89%E8%A3%85"></span>Dompdf安装<span class="ez-toc-section-end"></span></h4>



<p>要安装 Dompdf，请按照以下步骤操作：</p>



<ol class="wp-block-list">
<li><strong>创建一个新的 PHP 项目：</strong> 如果您还没有现有项目，请使用您选择的基本结构创建一个新项目。</li>



<li><strong>通过 Composer 添加 Dompdf 依赖项：</strong> 打开控制台并导航到您的项目目录。运行以下命令将 Dompdf 添加到您的项目中：     <pre><code>作曲家需要 dompdf/dompdf</code></pre>     此命令将自动下载并安装 Dompdf 及其依赖项。</li>



<li><strong>在您的应用程序中使用 Dompdf：</strong> 您现在可以在项目中使用 Dompdf。使用 Dompdf 创建 PDF 文件的方法有很多种，但这里有一个基本示例可以帮助您入门：
<pre><code>// 包含 Composer 自动加载器
需要“供应商/autoload.php”；

// 创建一个新的 Dompdf 对象
$dompdf = new Dompdf();

// 从文件或字符串加载 HTML 内容
$html = '<h1><span class="ez-toc-section" id="%E6%88%91%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%BD%BF%E7%94%A8_Dompdf_%E7%9A%84_PDF_%E6%96%87%E6%A1%A3"></span>我的第一个使用 Dompdf 的 PDF 文档<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// 渲染PDF文档
$dompdf->render();

// 发送PDF文档到输出
$dompdf->stream('document.pdf');</code></pre>
    此示例创建一个带有标题的新 PDF 文档，并将其作为“document.pdf”文件上传。您可以根据需要自定义 HTML 内容。</li>
</ol>



<p>现在您已经安装了 Dompdf，您可以开始在 Web 应用程序中生成优雅且实用的 PDF 文件。 Dompdf 提供了许多用于自定义 PDF 渲染的高级功能，例如管理图像、自定义字体和 CSS 样式。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E7%94%A8_PHP_%E5%88%9B%E5%BB%BA%E4%BC%98%E9%9B%85%E7%9A%84_PDF"></span>用 PHP 创建优雅的 PDF<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8Dompdf%E7%9A%84%E5%8F%A6%E4%B8%80%E7%A7%8D%E6%96%B9%E6%B3%95"></span>安装和使用Dompdf的另一种方法<span class="ez-toc-section-end"></span></h3>



<p>以下是要遵循的步骤：<br>1.从官网下载最新版本的Dompdf。<br>2. 解压下载的文件并将其放入您的 PHP 项目中。<br>3. 包含 Dompdfautoload.php 文件以将该库加载到 PHP 脚本中。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E4%BB%8E_HTML_%E6%A8%A1%E6%9D%BF%E5%88%9B%E5%BB%BA_PDF"></span>从 HTML 模板创建 PDF<span class="ez-toc-section-end"></span></h4>



<p>现在我们已经安装了 Dompdf，我们将了解如何使用 HTML 模板创建 PDF。按着这些次序：</p>



<p>1. 创建一个 HTML 文件，其中包含您想要的 PDF 结构和布局。<br>2. 使用 CSS 功能设置文档样式，使用 font-family、font-size、border 等属性。<br>3. 使用 Dompdf 特定标签包含动态数据，例如“{{name}}”或“{{address}}”。<br>4. 使用 Dompdf 类通过您创建的 HTML 模板生成 PDF。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E7%AE%A1%E7%90%86%E5%9B%BE%E5%83%8F%E5%92%8C%E5%AD%97%E4%BD%93"></span>管理图像和字体<span class="ez-toc-section-end"></span></h4>



<p>创建优雅的 PDF 时，通常需要包含图像或使用特定字体。以下是使用 Dompdf 执行此操作的方法：</p>



<p>1. 使用标签将图像包含在 HTML 模板中 <img decoding="async" src="chemin_vers_image">。<br>2. 请注意，Dompdf 默认情况下并不包含所有字体。您可以在 CSS 中使用 @font-face 或使用 Dompdf 提供的字体添加自定义字体。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E4%BC%98%E5%8C%96%E6%B8%B2%E6%9F%93%E5%B9%B6%E4%BF%AE%E5%A4%8D_Dompdf_%E9%97%AE%E9%A2%98"></span>优化渲染并修复 Dompdf 问题<span class="ez-toc-section-end"></span></h4>



<p>有时，您可能会在渲染 PDF 或生成文件时遇到问题。以下是解决这些问题的一些技巧：</p>



<p>1. 检查您的 HTML 模板是否正确构建且有效。<br>2. 确保可以从服务器访问所有外部资源（图像、字体等）。<br>3. 通过激活 Dompdf 调试模式并检查显示的错误来调试代码。<br>4. 有关常见配置和问题的更多信息，请参阅 Dompdf 文档。</p>



<p>使用 Dompdf，您可以通过提供专业且格式良好的 PDF 文档来提供增强的用户体验。无论是生成报告、发票还是其他类型的文档，Dompdf 都是可靠而强大的选择。</p>



<p>总之，借助 Composer，安装 Dompdf 既快速又简单。安装后，您就可以开始创建高质量的 PDF 文件来满足您的 Web 应用程序需求。不要忘记查看官方 Dompdf 文档，以了解有关其功能和可用自定义选项的更多信息。</p>



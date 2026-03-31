---
title: "Dompdf: PHP로 우아한 PDF를 만드는 방법은 무엇입니까?"
slug: "dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c"
excerpt: "돔 소개pdf Dompdf는 HTML 콘텐츠에서 PDF 파일을 생성할 수 있는 PHP 라이브러리입니다. 이 솔루션은 보고서, 송장 또는 기타 PDF 형식의 문서를 생성하는 데 매우 유용합니다. 이 기사에서는 Dompdf의 기본 기능을 알아보고 이를 사용하여 우아하고 기능적인 PDF를 만드는 방법을 알아봅니다. 전제 조건 Dompdf를 설치하기 전에 다음 사항을 확인하세요. 돔PDF 설치 Dompdf를 설치하려면 다음 단계를 따르세요. 이제 [&hellip;]"
date: "2024-03-09T12:41:25"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%ea%b8%b0%ec%88%a0%ea%b3%bc-%eb%94%94%ec%a7%80%ed%84%b8-ko", "%ec%bb%b4%ed%93%a8%ed%8c%85-%eb%b0%8f-%eb%8d%b0%ec%9d%b4%ed%84%b0-ko"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#%EB%8F%94_%EC%86%8C%EA%B0%9Cpdf" >돔 소개pdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#%EC%A0%84%EC%A0%9C_%EC%A1%B0%EA%B1%B4" >전제 조건</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#%EB%8F%94PDF_%EC%84%A4%EC%B9%98" >돔PDF 설치</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#Dompdf%EB%A5%BC_%EC%82%AC%EC%9A%A9%ED%95%9C_%EC%B2%AB_%EB%B2%88%EC%A7%B8_PDF_%EB%AC%B8%EC%84%9C" >Dompdf를 사용한 첫 번째 PDF 문서</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#PHP%EB%A1%9C_%EC%9A%B0%EC%95%84%ED%95%9C_PDF_%EB%A7%8C%EB%93%A4%EA%B8%B0" >PHP로 우아한 PDF 만들기</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#Dompdf%EB%A5%BC_%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0_%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94_%EB%98%90_%EB%8B%A4%EB%A5%B8_%EB%B0%A9%EB%B2%95" >Dompdf를 설치하고 사용하는 또 다른 방법</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#HTML_%ED%85%9C%ED%94%8C%EB%A6%BF%EC%97%90%EC%84%9C_PDF_%EB%A7%8C%EB%93%A4%EA%B8%B0" >HTML 템플릿에서 PDF 만들기</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#%EC%9D%B4%EB%AF%B8%EC%A7%80_%EB%B0%8F_%EA%B8%80%EA%BC%B4_%EA%B4%80%EB%A6%AC" >이미지 및 글꼴 관리</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ko/dompdf-php%eb%a1%9c-%ec%9a%b0%ec%95%84%ed%95%9c-pdf%eb%a5%bc-%eb%a7%8c%eb%93%9c%eb%8a%94-%eb%b0%a9%eb%b2%95%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9e%85%eb%8b%88%ea%b9%8c/#%EB%A0%8C%EB%8D%94%EB%A7%81_%EC%B5%9C%EC%A0%81%ED%99%94_%EB%B0%8F_Dompdf_%EB%AC%B8%EC%A0%9C_%EC%88%98%EC%A0%95" >렌더링 최적화 및 Dompdf 문제 수정</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%EB%8F%94_%EC%86%8C%EA%B0%9Cpdf"></span>돔 소개pdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf는 HTML 콘텐츠에서 PDF 파일을 생성할 수 있는 PHP 라이브러리입니다. 이 솔루션은 보고서, 송장 또는 기타 PDF 형식의 문서를 생성하는 데 매우 유용합니다. 이 기사에서는 Dompdf의 기본 기능을 알아보고 이를 사용하여 우아하고 기능적인 PDF를 만드는 방법을 알아봅니다.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%EC%A0%84%EC%A0%9C_%EC%A1%B0%EA%B1%B4"></span>전제 조건<span class="ez-toc-section-end"></span></h3>



<p>Dompdf를 설치하기 전에 다음 사항을 확인하세요.</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf에는 PHP >= 5.4가 필요합니다. PHP 버전 7.x와 호환됩니다.</li>



<li><strong>PHP 확장:</strong> mbstring, DOM 및 GD와 같은 PHP 확장을 활성화했는지 확인하십시오. 이러한 확장은 Dompdf가 제대로 작동하는 데 필수적입니다.</li>



<li><strong>구성하다 :</strong> Dompdf는 PHP의 종속성 관리자인 Composer를 통해 배포됩니다. 시스템에 Composer가 설치되어 있는지 확인하십시오.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EB%8F%94PDF_%EC%84%A4%EC%B9%98"></span>돔PDF 설치<span class="ez-toc-section-end"></span></h4>



<p>Dompdf를 설치하려면 다음 단계를 따르세요.</p>



<ol class="wp-block-list">
<li><strong>새 PHP 프로젝트를 만듭니다.</strong> 기존 프로젝트가 아직 없는 경우 선택한 기본 구조를 사용하여 새 프로젝트를 만듭니다.</li>



<li><strong>Composer를 통해 Dompdf 종속성을 추가합니다.</strong> 콘솔을 열고 프로젝트 디렉터리로 이동합니다. 다음 명령을 실행하여 프로젝트에 Dompdf를 추가하세요.     <pre><code>작곡가는 dompdf/dompdf가 필요합니다.</code></pre>     이 명령은 종속성과 함께 Dompdf를 자동으로 다운로드하고 설치합니다.</li>



<li><strong>애플리케이션에 Dompdf를 사용하세요.</strong> 이제 프로젝트에서 Dompdf를 사용할 수 있습니다. Dompdf를 사용하여 PDF 파일을 생성하는 방법은 여러 가지가 있지만 시작하는 데 도움이 되는 기본 예는 다음과 같습니다.
<pre><code>// Composer 오토로더 포함
'vendor/autoload.php'가 필요합니다.

// 새 Dompdf 객체를 생성합니다.
$dompdf = 새로운 Dompdf();

// 파일이나 문자열에서 HTML 콘텐츠를 로드합니다.
$html = '<h1><span class="ez-toc-section" id="Dompdf%EB%A5%BC_%EC%82%AC%EC%9A%A9%ED%95%9C_%EC%B2%AB_%EB%B2%88%EC%A7%B8_PDF_%EB%AC%B8%EC%84%9C"></span>Dompdf를 사용한 첫 번째 PDF 문서<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// PDF 문서 렌더링
$dompdf->렌더();

// 출력할 PDF 문서 보내기
$dompdf->stream('document.pdf');</code></pre>
    이 예에서는 제목이 있는 새 PDF 문서를 만들고 이를 &#8220;document.pdf&#8221; 파일로 업로드합니다. 필요에 따라 HTML 콘텐츠를 사용자 정의할 수 있습니다.</li>
</ol>



<p>이제 Dompdf가 설치되었으므로 웹 애플리케이션에서 우아하고 기능적인 PDF 파일 생성을 시작할 수 있습니다. Dompdf는 이미지 관리, 사용자 정의 글꼴, CSS 스타일 등 PDF 렌더링을 사용자 정의하기 위한 다양한 고급 기능을 제공합니다.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="PHP%EB%A1%9C_%EC%9A%B0%EC%95%84%ED%95%9C_PDF_%EB%A7%8C%EB%93%A4%EA%B8%B0"></span>PHP로 우아한 PDF 만들기<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf%EB%A5%BC_%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0_%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94_%EB%98%90_%EB%8B%A4%EB%A5%B8_%EB%B0%A9%EB%B2%95"></span>Dompdf를 설치하고 사용하는 또 다른 방법<span class="ez-toc-section-end"></span></h3>



<p>따라야 할 단계는 다음과 같습니다.<br>1. 공식 홈페이지에서 최신 버전의 Dompdf를 다운로드하세요.<br>2. 다운로드한 파일을 추출하여 PHP 프로젝트에 배치합니다.<br>3. Dompdfautoload.php 파일을 포함하여 PHP 스크립트에 라이브러리를 로드합니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="HTML_%ED%85%9C%ED%94%8C%EB%A6%BF%EC%97%90%EC%84%9C_PDF_%EB%A7%8C%EB%93%A4%EA%B8%B0"></span>HTML 템플릿에서 PDF 만들기<span class="ez-toc-section-end"></span></h4>



<p>이제 Dompdf를 설치했으므로 HTML 템플릿을 사용하여 PDF를 만드는 방법을 살펴보겠습니다. 다음과 같이하세요:</p>



<p>1. PDF에 원하는 구조와 레이아웃이 포함된 HTML 파일을 만듭니다.<br>2. CSS 기능을 사용하여 글꼴 모음, 글꼴 크기, 테두리 등과 같은 속성을 사용하여 문서 스타일을 지정합니다.<br>3. &#8220;{{name}}&#8221; 또는 &#8220;{{address}}&#8221;와 같은 Dompdf 관련 태그를 사용하여 동적 데이터를 포함합니다.<br>4. Dompdf 클래스를 사용하여 생성한 HTML 템플릿을 사용하여 PDF를 생성합니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%9D%B4%EB%AF%B8%EC%A7%80_%EB%B0%8F_%EA%B8%80%EA%BC%B4_%EA%B4%80%EB%A6%AC"></span>이미지 및 글꼴 관리<span class="ez-toc-section-end"></span></h4>



<p>세련된 PDF를 만들 때 이미지를 포함하거나 특정 글꼴을 사용해야 하는 경우가 많습니다. Dompdf를 사용하여 수행하는 방법은 다음과 같습니다.</p>



<p>1. 태그를 사용하여 HTML 템플릿에 이미지를 포함합니다. <img decoding="async" src="chemin_vers_image">.<br>2. Dompdf에는 기본적으로 모든 글꼴이 포함되어 있지 않습니다. CSS에서 @font-face를 사용하거나 Dompdf에서 제공하는 글꼴을 사용하여 사용자 정의 글꼴을 추가할 수 있습니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EB%A0%8C%EB%8D%94%EB%A7%81_%EC%B5%9C%EC%A0%81%ED%99%94_%EB%B0%8F_Dompdf_%EB%AC%B8%EC%A0%9C_%EC%88%98%EC%A0%95"></span>렌더링 최적화 및 Dompdf 문제 수정<span class="ez-toc-section-end"></span></h4>



<p>때로는 PDF를 렌더링하거나 파일을 생성하는 데 문제가 발생할 수 있습니다. 다음은 이 문제를 해결하기 위한 몇 가지 팁입니다.</p>



<p>1. HTML 템플릿이 올바르게 구성되어 있고 유효한지 확인하세요.<br>2. 서버에서 모든 외부 리소스(이미지, 글꼴 등)에 액세스할 수 있는지 확인하세요.<br>3. Dompdf 디버그 모드를 활성화하고 표시된 오류를 확인하여 코드를 디버깅합니다.<br>4. 일반적인 구성 및 문제에 대한 자세한 내용은 Dompdf 설명서를 참조하십시오.</p>



<p>Dompdf를 사용하면 전문적이고 올바른 형식의 PDF 문서를 제공하여 향상된 사용자 경험을 제공할 수 있습니다. 보고서, 송장 또는 기타 유형의 문서를 생성하든 Dompdf는 안정적이고 강력한 선택입니다.</p>



<p>결론적으로 Composer 덕분에 Dompdf 설치가 빠르고 쉽습니다. 일단 설치되면 웹 애플리케이션 요구 사항을 충족하는 고품질 PDF 파일 생성을 시작할 수 있습니다. 해당 기능과 사용 가능한 사용자 정의 옵션에 대해 자세히 알아보려면 공식 Dompdf 문서를 확인하는 것을 잊지 마십시오.</p>



---

title: "객체지향 프로그래밍: 그것은 무엇이며 무엇을 위한 것인가?"
slug: "article-171"
excerpt: "객체 지향 프로그래밍의 기초 거기 객체 지향 프로그래밍 (OOP)는 &#8220;객체&#8221;를 사용하여 컴퓨터 응용 프로그램 및 프로그램을 설계하는 프로그래밍 패러다임입니다. 이러한 개체는 실제 엔터티를 나타내며 개발자가 보다 유연하고 확장 가능하며 유지 관리 가능한 소프트웨어를 만들 수 있도록 해줍니다. 이번 글에서는 OOP의 기초를 이루는 기본 개념을 살펴보겠습니다. 추출 엘&#8217;추출 프로그래머가 사용자에게 중요한 기능만 보여주기 위해 객체의 관련 [&hellip;]"
date: "2024-03-09T12:47:12"
featuredImage: "/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-3.png"
categories: ["%ea%b8%b0%ec%88%a0%ea%b3%bc-%eb%94%94%ec%a7%80%ed%84%b8-ko", "%ec%bb%b4%ed%93%a8%ed%8c%85-%eb%b0%8f-%eb%8d%b0%ec%9d%b4%ed%84%b0-ko"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98_%EA%B8%B0%EC%B4%88" >객체 지향 프로그래밍의 기초</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%B6%94%EC%B6%9C" >추출</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%BA%A1%EC%8A%90%ED%99%94" >캡슐화</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%9C%A0%EC%82%B0" >유산</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EB%8B%A4%ED%98%95%EC%84%B1" >다형성</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%ED%81%B4%EB%9E%98%EC%8A%A4%EC%99%80_%EA%B0%9D%EC%B2%B4" >클래스와 객체</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%83%9D%EC%84%B1%EC%9E%90%EC%99%80_%EC%86%8C%EB%A9%B8%EC%9E%90" >생성자와 소멸자</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EB%B0%A9%EB%B2%95" >방법</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%86%8D%EC%84%B1" >속성</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EA%B0%80%EC%8B%9C%EC%84%B1_%EA%B3%B5%EA%B0%9C_%EB%B9%84%EA%B3%B5%EA%B0%9C_%EB%B0%8F_%EB%B3%B4%ED%98%B8" >가시성: 공개, 비공개 및 보호</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%97%B0%EA%B4%80_%EC%A7%91%ED%95%A9_%EB%B0%8F_%EA%B5%AC%EC%84%B1" >연관, 집합 및 구성</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#OOP%EC%9D%98_%EC%9D%B4%EC%A0%90%EA%B3%BC_%EC%8B%A4%EC%A0%9C_%EC%A0%81%EC%9A%A9" >OOP의 이점과 실제 적용</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98_%EC%9D%B4%EC%A0%90" >객체 지향 프로그래밍의 이점</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98_%EC%8B%A4%EC%A0%9C_%EC%A0%81%EC%9A%A9" >객체지향 프로그래밍의 실제 적용</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-15" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EB%8B%A4%EB%A5%B8_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%ED%8C%A8%EB%9F%AC%EB%8B%A4%EC%9E%84%EA%B3%BC%EC%9D%98_%EB%B9%84%EA%B5%90" >다른 프로그래밍 패러다임과의 비교</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-16" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EB%AA%85%EB%A0%B9%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D" >명령형 프로그래밍</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EC%84%A0%EC%96%B8%EC%A0%81_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D" >선언적 프로그래밍</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%ED%95%A8%EC%88%98%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D" >함수형 프로그래밍</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-19" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8DOOP" >객체 지향 프로그래밍(OOP)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/ko/%ea%b0%9d%ec%b2%b4%ec%a7%80%ed%96%a5-%ed%94%84%eb%a1%9c%ea%b7%b8%eb%9e%98%eb%b0%8d-%ea%b7%b8%ea%b2%83%ec%9d%80-%eb%ac%b4%ec%97%87%ec%9d%b4%eb%a9%b0-%eb%ac%b4%ec%97%87%ec%9d%84-%ec%9c%84%ed%95%9c/#%EB%B0%98%EC%9D%91%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D" >반응형 프로그래밍</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98_%EA%B8%B0%EC%B4%88"></span>객체 지향 프로그래밍의 기초<span class="ez-toc-section-end"></span></h2>



<p>거기 <strong>객체 지향 프로그래밍</strong> (OOP)는 &#8220;객체&#8221;를 사용하여 컴퓨터 응용 프로그램 및 프로그램을 설계하는 프로그래밍 패러다임입니다. 이러한 개체는 실제 엔터티를 나타내며 개발자가 보다 유연하고 확장 가능하며 유지 관리 가능한 소프트웨어를 만들 수 있도록 해줍니다. 이번 글에서는 OOP의 기초를 이루는 기본 개념을 살펴보겠습니다.</p>



<figure class="wp-block-image size-large"><img loading="lazy" decoding="async" width="1024" height="585" src="/images/blog/image-1024x585.png" alt="" class="wp-image-13812" srcset="/images/blog/image-1024x585.png 1024w, /images/blog/image-300x171.png 300w, /images/blog/image-150x86.png 150w, /images/blog/image-768x439.png 768w, /images/blog/image-1536x878.png 1536w, /images/blog/image.png 1792w" sizes="(max-width: 1024px) 100vw, 1024px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%EC%B6%94%EC%B6%9C"></span>추출<span class="ez-toc-section-end"></span></h3>



<p>엘&#8217;<strong>추출</strong> 프로그래머가 사용자에게 중요한 기능만 보여주기 위해 객체의 관련 없는 세부 사항을 모두 숨기는 프로세스입니다. 이렇게 하면 내부 복잡성에 대해 걱정하지 않고도 개체의 작동 방식을 더 쉽게 이해할 수 있습니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%BA%A1%EC%8A%90%ED%99%94"></span>캡슐화<span class="ez-toc-section-end"></span></h4>



<p>엘&#8217;<strong>캡슐화</strong> 데이터를 그룹화하고 클래스라고 불리는 동일한 단위 내에서 데이터를 조작하는 방법으로 구성된 기술입니다. 또한 캡슐화는 정의된 방법을 통해서만 수정을 허용하고 직접적인 무단 액세스를 방지함으로써 데이터 무결성을 보호합니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%9C%A0%EC%82%B0"></span>유산<span class="ez-toc-section-end"></span></h4>



<p>엘&#8217;<strong>유산</strong> 기존 클래스를 기반으로 새 클래스를 만들 수 있는 OOP의 기능입니다. 파생 클래스라고 하는 새 클래스는 기본 클래스의 특성과 메서드를 상속하므로 코드 재사용과 클래스 계층 생성이 가능합니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EB%8B%A4%ED%98%95%EC%84%B1"></span>다형성<span class="ez-toc-section-end"></span></h4>



<p>그만큼 <strong>다형성</strong> 호출된 개체에 따라 다른 작업을 수행하는 메서드의 기능입니다. 다형성에는 두 가지 주요 유형이 있습니다. 오버로딩 다형성(여러 메소드가 동일한 이름을 공유하지만 매개변수가 다름)과 상속 다형성(파생 클래스가 상위 클래스의 메소드와 이름이 같은 메소드를 사용함)입니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%ED%81%B4%EB%9E%98%EC%8A%A4%EC%99%80_%EA%B0%9D%EC%B2%B4"></span>클래스와 객체<span class="ez-toc-section-end"></span></h4>



<p>그만큼 <strong>클래스</strong> 이라는 개별 인스턴스를 생성하는 데 사용되는 모델 또는 청사진입니다. <strong>사물</strong>. 클래스에서 생성된 각 객체는 클래스 속성에 대해 고유한 값을 가질 수 있지만 동일한 메서드를 공유합니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%83%9D%EC%84%B1%EC%9E%90%EC%99%80_%EC%86%8C%EB%A9%B8%EC%9E%90"></span>생성자와 소멸자<span class="ez-toc-section-end"></span></h4>



<p>ㅏ <strong>건설자</strong> 해당 클래스의 객체가 생성될 때 자동으로 호출되는 클래스의 특수 메서드입니다. 일반적으로 객체의 속성을 초기화하는 데 사용됩니다. ㅏ <strong>파괴적인</strong>는 객체가 파괴되려고 할 때 호출되어 할당된 리소스를 해제할 수 있습니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EB%B0%A9%EB%B2%95"></span>방법<span class="ez-toc-section-end"></span></h4>



<p>그만큼 <strong>행동 양식</strong> 객체가 수행할 수 있는 동작이나 동작을 설명하는 클래스 내부에 정의된 함수입니다. 각 메소드는 객체의 내부 속성과 함께 작동하여 특정 작업을 수행할 수 있습니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%86%8D%EC%84%B1"></span>속성<span class="ez-toc-section-end"></span></h4>



<p>그만큼 <strong>속성</strong> 클래스 내부에 정의되고 객체의 상태나 특정 특성을 나타내는 변수입니다. 속성은 숫자, 문자열 또는 다른 클래스의 개체와 같은 다양한 데이터 유형일 수 있습니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EA%B0%80%EC%8B%9C%EC%84%B1_%EA%B3%B5%EA%B0%9C_%EB%B9%84%EA%B3%B5%EA%B0%9C_%EB%B0%8F_%EB%B3%B4%ED%98%B8"></span>가시성: 공개, 비공개 및 보호<span class="ez-toc-section-end"></span></h4>



<p><strong>청중</strong>, <strong>사적인</strong> 그리고 <strong>보호됨</strong> 클래스의 속성과 메소드에 대한 액세스를 제어하는 ​​가시성 수정자입니다. Public 멤버는 어디에서나 액세스할 수 있고, Private 멤버는 해당 클래스가 정의된 클래스에서만 액세스할 수 있으며, Protected 멤버는 파생 클래스뿐만 아니라 정의된 클래스에서도 액세스할 수 있습니다.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%97%B0%EA%B4%80_%EC%A7%91%ED%95%A9_%EB%B0%8F_%EA%B5%AC%EC%84%B1"></span>연관, 집합 및 구성<span class="ez-toc-section-end"></span></h4>



<p>OOP에서는 용어 <strong>협회</strong>, <strong>집합</strong> 그리고 <strong>구성</strong> 객체를 서로 연결할 수 있는 다양한 방법을 설명합니다. 연관(Association)은 서로 독립적인 두 개체 사이의 관계이고, 집합(aggregation)은 부분이 전체와 별도로 존재할 수 있는 &#8220;전체 부분&#8221; 관계이며, 구성(Composition)은 &#8220;부분이 없이는 존재할 수 없는 전체 부분&#8221; 관계입니다. 전체.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="OOP%EC%9D%98_%EC%9D%B4%EC%A0%90%EA%B3%BC_%EC%8B%A4%EC%A0%9C_%EC%A0%81%EC%9A%A9"></span>OOP의 이점과 실제 적용<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1.png" alt="" class="wp-image-1341" srcset="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1.png 1792w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-300x171.png 300w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-1024x585.png 1024w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-150x86.png 150w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-768x439.png 768w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98_%EC%9D%B4%EC%A0%90"></span>객체 지향 프로그래밍의 이점<span class="ez-toc-section-end"></span></h3>



<p>        OOP에는 복잡한 소프트웨어 개발에 선호되는 접근 방식인 여러 가지 장점이 있습니다.</p>



<ul class="wp-block-list">
<li><strong>캡슐화</strong>: 데이터와 이를 조작하는 기능을 개체 내에서 캡슐화하여 데이터 무결성을 보호할 수 있습니다.</li>



<li><strong>추출</strong>: 내부 작업에 대한 깊은 이해 없이도 높은 수준의 개념을 사용할 수 있도록 하여 개발을 단순화합니다.</li>



<li><strong>코드 재사용</strong>: 기존 코드를 재사용 가능한 클래스로 공유하고 사용하도록 장려하여 개발 시간과 유지 관리 비용을 줄입니다.</li>



<li><strong>모듈성</strong>: 프로그램을 독립적으로 개발하고 테스트할 수 있는 독립적이고 상호 교환 가능한 부분으로 나누는 것을 선호합니다.</li>



<li><strong>다형성</strong>: 공통 인터페이스를 통해 객체를 쉽게 교환할 수 있어 프로그래밍 및 시스템 설계에 뛰어난 유연성을 제공합니다.</li>



<li><strong>유산</strong>: 기존 클래스에서 속성과 메서드를 상속하는 파생 클래스를 생성하여 확장 및 사용자 지정을 용이하게 하는 기능을 제공합니다.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98_%EC%8B%A4%EC%A0%9C_%EC%A0%81%EC%9A%A9"></span>객체지향 프로그래밍의 실제 적용<span class="ez-toc-section-end"></span></h4>



<p>        OOP는 다양한 분야와 다양한 애플리케이션에 사용됩니다. 다음은 몇 가지 구체적인 예입니다.</p>



<ul class="wp-block-list">
<li><strong>비디오 게임 개발</strong>: 객체는 캐릭터, 장애물, 파워업 등을 나타낼 수 있어 객체의 상태와 동작을 더 쉽게 관리할 수 있습니다.</li>



<li><strong>그래픽 사용자 인터페이스(GUI)</strong>: 버튼, 메뉴 등 각 인터페이스 요소가 객체이기 때문에 인터랙티브 인터페이스 구축이 더욱 직관적입니다.</li>



<li><strong>데이터베이스 관리 시스템</strong>: 테이블, 레코드, 쿼리와 같은 엔터티를 객체로 모델링하여 효율성과 유지 관리성을 높일 수 있습니다.</li>



<li><strong>웹 개발</strong>: OOP 기반 프레임워크 등 <strong>장고</strong> Python의 경우 또는 <strong>루비 온 레일즈</strong> Ruby의 경우 객체를 사용하여 요청, 응답 및 기타 웹 구성 요소를 나타냅니다.</li>



<li><strong>모바일 앱</strong>: 다음과 같은 플랫폼 <strong>기계적 인조 인간</strong> 그리고 <strong>iOS</strong> 사용자 인터페이스 구성 요소의 이벤트 처리 및 조작을 위해 OOP 모델을 활용합니다.</li>



<li><strong>시뮬레이션 소프트웨어</strong>: 물리적, 경제적 또는 생물학적 시스템을 시뮬레이션하기 위해 객체를 사용하면 시스템 구성 요소 간의 복잡한 상호 작용을 모델링할 수 있습니다.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%EB%8B%A4%EB%A5%B8_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%ED%8C%A8%EB%9F%AC%EB%8B%A4%EC%9E%84%EA%B3%BC%EC%9D%98_%EB%B9%84%EA%B5%90"></span>다른 프로그래밍 패러다임과의 비교<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2.png" alt="" class="wp-image-1342" srcset="/images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2.png 1792w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-300x171.png 300w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-1024x585.png 1024w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-150x86.png 150w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-768x439.png 768w, /images/blog/Programmation-orientee-objet-quest-ce-que-cest-et-a-quoi-ca-sert-1-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<figure class="wp-block-embed is-type-video is-provider-tiktok wp-block-embed-tiktok"><div class="wp-block-embed__wrapper">
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@louis_dhanis/video/7291716348722351392" data-video-id="7291716348722351392" data-embed-from="oembed" style="max-width:605px; min-width:325px;"> <section> <a target="_blank" title="@louis_dhanis" href="https://www.tiktok.com/@louis_dhanis?refer=embed" rel="noopener">@louis_dhanis</a> <p>C’est quoi la programmation orientée objet ? Comment ça marche ? C&#8217;est quoi la différence entre une voiture et une maison ? <a title="astucetech" target="_blank" href="https://www.tiktok.com/tag/astucetech?refer=embed" rel="noopener">#astucetech</a> <a title="louis_dhanis" target="_blank" href="https://www.tiktok.com/tag/louis_dhanis?refer=embed" rel="noopener">#louis_dhanis</a> <a title="apprendreautrement" target="_blank" href="https://www.tiktok.com/tag/apprendreautrement?refer=embed" rel="noopener">#apprendreautrement</a> <a title="apprendreacoder" target="_blank" href="https://www.tiktok.com/tag/apprendreacoder?refer=embed" rel="noopener">#apprendreacoder</a> <a title="devweb" target="_blank" href="https://www.tiktok.com/tag/devweb?refer=embed" rel="noopener">#devweb</a> <a title="entrepreneuriat" target="_blank" href="https://www.tiktok.com/tag/entrepreneuriat?refer=embed" rel="noopener">#entrepreneuriat</a> <a title="entrepreneurtech" target="_blank" href="https://www.tiktok.com/tag/entrepreneurtech?refer=embed" rel="noopener">#entrepreneurtech</a> <a title="developpement" target="_blank" href="https://www.tiktok.com/tag/developpement?refer=embed" rel="noopener">#developpement</a> <a title="poo" target="_blank" href="https://www.tiktok.com/tag/poo?refer=embed" rel="noopener">#POO</a> <a title="programmation" target="_blank" href="https://www.tiktok.com/tag/programmation?refer=embed" rel="noopener">#programmation</a></p> <a target="_blank" title="♬ son original - Louis Dhanis - Louis Dhanis" href="https://www.tiktok.com/music/son-original-Louis-Dhanis-7291716399008598816?refer=embed" rel="noopener">♬ son original &#8211; Louis Dhanis &#8211; Louis Dhanis</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%EB%AA%85%EB%A0%B9%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D"></span>명령형 프로그래밍<span class="ez-toc-section-end"></span></h3>



<p>명령형 프로그래밍은 가장 오래되고 가장 간단한 패러다임입니다. 결과를 얻기 위해 컴퓨터가 따라야 하는 단계를 설명하는 것으로 구성됩니다. C 언어는 이러한 패러다임의 전형적인 예입니다.</p>



<p><strong>이익 :</strong></p>



<ul class="wp-block-list">
<li>프로그램 흐름과 시스템 리소스 사용을 정밀하게 제어합니다.</li>



<li>개념적으로 간단하고 이해하기 쉽습니다.</li>
</ul>



<p><strong>단점:</strong></p>



<ul class="wp-block-list">
<li>대규모 프로그램의 경우 매우 복잡해질 수 있습니다.</li>



<li>코드 유연성과 재사용성이 부족합니다.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EC%84%A0%EC%96%B8%EC%A0%81_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D"></span>선언적 프로그래밍<span class="ez-toc-section-end"></span></h4>



<p>명령형 프로그래밍과 달리 선언적 프로그래밍은 결과를 달성하는 방법을 명시적으로 설명하지 않고 결과가 무엇인지에 중점을 둡니다. SQL과 HTML은 선언적 언어의 예입니다.</p>



<p><strong>이익 :</strong></p>



<ul class="wp-block-list">
<li>원하는 결과를 간단하게 표현합니다.</li>



<li>컴파일러나 인터프리터에 의한 더 나은 최적화를 가능하게 하는 구현 세부 사항의 추상화.</li>
</ul>



<p><strong>단점:</strong></p>



<ul class="wp-block-list">
<li>기계가 따르는 정확한 프로세스에 대한 통제력이 떨어집니다.</li>



<li>보다 절차적인 접근 방식에 익숙한 개발자에게는 덜 직관적일 수 있습니다.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%ED%95%A8%EC%88%98%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D"></span>함수형 프로그래밍<span class="ez-toc-section-end"></span></h4>



<p>함수형 프로그래밍은 계산을 수학 함수의 평가처럼 처리하는 선언적 프로그래밍의 하위 집합입니다. Haskell과 Scala는 이러한 패러다임을 지원하는 언어입니다.</p>



<p><strong>이익 :</strong></p>



<ul class="wp-block-list">
<li>코드에 대한 추론을 촉진하고 뛰어난 모듈성을 보장합니다.</li>



<li>부작용이 없기 때문에 병렬 프로그래밍 및 분산 시스템에 이상적입니다.</li>
</ul>



<p><strong>단점:</strong></p>



<ul class="wp-block-list">
<li>익숙하지 않은 개발자에게는 가파른 학습 곡선이 나타날 수 있습니다.</li>



<li>높은 수준의 추상화로 인해 성능 예측이 어려울 수 있습니다.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EA%B0%9D%EC%B2%B4_%EC%A7%80%ED%96%A5_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8DOOP"></span>객체 지향 프로그래밍(OOP)<span class="ez-toc-section-end"></span></h4>



<p>OOP는 &#8220;클래스&#8221;의 인스턴스인 &#8220;객체&#8221; 개념을 기반으로 합니다. 객체에는 데이터와 메소드가 모두 포함됩니다. Java와 Python은 이러한 패러다임을 구현하는 언어입니다.</p>



<p><strong>이익 :</strong></p>



<ul class="wp-block-list">
<li>코드 재사용성을 높이고 유지 관리를 용이하게 합니다.</li>



<li>데이터 캡슐화 및 추상화를 촉진합니다.</li>
</ul>



<p><strong>단점:</strong></p>



<ul class="wp-block-list">
<li>과도한 추상화는 불필요한 복잡성을 초래할 수 있습니다.</li>



<li>추가 추상화 계층으로 인해 성능이 저하될 수 있습니다.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%EB%B0%98%EC%9D%91%ED%98%95_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D"></span>반응형 프로그래밍<span class="ez-toc-section-end"></span></h4>



<p>반응형 프로그래밍은 데이터 흐름을 관리하고 변경 사항을 전파하는 데 초점을 맞춘 패러다임입니다. 이는 대화형 사용자 인터페이스나 실시간 시스템을 갖춘 애플리케이션에 특히 효과적입니다.</p>



<p><strong>이익 :</strong></p>



<ul class="wp-block-list">
<li>복잡한 비동기 시스템의 관리를 개선합니다.</li>



<li>대화형 컨텍스트에서 더 읽기 쉽고 오류가 발생하기 쉬운 코드를 장려합니다.</li>
</ul>



<p><strong>단점:</strong></p>



<ul class="wp-block-list">
<li>효과적으로 사용하려면 반응형 개념에 대한 철저한 이해가 필요합니다.</li>



<li>반응 순서는 때때로 디버그하기 어려울 수 있습니다.</li>
</ul>



<p>결론적으로, 프로그래밍 패러다임의 선택은 해결하려는 문제의 성격, 개발자의 선호도, 시스템의 성능 제약 조건에 따라 달라지는 경우가 많습니다. 차이점과 응용 프로그램을 이해하면 개발자가 프로젝트에 적합한 접근 방식을 선택하고 더 깔끔하고 유지 관리가 용이하며 효율적인 코드를 작성하는 데 도움이 될 수 있습니다.</p>



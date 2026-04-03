---
title: "HIDS 与 NIDS：差异和用途"
slug: "hids-nids"
excerpt: "入侵检测系统简介：HIDS 和 NIDS 信息系统安全是各种规模的企业和组织的核心关注点。面对日益增长的威胁和网络攻击的复杂性，建立有效的防御机制势在必行。其中， 入侵检测系统 （入侵检测系统）在监控计算机网络和检测可疑活动方面发挥着至关重要的作用。特别是， 主机入侵检测系统 （HIDS）和 网络入侵检测系统 （巢穴) 是两种互补类型，可提供额外的保护层。 什么是 HIDS（基于主机的入侵检测系统）？ A HIDS 是安装在个人计算机或主机上的软件。它监视安装它的系统是否存在可疑活动，并将这些事件报告给管理员或中央安全事件管理 (SIEM) 系统。 HIDS 分析系统文件、运行进程、活动日志和文件系统完整性以检测可能的入侵。 什么是 NIDS（基于网络的入侵检测系统）？ 相比之下，一个 巢穴 位于网络层，监视通过交换和路由系统的流量。它能够检测针对网络基础设施的攻击，例如分布式拒绝服务 (DDoS)、端口扫描或穿越网络的其他形式的异常行为。 HIDS 与 NIDS 的比较 在选择入侵检测系统时，必须了解 HIDS 和 NIDS 之间的差异，以确定哪种系统最适合组织的特定环境。 标准 HIDS 巢穴 定位 安装在各个主机上 在网络基础设施中实施 发挥作用 监控本地文件和进程 监控网络流量 检测到的攻击类型 文件修改、rootkit 等 端口扫描、DDoS 等 范围 仅限于主机 扩展到全网 表现 可能受主机负载影响 取决于网络流量 [&hellip;]"
date: "2024-03-09T11:59:28"
featuredImage: "/images/blog/HIDS-vs-NIDS-differences-et-utilisation-3.png"
categories: ["%e5%9f%ba%e7%a1%80%e8%ae%be%e6%96%bd%e5%92%8c%e7%bd%91%e7%bb%9c-zh", "%e7%a7%91%e6%8a%80%e4%b8%8e%e6%95%b0%e5%ad%97-zh"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Network Based IDS (NIDS)" width="500" height="281" src="https://www.youtube.com/embed/sjnJrc_iNho?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F%E7%AE%80%E4%BB%8B%EF%BC%9AHIDS_%E5%92%8C_NIDS" >入侵检测系统简介：HIDS 和 NIDS</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#%E4%BB%80%E4%B9%88%E6%98%AF_HIDS%EF%BC%88%E5%9F%BA%E4%BA%8E%E4%B8%BB%E6%9C%BA%E7%9A%84%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F%EF%BC%89%EF%BC%9F" >什么是 HIDS（基于主机的入侵检测系统）？</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#%E4%BB%80%E4%B9%88%E6%98%AF_NIDS%EF%BC%88%E5%9F%BA%E4%BA%8E%E7%BD%91%E7%BB%9C%E7%9A%84%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F%EF%BC%89%EF%BC%9F" >什么是 NIDS（基于网络的入侵检测系统）？</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#HIDS_%E4%B8%8E_NIDS_%E7%9A%84%E6%AF%94%E8%BE%83" >HIDS 与 NIDS 的比较</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#%E4%BA%86%E8%A7%A3_HIDS%EF%BC%9A%E7%89%B9%E6%80%A7%E5%92%8C%E4%BC%98%E7%82%B9" >了解 HIDS：特性和优点</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#HIDS_%E7%9A%84%E7%89%B9%E7%82%B9" >HIDS 的特点</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#HIDS%E7%9A%84%E4%BC%98%E7%82%B9" >HIDS的优点</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#NIDS_%E8%A7%A3%E9%87%8A%EF%BC%9A%E5%AE%83%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86%E5%92%8C%E5%A5%BD%E5%A4%84" >NIDS 解释：它的工作原理和好处</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#NIDS_%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86" >NIDS 的工作原理</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-10" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#NIDS_%E7%9A%84%E5%A5%BD%E5%A4%84" >NIDS 的好处</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#%E9%80%89%E6%8B%A9_NIDS_%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9" >选择 NIDS 的注意事项</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#HIDS_%E5%92%8C_NIDS_%E4%B9%8B%E9%97%B4%E7%9A%84%E9%80%89%E6%8B%A9%EF%BC%9A%E5%86%B3%E7%AD%96%E6%A0%87%E5%87%86%E5%92%8C%E4%BD%BF%E7%94%A8%E8%83%8C%E6%99%AF" >HIDS 和 NIDS 之间的选择：决策标准和使用背景</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#%E5%9C%A8_HIDS_%E5%92%8C_NIDS_%E4%B9%8B%E9%97%B4%E8%BF%9B%E8%A1%8C%E9%80%89%E6%8B%A9%E7%9A%84%E5%86%B3%E7%AD%96%E6%A0%87%E5%87%86" >在 HIDS 和 NIDS 之间进行选择的决策标准</a></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/zh/hids-%e4%b8%8e-nids%ef%bc%9a%e5%b7%ae%e5%bc%82%e5%92%8c%e7%94%a8%e9%80%94/#HIDS_%E5%92%8C_NIDS_%E7%9A%84%E4%BD%BF%E7%94%A8%E8%83%8C%E6%99%AF" >HIDS 和 NIDS 的使用背景</a></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F%E7%AE%80%E4%BB%8B%EF%BC%9AHIDS_%E5%92%8C_NIDS"></span>入侵检测系统简介：HIDS 和 NIDS<span class="ez-toc-section-end"></span></h2>



<p>信息系统安全是各种规模的企业和组织的核心关注点。面对日益增长的威胁和网络攻击的复杂性，建立有效的防御机制势在必行。其中， <strong>入侵检测系统</strong> （<strong>入侵检测系统</strong>）在监控计算机网络和检测可疑活动方面发挥着至关重要的作用。特别是， <strong>主机入侵检测系统</strong> （<strong>HIDS</strong>）和 <strong>网络入侵检测系统</strong> （<strong>巢穴</strong>) 是两种互补类型，可提供额外的保护层。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E4%BB%80%E4%B9%88%E6%98%AF_HIDS%EF%BC%88%E5%9F%BA%E4%BA%8E%E4%B8%BB%E6%9C%BA%E7%9A%84%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F%EF%BC%89%EF%BC%9F"></span>什么是 HIDS（基于主机的入侵检测系统）？<span class="ez-toc-section-end"></span></h3>



<p>A <strong>HIDS</strong> 是安装在个人计算机或主机上的软件。它监视安装它的系统是否存在可疑活动，并将这些事件报告给管理员或中央安全事件管理 (SIEM) 系统。 HIDS 分析系统文件、运行进程、活动日志和文件系统完整性以检测可能的入侵。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E4%BB%80%E4%B9%88%E6%98%AF_NIDS%EF%BC%88%E5%9F%BA%E4%BA%8E%E7%BD%91%E7%BB%9C%E7%9A%84%E5%85%A5%E4%BE%B5%E6%A3%80%E6%B5%8B%E7%B3%BB%E7%BB%9F%EF%BC%89%EF%BC%9F"></span>什么是 NIDS（基于网络的入侵检测系统）？<span class="ez-toc-section-end"></span></h4>



<p>相比之下，一个 <strong>巢穴</strong> 位于网络层，监视通过交换和路由系统的流量。它能够检测针对网络基础设施的攻击，例如分布式拒绝服务 (DDoS)、端口扫描或穿越网络的其他形式的异常行为。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="HIDS_%E4%B8%8E_NIDS_%E7%9A%84%E6%AF%94%E8%BE%83"></span>HIDS 与 NIDS 的比较<span class="ez-toc-section-end"></span></h4>



<p>在选择入侵检测系统时，必须了解 HIDS 和 NIDS 之间的差异，以确定哪种系统最适合组织的特定环境。</p>



<figure class="wp-block-table"><table><thead><tr><th>标准</th><th>HIDS</th><th>巢穴</th></tr></thead><tbody><tr><td>定位</td><td>安装在各个主机上</td><td>在网络基础设施中实施</td></tr><tr><td>发挥作用</td><td>监控本地文件和进程</td><td>监控网络流量</td></tr><tr><td>检测到的攻击类型</td><td>文件修改、rootkit 等</td><td>端口扫描、DDoS 等</td></tr><tr><td>范围</td><td>仅限于主机</td><td>扩展到全网</td></tr><tr><td>表现</td><td>可能受主机负载影响</td><td>取决于网络流量</td></tr></tbody></table></figure>



<p>通过有效结合 <strong>HIDS</strong> 和 <strong>巢穴</strong>，企业可以从整体安全视角中受益，并确保更好地检测恶意活动。</p>



<p>HIDS 和 NIDS 的实施代表了对抗网络威胁的主动战略。每个组织都应该评估其具体需求，通过集成这些基本的入侵检测系统来创建最佳的安全基础设施。通过保持警惕并配备正确的工具，可以显着保护数字资源免受入侵。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E4%BA%86%E8%A7%A3_HIDS%EF%BC%9A%E7%89%B9%E6%80%A7%E5%92%8C%E4%BC%98%E7%82%B9"></span>了解 HIDS：特性和优点<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/HIDS-vs-NIDS-differences-et-utilisation.png" alt="" class="wp-image-1641" srcset="/images/blog/HIDS-vs-NIDS-differences-et-utilisation.png 1792w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-300x171.png 300w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1024x585.png 1024w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-150x86.png 150w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-768x439.png 768w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="HIDS_%E7%9A%84%E7%89%B9%E7%82%B9"></span>HIDS 的特点<span class="ez-toc-section-end"></span></h3>



<p>        这 <strong>特征</strong> HIDS 的主要功能包括配置和文件审核、文件完整性监控、恶意行为模式识别和日志管理。当检测到可疑活动时，HIDS 系统还可以通过关闭连接或更改访问权限来主动采取行动。 HIDS 通常与 NIDS 一起使用，以实现更全面的 IT 安全覆盖。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="HIDS%E7%9A%84%E4%BC%98%E7%82%B9"></span>HIDS的优点<span class="ez-toc-section-end"></span></h3>



<p>        HIDS 的使用提供了多种 <strong>好处</strong>。首先，对主机系统的精确监控可以对 NIDS 可能遗漏的入侵进行细粒度检测。它们在识别关键系统文件的非法更改和本地利用尝试方面特别有效。另一个优点是，即使网络流量被加密，HIDS 仍能保持其有效性，而 NIDS 的情况并非总是如此。此外，HIDS 可以帮助确保遵守适用的安全策略和法规。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="NIDS_%E8%A7%A3%E9%87%8A%EF%BC%9A%E5%AE%83%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86%E5%92%8C%E5%A5%BD%E5%A4%84"></span>NIDS 解释：它的工作原理和好处<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-1.png" alt="" class="wp-image-1642" srcset="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-1.png 1792w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-300x171.png 300w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-1024x585.png 1024w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-150x86.png 150w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-768x439.png 768w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="NIDS_%E7%9A%84%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86"></span>NIDS 的工作原理<span class="ez-toc-section-end"></span></h3>



<p>的运作 <strong>巢穴</strong> 可以分为几个关键阶段：</p>



<ul class="wp-block-list">
<li><strong>数据收集</strong> ：NIDS 通过吸收通过网络传输的数据包来实时监控网络流量。</li>



<li><strong>流量分析</strong> ：使用不同的方法对收集的数据进行分析，例如签名检查、启发式分析或行为分析。</li>



<li><strong>警报和通知</strong> ：当检测到可疑活动时，NIDS 会发出警报并向网络管理员发送通知。</li>



<li><strong>整合与响应</strong> ：一些 NIDS 可以与其他安全系统集成，以协调对检测到的威胁的自动响应。</li>
</ul>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="NIDS_%E7%9A%84%E5%A5%BD%E5%A4%84"></span>NIDS 的好处<span class="ez-toc-section-end"></span></h3>



<p>实施一个 <strong>巢穴</strong> 公司网络内提供了几个相当大的优势：</p>



<ul class="wp-block-list">
<li><strong>实时警报</strong> ：让管理员能够立即意识到潜在的威胁并迅速做出反应。</li>



<li><strong>入侵防御</strong> ：通过快速检测异常活动，NIDS 有助于在入侵造成重大损害之前对其进行预防。</li>



<li><strong>了解交通</strong> ：提供对网络上发生的情况的更好可见性，这对于安全管理至关重要。</li>



<li><strong>监管合规性</strong> ：在某些情况下，使用 NIDS 有助于满足不同网络安全标准和法规的要求。</li>



<li><strong>事件记录</strong> ：能够记录安全事件以供日后分析，并可能作为法律证据。</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E9%80%89%E6%8B%A9_NIDS_%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9"></span>选择 NIDS 的注意事项<span class="ez-toc-section-end"></span></h4>



<p>选择正确的一个 <strong>巢穴</strong> 需要深入分析公司的具体需求。以下是一些重要的注意事项：</p>



<ul class="wp-block-list">
<li><strong>网络兼容性</strong> ：确保NIDS能够与现有网络基础设施无缝集成。</li>



<li><strong>检测能力</strong> ：评估 NIDS 签名和检测方法的有效性及其随威胁演变的能力。</li>



<li><strong>表现</strong> ：NIDS 必须能够处理网络流量而不引入显着的延迟。</li>



<li><strong>易于管理</strong> ：NIDS 界面必须用户友好，以便轻松有效地管理警报。</li>



<li></li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="HIDS_%E5%92%8C_NIDS_%E4%B9%8B%E9%97%B4%E7%9A%84%E9%80%89%E6%8B%A9%EF%BC%9A%E5%86%B3%E7%AD%96%E6%A0%87%E5%87%86%E5%92%8C%E4%BD%BF%E7%94%A8%E8%83%8C%E6%99%AF"></span>HIDS 和 NIDS 之间的选择：决策标准和使用背景<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-2.png" alt="" class="wp-image-1643" srcset="/images/blog/HIDS-vs-NIDS-differences-et-utilisation-2.png 1792w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-300x171.png 300w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-1024x585.png 1024w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-150x86.png 150w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-768x439.png 768w, /images/blog/HIDS-vs-NIDS-differences-et-utilisation-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E5%9C%A8_HIDS_%E5%92%8C_NIDS_%E4%B9%8B%E9%97%B4%E8%BF%9B%E8%A1%8C%E9%80%89%E6%8B%A9%E7%9A%84%E5%86%B3%E7%AD%96%E6%A0%87%E5%87%86"></span>在 HIDS 和 NIDS 之间进行选择的决策标准<span class="ez-toc-section-end"></span></h3>



<p>HIDS 或 NIDS 系统之间的选择取决于以下几个因素：</p>



<ul class="wp-block-list">
<li><strong>监控规模</strong> ：HIDS更适合监控单个系统，而NIDS是为网络环境设计的。</li>



<li><strong>要保护的数据类型</strong> ：如果您需要保护存储在特定服务器上的关键数据，HIDS 可能更相关。为了确保数据传输的安全，NIDS 更可取。</li>



<li><strong>系统性能</strong> ：HIDS 会消耗其所保护的主机上更多的系统资源，而 NIDS 通常需要专用资源来进行网络监控。</li>



<li><strong>部署复杂度</strong> ：安装 HIDS 比设置 NIDS 更简单，后者需要更专门的网络配置。</li>
</ul>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="HIDS_%E5%92%8C_NIDS_%E7%9A%84%E4%BD%BF%E7%94%A8%E8%83%8C%E6%99%AF"></span>HIDS 和 NIDS 的使用背景<span class="ez-toc-section-end"></span></h3>



<p>使用 HIDS 还是 NIDS 的决定通常取决于使用环境：</p>



<ul class="wp-block-list">
<li>对于拥有许多远程端点的企业，在每个设备上使用 HIDS 可以提供密切监控。</li>



<li>拥有大型异构网络的组织可能会青睐 NIDS，以实现对其网络活动的全局可见性。</li>



<li>服务器性能和完整性至关重要的数据中心可以从基于每台服务器实施 HIDS 中受益。</li>
</ul>



<p>HIDS 和 NIDS 之间的选择必须谨慎，并与组织的安全目标、IT 结构和运营条件保持一致。 HIDS 非常适合详细的系统级监控，而 NIDS 将更好地满足网络范围的监控需求。两者的结合有时可以成为抵御网络安全威胁的最佳防御措施。</p>



<p>请注意，一些供应商提供混合解决方案，集成了两个系统的功能，例如 <strong>赛门铁克</strong>, <strong>迈克菲</strong>， 或者 <strong>鼻息</strong>。在做出最终选择之前，请花时间评估您的需求。</p>



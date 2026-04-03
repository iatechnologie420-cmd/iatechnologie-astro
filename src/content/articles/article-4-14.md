---
slug: "article-4-14"
title: "什么是自动编码器？终极指南！"
excerpt: "自动编码器，或 自动编码器 在英语中，将自己定位为机器学习和人工智能领域的强大工具。这些特殊的神经网络用于降维、异常检测、数据去噪等。本文介绍了这项令人着迷的技术，重点介绍了其工作原理、应用及其在研究和工业中日益增长的重要性。 什么是自动编码器？ A 自动编码器 是一种用于无监督学习的人工神经网络。自动编码器的主要目标是生成一组输入数据的紧凑表示（编码），然后根据该表示重建数据。这个想法是捕获数据最重要的方面，通常是为了降维。自动编码器的结构通常由两个主要部分组成： 自动编码器如何工作？ 自动编码器的操作可以分为几个步骤： 通过这个迭代过程，自动编码器学习数据的有效表示，重点是在重建过程中保留最重要的特征。 自动编码器的实际应用 自动编码器用途广泛，可应用于多个领域： 简而言之，自动编码器发现和定义有意义的数据特征的能力使它们成为任何人工智能从业者工具包中的必备工具。 自动编码器：编码、瓶颈和解码 编码 编码或编码阶段涉及将输入数据转换为压缩表示。初始数据可能很大，被输入到自动编码器网络中。网络的各层将逐渐降低数据的维度，将重要信息压缩到更小的表示空间中。网络的每一层都由应用非线性变换的神经元组成，例如使用 ReLU 或 Sigmoid 等激活函数，以获得保留基本信息的新数据表示。 瓶颈 瓶颈是自动编码器的中心部分，其中数据表示达到最低维度，也称为代码。正是这种压缩表示保留了输入数据最重要的特征。瓶颈充当过滤器，迫使自动编码器学习压缩信息的有效方法。这可以与数据压缩的一种形式进行比较，但压缩是从数据中自动学习的，而不是由标准算法定义的。 解码 解码阶段是与编码对称的步骤，其中压缩表示被重构为输出，其目标是尽可能忠实于原始输入。从瓶颈表示开始，神经网络会逐渐增加数据的维度。这是编码的逆过程：连续的层根据简化的表示重建初始特征。如果解码有效，则自动编码器的输出应该非常接近原始数据。 在无监督学习中，自动编码器对于理解数据的底层结构特别有用。这些网络的有效性不是通过其完美再现输入的能力来衡量的，而是通过其捕获代码中数据最显着和相关属性的能力来衡量的。然后，该代码可用于降维、可视化等任务，甚至可以用于更复杂架构中的其他神经网络的预处理。 自动编码器的实际应用和变体 L&#8217;自动编码器是人工智能 (AI) 驱动的深度学习库中的关键组成部分，它是一种神经网络，旨在将数据编码为较低维的表示形式，并以可以进行相关重建的方式对其进行分解。让我们检查一下它们 实际应用 以及这个迷人领域中出现的变体。 自动编码器的实际应用 由于自动编码器能够在没有监督的情况下学习有效且有意义的数据表示，因此已经进入了多种应用程序。这里有些例子： 降维 与 PCA（主成分分析）一样，自动编码器经常用于 降维。该技术可以通过减少要考虑的变量数量来简化数据处理，同时保留原始数据集中包含的大部分信息。 噪音消除（去噪） 自动编码器具有学习从部分破坏的数据中重建输入的能力，因此对于 噪音消除。尽管有噪音的干扰，它们仍然能够识别并恢复有用的数据。 数据压缩 通过学习将数据编码为更紧凑的形式，自动编码器可用于 数据压缩。尽管它们在实践中尚未广泛用于此目的，但它们的潜力是巨大的，特别是对于压缩特定数据类型。 数据生成和估算 自动编码器能够生成与其训练数据相似的新数据实例。该能力还可以用于 归因，这涉及填充数据集中缺失的数据。 自动编码器变体 除了标准自动编码器之外，还开发了各种变体来适应数据的具体情况和所需的任务。以下是一些值得注意的变化： 变分自动编码器 (VAE) 这 变分自动编码器 （VAE）添加一个允许生成数据的随机层。 VAE 在图像或音乐等内容的生成中特别受欢迎，因为它们可以根据同一模型生成新的、多样化的元素。 [&hellip;]"
date: "2024-03-09T12:08:15"
categories: ["%e7%a7%91%e6%8a%80%e4%b8%8e%e6%95%b0%e5%ad%97-zh", "%e8%ae%a1%e7%ae%97%e4%b8%8e%e6%95%b0%e6%8d%ae-zh"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Tracking Corn &amp; Weed with Yolov5 and Auto Encoder - Tracker" width="500" height="281" src="https://www.youtube.com/embed/8-jWgsGWaR0?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<p>自动编码器，或 <em>自动编码器</em> 在英语中，将自己定位为机器学习和人工智能领域的强大工具。这些特殊的神经网络用于降维、异常检测、数据去噪等。本文介绍了这项令人着迷的技术，重点介绍了其工作原理、应用及其在研究和工业中日益增长的重要性。</p>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E4%BB%80%E4%B9%88%E6%98%AF%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%EF%BC%9F" >什么是自动编码器？</a></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-2" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E5%A6%82%E4%BD%95%E5%B7%A5%E4%BD%9C%EF%BC%9F" >自动编码器如何工作？</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-3" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8" >自动编码器的实际应用</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-4" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%EF%BC%9A%E7%BC%96%E7%A0%81%E3%80%81%E7%93%B6%E9%A2%88%E5%92%8C%E8%A7%A3%E7%A0%81" >自动编码器：编码、瓶颈和解码</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E7%BC%96%E7%A0%81" >编码</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E7%93%B6%E9%A2%88" >瓶颈</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%A7%A3%E7%A0%81" >解码</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-8" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8%E5%92%8C%E5%8F%98%E4%BD%93" >自动编码器的实际应用和变体</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-9" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8-2" >自动编码器的实际应用</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E9%99%8D%E7%BB%B4" >降维</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E5%99%AA%E9%9F%B3%E6%B6%88%E9%99%A4%EF%BC%88%E5%8E%BB%E5%99%AA%EF%BC%89" >噪音消除（去噪）</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E6%95%B0%E6%8D%AE%E5%8E%8B%E7%BC%A9" >数据压缩</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E6%95%B0%E6%8D%AE%E7%94%9F%E6%88%90%E5%92%8C%E4%BC%B0%E7%AE%97" >数据生成和估算</a></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-14" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E5%8F%98%E4%BD%93" >自动编码器变体</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E5%8F%98%E5%88%86%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8_VAE" >变分自动编码器 (VAE)</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-16" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E7%A8%80%E7%96%8F%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8" >稀疏自动编码器</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-17" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E5%8E%BB%E5%99%AA%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8" >去噪自动编码器</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-18" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E9%A1%BA%E5%BA%8F%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8" >顺序自动编码器</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-19" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E5%A6%82%E4%BD%95%E8%AE%AD%E7%BB%83%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E5%92%8C%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B" >如何训练自动编码器和代码示例</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-20" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%AE%AD%E7%BB%83%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E8%BF%87%E7%A8%8B" >训练自动编码器的过程</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-21" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#Keras_%E7%9A%84%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81" >Keras 的示例代码</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-22" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%89%AF%E5%A5%BD%E9%94%BB%E7%82%BC%E7%9A%84%E7%A7%98%E8%AF%80" >良好锻炼的秘诀</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-23" href="/zh/%e4%bb%80%e4%b9%88%e6%98%af%e8%87%aa%e5%8a%a8%e7%bc%96%e7%a0%81%e5%99%a8%ef%bc%9f%e7%bb%88%e6%9e%81%e6%8c%87%e5%8d%97%ef%bc%81/#%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%BA%94%E7%94%A8" >自动编码器的应用</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E4%BB%80%E4%B9%88%E6%98%AF%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%EF%BC%9F"></span>什么是自动编码器？<span class="ez-toc-section-end"></span></h2>



<p>A <strong>自动编码器</strong> 是一种用于无监督学习的人工神经网络。自动编码器的主要目标是生成一组输入数据的紧凑表示（编码），然后根据该表示重建数据。这个想法是捕获数据最重要的方面，通常是为了降维。自动编码器的结构通常由两个主要部分组成：</p>



<ul class="wp-block-list">
<li><strong>编码器</strong> （<em>编码</em>)：网络的第一部分负责将输入数据压缩为简化形式。</li>



<li><strong>解码器</strong> （<em>解码</em>)：第二部分接收压缩编码并尝试重建原始数据。</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E5%A6%82%E4%BD%95%E5%B7%A5%E4%BD%9C%EF%BC%9F"></span>自动编码器如何工作？<span class="ez-toc-section-end"></span></h2>



<p>自动编码器的操作可以分为几个步骤：</p>



<ol class="wp-block-list">
<li>网络接收数据作为输入。</li>



<li>编码器将数据压缩成特征向量，称为代码或潜在空间。</li>



<li>解码器采用该向量并尝试重建初始数据。</li>



<li>重建的质量是使用损失函数来测量的，该函数评估原始输入和重建输出之间的差异。</li>



<li>网络通过反向传播算法调整其权重，以最小化该损失函数。</li>
</ol>



<p>通过这个迭代过程，自动编码器学习数据的有效表示，重点是在重建过程中保留最重要的特征。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8"></span>自动编码器的实际应用<span class="ez-toc-section-end"></span></h3>



<p>自动编码器用途广泛，可应用于多个领域：</p>



<ul class="wp-block-list">
<li><strong>降维</strong>：类似于PCA（主成分分析），但具有非线性能力。</li>



<li><strong>去噪</strong>：他们能够学会忽略数据中的“噪音”。</li>



<li><strong>数据压缩</strong>：他们可以学习比传统压缩方法更有效的编码。</li>



<li><strong>数据生成</strong>：通过导航潜在空间，它们允许创建类似于原始条目的新数据实例。</li>



<li><strong>异常检测</strong>：自动编码器可以帮助发现不符合学习分布的数据。</li>
</ul>



<p>简而言之，自动编码器发现和定义有意义的数据特征的能力使它们成为任何人工智能从业者工具包中的必备工具。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%EF%BC%9A%E7%BC%96%E7%A0%81%E3%80%81%E7%93%B6%E9%A2%88%E5%92%8C%E8%A7%A3%E7%A0%81"></span>自动编码器：编码、瓶颈和解码<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png" alt="" class="wp-image-1191" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E7%BC%96%E7%A0%81"></span>编码<span class="ez-toc-section-end"></span></h3>



<p>编码或编码阶段涉及将输入数据转换为压缩表示。初始数据可能很大，被输入到自动编码器网络中。网络的各层将逐渐降低数据的维度，将重要信息压缩到更小的表示空间中。网络的每一层都由应用非线性变换的神经元组成，例如使用 ReLU 或 Sigmoid 等激活函数，以获得保留基本信息的新数据表示。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E7%93%B6%E9%A2%88"></span>瓶颈<span class="ez-toc-section-end"></span></h4>



<p>瓶颈是自动编码器的中心部分，其中数据表示达到最低维度，也称为代码。正是这种压缩表示保留了输入数据最重要的特征。瓶颈充当过滤器，迫使自动编码器学习压缩信息的有效方法。这可以与数据压缩的一种形式进行比较，但压缩是从数据中自动学习的，而不是由标准算法定义的。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E8%A7%A3%E7%A0%81"></span>解码<span class="ez-toc-section-end"></span></h4>



<p>解码阶段是与编码对称的步骤，其中压缩表示被重构为输出，其目标是尽可能忠实于原始输入。从瓶颈表示开始，神经网络会逐渐增加数据的维度。这是编码的逆过程：连续的层根据简化的表示重建初始特征。如果解码有效，则自动编码器的输出应该非常接近原始数据。</p>



<p>在无监督学习中，自动编码器对于理解数据的底层结构特别有用。这些网络的有效性不是通过其完美再现输入的能力来衡量的，而是通过其捕获代码中数据最显着和相关属性的能力来衡量的。然后，该代码可用于降维、可视化等任务，甚至可以用于更复杂架构中的其他神经网络的预处理。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8%E5%92%8C%E5%8F%98%E4%BD%93"></span>自动编码器的实际应用和变体<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png" alt="" class="wp-image-1192" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>L&#8217;<strong>自动编码器</strong>是人工智能 (AI) 驱动的深度学习库中的关键组成部分，它是一种神经网络，旨在将数据编码为较低维的表示形式，并以可以进行相关重建的方式对其进行分解。让我们检查一下它们 <strong>实际应用</strong> 以及这个迷人领域中出现的变体。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%AE%9E%E9%99%85%E5%BA%94%E7%94%A8-2"></span>自动编码器的实际应用<span class="ez-toc-section-end"></span></h3>



<p>由于自动编码器能够在没有监督的情况下学习有效且有意义的数据表示，因此已经进入了多种应用程序。这里有些例子：</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E9%99%8D%E7%BB%B4"></span>降维<span class="ez-toc-section-end"></span></h4>



<p>与 PCA（主成分分析）一样，自动编码器经常用于 <strong>降维</strong>。该技术可以通过减少要考虑的变量数量来简化数据处理，同时保留原始数据集中包含的大部分信息。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E5%99%AA%E9%9F%B3%E6%B6%88%E9%99%A4%EF%BC%88%E5%8E%BB%E5%99%AA%EF%BC%89"></span>噪音消除（去噪）<span class="ez-toc-section-end"></span></h4>



<p>自动编码器具有学习从部分破坏的数据中重建输入的能力，因此对于 <strong>噪音消除</strong>。尽管有噪音的干扰，它们仍然能够识别并恢复有用的数据。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E6%95%B0%E6%8D%AE%E5%8E%8B%E7%BC%A9"></span>数据压缩<span class="ez-toc-section-end"></span></h4>



<p>通过学习将数据编码为更紧凑的形式，自动编码器可用于 <strong>数据压缩</strong>。尽管它们在实践中尚未广泛用于此目的，但它们的潜力是巨大的，特别是对于压缩特定数据类型。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E6%95%B0%E6%8D%AE%E7%94%9F%E6%88%90%E5%92%8C%E4%BC%B0%E7%AE%97"></span>数据生成和估算<span class="ez-toc-section-end"></span></h4>



<p>自动编码器能够生成与其训练数据相似的新数据实例。该能力还可以用于 <strong>归因</strong>，这涉及填充数据集中缺失的数据。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E5%8F%98%E4%BD%93"></span>自动编码器变体<span class="ez-toc-section-end"></span></h3>



<p>除了标准自动编码器之外，还开发了各种变体来适应数据的具体情况和所需的任务。以下是一些值得注意的变化：</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E5%8F%98%E5%88%86%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8_VAE"></span>变分自动编码器 (VAE)<span class="ez-toc-section-end"></span></h4>



<p>这 <strong>变分自动编码器</strong> （<strong>VAE</strong>）添加一个允许生成数据的随机层。 VAE 在图像或音乐等内容的生成中特别受欢迎，因为它们可以根据同一模型生成新的、多样化的元素。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E7%A8%80%E7%96%8F%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8"></span>稀疏自动编码器<span class="ez-toc-section-end"></span></h4>



<p>这 <strong>稀疏自动编码器</strong> 纳入对隐藏节点施加有限活动的惩罚。它们可以有效地发现数据的独特特征，这使得它们对于 <strong>分类</strong> 和 <strong>异常检测</strong>。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E5%8E%BB%E5%99%AA%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8"></span>去噪自动编码器<span class="ez-toc-section-end"></span></h4>



<p>这 <strong>非规范化自动编码器</strong> 旨在抵抗将噪声引入输入数据。它们对于学习稳健的表示和 <strong>数据预处理</strong> 在执行其他机器学习任务之前。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E9%A1%BA%E5%BA%8F%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8"></span>顺序自动编码器<span class="ez-toc-section-end"></span></h4>



<p>这 <strong>顺序自动编码器</strong> 处理按顺序组织的数据，例如文本或时间序列。他们经常使用 LSTM（长短期记忆）等循环网络来随着时间的推移对信息进行编码和解码。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="%E5%A6%82%E4%BD%95%E8%AE%AD%E7%BB%83%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E5%92%8C%E4%BB%A3%E7%A0%81%E7%A4%BA%E4%BE%8B"></span>如何训练自动编码器和代码示例<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png" alt="" class="wp-image-1193" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2.png 1792w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-300x171.png 300w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1024x585.png 1024w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-150x86.png 150w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-768x439.png 768w, /images/blog/Quest-ce-quun-auto-encodeur-Le-guide-complet-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>的培训 <strong>自动编码器</strong> 是机器学习领域中用于降维和异常检测等应用的一项重要任务。在这里我们将看到如何使用 Python 和库来训练这样的模型 <strong>喀拉斯</strong>，以及您可以测试并适应您的项目的代码示例。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E8%AE%AD%E7%BB%83%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E8%BF%87%E7%A8%8B"></span>训练自动编码器的过程<span class="ez-toc-section-end"></span></h4>



<p>为了训练自动编码器，通常使用一种损失度量，例如均方误差 (MSE)，它测量原始输入与其重建之间的差异。训练的目标是最小化这种损失函数。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Keras_%E7%9A%84%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81"></span>Keras 的示例代码<span class="ez-toc-section-end"></span></h4>



<p>这是使用训练自动编码器的简单示例 <strong>喀拉斯</strong>：</p>



<pre class="wp-block-code"><code>

从 keras.layers 导入输入，密集
从 keras.models 导入模型

# 入口尺寸
# 潜在空间的维度（特征表示）
编码_dim = 32

# 编码器的定义
input_img = 输入（形状=（input_dim，））
编码=密集（encoding_dim，激活='relu'）（input_img）

# 解码器的定义
解码=密集（input_dim，激活='sigmoid'）（编码）

# 自动编码器模型
自动编码器=模型（input_img，解码）

# 模型编译
autoencoder.compile（优化器='adam'，损失='binary_crossentropy'）

# 自动编码器训练
自动编码器.fit(X_train,
                纪元=50，
                批量大小=256，
                随机播放=真，
                验证数据=（X_测试，X_测试））

</code></pre>



<p>在此示例中，“X_train”和“X_test”代表训练和测试数据。请注意，自动编码器经过训练以将其自己的输入“X_train”预测为输出。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E8%89%AF%E5%A5%BD%E9%94%BB%E7%82%BC%E7%9A%84%E7%A7%98%E8%AF%80"></span>良好锻炼的秘诀<span class="ez-toc-section-end"></span></h4>



<p></p>



<p>使用类似的技术 <strong>交叉验证</strong>， 那里 <strong>批量归一化</strong> 和 <strong>回调</strong> Keras 还可以帮助提高自动编码器驱动的性能和稳定性。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E8%87%AA%E5%8A%A8%E7%BC%96%E7%A0%81%E5%99%A8%E7%9A%84%E5%BA%94%E7%94%A8"></span>自动编码器的应用<span class="ez-toc-section-end"></span></h4>



<p>训练后，自动编码器可用于：</p>



<ul class="wp-block-list">
<li>降维，</li>



<li>异常检测，</li>



<li>对其他机器学习任务有用的描述符的无监督学习。</li>
</ul>



<p>总而言之，训练自动编码器是一项需要了解神经网络架构和微调超参数的经验的任务。然而，自动编码器的简单性和灵活性使其成为解决许多数据处理问题的宝贵工具。</p>



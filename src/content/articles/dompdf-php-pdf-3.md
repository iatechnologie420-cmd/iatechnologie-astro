---

title: "Dompdf: PHP でエレガントな PDF を作成するには?"
slug: "dompdf-php-pdf-3"
excerpt: "Dompdf の概要 Dompdf は、HTML コンテンツから PDF ファイルを生成できる PHP ライブラリです。このソリューションは、レポート、請求書、またはその他のドキュメントを PDF 形式で生成する場合に非常に役立ちます。この記事では、Dompdf の基本機能を発見し、それを使用してエレガントで機能的な PDF を作成する方法を学びます。 前提条件 Dompdf をインストールする前に、以下があることを確認してください。 Dompdf のインストール Dompdf をインストールするには、次の手順に従います。 Dompdf がインストールされたので、Web アプリケーションでエレガントで機能的な PDF ファイルの生成を開始できます。 Dompdf は、画像、カスタム フォント、CSS スタイルの管理など、PDF レンダリングをカスタマイズするための多くの高度な機能を提供します。 PHP でエレガントな PDF を作成する Dompdf をインストールして使用する別の方法 従うべき手順は次のとおりです。1. 公式 Web サイトから Dompdf の最新バージョンをダウンロードします。2. ダウンロードしたファイルを解凍し、PHP プロジェクトに配置します。3. Dompdfautoload.php ファイルをインクルードして、ライブラリを PHP スクリプトにロードします。 HTML テンプレートから PDF を作成する Dompdf をインストールしたので、HTML [&hellip;]"
date: "2024-03-09T12:41:03"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["%e3%82%b3%e3%83%b3%e3%83%94%e3%83%a5%e3%83%bc%e3%83%86%e3%82%a3%e3%83%b3%e3%82%b0%e3%81%a8%e3%83%87%e3%83%bc%e3%82%bf-ja", "%e3%83%86%e3%82%af%e3%83%8e%e3%83%ad%e3%82%b8%e3%83%bc%e3%81%a8%e3%83%87%e3%82%b8%e3%82%bf%e3%83%ab-ja"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#Dompdf_%E3%81%AE%E6%A6%82%E8%A6%81" >Dompdf の概要</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6" >前提条件</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#Dompdf_%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB" >Dompdf のインストール</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#Dompdf_%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E6%9C%80%E5%88%9D%E3%81%AE_PDF_%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88" >Dompdf を使用した最初の PDF ドキュメント</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#PHP_%E3%81%A7%E3%82%A8%E3%83%AC%E3%82%AC%E3%83%B3%E3%83%88%E3%81%AA_PDF_%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B" >PHP でエレガントな PDF を作成する</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#Dompdf_%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%A6%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E5%88%A5%E3%81%AE%E6%96%B9%E6%B3%95" >Dompdf をインストールして使用する別の方法</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#HTML_%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89_PDF_%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B" >HTML テンプレートから PDF を作成する</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#%E7%94%BB%E5%83%8F%E3%81%A8%E3%83%95%E3%82%A9%E3%83%B3%E3%83%88%E3%81%AE%E7%AE%A1%E7%90%86" >画像とフォントの管理</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/ja/dompdf-php-%e3%81%a7%e3%82%a8%e3%83%ac%e3%82%ac%e3%83%b3%e3%83%88%e3%81%aa-pdf-%e3%82%92%e4%bd%9c%e6%88%90%e3%81%99%e3%82%8b%e3%81%ab%e3%81%af/#%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%A8_Dompdf_%E3%81%AE%E5%95%8F%E9%A1%8C%E3%81%AE%E4%BF%AE%E6%AD%A3" >レンダリングの最適化と Dompdf の問題の修正</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_%E3%81%AE%E6%A6%82%E8%A6%81"></span>Dompdf の概要<span class="ez-toc-section-end"></span></h2>



<p>Dompdf は、HTML コンテンツから PDF ファイルを生成できる PHP ライブラリです。このソリューションは、レポート、請求書、またはその他のドキュメントを PDF 形式で生成する場合に非常に役立ちます。この記事では、Dompdf の基本機能を発見し、それを使用してエレガントで機能的な PDF を作成する方法を学びます。</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6"></span>前提条件<span class="ez-toc-section-end"></span></h3>



<p>Dompdf をインストールする前に、以下があることを確認してください。</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf には PHP 5.4 以上が必要です。 PHP のバージョン 7.x と互換性があります。</li>



<li><strong>PHP 拡張機能:</strong> PHP 拡張機能 mbstring、DOM、GD が有効になっていることを確認してください。これらの拡張機能は、Dompdf が適切に機能するために不可欠です。</li>



<li><strong>作成:</strong> Dompdf は、PHP の依存関係マネージャーである Composer 経由で配布されます。システムに Composer がインストールされていることを確認してください。</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB"></span>Dompdf のインストール<span class="ez-toc-section-end"></span></h4>



<p>Dompdf をインストールするには、次の手順に従います。</p>



<ol class="wp-block-list">
<li><strong>新しい PHP プロジェクトを作成します。</strong> 既存のプロジェクトがない場合は、選択した基本構造を使用して新しいプロジェクトを作成します。</li>



<li><strong>Composer 経由で Dompdf 依存関係を追加します。</strong> コンソールを開き、プロジェクト ディレクトリに移動します。次のコマンドを実行して、Dompdf をプロジェクトに追加します。     <pre><code>作曲家には dompdf/dompdf が必要です</code></pre>     このコマンドは、Dompdf をその依存関係とともに自動的にダウンロードしてインストールします。</li>



<li><strong>アプリケーションで Dompdf を使用します。</strong> これで、プロジェクトで Dompdf を使用できるようになりました。 Dompdf を使用して PDF ファイルを作成する方法はたくさんありますが、始めるための基本的な例を次に示します。
<pre><code>// Composer オートローダーを含めます
'vendor/autoload.php' が必要です。

// 新しい Dompdf オブジェクトを作成します
$dompdf = 新しい Dompdf();

// ファイルまたは文字列から HTML コンテンツをロードします
$html = '<h1><span class="ez-toc-section" id="Dompdf_%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%9F%E6%9C%80%E5%88%9D%E3%81%AE_PDF_%E3%83%89%E3%82%AD%E3%83%A5%E3%83%A1%E3%83%B3%E3%83%88"></span>Dompdf を使用した最初の PDF ドキュメント<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// PDF ドキュメントをレンダリングします
$dompdf->render();

// PDF ドキュメントを出力に送信します
$dompdf->stream('document.pdf');</code></pre>
    この例では、タイトル付きの新しい PDF ドキュメントを作成し、それを「document.pdf」ファイルとしてアップロードします。必要に応じて HTML コンテンツをカスタマイズできます。</li>
</ol>



<p>Dompdf がインストールされたので、Web アプリケーションでエレガントで機能的な PDF ファイルの生成を開始できます。 Dompdf は、画像、カスタム フォント、CSS スタイルの管理など、PDF レンダリングをカスタマイズするための多くの高度な機能を提供します。</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="PHP_%E3%81%A7%E3%82%A8%E3%83%AC%E3%82%AC%E3%83%B3%E3%83%88%E3%81%AA_PDF_%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B"></span>PHP でエレガントな PDF を作成する<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf_%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%A6%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E5%88%A5%E3%81%AE%E6%96%B9%E6%B3%95"></span>Dompdf をインストールして使用する別の方法<span class="ez-toc-section-end"></span></h3>



<p>従うべき手順は次のとおりです。<br>1. 公式 Web サイトから Dompdf の最新バージョンをダウンロードします。<br>2. ダウンロードしたファイルを解凍し、PHP プロジェクトに配置します。<br>3. Dompdfautoload.php ファイルをインクルードして、ライブラリを PHP スクリプトにロードします。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="HTML_%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89_PDF_%E3%82%92%E4%BD%9C%E6%88%90%E3%81%99%E3%82%8B"></span>HTML テンプレートから PDF を作成する<span class="ez-toc-section-end"></span></h4>



<p>Dompdf をインストールしたので、HTML テンプレートを使用して PDF を作成する方法を見てみましょう。次の手順を実行します：</p>



<p>1. PDF に必要な構造とレイアウトを含む HTML ファイルを作成します。<br>2. CSS 機能を使用して、font-family、font-size、border などのプロパティを使用してドキュメントのスタイルを設定します。<br>3. 「{{name}}」や「{{address}}」などの Dompdf 固有のタグを使用して動的データを含めます。<br>4. Dompdf クラスを使用して、作成した HTML テンプレートを使用して PDF を生成します。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E7%94%BB%E5%83%8F%E3%81%A8%E3%83%95%E3%82%A9%E3%83%B3%E3%83%88%E3%81%AE%E7%AE%A1%E7%90%86"></span>画像とフォントの管理<span class="ez-toc-section-end"></span></h4>



<p>スタイリッシュな PDF を作成する場合、多くの場合、画像を含めたり、特定のフォントを使用したりする必要があります。 Dompdf を使用してそれを行う方法は次のとおりです。</p>



<p>1. タグを使用して HTML テンプレートに画像を含めます <img decoding="async" src="chemin_vers_image">。<br>2. Dompdf にはデフォルトですべてのフォントが含まれていないことに注意してください。 CSS で @font-face を使用するか、Dompdf によって提供されるフォントを使用して、カスタム フォントを追加できます。</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="%E3%83%AC%E3%83%B3%E3%83%80%E3%83%AA%E3%83%B3%E3%82%B0%E3%81%AE%E6%9C%80%E9%81%A9%E5%8C%96%E3%81%A8_Dompdf_%E3%81%AE%E5%95%8F%E9%A1%8C%E3%81%AE%E4%BF%AE%E6%AD%A3"></span>レンダリングの最適化と Dompdf の問題の修正<span class="ez-toc-section-end"></span></h4>



<p>PDF のレンダリングまたはファイルの生成で問題が発生する場合があります。それらを解決するためのヒントをいくつか紹介します。</p>



<p>1. HTML テンプレートが正しく構築され、有効であることを確認します。<br>2. すべての外部リソース (画像、フォントなど) がサーバーからアクセスできることを確認します。<br>3. Dompdf デバッグ モードをアクティブにし、表示されたエラーを確認してコードをデバッグします。<br>4. 一般的な構成と問題の詳細については、Dompdf ドキュメントを参照してください。</p>



<p>Dompdf を使用すると、プロフェッショナルで適切にフォーマットされた PDF ドキュメントを配信することで、強化されたユーザー エクスペリエンスを提供できます。レポート、請求書、その他の種類のドキュメントを生成する場合、Dompdf は信頼性が高く強力な選択肢です。</p>



<p>結論として、Composer のおかげで、Dompdf のインストールは迅速かつ簡単です。インストールしたら、Web アプリケーションのニーズを満たす高品質の PDF ファイルの作成を開始できます。 Dompdf の機能と利用可能なカスタマイズ オプションの詳細については、公式 Dompdf ドキュメントを必ずチェックしてください。</p>



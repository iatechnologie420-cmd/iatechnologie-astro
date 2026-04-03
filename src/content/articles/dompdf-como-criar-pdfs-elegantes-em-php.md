---
title: "Dompdf: Como criar PDFs elegantes em PHP?"
slug: "dompdf-como-criar-pdfs-elegantes-em-php"
excerpt: "Introdução ao Dompdf Dompdf é uma biblioteca PHP que permite gerar arquivos PDF a partir de conteúdo HTML. Esta solução é muito útil para gerar relatórios, faturas ou qualquer outro documento em formato PDF. Neste artigo descobriremos os recursos básicos do Dompdf e aprenderemos como usá-lo para criar PDFs elegantes e funcionais. Pré-requisitos Antes de [&hellip;]"
date: "2024-03-09T12:42:54"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["computacao-e-dados-pt", "tecnologia-e-digital-pt"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Introducao_ao_Dompdf" >Introdução ao Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Pre-requisitos" >Pré-requisitos</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Instalacao_dompdf" >Instalação dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Meu_primeiro_documento_PDF_com_Dompdf" >Meu primeiro documento PDF com Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Criando_um_PDF_elegante_em_PHP" >Criando um PDF elegante em PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Outro_metodo_de_instalacao_e_uso_do_Dompdf" >Outro método de instalação e uso do Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Criando_um_PDF_a_partir_de_um_modelo_HTML" >Criando um PDF a partir de um modelo HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Gerenciando_imagens_e_fontes" >Gerenciando imagens e fontes</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/pt/dompdf-como-criar-pdfs-elegantes-em-php/#Otimizando_a_renderizacao_e_corrigindo_problemas_do_Dompdf" >Otimizando a renderização e corrigindo problemas do Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introducao_ao_Dompdf"></span>Introdução ao Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf é uma biblioteca PHP que permite gerar arquivos PDF a partir de conteúdo HTML. Esta solução é muito útil para gerar relatórios, faturas ou qualquer outro documento em formato PDF. Neste artigo descobriremos os recursos básicos do Dompdf e aprenderemos como usá-lo para criar PDFs elegantes e funcionais.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Pre-requisitos"></span>Pré-requisitos<span class="ez-toc-section-end"></span></h3>



<p>Antes de instalar o Dompdf, certifique-se de ter o seguinte:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf requer PHP >= 5.4. É compatível com as versões 7.x do PHP.</li>



<li><strong>Extensões PHP:</strong> Certifique-se de ter habilitado as seguintes extensões PHP: mbstring, DOM e GD. Estas extensões são essenciais para o bom funcionamento do Dompdf.</li>



<li><strong>Compor:</strong> Dompdf é distribuído via Composer, que é um gerenciador de dependências para PHP. Certifique-se de ter o Composer instalado em seu sistema.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Instalacao_dompdf"></span>Instalação dompdf<span class="ez-toc-section-end"></span></h4>



<p>Para instalar o Dompdf, siga os seguintes passos:</p>



<ol class="wp-block-list">
<li><strong>Crie um novo projeto PHP:</strong> Se você ainda não possui um projeto, crie um novo usando a estrutura básica de sua escolha.</li>



<li><strong>Adicione a dependência Dompdf via Composer:</strong> Abra um console e navegue até o diretório do seu projeto. Execute o seguinte comando para adicionar Dompdf ao seu projeto:     <pre><code>compositor requer dompdf/dompdf</code></pre>     Este comando irá baixar e instalar automaticamente o Dompdf junto com suas dependências.</li>



<li><strong>Use Dompdf em sua aplicação:</strong> Agora você pode usar Dompdf em seu projeto. Há muitas maneiras de criar arquivos PDF com Dompdf, mas aqui está um exemplo básico para você começar:
<pre><code>// Inclui o autoloader do Composer
requer 'vendor/autoload.php';

// Cria um novo objeto Dompdf
$dompdf = novo Dompdf();

// Carrega conteúdo HTML de um arquivo ou string
$html = '<h1><span class="ez-toc-section" id="Meu_primeiro_documento_PDF_com_Dompdf"></span>Meu primeiro documento PDF com Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Renderiza o documento PDF
$dompdf->renderizar();

//Envia documento PDF para saída
$dompdf->stream('document.pdf');</code></pre>
    Este exemplo cria um novo documento PDF com um título e carrega-o como um arquivo “document.pdf”. Você pode personalizar o conteúdo HTML de acordo com suas necessidades.</li>
</ol>



<p>Agora que o Dompdf está instalado, você pode começar a gerar arquivos PDF elegantes e funcionais em seus aplicativos da web. Dompdf oferece muitos recursos avançados para personalizar a renderização de PDF, como gerenciamento de imagens, fontes personalizadas e estilos CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Criando_um_PDF_elegante_em_PHP"></span>Criando um PDF elegante em PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Outro_metodo_de_instalacao_e_uso_do_Dompdf"></span>Outro método de instalação e uso do Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Aqui estão as etapas a seguir:<br>1. Baixe a versão mais recente do Dompdf no site oficial.<br>2. Extraia os arquivos baixados e coloque-os em seu projeto PHP.<br>3. Inclua o arquivo Dompdfautoload.php para carregar a biblioteca em seu script PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Criando_um_PDF_a_partir_de_um_modelo_HTML"></span>Criando um PDF a partir de um modelo HTML<span class="ez-toc-section-end"></span></h4>



<p>Agora que instalamos o Dompdf, veremos como criar um PDF usando um modelo HTML. Siga esses passos:</p>



<p>1. Crie um arquivo HTML contendo a estrutura e o layout desejado para o seu PDF.<br>2. Use recursos CSS para estilizar seu documento, usando propriedades como família de fontes, tamanho da fonte, borda, etc.<br>3. Inclua dados dinâmicos usando tags específicas do Dompdf, como &#8220;{{name}}&#8221; ou &#8220;{{address}}&#8221;.<br>4. Use a classe Dompdf para gerar o PDF usando o modelo HTML que você criou.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gerenciando_imagens_e_fontes"></span>Gerenciando imagens e fontes<span class="ez-toc-section-end"></span></h4>



<p>Ao criar PDFs elegantes, muitas vezes é necessário incluir imagens ou usar fontes específicas. Veja como fazer isso com Dompdf:</p>



<p>1. Inclua imagens em seu modelo HTML usando a tag <img decoding="async" src="chemin_vers_image">.<br>2. Observe que Dompdf não inclui todas as fontes por padrão. Você pode adicionar fontes personalizadas usando @font-face em seu CSS ou usando fontes fornecidas pelo Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Otimizando_a_renderizacao_e_corrigindo_problemas_do_Dompdf"></span>Otimizando a renderização e corrigindo problemas do Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Às vezes, você pode encontrar problemas ao renderizar seu PDF ou gerar os arquivos. Aqui estão algumas dicas para resolvê-los:</p>



<p>1. Verifique se o seu modelo HTML está construído corretamente e é válido.<br>2. Certifique-se de que todos os recursos externos (imagens, fontes, etc.) estejam acessíveis no servidor.<br>3. Depure seu código ativando o modo de depuração Dompdf e verificando os erros exibidos.<br>4. Consulte a documentação do Dompdf para obter mais informações sobre configurações e problemas comuns.</p>



<p>Usando Dompdf, você pode fornecer uma experiência de usuário aprimorada, fornecendo documentos PDF profissionais e bem formatados. Seja gerando relatórios, faturas ou outros tipos de documentos, o Dompdf é uma escolha confiável e poderosa.</p>



<p>Concluindo, instalar o Dompdf é rápido e fácil graças ao Composer. Depois de instalado, você pode começar a criar arquivos PDF de alta qualidade para atender às necessidades de seu aplicativo da web. Não se esqueça de conferir a documentação oficial do Dompdf para saber mais sobre seus recursos e opções de personalização disponíveis.</p>



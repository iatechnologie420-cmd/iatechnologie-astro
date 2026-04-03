---

title: "Dompdf: ¿Cómo crear archivos PDF elegantes en PHP?"
slug: "dompdf-como-crear-archivos-pdf-elegantes-en-php"
excerpt: "Introducción a Dompdf Dompdf es una biblioteca PHP que le permite generar archivos PDF a partir de contenido HTML. Esta solución es muy útil para generar informes, facturas o cualquier otro documento en formato PDF. En este artículo, descubriremos las características básicas de Dompdf y aprenderemos cómo usarlo para crear archivos PDF elegantes y funcionales. [&hellip;]"
date: "2024-03-09T12:40:14"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["computacion-y-datos-es", "tecnologia-y-digital-es"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Introduccion_a_Dompdf" >Introducción a Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Requisitos_previos" >Requisitos previos</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#instalacion_de_dompdf" >instalación de dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Mi_primer_documento_PDF_con_Dompdf" >Mi primer documento PDF con Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Creando_un_PDF_elegante_en_PHP" >Creando un PDF elegante en PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Otro_metodo_para_instalar_y_utilizar_Dompdf" >Otro método para instalar y utilizar Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Crear_un_PDF_a_partir_de_una_plantilla_HTML" >Crear un PDF a partir de una plantilla HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Administrar_imagenes_y_fuentes" >Administrar imágenes y fuentes</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/es/dompdf-como-crear-archivos-pdf-elegantes-en-php/#Optimizacion_del_renderizado_y_solucion_de_problemas_de_Dompdf" >Optimización del renderizado y solución de problemas de Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introduccion_a_Dompdf"></span>Introducción a Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf es una biblioteca PHP que le permite generar archivos PDF a partir de contenido HTML. Esta solución es muy útil para generar informes, facturas o cualquier otro documento en formato PDF. En este artículo, descubriremos las características básicas de Dompdf y aprenderemos cómo usarlo para crear archivos PDF elegantes y funcionales.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Requisitos_previos"></span>Requisitos previos<span class="ez-toc-section-end"></span></h3>



<p>Antes de instalar Dompdf, asegúrese de tener lo siguiente:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf requiere PHP >= 5.4. Es compatible con las versiones 7.x de PHP.</li>



<li><strong>Extensiones PHP:</strong> Asegúrese de haber habilitado las siguientes extensiones PHP: mbstring, DOM y GD. Estas extensiones son esenciales para el correcto funcionamiento de Dompdf.</li>



<li><strong>Redactar:</strong> Dompdf se distribuye a través de Composer, que es un administrador de dependencias para PHP. Asegúrese de tener Composer instalado en su sistema.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="instalacion_de_dompdf"></span>instalación de dompdf<span class="ez-toc-section-end"></span></h4>



<p>Para instalar Dompdf, siga los siguientes pasos:</p>



<ol class="wp-block-list">
<li><strong>Crea un nuevo proyecto PHP:</strong> Si aún no tiene un proyecto existente, cree uno nuevo utilizando la estructura básica de su elección.</li>



<li><strong>Agregue la dependencia Dompdf a través de Composer:</strong> Abra una consola y navegue hasta el directorio de su proyecto. Ejecute el siguiente comando para agregar Dompdf a su proyecto:     <pre><code>el compositor requiere dompdf/dompdf</code></pre>     Este comando descargará e instalará automáticamente Dompdf junto con sus dependencias.</li>



<li><strong>Utilice Dompdf en su aplicación:</strong> Ahora puedes usar Dompdf en tu proyecto. Hay muchas formas de crear archivos PDF con Dompdf, pero aquí tienes un ejemplo básico para empezar:
<pre><code>// Incluir el cargador automático de Composer
requiere 'proveedor/autoload.php';

// Crea un nuevo objeto Dompdf
$dompdf = nuevo Dompdf();

// Carga contenido HTML desde un archivo o cadena
$html = '<h1><span class="ez-toc-section" id="Mi_primer_documento_PDF_con_Dompdf"></span>Mi primer documento PDF con Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Renderizar el documento PDF
$dompdf->render();

// Enviar documento PDF a salida
$dompdf->stream('documento.pdf');</code></pre>
    Este ejemplo crea un nuevo documento PDF con un título y lo carga como un archivo &#8220;document.pdf&#8221;. Puede personalizar el contenido HTML según sus necesidades.</li>
</ol>



<p>Ahora que tiene Dompdf instalado, puede comenzar a generar archivos PDF elegantes y funcionales en sus aplicaciones web. Dompdf ofrece muchas funciones avanzadas para personalizar la representación de PDF, como la gestión de imágenes, fuentes personalizadas y estilos CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Creando_un_PDF_elegante_en_PHP"></span>Creando un PDF elegante en PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Otro_metodo_para_instalar_y_utilizar_Dompdf"></span>Otro método para instalar y utilizar Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Estos son los pasos a seguir:<br>1. Descargue la última versión de Dompdf del sitio web oficial.<br>2. Extraiga los archivos descargados y colóquelos en su proyecto PHP.<br>3. Incluya el archivo Dompdfautoload.php para cargar la biblioteca en su script PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Crear_un_PDF_a_partir_de_una_plantilla_HTML"></span>Crear un PDF a partir de una plantilla HTML<span class="ez-toc-section-end"></span></h4>



<p>Ahora que hemos instalado Dompdf, veremos cómo crear un PDF usando una plantilla HTML. Sigue estos pasos:</p>



<p>1. Cree un archivo HTML que contenga la estructura y el diseño que desea para su PDF.<br>2. Utilice funciones CSS para diseñar su documento, utilizando propiedades como familia de fuentes, tamaño de fuente, borde, etc.<br>3. Incluya datos dinámicos utilizando etiquetas específicas de Dompdf, como &#8220;{{name}}&#8221; o &#8220;{{address}}&#8221;.<br>4. Utilice la clase Dompdf para generar el PDF utilizando la plantilla HTML que creó.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Administrar_imagenes_y_fuentes"></span>Administrar imágenes y fuentes<span class="ez-toc-section-end"></span></h4>



<p>Al crear archivos PDF con estilo, a menudo es necesario incluir imágenes o utilizar fuentes específicas. Aquí se explica cómo hacerlo con Dompdf:</p>



<p>1. Incluye imágenes en tu plantilla HTML usando la etiqueta <img decoding="async" src="chemin_vers_image">.<br>2. Tenga en cuenta que Dompdf no incluye todas las fuentes de forma predeterminada. Puede agregar fuentes personalizadas usando @font-face en su CSS o usando fuentes proporcionadas por Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimizacion_del_renderizado_y_solucion_de_problemas_de_Dompdf"></span>Optimización del renderizado y solución de problemas de Dompdf<span class="ez-toc-section-end"></span></h4>



<p>A veces puede encontrar problemas al renderizar su PDF o generar los archivos. A continuación se ofrecen algunos consejos para solucionarlos:</p>



<p>1. Verifique que su plantilla HTML esté correctamente construida y sea válida.<br>2. Asegúrese de que todos los recursos externos (imágenes, fuentes, etc.) sean accesibles desde el servidor.<br>3. Depure su código activando el modo de depuración de Dompdf y verificando los errores mostrados.<br>4. Consulte la documentación de Dompdf para obtener más información sobre configuraciones y problemas comunes.</p>



<p>Con Dompdf, puede proporcionar una experiencia de usuario mejorada al entregar documentos PDF profesionales y bien formateados. Ya sea generando informes, facturas u otro tipo de documentos, Dompdf es una opción confiable y poderosa.</p>



<p>En conclusión, instalar Dompdf es rápido y sencillo gracias a Composer. Una vez instalado, puede comenzar a crear archivos PDF de alta calidad para satisfacer las necesidades de su aplicación web. No olvide consultar la documentación oficial de Dompdf para obtener más información sobre sus características y opciones de personalización disponibles.</p>



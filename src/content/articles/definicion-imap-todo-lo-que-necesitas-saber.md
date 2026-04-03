---
title: "Definición IMAP: todo lo que necesitas saber"
slug: "definicion-imap-todo-lo-que-necesitas-saber"
excerpt: "Introducción a IMAP El Protocolo de acceso a mensajes de Internet (IMAP) es un estándar de comunicaciones que permite a los usuarios recibir y administrar sus correos electrónicos directamente en servidores de correo electrónico, lo que difiere del enfoque tradicional donde los correos electrónicos se descargan al cliente de correo electrónico local. Esto trae muchos [&hellip;]"
date: "2024-03-09T12:11:26"
featuredImage: "/images/blog/Tout-savoir-sur-le-protocole-IMAP-3.png"
categories: ["infraestructura-y-redes-es", "tecnologia-y-digital-es"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="What is SMTP - Simple Mail Transfer Protocol" width="500" height="375" src="https://www.youtube.com/embed/PJo5yOtu7o8?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Introduccion_a_IMAP" >Introducción a IMAP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Como_funciona_IMAP" >Cómo funciona IMAP</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Las_ventajas_de_IMAP" >Las ventajas de IMAP</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#IMAP_frente_a_POP3" >IMAP frente a POP3</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Caracteristicas_especiales_de_IMAP" >Características especiales de IMAP</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Comparacion_entre_IMAP_y_otros_protocolos_de_correo_electronico" >Comparación entre IMAP y otros protocolos de correo electrónico</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Introduccion_a_los_protocolos_de_correo_electronico" >Introducción a los protocolos de correo electrónico</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#POP3_El_protocolo_mas_antiguo" >POP3: El protocolo más antiguo</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#SMTP_Imprescindible_para_enviar_correos_electronicos" >SMTP: Imprescindible para enviar correos electrónicos</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Comparacion_de_caracteristicas" >Comparación de características</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#La_eleccion_segun_las_necesidades" >La elección según las necesidades.</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-12" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Configurar_y_optimizar_el_uso_de_IMAP" >Configurar y optimizar el uso de IMAP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-13" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Configuraciones_IMAP_basicas" >Configuraciones IMAP básicas</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-14" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Optimizacion_del_uso_de_IMAP" >Optimización del uso de IMAP</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-15" href="/es/definicion-imap-todo-lo-que-necesitas-saber/#Practicas_de_seguridad_con_IMAP" >Prácticas de seguridad con IMAP</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introduccion_a_IMAP"></span>Introducción a IMAP<span class="ez-toc-section-end"></span></h2>



<p>El Protocolo de acceso a mensajes de Internet (IMAP) es un estándar de comunicaciones que permite a los usuarios recibir y administrar sus correos electrónicos directamente en servidores de correo electrónico, lo que difiere del enfoque tradicional donde los correos electrónicos se descargan al cliente de correo electrónico local. Esto trae muchos beneficios prácticos, especialmente en un mundo donde accedemos a nuestros correos electrónicos desde múltiples dispositivos. En este artículo, exploraremos cómo funciona IMAP, sus beneficios y cómo se compara con otros protocolos como POP3.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Como_funciona_IMAP"></span>Cómo funciona IMAP<span class="ez-toc-section-end"></span></h3>



<p>EL <strong>IMAP</strong> es un protocolo que opera en el puerto 143, o en el puerto 993 para una versión segura llamada <strong>IMÁGENES</strong>. Cuando un usuario revisa su bandeja de entrada mediante IMAP, no descarga todo el contenido. En cambio, el correo electrónico permanece almacenado en el servidor y el cliente de correo electrónico muestra una vista previa. Esto permite al usuario organizar, filtrar y buscar sus correos electrónicos directamente en el servidor. Cuando se abre un correo electrónico, sólo entonces se descarga su contenido.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Las_ventajas_de_IMAP"></span>Las ventajas de IMAP<span class="ez-toc-section-end"></span></h4>



<p>El uso de <strong>IMAP</strong> ofrece varios beneficios clave:</p>



<ul class="wp-block-list">
<li><strong>Sincronización entre dispositivos</strong>: Editar un correo electrónico en un dispositivo lo editará en todos los dispositivos sincronizados.</li>



<li><strong>Gestión de correo electrónico en línea</strong>: La capacidad de leer y administrar correos electrónicos sin descargarlos ahorra tiempo y espacio de almacenamiento.</li>



<li><strong>Flexibilidad</strong>: Le permite manipular sus carpetas de correo electrónico y organizarlas desde cualquier interfaz de cliente IMAP.</li>



<li><strong>Robustez</strong>: Los correos electrónicos se almacenan en el servidor incluso después de leerlos, lo que proporciona seguridad adicional en caso de pérdida o rotura del dispositivo local.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="IMAP_frente_a_POP3"></span>IMAP frente a POP3<span class="ez-toc-section-end"></span></h4>



<p><strong>IMAP</strong> a menudo se compara con <strong>POP3</strong> (Protocolo de oficina de correos versión 3), otro protocolo para recibir correos electrónicos. La principal diferencia es que POP3 descarga los correos electrónicos en el dispositivo del usuario y, de forma predeterminada, los elimina del servidor. Esto significa que los mensajes sólo se pueden leer en un dispositivo, lo que resulta menos práctico en nuestro contexto multidispositivo. Además, con POP3 el archivado y organización de los correos electrónicos debe repetirse en cada dispositivo, mientras que con IMAP estas operaciones son universales y se reflejan en todos los dispositivos.</p>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-savoir-sur-le-protocole-IMAP.png" alt="" class="wp-image-1376" srcset="/images/blog/Tout-savoir-sur-le-protocole-IMAP.png 1792w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-300x171.png 300w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1024x585.png 1024w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-150x86.png 150w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-768x439.png 768w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Caracteristicas_especiales_de_IMAP"></span>Características especiales de IMAP<span class="ez-toc-section-end"></span></h4>



<p>                    Estas son algunas de las características que distinguen al protocolo IMAP:</p>



<ul class="wp-block-list">
<li><strong>Carpetas múltiples:</strong> Puede crear varias carpetas en el servidor de correo para organizar sus mensajes.</li>



<li><strong>Sincronización:</strong> A través de la sincronización, el cliente de correo electrónico refleja lo que hay en el servidor. Si elimina un mensaje en su teléfono, también desaparecerá en su cliente de escritorio.</li>



<li><strong>Gestión del estado de los mensajes:</strong> Los mensajes se pueden marcar como leídos, no leídos, eliminados o pausados ​​para un seguimiento posterior.</li>



<li><strong>Investigación:</strong> IMAP permite búsquedas complejas de mensajes directamente en el servidor sin necesidad de descargar mensajes localmente.</li>



<li><strong>Filtración:</strong> Es posible filtrar mensajes directamente en el servidor, permitiendo una mejor gestión del correo electrónico.</li>
</ul>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Comparacion_entre_IMAP_y_otros_protocolos_de_correo_electronico"></span>Comparación entre IMAP y otros protocolos de correo electrónico<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-savoir-sur-le-protocole-IMAP-1.png" alt="" class="wp-image-1377" srcset="/images/blog/Tout-savoir-sur-le-protocole-IMAP-1.png 1792w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-300x171.png 300w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-1024x585.png 1024w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-150x86.png 150w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-768x439.png 768w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Introduccion_a_los_protocolos_de_correo_electronico"></span>Introducción a los protocolos de correo electrónico<span class="ez-toc-section-end"></span></h3>



<p>                Antes de comparar <strong>IMAP</strong> (Protocolo de acceso a mensajes de Internet) junto con otros protocolos, es importante comprender qué son los protocolos de mensajería. Son estándares que permiten a los usuarios recibir y enviar correos electrónicos a través de redes de servidores de correo. Cada protocolo tiene sus propias particularidades, ventajas y desventajas, que dictan cómo se almacenan, gestionan y acceden a los mensajes.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="POP3_El_protocolo_mas_antiguo"></span>POP3: El protocolo más antiguo<span class="ez-toc-section-end"></span></h4>



<p>                EL <strong>POP3</strong> (Protocolo de oficina postal versión 3) es un protocolo más antiguo que se centra en descargar correos electrónicos desde el servidor al dispositivo local del usuario. Una vez descargados, generalmente ya no se puede acceder a los correos electrónicos a través del servidor. Esto puede resultar limitante para el usuario que desea acceder a sus correos electrónicos desde múltiples dispositivos, pero ofrece la ventaja de poder ver sus correos electrónicos sin conexión.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="SMTP_Imprescindible_para_enviar_correos_electronicos"></span>SMTP: Imprescindible para enviar correos electrónicos<span class="ez-toc-section-end"></span></h4>



<p>                <strong>SMTP</strong> (Protocolo simple de transferencia de correo) es el protocolo estándar para enviar correos electrónicos. Se utiliza junto con <strong>IMAP</strong> O <strong>POP3</strong>, que gestionan la recepción de mensajes. <strong>SMTP</strong> es necesario para enviar correos electrónicos, pero no maneja la recepción o sincronización de mensajes entre diferentes dispositivos.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Comparacion_de_caracteristicas"></span>Comparación de características<span class="ez-toc-section-end"></span></h4>



<figure class="wp-block-table"><table><tbody><tr><td>Protocolo</td><td>Descripción</td><td>Acceso a correos electrónicos</td><td>Gestión de múltiples dispositivos</td><td>Fuera de linea</td></tr><tr><td><strong>IMAP</strong></td><td>Gestión avanzada de correo electrónico en el servidor.</td><td>En cualquier lugar, siempre y cuando esté conectado a Internet.</td><td>Sí, sincronización en tiempo real.</td><td>Sólo lectura, en caché.</td></tr><tr><td><strong>POP3</strong></td><td>Descarga de correos electrónicos al dispositivo.</td><td>Solo en el dispositivo descargado.</td><td>No, no hay sincronización.</td><td>Sí, acceso completo.</td></tr><tr><td><strong>SMTP</strong></td><td>Envío de correos electrónicos desde un cliente de correo electrónico.</td><td>No aplicable, solo protocolo de envío.</td><td>No aplicable.</td><td>No aplicable.</td></tr></tbody></table></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="La_eleccion_segun_las_necesidades"></span>La elección según las necesidades.<span class="ez-toc-section-end"></span></h4>



<p>                La elección entre <strong>IMAP</strong> y otros protocolos como <strong>POP3</strong> Y <strong>SMTP</strong> depende estrechamente de las necesidades del usuario. Si el acceso sobre la marcha y la gestión de múltiples dispositivos son esenciales, <strong>IMAP</strong> es la solución ideal. Para aquellos que prefieren la recuperación sencilla de sus correos electrónicos en un solo dispositivo, <strong>POP3</strong> puede ser suficiente. Finalmente, <strong>SMTP</strong> Siempre será necesario para el envío de correos electrónicos, independientemente del protocolo de recepción elegido.</p>



<p>                En comparación, <strong>IMAP</strong> proporciona flexibilidad y comodidad que otros protocolos no pueden igualar para los usuarios que requieren acceso constante a su correo electrónico desde diferentes dispositivos. Sin embargo, cada protocolo tiene su importancia y utilidad dependiendo de los requerimientos personales o profesionales. Comprender estas diferencias es esencial para elegir la configuración de correo electrónico más adecuada.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Configurar_y_optimizar_el_uso_de_IMAP"></span>Configurar y optimizar el uso de IMAP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="/images/blog/Tout-savoir-sur-le-protocole-IMAP-2.png" alt="" class="wp-image-1378" srcset="/images/blog/Tout-savoir-sur-le-protocole-IMAP-2.png 1792w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-300x171.png 300w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-1024x585.png 1024w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-150x86.png 150w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-768x439.png 768w, /images/blog/Tout-savoir-sur-le-protocole-IMAP-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<figure class="wp-block-embed is-type-video is-provider-tiktok wp-block-embed-tiktok"><div class="wp-block-embed__wrapper">
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@formip/video/7295627671319383328" data-video-id="7295627671319383328" data-embed-from="oembed" style="max-width:605px; min-width:325px;"> <section> <a target="_blank" title="@formip" href="https://www.tiktok.com/@formip?refer=embed" rel="noopener">@formip</a> <p>Mister IMAP : Le DJ des E-mails 🎧📧 PART 2 <a title="misterimap" target="_blank" href="https://www.tiktok.com/tag/misterimap?refer=embed" rel="noopener">#MisterIMAP</a>E-mailsSynchronisésDJDesE-mails<a title="portiervip" target="_blank" href="https://www.tiktok.com/tag/portiervip?refer=embed" rel="noopener">#PortierVIP</a>BibliothécaireE-mails<a title="sécuritéimap" target="_blank" href="https://www.tiktok.com/tag/s%C3%A9curit%C3%A9imap?refer=embed" rel="noopener">#SécuritéIMAP</a>ChefOrchestreE-mails<a title="messagerienumérique" target="_blank" href="https://www.tiktok.com/tag/messagerienum%C3%A9rique?refer=embed" rel="noopener">#MessagerieNumérique</a><a title="mozartmessagerie" target="_blank" href="https://www.tiktok.com/tag/mozartmessagerie?refer=embed" rel="noopener">#MozartMessagerie</a><a title="playlistimap" target="_blank" href="https://www.tiktok.com/tag/playlistimap?refer=embed" rel="noopener">#PlaylistIMAP</a></p> <a target="_blank" title="♬ son original - Formip - Formip" href="https://www.tiktok.com/music/son-original-Formip-7295627771307395873?refer=embed" rel="noopener">♬ son original &#8211; Formip &#8211; Formip</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Configuraciones_IMAP_basicas"></span>Configuraciones IMAP básicas<span class="ez-toc-section-end"></span></h3>



<p>Para configurar IMAP en su cliente de correo electrónico, necesitará la siguiente información:</p>



<ul class="wp-block-list">
<li>Nombre de usuario: Su dirección de correo electrónico completa</li>



<li>Contraseña: La contraseña asociada con su dirección de correo electrónico.</li>



<li>Servidor IMAP: la dirección del servidor IMAP proporcionada por su servidor de correo electrónico</li>



<li>Puerto IMAP: normalmente 993 para una conexión segura (SSL)</li>
</ul>



<p>Una vez que ingrese esta información en la configuración de su cliente de correo electrónico, tendrá acceso a sus mensajes.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimizacion_del_uso_de_IMAP"></span>Optimización del uso de IMAP<span class="ez-toc-section-end"></span></h4>



<p>Para una experiencia mejorada, aquí hay algunos consejos de optimización:</p>



<ul class="wp-block-list">
<li><strong>Carpetas sincronizadas:</strong> A menudo es posible elegir qué carpetas desea sincronizar. Seleccione solo aquellos que ve regularmente para ahorrar espacio de almacenamiento y datos.</li>



<li><strong>Gestión de correo electrónico:</strong> Aprovecha las funciones que ofrece tu cliente para organizar tus correos electrónicos de manera eficiente. El uso de filtros, carpetas inteligentes y reglas de clasificación puede mejorar enormemente su productividad.</li>



<li><strong>Tamaño de sincronización:</strong> Algunos clientes le permiten limitar la cantidad de datos a sincronizar (por ejemplo, solo correos electrónicos de los últimos 30 días). Esto puede acelerar la sincronización y reducir el uso del ancho de banda.</li>



<li><strong>Desconexión de dispositivos no utilizados:</strong> Para evitar sincronizaciones innecesarias y posibles violaciones de seguridad, asegúrese de desconectar los dispositivos que ya no utiliza.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Practicas_de_seguridad_con_IMAP"></span>Prácticas de seguridad con IMAP<span class="ez-toc-section-end"></span></h4>



<p>La seguridad es un aspecto esencial cuando se utilizan protocolos de comunicación como IMAP. Estas son algunas de las mejores prácticas:</p>



<ul class="wp-block-list">
<li><strong>Utilice conexiones cifradas:</strong> Utilice siempre el puerto IMAP seguro (SSL/TLS) para cifrar los datos intercambiados entre su cliente de correo electrónico y el servidor.</li>



<li><strong>Contraseñas seguras:</strong> Asegúrese de que su contraseña de correo electrónico sea segura y única para evitar el acceso no autorizado.</li>



<li><strong>Verificación de dos pasos:</strong> Si su proveedor lo permite, habilite la verificación en dos pasos para agregar una capa adicional de seguridad.</li>
</ul>



<p>Configurar y optimizar el uso de<strong>IMAP</strong> son esenciales para disfrutar de una experiencia de correo electrónico fluida y segura. Si sigue los consejos anteriores, puede mejorar su productividad mientras mantiene sus datos seguros. Recuerde también actualizar periódicamente su cliente de correo electrónico y mantenerse informado sobre las mejores prácticas de seguridad digital.</p>



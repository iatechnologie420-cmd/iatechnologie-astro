---
lang: "fr"
title: "Dompdf : Comment créer des PDF élégants en PHP ?"
slug: "creer-pdf-avec-dompdf-tuto"
excerpt: "Introduction au Dompdf Le Dompdf est une bibliothèque PHP qui permet de générer des fichiers PDF à partir de contenus HTML. Cette solution est très utile pour générer des rapports, des factures ou tout autre document au format PDF. Dans cet article, nous allons découvrir les fonctionnalités de base du Dompdf et apprendre comment l’utiliser […]"
date: "2024-01-29T08:07:39"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["computing-et-data", "technologie-numerique"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/creer-pdf-avec-dompdf-tuto/#Introduction_au_Dompdf" >Introduction au Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/creer-pdf-avec-dompdf-tuto/#Prerequis" >Prérequis</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/creer-pdf-avec-dompdf-tuto/#Installation_Dompdf" >Installation Dompdf</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-4" href="/creer-pdf-avec-dompdf-tuto/#Creation_dun_PDF_elegant_en_PHP" >Création d’un PDF élégant en PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-5" href="/creer-pdf-avec-dompdf-tuto/#Autre_methode_dinstallation_et_dutilisation_de_Dompdf" >Autre methode d’installation et d’utilisation de Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-6" href="/creer-pdf-avec-dompdf-tuto/#Creation_dun_PDF_a_partir_dun_template_HTML" >Création d’un PDF à partir d’un template HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/creer-pdf-avec-dompdf-tuto/#Gestion_des_images_et_des_polices_de_caracteres" >Gestion des images et des polices de caractères</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/creer-pdf-avec-dompdf-tuto/#Optimisation_du_rendu_et_resolution_des_problemes_Dompdf" >Optimisation du rendu et résolution des problèmes Dompdf</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introduction_au_Dompdf"></span>Introduction au Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Le Dompdf est une bibliothèque PHP qui permet de générer des fichiers PDF à partir de contenus HTML. Cette solution est très utile pour générer des rapports, des factures ou tout autre document au format PDF. Dans cet article, nous allons découvrir les fonctionnalités de base du Dompdf et apprendre comment l’utiliser pour créer des PDF élégants et fonctionnels.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Prerequis"></span>Prérequis<span class="ez-toc-section-end"></span></h3>



<p>Avant d’installer Dompdf, assurez-vous de disposer des éléments suivants :</p>



<ul class="wp-block-list">
<li><strong>PHP :</strong> Dompdf nécessite PHP >= 5.4. Il est compatible avec les versions 7.x de PHP.</li>



<li><strong>Extensions PHP :</strong> Assurez-vous d’avoir activé les extensions PHP suivantes : mbstring, DOM et GD. Ces extensions sont essentielles pour le bon fonctionnement de Dompdf.</li>



<li><strong>Composer :</strong> Dompdf est distribué via Composer, qui est un gestionnaire de dépendances pour PHP. Assurez-vous d’avoir Composer installé sur votre système.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Installation_Dompdf"></span>Installation Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Pour installer Dompdf, suivez les étapes suivantes :</p>



<ol class="wp-block-list">
<li><strong>Créez un nouveau projet PHP :</strong> Si vous n’avez pas encore de projet existant, créez-en un nouveau en utilisant la structure de base de votre choix.</li>



<li><strong>Ajoutez la dépendance Dompdf via Composer :</strong> Ouvrez une console et naviguez jusqu’au répertoire de votre projet. Exécutez la commande suivante pour ajouter Dompdf à votre projet :     <pre><code>composer require dompdf/dompdf</code></pre>     Cette commande téléchargera et installera automatiquement Dompdf ainsi que ses dépendances.</li>



<li><strong>Utilisez Dompdf dans votre application :</strong> Vous pouvez maintenant utiliser Dompdf dans votre projet. Il existe de nombreuses façons de créer des fichiers PDF avec Dompdf, mais voici un exemple de base pour commencer :
    <pre><code>// Inclure l'autoloader de Composer
require 'vendor/autoload.php';

// Créer un nouvel objet Dompdf
$dompdf = new Dompdf();

// Charger le contenu HTML à partir d'un fichier ou d'une chaîne
$html = '<h1>Mon premier document PDF avec Dompdf</h1>';
$dompdf->loadHtml($html);

// Rendre le document PDF
$dompdf->render();

// Envoyer le document PDF à la sortie
$dompdf->stream('document.pdf');</code></pre>
    Cet exemple crée un nouveau document PDF avec un titre et le télécharge en tant que fichier “document.pdf”. Vous pouvez personnaliser le contenu HTML selon vos besoins.</li>
</ol>



<p>Maintenant que vous avez installé Dompdf, vous pouvez commencer à générer des fichiers PDF élégants et fonctionnels dans vos applications web. Dompdf offre de nombreuses fonctionnalités avancées pour personnaliser le rendu du PDF, telles que la gestion des images, des polices de caractères personnalisées et des styles CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Creation_dun_PDF_elegant_en_PHP"></span>Création d’un PDF élégant en PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Autre_methode_dinstallation_et_dutilisation_de_Dompdf"></span>Autre methode d’installation et d’utilisation de Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Voici les étapes à suivre :<br>1. Téléchargez la dernière version de Dompdf depuis le site officiel.<br>2. Extrayez les fichiers téléchargés et placez-les dans votre projet PHP.<br>3. Incluez le fichier Dompdfautoload.php pour charger la bibliothèque dans votre script PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Creation_dun_PDF_a_partir_dun_template_HTML"></span>Création d’un PDF à partir d’un template HTML<span class="ez-toc-section-end"></span></h4>



<p>Maintenant que nous avons installé Dompdf, nous allons voir comment créer un PDF en utilisant un template HTML. Suivez ces étapes :</p>



<p>1. Créez un fichier HTML contenant la structure et la mise en page souhaitées pour votre PDF.<br>2. Utilisez les fonctionnalités CSS pour styliser votre document, en utilisant des propriétés comme font-family, font-size, border, etc.<br>3. Incluez les données dynamiques en utilisant des balises spécifiques à Dompdf, comme “{{nom}}” ou “{{adresse}}”.<br>4. Utilisez la classe Dompdf pour générer le PDF en utilisant le template HTML que vous avez créé.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gestion_des_images_et_des_polices_de_caracteres"></span>Gestion des images et des polices de caractères<span class="ez-toc-section-end"></span></h4>



<p>Lors de la création de PDF élégants, il est souvent nécessaire d’inclure des images ou d’utiliser des polices de caractères spécifiques. Voici comment le faire avec Dompdf :</p>



<p>1. Incluez les images dans votre template HTML en utilisant la balise <img decoding="async" src="chemin_vers_image">.<br>2. Sachez que Dompdf n’inclut pas par défaut toutes les polices de caractères. Vous pouvez ajouter des polices personnalisées en utilisant @font-face dans votre CSS ou en utilisant les polices fournies par Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimisation_du_rendu_et_resolution_des_problemes_Dompdf"></span>Optimisation du rendu et résolution des problèmes Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Parfois, vous pouvez rencontrer des problèmes liés au rendu de votre PDF ou à la génération des fichiers. Voici quelques conseils pour les résoudre :</p>



<p>1. Vérifiez que votre template HTML est correctement construit et valide.<br>2. Assurez-vous que toutes les ressources externes (images, polices, etc.) sont accessibles depuis le serveur.<br>3. Débuguez votre code en activant le mode de débogage de Dompdf et en vérifiant les erreurs affichées.<br>4. Consultez la documentation de Dompdf pour plus d’informations sur les configurations et les problèmes courants.</p>



<p>En utilisant Dompdf, vous pouvez offrir une expérience utilisateur améliorée en fournissant des documents PDF professionnels et bien formatés. Que ce soit pour générer des rapports, des factures ou d’autres types de documents, Dompdf est un choix fiable et puissant.</p>



<p>En conclusion, l’installation de Dompdf est simple et rapide grâce à Composer. Une fois installé, vous pouvez commencer à créer des fichiers PDF de haute qualité pour répondre aux besoins de votre application web. N’oubliez pas de consulter la documentation officielle de Dompdf pour en savoir plus sur ses fonctionnalités et les options de personnalisation disponibles.</p>


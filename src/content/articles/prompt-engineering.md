---
lang: "fr"
title: "Apprendre le prompt engineering : en 12 étape"
slug: "prompt-engineering"
excerpt: "Introduction au prompt engineering Qu’est-ce que le Prompt Engineering? Le Prompt Engineering est un domaine émergent qui se concentre sur l’optimisation des prompts, ou des commandes, que nous donnons aux systèmes d’intelligence artificielle (IA), notamment ceux basés sur le langage naturel, tel que les générateurs de texte. C’est une discipline particulièrement importante avec l’arrivée des […]"
date: "2024-01-22T11:57:36"
featuredImage: "https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-3.png"
categories: ["formation-ia-fondamentaux-fr"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/prompt-engineering/#Introduction_au_prompt_engineering" >Introduction au prompt engineering</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/prompt-engineering/#Quest-ce_que_le_Prompt_Engineering" >Qu’est-ce que le Prompt Engineering?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/prompt-engineering/#Pourquoi_le_Prompt_Engineering_est-il_important" >Pourquoi le Prompt Engineering est-il important?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/prompt-engineering/#Comment_fonctionne_le_Prompt_Engineering" >Comment fonctionne le Prompt Engineering</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/prompt-engineering/#Bonne_pratique_et_technique_en_Prompt_Engineering" >Bonne pratique et technique en Prompt Engineering</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/prompt-engineering/#Les_principes_fondamentaux_du_prompt_engineering" >Les principes fondamentaux du prompt engineering</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-7" href="/prompt-engineering/#Comprendre_la_pertinence_du_contexte" >Comprendre la pertinence du contexte</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/prompt-engineering/#Clarifier_lintention_de_lutilisateur" >Clarifier l’intention de l’utilisateur</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/prompt-engineering/#Structuration_et_hierarchisation_de_linformation" >Structuration et hiérarchisation de l’information</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/prompt-engineering/#Choix_du_langage_et_de_la_formulation" >Choix du langage et de la formulation</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-11" href="/prompt-engineering/#Utilisation_iterative_et_amelioration_continue" >Utilisation itérative et amélioration continue</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-12" href="/prompt-engineering/#Gestion_des_resultats_atypiques" >Gestion des résultats atypiques</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-13" href="/prompt-engineering/#Connaissance_du_modele_dIA_utilise" >Connaissance du modèle d’IA utilisé</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Introduction_au_prompt_engineering"></span>Introduction au prompt engineering<span class="ez-toc-section-end"></span></h2>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Quest-ce_que_le_Prompt_Engineering"></span>Qu’est-ce que le Prompt Engineering?<span class="ez-toc-section-end"></span></h3>



<p>    Le <strong>Prompt Engineering</strong> est un domaine émergent qui se concentre sur l’optimisation des prompts, ou des commandes, que nous donnons aux systèmes d’intelligence artificielle (IA), notamment ceux basés sur le langage naturel, tel que les générateurs de texte. C’est une discipline particulièrement importante avec l’arrivée des modèles de traitement du langage comme GPT-4 de <strong>OpenAI</strong>. L’idée est d’apprendre à « parler » de façon efficace à ces IA pour améliorer la qualité et la pertinence des réponses obtenues.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Pourquoi_le_Prompt_Engineering_est-il_important"></span>Pourquoi le Prompt Engineering est-il important?<span class="ez-toc-section-end"></span></h4>



<p>Le rôle du <strong>Prompt Engineering</strong> est crucial car la façon dont on formule une commande à une IA peut grandement varier les résultats. Par exemple, des prompts mal conçus pourraient produire des réponses inexactes ou hors sujet, tandis que des prompts bien élaborés peuvent améliorer la précision et la pertinence des informations générées. Les experts en prompt engineering travaillent à peaufiner la formulation des questions pour obtenir des résultats précis et utiles.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Comment_fonctionne_le_Prompt_Engineering"></span>Comment fonctionne le Prompt Engineering<span class="ez-toc-section-end"></span></h4>



<p> Le processus du prompt engineering implique de comprendre en profondeur le fonctionnement des modèles d’IA, tel que les réseaux de neurones, et d’utiliser cette compréhension pour élaborer des prompts qui tirent parti des capacités de l’IA tout en contournant ses limites. Cela peut nécessiter une certaine créativité, beaucoup d’expérimentation et une analyse approfondie des résultats pour peaufiner les prompts de façon itérative.</p>



<p>L’art du <strong>Prompt Engineering</strong> représente une compétence essentielle pour quiconque cherche à interagir efficacement avec les systèmes d’intelligence artificielle les plus avancés. Comprendre et appliquer les principes du prompt engineering peut grandement améliorer la qualité et l’efficacité de notre engagement avec les technologies basées sur l’IA.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Bonne_pratique_et_technique_en_Prompt_Engineering"></span>Bonne pratique et technique en Prompt Engineering<span class="ez-toc-section-end"></span></h4>



<p>L’art du “prompt engineering” pour les IA génératives de contenu et d’images, comme OpenAI et MidJourney, exige une combinaison de techniques et de bonnes pratiques pour obtenir des résultats de qualité. Voici quelques-unes de ces bonnes pratiques et techniques :</p>



<ol class="wp-block-list">
<li><strong>Utilisation d’exemples :</strong> Intégrer des exemples de demandes et de réponses dans vos prompts peut conditionner le modèle à répondre de manière souhaitée, en utilisant des techniques de “one-shot” ou “few-shot learning” pour améliorer la précision de la réponse du modèle.</li>



<li><strong>Attention aux indices :</strong> Inclure des indices dans votre prompt peut guider le modèle pour générer une sortie alignée sur vos intentions. Cela peut être particulièrement utile pour diriger le modèle vers la réponse désirée.</li>



<li><strong>Tester différents arrangements :</strong> L’ordre dans lequel les informations sont présentées dans le prompt peut influencer la sortie du modèle. Il est utile d’expérimenter avec différents arrangements d’instructions, de contenu principal, d’exemples et d’indices.</li>



<li><strong>Fournir une “sortie” au modèle :</strong> Parfois, le modèle peut avoir du mal à compléter une tâche avec précision. Pour atténuer cela, fournissez des chemins ou des instructions alternatifs pour que le modèle suive s’il ne peut pas trouver une réponse satisfaisante.</li>



<li><strong>Surveillez la longueur :</strong> Les prompts peuvent être soumis à des limites de nombre de caractères. Des prompts trop longs peuvent être difficiles pour les systèmes d’IA à traiter.</li>



<li><strong>Choisissez vos mots avec soin :</strong> Les prompts les plus efficaces utilisent un langage clair et direct. Évitez l’ambiguïté, le langage coloré, les métaphores et l’argot.</li>



<li><strong>Posez des questions ouvertes :</strong> Les questions ouvertes offrent plus de flexibilité dans la sortie. Par exemple, un prompt demandant de décrire des facteurs complexes est plus susceptible de provoquer une réponse détaillée et complète.</li>



<li><strong>Incluez le contexte :</strong> Les prompts bien conçus incluent souvent un contexte qui aide le système d’IA à adapter sa sortie à l’audience visée de l’utilisateur.</li>



<li><strong>Définissez des objectifs ou des limites de longueur de sortie :</strong> Bien que l’IA soit conçue pour être créative, il est souvent judicieux d’inclure des garde-fous sur des facteurs tels que la longueur de la sortie.</li>



<li><strong>Évitez les termes contradictoires :</strong> Les prompts longs et complexes peuvent inclure des termes ambigus ou contradictoires. Assurez-vous que tous les termes sont cohérents.</li>



<li><strong>Utilisez la ponctuation pour clarifier des prompts complexes :</strong> Tout comme les humains s’appuient sur la ponctuation pour aider à interpréter le texte, les prompts d’IA peuvent également bénéficier de l’utilisation judicieuse de la virgule, des guillemets et des sauts de ligne.</li>
</ol>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Les_principes_fondamentaux_du_prompt_engineering"></span>Les principes fondamentaux du prompt engineering<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img loading="lazy" decoding="async" width="1792" height="1024" src="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering.png" alt="" class="wp-image-1714" srcset="https://pub-5bb2cd26c04a41efbcb7bf8a165f9044.r2.dev/images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering.png 1792w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-300x171.png 300w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-1024x585.png 1024w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-150x86.png 150w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-768x439.png 768w, /images/blog/Tout-ce-que-vous-devez-savoir-sur-le-prompt-engineering-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Comprendre_la_pertinence_du_contexte"></span>Comprendre la pertinence du contexte<span class="ez-toc-section-end"></span></h3>



<p>Un principe essentiel du <strong>prompt engineering</strong> est la compréhension du contexte dans lequel une requête est faite. Tout comme dans une conversation humaine, le contexte influence fortement la signification et la pertinence des réponses. Cela implique que les prompts doivent être conçus d’une manière qui prend en compte l’environnement spécifique, les objectifs de l’utilisateur et le domaine précis d’application.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Clarifier_lintention_de_lutilisateur"></span>Clarifier l’intention de l’utilisateur<span class="ez-toc-section-end"></span></h4>



<p>La clarté de l’intention dans un prompt est cruciale pour obtenir une réponse pertinente de l’IA. Il est important que le prompt soit aussi précis que possible pour minimiser les ambiguïtés. Cela signifie parfois reformuler ou ajouter des détails qui orientent l’IA vers une compréhension plus exacte de ce que cherche l’utilisateur.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Structuration_et_hierarchisation_de_linformation"></span>Structuration et hiérarchisation de l’information<span class="ez-toc-section-end"></span></h4>



<p>La manière dont un prompt est structuré peut avoir un impact considérable sur la qualité de la réponse obtenue. Il s’agit de hiérarchiser l’information de façon logique et cohérente pour que l’IA puisse traiter la requête de manière efficace, et de structurer la demande pour que les éléments les plus importants soient mis en avant, guidant ainsi l’IA vers une réponse adéquate.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Choix_du_langage_et_de_la_formulation"></span>Choix du langage et de la formulation<span class="ez-toc-section-end"></span></h4>



<p>Les mots choisis, le style de langage et la formulation globale du prompt jouent un rôle non négligeable dans le prompt engineering. Un langage clair, précis et adapté au modèle d’IA concerné est essentiel. Par exemple, certains modèles sont plus réceptifs à un langage naturel, tandis que d’autres nécessitent une formulation plus formelle ou technique.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Utilisation_iterative_et_amelioration_continue"></span>Utilisation itérative et amélioration continue<span class="ez-toc-section-end"></span></h4>



<p>Le <strong>prompt engineering</strong> est souvent un processus itératif. Il n’est pas rare de devoir ajuster les prompts plusieurs fois avant de parvenir à la réponse souhaitée. Analyser les réponses de l’IA et affiner les prompts sur la base de ces réponses est une partie essentielle du processus de prompt engineering.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Gestion_des_resultats_atypiques"></span>Gestion des résultats atypiques<span class="ez-toc-section-end"></span></h4>



<p>Il est essentiel de savoir comment gérer les résultats inattendus ou atypiques, qui peuvent survenir même avec un prompt bien conçu. Cela inclut la capacité à diagnostiquer les raisons de tels résultats et à reformuler les prompts pour corriger le problème.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Connaissance_du_modele_dIA_utilise"></span>Connaissance du modèle d’IA utilisé<span class="ez-toc-section-end"></span></h4>



<p>Enfin, une compréhension approfondie du modèle d’IA avec lequel on travaille est fondamentale. Connaître ses forces, ses limitations et la manière dont il traite les prompts est crucial pour formuler des prompts qui seront efficacement interprétés et exécutés par l’IA.</p>



<p>Vous comprendrez donc que le <strong>prompt engineering</strong> est une compétence de plus en plus importante à mesure que les technologies d’IA deviennent plus sophistiquées et intégrées dans notre quotidien. Alors commencer a la mettre en place le plus rapidement.</p>


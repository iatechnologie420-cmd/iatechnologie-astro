---

title: "Dompdf: Wie erstelle ich elegante PDFs in PHP?"
slug: "dompdf-wie-erstelle-ich-elegante-pdfs-in-php"
excerpt: "Einführung in Dompdf Dompdf ist eine PHP-Bibliothek, mit der Sie PDF-Dateien aus HTML-Inhalten generieren können. Diese Lösung ist sehr nützlich für die Erstellung von Berichten, Rechnungen oder anderen Dokumenten im PDF-Format. In diesem Artikel entdecken wir die Grundfunktionen von Dompdf und erfahren, wie Sie damit elegante und funktionale PDFs erstellen. Voraussetzungen Stellen Sie vor der [&hellip;]"
date: "2024-03-09T12:39:57"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["computer-und-daten-de", "technologie-und-digital-de"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Einfuhrung_in_Dompdf" >Einführung in Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Voraussetzungen" >Voraussetzungen</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Dompdf-Installation" >Dompdf-Installation</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Mein_erstes_PDF-Dokument_mit_Dompdf" >Mein erstes PDF-Dokument mit Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Erstellen_eines_eleganten_PDFs_in_PHP" >Erstellen eines eleganten PDFs in PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Eine_weitere_Methode_zur_Installation_und_Verwendung_von_Dompdf" >Eine weitere Methode zur Installation und Verwendung von Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Erstellen_einer_PDF-Datei_aus_einer_HTML-Vorlage" >Erstellen einer PDF-Datei aus einer HTML-Vorlage</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Verwalten_von_Bildern_und_Schriftarten" >Verwalten von Bildern und Schriftarten</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/de/dompdf-wie-erstelle-ich-elegante-pdfs-in-php/#Optimierung_des_Renderings_und_Behebung_von_Dompdf-Problemen" >Optimierung des Renderings und Behebung von Dompdf-Problemen</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Einfuhrung_in_Dompdf"></span>Einführung in Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf ist eine PHP-Bibliothek, mit der Sie PDF-Dateien aus HTML-Inhalten generieren können. Diese Lösung ist sehr nützlich für die Erstellung von Berichten, Rechnungen oder anderen Dokumenten im PDF-Format. In diesem Artikel entdecken wir die Grundfunktionen von Dompdf und erfahren, wie Sie damit elegante und funktionale PDFs erstellen.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Voraussetzungen"></span>Voraussetzungen<span class="ez-toc-section-end"></span></h3>



<p>Stellen Sie vor der Installation von Dompdf sicher, dass Sie über Folgendes verfügen:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf erfordert PHP >= 5.4. Es ist mit den Versionen 7.x von PHP kompatibel.</li>



<li><strong>PHP-Erweiterungen:</strong> Stellen Sie sicher, dass Sie die folgenden PHP-Erweiterungen aktiviert haben: mbstring, DOM und GD. Diese Erweiterungen sind für das ordnungsgemäße Funktionieren von Dompdf unerlässlich.</li>



<li><strong>Verfassen:</strong> Dompdf wird über Composer verteilt, einen Abhängigkeitsmanager für PHP. Stellen Sie sicher, dass Composer auf Ihrem System installiert ist.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Dompdf-Installation"></span>Dompdf-Installation<span class="ez-toc-section-end"></span></h4>



<p>Um Dompdf zu installieren, führen Sie die folgenden Schritte aus:</p>



<ol class="wp-block-list">
<li><strong>Erstellen Sie ein neues PHP-Projekt:</strong> Wenn Sie noch kein Projekt haben, erstellen Sie ein neues mit der Grundstruktur Ihrer Wahl.</li>



<li><strong>Fügen Sie die Dompdf-Abhängigkeit über Composer hinzu:</strong> Öffnen Sie eine Konsole und navigieren Sie zu Ihrem Projektverzeichnis. Führen Sie den folgenden Befehl aus, um Dompdf zu Ihrem Projekt hinzuzufügen:     <pre><code>Komponist benötigt dompdf/dompdf</code></pre>     Dieser Befehl lädt Dompdf automatisch herunter und installiert es zusammen mit seinen Abhängigkeiten.</li>



<li><strong>Verwenden Sie Dompdf in Ihrer Anwendung:</strong> Sie können Dompdf jetzt in Ihrem Projekt verwenden. Es gibt viele Möglichkeiten, PDF-Dateien mit Dompdf zu erstellen, aber hier ist ein einfaches Beispiel, um Ihnen den Einstieg zu erleichtern:
<pre><code>// Den Composer-Autoloader einbinden
require 'vendor/autoload.php';

// Ein neues Dompdf-Objekt erstellen
$dompdf = neues Dompdf();

// HTML-Inhalt aus einer Datei oder einem String laden
$html = '<h1><span class="ez-toc-section" id="Mein_erstes_PDF-Dokument_mit_Dompdf"></span>Mein erstes PDF-Dokument mit Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Rendern Sie das PDF-Dokument
$dompdf->render();

// PDF-Dokument zur Ausgabe senden
$dompdf->stream('document.pdf');</code></pre>
    In diesem Beispiel wird ein neues PDF-Dokument mit einem Titel erstellt und als Datei „document.pdf“ hochgeladen. Sie können den HTML-Inhalt entsprechend Ihren Anforderungen anpassen.</li>
</ol>



<p>Nachdem Sie Dompdf nun installiert haben, können Sie mit der Generierung eleganter und funktionaler PDF-Dateien in Ihren Webanwendungen beginnen. Dompdf bietet viele erweiterte Funktionen zum Anpassen des PDF-Renderings, wie zum Beispiel die Verwaltung von Bildern, benutzerdefinierten Schriftarten und CSS-Stilen.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Erstellen_eines_eleganten_PDFs_in_PHP"></span>Erstellen eines eleganten PDFs in PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Eine_weitere_Methode_zur_Installation_und_Verwendung_von_Dompdf"></span>Eine weitere Methode zur Installation und Verwendung von Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Hier sind die Schritte, die Sie befolgen müssen:<br>1. Laden Sie die neueste Version von Dompdf von der offiziellen Website herunter.<br>2. Extrahieren Sie die heruntergeladenen Dateien und platzieren Sie sie in Ihrem PHP-Projekt.<br>3. Fügen Sie die Datei Dompdfautoload.php ein, um die Bibliothek in Ihr PHP-Skript zu laden.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Erstellen_einer_PDF-Datei_aus_einer_HTML-Vorlage"></span>Erstellen einer PDF-Datei aus einer HTML-Vorlage<span class="ez-toc-section-end"></span></h4>



<p>Nachdem wir Dompdf nun installiert haben, werden wir sehen, wie man mithilfe einer HTML-Vorlage ein PDF erstellt. Folge diesen Schritten:</p>



<p>1. Erstellen Sie eine HTML-Datei mit der gewünschten Struktur und dem gewünschten Layout für Ihr PDF.<br>2. Verwenden Sie CSS-Funktionen, um Ihr Dokument zu formatieren, indem Sie Eigenschaften wie Schriftfamilie, Schriftgröße, Rahmen usw. verwenden.<br>3. Fügen Sie dynamische Daten mithilfe von Dompdf-spezifischen Tags ein, z. B. „{{name}}“ oder „{{address}}“.<br>4. Verwenden Sie die Dompdf-Klasse, um das PDF mithilfe der von Ihnen erstellten HTML-Vorlage zu generieren.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Verwalten_von_Bildern_und_Schriftarten"></span>Verwalten von Bildern und Schriftarten<span class="ez-toc-section-end"></span></h4>



<p>Beim Erstellen eleganter PDFs ist es oft notwendig, Bilder einzubinden oder bestimmte Schriftarten zu verwenden. So machen Sie es mit Dompdf:</p>



<p>1. Fügen Sie mithilfe des Tags Bilder in Ihre HTML-Vorlage ein <img decoding="async" src="chemin_vers_image">.<br>2. Bitte beachten Sie, dass Dompdf standardmäßig nicht alle Schriftarten enthält. Sie können benutzerdefinierte Schriftarten hinzufügen, indem Sie @font-face in Ihrem CSS verwenden oder die von Dompdf bereitgestellten Schriftarten verwenden.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optimierung_des_Renderings_und_Behebung_von_Dompdf-Problemen"></span>Optimierung des Renderings und Behebung von Dompdf-Problemen<span class="ez-toc-section-end"></span></h4>



<p>Manchmal kann es beim Rendern Ihrer PDF-Datei oder beim Generieren der Dateien zu Problemen kommen. Hier sind einige Tipps zur Lösung:</p>



<p>1. Überprüfen Sie, ob Ihre HTML-Vorlage korrekt aufgebaut und gültig ist.<br>2. Stellen Sie sicher, dass alle externen Ressourcen (Bilder, Schriftarten usw.) vom Server aus zugänglich sind.<br>3. Debuggen Sie Ihren Code, indem Sie den Dompdf-Debug-Modus aktivieren und die angezeigten Fehler überprüfen.<br>4. Weitere Informationen zu häufigen Konfigurationen und Problemen finden Sie in der Dompdf-Dokumentation.</p>



<p>Mit Dompdf können Sie durch die Bereitstellung professioneller und gut formatierter PDF-Dokumente ein verbessertes Benutzererlebnis bieten. Ob Sie Berichte, Rechnungen oder andere Arten von Dokumenten erstellen, Dompdf ist eine zuverlässige und leistungsstarke Wahl.</p>



<p>Zusammenfassend lässt sich sagen, dass die Installation von Dompdf dank Composer schnell und einfach ist. Nach der Installation können Sie mit der Erstellung hochwertiger PDF-Dateien beginnen, die Ihren Webanwendungsanforderungen entsprechen. Vergessen Sie nicht, einen Blick in die offizielle Dompdf-Dokumentation zu werfen, um mehr über die Funktionen und verfügbaren Anpassungsoptionen zu erfahren.</p>



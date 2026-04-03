---

title: "Dompdf: Jak tworzyć eleganckie pliki PDF w PHP?"
slug: "dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php"
excerpt: "Wprowadzenie do Dompdf Dompdf to biblioteka PHP, która umożliwia generowanie plików PDF z zawartości HTML. Rozwiązanie to jest bardzo przydatne przy generowaniu raportów, faktur czy innych dokumentów w formacie PDF. W tym artykule odkryjemy podstawowe funkcje Dompdf i nauczymy się go używać do tworzenia eleganckich i funkcjonalnych plików PDF. Warunki wstępne Przed zainstalowaniem Dompdf upewnij [&hellip;]"
date: "2024-03-09T12:42:35"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["obliczenia-i-dane-pl", "technologia-i-cyfrowosc-pl"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Wprowadzenie_do_Dompdf" >Wprowadzenie do Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Warunki_wstepne" >Warunki wstępne</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Instalacja_Dompdf" >Instalacja Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Moj_pierwszy_dokument_PDF_w_Dompdf" >Mój pierwszy dokument PDF w Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Tworzenie_eleganckiego_pliku_PDF_w_PHP" >Tworzenie eleganckiego pliku PDF w PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Inna_metoda_instalacji_i_uzywania_Dompdf" >Inna metoda instalacji i używania Dompdf</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Tworzenie_pliku_PDF_z_szablonu_HTML" >Tworzenie pliku PDF z szablonu HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Zarzadzanie_obrazami_i_czcionkami" >Zarządzanie obrazami i czcionkami</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/pl/dompdf-jak-tworzyc-eleganckie-pliki-pdf-w-php/#Optymalizacja_renderowania_i_naprawianie_problemow_z_Dompdf" >Optymalizacja renderowania i naprawianie problemów z Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Wprowadzenie_do_Dompdf"></span>Wprowadzenie do Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf to biblioteka PHP, która umożliwia generowanie plików PDF z zawartości HTML. Rozwiązanie to jest bardzo przydatne przy generowaniu raportów, faktur czy innych dokumentów w formacie PDF. W tym artykule odkryjemy podstawowe funkcje Dompdf i nauczymy się go używać do tworzenia eleganckich i funkcjonalnych plików PDF.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Warunki_wstepne"></span>Warunki wstępne<span class="ez-toc-section-end"></span></h3>



<p>Przed zainstalowaniem Dompdf upewnij się, że masz następujące elementy:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf wymaga PHP >= 5.4. Jest kompatybilny z wersjami 7.x PHP.</li>



<li><strong>Rozszerzenia PHP:</strong> Upewnij się, że masz włączone następujące rozszerzenia PHP: mbstring, DOM i GD. Rozszerzenia te są niezbędne do prawidłowego funkcjonowania Dompdf.</li>



<li><strong>Skomponuj:</strong> Dompdf jest dystrybuowany za pośrednictwem Composer, który jest menedżerem zależności dla PHP. Upewnij się, że masz zainstalowany Composer w swoim systemie.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Instalacja_Dompdf"></span>Instalacja Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Aby zainstalować Dompdf, wykonaj następujące kroki:</p>



<ol class="wp-block-list">
<li><strong>Utwórz nowy projekt PHP:</strong> Jeśli nie masz jeszcze istniejącego projektu, utwórz nowy, korzystając z wybranej przez siebie podstawowej struktury.</li>



<li><strong>Dodaj zależność Dompdf za pośrednictwem Composer:</strong> Otwórz konsolę i przejdź do katalogu projektu. Uruchom następujące polecenie, aby dodać Dompdf do swojego projektu:     <pre><code>kompozytor wymaga dompdf/dompdf</code></pre>     To polecenie automatycznie pobierze i zainstaluje Dompdf wraz z jego zależnościami.</li>



<li><strong>Użyj Dompdf w swojej aplikacji:</strong> Możesz teraz używać Dompdf w swoim projekcie. Istnieje wiele sposobów tworzenia plików PDF za pomocą Dompdf, ale oto podstawowy przykład na początek:
<pre><code>// Dołącz moduł automatycznego ładowania Composer
wymagaj „vendor/autoload.php”;

// Utwórz nowy obiekt Dompdf
$dompdf = nowy Dompdf();

// Załaduj zawartość HTML z pliku lub ciągu znaków
$html = '<h1><span class="ez-toc-section" id="Moj_pierwszy_dokument_PDF_w_Dompdf"></span>Mój pierwszy dokument PDF w Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Renderuj dokument PDF
$dompdf->render();

// Wyślij dokument PDF do wyjścia
$dompdf->stream('dokument.pdf');</code></pre>
    W tym przykładzie tworzony jest nowy dokument PDF z tytułem i przesyłany jako plik „document.pdf”. Możesz dostosować zawartość HTML do swoich potrzeb.</li>
</ol>



<p>Teraz, gdy masz już zainstalowany Dompdf, możesz zacząć generować eleganckie i funkcjonalne pliki PDF w swoich aplikacjach internetowych. Dompdf oferuje wiele zaawansowanych funkcji dostosowywania renderowania plików PDF, takich jak zarządzanie obrazami, niestandardowymi czcionkami i stylami CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Tworzenie_eleganckiego_pliku_PDF_w_PHP"></span>Tworzenie eleganckiego pliku PDF w PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Inna_metoda_instalacji_i_uzywania_Dompdf"></span>Inna metoda instalacji i używania Dompdf<span class="ez-toc-section-end"></span></h3>



<p>Oto kroki, które należy wykonać:<br>1. Pobierz najnowszą wersję Dompdf z oficjalnej strony internetowej.<br>2. Wyodrębnij pobrane pliki i umieść je w swoim projekcie PHP.<br>3. Dołącz plik Dompdfautoload.php, aby załadować bibliotekę do skryptu PHP.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Tworzenie_pliku_PDF_z_szablonu_HTML"></span>Tworzenie pliku PDF z szablonu HTML<span class="ez-toc-section-end"></span></h4>



<p>Teraz, gdy mamy zainstalowany Dompdf, zobaczymy, jak utworzyć plik PDF przy użyciu szablonu HTML. Wykonaj następujące kroki:</p>



<p>1. Utwórz plik HTML zawierający żądaną strukturę i układ pliku PDF.<br>2. Użyj funkcji CSS, aby nadać styl swojemu dokumentowi, używając właściwości takich jak rodzina czcionek, rozmiar czcionki, obramowanie itp.<br>3. Dołącz dane dynamiczne, używając tagów specyficznych dla Dompdf, takich jak „{{name}}” lub „{{address}}”.<br>4. Użyj klasy Dompdf, aby wygenerować plik PDF przy użyciu utworzonego szablonu HTML.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Zarzadzanie_obrazami_i_czcionkami"></span>Zarządzanie obrazami i czcionkami<span class="ez-toc-section-end"></span></h4>



<p>Podczas tworzenia stylowych plików PDF często konieczne jest dołączenie obrazów lub użycie określonych czcionek. Oto jak to zrobić za pomocą Dompdf:</p>



<p>1. Dołącz obrazy do szablonu HTML za pomocą tagu <img decoding="async" src="chemin_vers_image">.<br>2. Należy pamiętać, że Dompdf nie zawiera domyślnie wszystkich czcionek. Możesz dodać niestandardowe czcionki, używając @font-face w swoim CSS lub używając czcionek dostarczonych przez Dompdf.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Optymalizacja_renderowania_i_naprawianie_problemow_z_Dompdf"></span>Optymalizacja renderowania i naprawianie problemów z Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Czasami mogą wystąpić problemy z renderowaniem pliku PDF lub generowaniem plików. Oto kilka wskazówek, jak je rozwiązać:</p>



<p>1. Sprawdź, czy szablon HTML jest poprawnie skonstruowany i ważny.<br>2. Upewnij się, że wszystkie zasoby zewnętrzne (obrazy, czcionki itp.) są dostępne z serwera.<br>3. Zdebuguj swój kod, włączając tryb debugowania Dompdf i sprawdzając wyświetlane błędy.<br>4. Zobacz dokumentację Dompdf, aby uzyskać więcej informacji na temat typowych konfiguracji i problemów.</p>



<p>Korzystając z Dompdf, możesz zapewnić użytkownikom lepszą obsługę, dostarczając profesjonalne i dobrze sformatowane dokumenty PDF. Niezależnie od tego, czy generujesz raporty, faktury czy inne typy dokumentów, Dompdf to niezawodny i wydajny wybór.</p>



<p>Podsumowując, instalacja Dompdf jest szybka i łatwa dzięki Composer. Po zainstalowaniu możesz rozpocząć tworzenie wysokiej jakości plików PDF, aby spełnić potrzeby aplikacji internetowych. Nie zapomnij zapoznać się z oficjalną dokumentacją Dompdf, aby dowiedzieć się więcej o jego funkcjach i dostępnych opcjach dostosowywania.</p>



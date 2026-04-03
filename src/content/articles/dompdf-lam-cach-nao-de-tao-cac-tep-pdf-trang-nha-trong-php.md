---

title: "Dompdf: Làm cách nào để tạo các tệp PDF trang nhã trong PHP?"
slug: "dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php"
excerpt: "Giới thiệu về Dompdf Dompdf là thư viện PHP cho phép bạn tạo tệp PDF từ nội dung HTML. Giải pháp này rất hữu ích để tạo báo cáo, hóa đơn hoặc bất kỳ tài liệu nào khác ở định dạng PDF. Trong bài viết này, chúng ta sẽ khám phá các tính năng cơ [&hellip;]"
date: "2024-03-09T12:43:49"
featuredImage: "/images/blog/Dompdf-Comment-creer-des-PDF-elegants-en-PHP-.png"
categories: ["cong-nghe-va-ky-thuat-so-vi", "may-tinh-va-du-lieu-vi"]
---


<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Gioi_thieu_ve_Dompdf" >Giới thiệu về Dompdf</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Dieu_kien_tien_quyet" >Điều kiện tiên quyết</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Cai_dat_Dompdf" >Cài đặt Dompdf</a></li></ul></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-1'><a class="ez-toc-link ez-toc-heading-4" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Tai_lieu_PDF_dau_tien_cua_toi_voi_Dompdf" >Tài liệu PDF đầu tiên của tôi với Dompdf</a><ul class='ez-toc-list-level-2' ><li class='ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-5" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Tao_mot_tep_PDF_thanh_lich_bang_PHP" >Tạo một tệp PDF thanh lịch bằng PHP</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-6" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Mot_phuong_phap_cai_dat_va_su_dung_Dompdf_khac" >Một phương pháp cài đặt và sử dụng Dompdf khác</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Tao_tep_PDF_tu_mau_HTML" >Tạo tệp PDF từ mẫu HTML</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Quan_ly_hinh_anh_va_phong_chu" >Quản lý hình ảnh và phông chữ</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/vi/dompdf-lam-cach-nao-de-tao-cac-tep-pdf-trang-nha-trong-php/#Toi_uu_hoa_ket_xuat_va_khac_phuc_su_co_Dompdf" >Tối ưu hóa kết xuất và khắc phục sự cố Dompdf</a></li></ul></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Gioi_thieu_ve_Dompdf"></span>Giới thiệu về Dompdf<span class="ez-toc-section-end"></span></h2>



<p>Dompdf là thư viện PHP cho phép bạn tạo tệp PDF từ nội dung HTML. Giải pháp này rất hữu ích để tạo báo cáo, hóa đơn hoặc bất kỳ tài liệu nào khác ở định dạng PDF. Trong bài viết này, chúng ta sẽ khám phá các tính năng cơ bản của Dompdf và tìm hiểu cách sử dụng nó để tạo các tệp PDF trang nhã và tiện dụng.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Dieu_kien_tien_quyet"></span>Điều kiện tiên quyết<span class="ez-toc-section-end"></span></h3>



<p>Trước khi cài đặt Dompdf, hãy đảm bảo bạn có những điều sau:</p>



<ul class="wp-block-list">
<li><strong>PHP:</strong> Dompdf yêu cầu PHP >= 5.4. Nó tương thích với các phiên bản 7.x của PHP.</li>



<li><strong>Phần mở rộng PHP:</strong> Đảm bảo bạn đã bật các tiện ích mở rộng PHP sau: mbstring, DOM và GD. Những tiện ích mở rộng này rất cần thiết để Dompdf hoạt động bình thường.</li>



<li><strong>Soạn, biên soạn :</strong> Dompdf được phân phối thông qua Composer, một trình quản lý phụ thuộc cho PHP. Đảm bảo bạn đã cài đặt Composer trên hệ thống của mình.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Cai_dat_Dompdf"></span>Cài đặt Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Để cài đặt Dompdf, hãy làm theo các bước sau:</p>



<ol class="wp-block-list">
<li><strong>Tạo một dự án PHP mới:</strong> Nếu bạn chưa có dự án hiện có, hãy tạo một dự án mới bằng cách sử dụng cấu trúc cơ bản mà bạn chọn.</li>



<li><strong>Thêm phần phụ thuộc Dompdf qua Composer:</strong> Mở bảng điều khiển và điều hướng đến thư mục dự án của bạn. Chạy lệnh sau để thêm Dompdf vào dự án của bạn:     <pre><code>nhà soạn nhạc yêu cầu dompdf/dompdf</code></pre>     Lệnh này sẽ tự động tải xuống và cài đặt Dompdf cùng với các phần phụ thuộc của nó.</li>



<li><strong>Sử dụng Dompdf trong ứng dụng của bạn:</strong> Bây giờ bạn có thể sử dụng Dompdf trong dự án của mình. Có nhiều cách để tạo tệp PDF bằng Dompdf, nhưng đây là một ví dụ cơ bản để bạn bắt đầu:
<pre><code>// Bao gồm trình tải tự động Composer
yêu cầu 'nhà cung cấp/autoload.php';

// Tạo một đối tượng Dompdf mới
$dompdf = Dompdf mới();

// Tải nội dung HTML từ một tệp hoặc chuỗi
$html = '<h1><span class="ez-toc-section" id="Tai_lieu_PDF_dau_tien_cua_toi_voi_Dompdf"></span>Tài liệu PDF đầu tiên của tôi với Dompdf<span class="ez-toc-section-end"></span></h1>';
$dompdf->loadHtml($html);

// Hiển thị tài liệu PDF
$dompdf->render();

// Gửi tài liệu PDF tới đầu ra
$dompdf->stream('document.pdf');</code></pre>
    Ví dụ này tạo một tài liệu PDF mới có tiêu đề và tải nó lên dưới dạng tệp &#8220;document.pdf&#8221;. Bạn có thể tùy chỉnh nội dung HTML theo nhu cầu của mình.</li>
</ol>



<p>Bây giờ bạn đã cài đặt Dompdf, bạn có thể bắt đầu tạo các tệp PDF trang nhã và đầy chức năng trong các ứng dụng web của mình. Dompdf cung cấp nhiều tính năng nâng cao để tùy chỉnh hiển thị PDF, chẳng hạn như quản lý hình ảnh, phông chữ tùy chỉnh và kiểu CSS.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Tao_mot_tep_PDF_thanh_lich_bang_PHP"></span>Tạo một tệp PDF thanh lịch bằng PHP<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Генерация PDF в Laravel | DOMPDF - Создаем PDF файлы из HTML страницы" width="500" height="281" src="https://www.youtube.com/embed/zs_2_t3r52s?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Mot_phuong_phap_cai_dat_va_su_dung_Dompdf_khac"></span>Một phương pháp cài đặt và sử dụng Dompdf khác<span class="ez-toc-section-end"></span></h3>



<p>Dưới đây là các bước để làm theo:<br>1. Tải xuống phiên bản mới nhất của Dompdf từ trang web chính thức.<br>2. Giải nén các tệp đã tải xuống và đặt chúng vào dự án PHP của bạn.<br>3. Bao gồm tệp Dompdfautoload.php để tải thư viện vào tập lệnh PHP của bạn.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Tao_tep_PDF_tu_mau_HTML"></span>Tạo tệp PDF từ mẫu HTML<span class="ez-toc-section-end"></span></h4>



<p>Bây giờ chúng ta đã cài đặt Dompdf, chúng ta sẽ xem cách tạo tệp PDF bằng mẫu HTML. Thực hiện theo các bước sau:</p>



<p>1. Tạo một tệp HTML chứa cấu trúc và bố cục bạn muốn cho tệp PDF của mình.<br>2. Sử dụng các tính năng CSS để tạo kiểu cho tài liệu của bạn, sử dụng các thuộc tính như họ phông chữ, cỡ chữ, đường viền, v.v.<br>3. Bao gồm dữ liệu động bằng cách sử dụng các thẻ dành riêng cho Dompdf, chẳng hạn như &#8220;{{name}}&#8221; hoặc &#8220;{{address}}&#8221;.<br>4. Sử dụng lớp Dompdf để tạo tệp PDF bằng mẫu HTML bạn đã tạo.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Quan_ly_hinh_anh_va_phong_chu"></span>Quản lý hình ảnh và phông chữ<span class="ez-toc-section-end"></span></h4>



<p>Khi tạo các tệp PDF phong cách, thường cần phải bao gồm hình ảnh hoặc sử dụng các phông chữ cụ thể. Đây là cách thực hiện với Dompdf:</p>



<p>1. Đưa hình ảnh vào mẫu HTML của bạn bằng thẻ <img decoding="async" src="chemin_vers_image">.<br>2. Xin lưu ý rằng Dompdf không bao gồm tất cả các phông chữ theo mặc định. Bạn có thể thêm phông chữ tùy chỉnh bằng cách sử dụng @font-face trong CSS của mình hoặc sử dụng phông chữ do Dompdf cung cấp.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Toi_uu_hoa_ket_xuat_va_khac_phuc_su_co_Dompdf"></span>Tối ưu hóa kết xuất và khắc phục sự cố Dompdf<span class="ez-toc-section-end"></span></h4>



<p>Đôi khi bạn có thể gặp phải sự cố khi hiển thị tệp PDF hoặc tạo tệp. Dưới đây là một số mẹo để giải quyết chúng:</p>



<p>1. Kiểm tra xem mẫu HTML của bạn có được xây dựng chính xác và hợp lệ hay không.<br>2. Đảm bảo tất cả tài nguyên bên ngoài (hình ảnh, phông chữ, v.v.) đều có thể truy cập được từ máy chủ.<br>3. Gỡ lỗi mã của bạn bằng cách kích hoạt chế độ gỡ lỗi Dompdf và kiểm tra các lỗi được hiển thị.<br>4. Xem tài liệu Dompdf để biết thêm thông tin về các cấu hình và sự cố thường gặp.</p>



<p>Sử dụng Dompdf, bạn có thể cung cấp trải nghiệm người dùng nâng cao bằng cách cung cấp các tài liệu PDF chuyên nghiệp và được định dạng tốt. Dù tạo báo cáo, hóa đơn hay các loại tài liệu khác, Dompdf là sự lựa chọn đáng tin cậy và mạnh mẽ.</p>



<p>Tóm lại, việc cài đặt Dompdf rất nhanh chóng và dễ dàng nhờ Composer. Sau khi cài đặt, bạn có thể bắt đầu tạo các tệp PDF chất lượng cao để đáp ứng nhu cầu ứng dụng web của mình. Đừng quên xem tài liệu chính thức của Dompdf để tìm hiểu thêm về các tính năng của nó và các tùy chọn tùy chỉnh có sẵn.</p>



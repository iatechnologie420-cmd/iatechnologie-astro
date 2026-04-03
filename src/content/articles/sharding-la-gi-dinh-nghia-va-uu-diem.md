---
title: "Sharding là gì? định nghĩa và ưu điểm"
slug: "sharding-la-gi-dinh-nghia-va-uu-diem"
excerpt: "Hiểu về sharding: định nghĩa và nguyên tắc cơ bản Thế giới cơ sở dữ liệu và lưu trữ dữ liệu quy mô lớn rất phức tạp và không ngừng phát triển. Để quản lý hiệu quả khối lượng dữ liệu ngày càng tăng theo cấp số nhân, kiến ​​trúc CNTT phải đổi mới và [&hellip;]"
date: "2024-03-09T12:34:13"
featuredImage: "/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-3.png"
categories: ["co-so-ha-tang-va-mang-vi", "cong-nghe-va-ky-thuat-so-vi"]
---


<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
<iframe title="Database Sharding and Partitioning" width="500" height="281" src="https://www.youtube.com/embed/wXvljefXyEo?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div></figure>



<div id="ez-toc-container" class="ez-toc-v2_0_82_2 counter-hierarchy ez-toc-counter ez-toc-grey ez-toc-container-direction">
<div class="ez-toc-title-container">
<p class="ez-toc-title" style="cursor:inherit">Table of Contents</p>
<span class="ez-toc-title-toggle"><a href="#" class="ez-toc-pull-right ez-toc-btn ez-toc-btn-xs ez-toc-btn-default ez-toc-toggle" aria-label="Toggle Table of Content"><span class="ez-toc-js-icon-con"><span class=""><span class="eztoc-hide" style="display:none;">Toggle</span><span class="ez-toc-icon-toggle-span"><svg style="fill: #999;color:#999" xmlns="http://www.w3.org/2000/svg" class="list-377408" width="20px" height="20px" viewBox="0 0 24 24" fill="none"><path d="M6 6H4v2h2V6zm14 0H8v2h12V6zM4 11h2v2H4v-2zm16 0H8v2h12v-2zM4 16h2v2H4v-2zm16 0H8v2h12v-2z" fill="currentColor"></path></svg><svg style="fill: #999;color:#999" class="arrow-unsorted-368013" xmlns="http://www.w3.org/2000/svg" width="10px" height="10px" viewBox="0 0 24 24" version="1.2" baseProfile="tiny"><path d="M18.2 9.3l-6.2-6.3-6.2 6.3c-.2.2-.3.4-.3.7s.1.5.3.7c.2.2.4.3.7.3h11c.3 0 .5-.1.7-.3.2-.2.3-.5.3-.7s-.1-.5-.3-.7zM5.8 14.7l6.2 6.3 6.2-6.3c.2-.2.3-.5.3-.7s-.1-.5-.3-.7c-.2-.2-.4-.3-.7-.3h-11c-.3 0-.5.1-.7.3-.2.2-.3.5-.3.7s.1.5.3.7z"/></svg></span></span></span></a></span></div>
<nav><ul class='ez-toc-list ez-toc-list-level-1 ' ><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-1" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Hieu_ve_sharding_dinh_nghia_va_nguyen_tac_co_ban" >Hiểu về sharding: định nghĩa và nguyên tắc cơ bản</a><ul class='ez-toc-list-level-3' ><li class='ez-toc-heading-level-3'><a class="ez-toc-link ez-toc-heading-2" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Sharding_la_gi" >Sharding là gì?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-3" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Phan_manh_hoat_dong_nhu_the_nao" >Phân mảnh hoạt động như thế nào?</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-4" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Loi_ich_cua_Shending" >Lợi ích của Shending</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-5" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Nhung_thach_thuc_va_can_nhac" >Những thách thức và cân nhắc</a></li></ul></li></ul></li><li class='ez-toc-page-1 ez-toc-heading-level-2'><a class="ez-toc-link ez-toc-heading-6" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Du_lieu_duoc_phan_phoi_nhu_the_nao" >Dữ liệu được phân phối như thế nào?</a><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><ul class='ez-toc-list-level-4' ><li class='ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-7" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Luu_tru_du_lieu_theo_phan_doan" >Lưu trữ dữ liệu theo phân đoạn</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-8" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Nhuoc_diem_cua_Shending" >Nhược điểm của Shending</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-9" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Nhung_thach_thuc_ky_thuat_cua_sharding" >Những thách thức kỹ thuật của sharding</a></li><li class='ez-toc-page-1 ez-toc-heading-level-4'><a class="ez-toc-link ez-toc-heading-10" href="/vi/sharding-la-gi-dinh-nghia-va-uu-diem/#Nhung_can_nhac_thuc_te_cho_viec_bao_ve" >Những cân nhắc thực tế cho việc bảo vệ</a></li></ul></li></ul></li></ul></nav></div>
<h2 class="wp-block-heading"><span class="ez-toc-section" id="Hieu_ve_sharding_dinh_nghia_va_nguyen_tac_co_ban"></span>Hiểu về sharding: định nghĩa và nguyên tắc cơ bản<span class="ez-toc-section-end"></span></h2>



<p>Thế giới cơ sở dữ liệu và lưu trữ dữ liệu quy mô lớn rất phức tạp và không ngừng phát triển. Để quản lý hiệu quả khối lượng dữ liệu ngày càng tăng theo cấp số nhân, kiến ​​trúc CNTT phải đổi mới và tìm giải pháp để tối ưu hóa hiệu suất và quản lý dữ liệu này. Một cách tiếp cận vấn đề này là một kỹ thuật được gọi là <strong>mảnh vỡ</strong>. </p>



<p>Trong bài viết này, chúng ta sẽ định nghĩa sharding, hiểu các nguyên tắc cơ bản của nó và tại sao nó lại cần thiết trong các hệ thống cơ sở dữ liệu hiện đại.</p>



<h3 class="wp-block-heading"><span class="ez-toc-section" id="Sharding_la_gi"></span>Sharding là gì?<span class="ez-toc-section-end"></span></h3>



<p>CÁC <strong>mảnh vỡ</strong> là phương pháp phân vùng dữ liệu theo chiều ngang trong cơ sở dữ liệu phân tán hoặc hệ thống quản lý cơ sở dữ liệu. Kỹ thuật này bao gồm việc chia cơ sở dữ liệu thành các phần nhỏ hơn gọi là <em>mảnh vỡ</em>, có thể được phân phối trên một số máy chủ. Mỗi phân đoạn chứa một tập hợp con dữ liệu và hoạt động như một cơ sở dữ liệu độc lập. Ưu điểm chính của việc này là nó cho phép quản lý lượng lớn dữ liệu và giao dịch hiệu quả hơn bằng cách giảm tải trên từng máy chủ riêng lẻ.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Phan_manh_hoat_dong_nhu_the_nao"></span>Phân mảnh hoạt động như thế nào?<span class="ez-toc-section-end"></span></h4>



<p>Phân mảnh dựa trên logic phân phối dữ liệu được xác định bằng thuật toán phân mảnh. Có nhiều thuật toán khác nhau nhưng việc lựa chọn thường phụ thuộc vào bản chất của dữ liệu và truy vấn mà hệ thống phải xử lý. Các ví dụ phổ biến về thuật toán bao gồm phân mảnh dựa trên phạm vi (trong đó dữ liệu được phân phối theo phạm vi giá trị), phân mảnh băm (trong đó hàm băm của một số khóa nhất định xác định vị trí của dữ liệu) hoặc phân mảnh dựa trên thư mục (với bảng tra cứu để xác định vị trí). dữ liệu).</p>



<p>Sau khi các phân đoạn được tạo và dữ liệu được phân phối, một hệ thống quản lý tập trung, thường được gọi là <em>người quản lý phân đoạn</em> Hoặc <em>xích đu</em>, là cần thiết để điều phối các giao dịch và yêu cầu giữa các phân đoạn khác nhau. Hệ thống này đảm bảo rằng các truy vấn được chuyển hướng đến đúng phân đoạn, do đó chỉ cho phép tương tác với phần có liên quan của cơ sở dữ liệu.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Loi_ich_cua_Shending"></span>Lợi ích của Shending<span class="ez-toc-section-end"></span></h4>



<p>Sharding cung cấp một số ưu điểm khiến nó trở nên hấp dẫn đối với các hệ thống lớn:</p>



<ul class="wp-block-list">
<li><strong>Khả năng mở rộng</strong> : Sharding cho phép cơ sở dữ liệu dễ dàng thích ứng với tải tăng lên bằng cách thêm nhiều máy chủ hơn.</li>



<li><strong>Hiệu suất</strong> : Bằng cách giảm tải trên mỗi máy chủ, hiệu suất truy vấn có thể được cải thiện đáng kể, đặc biệt là đối với các hoạt động ghi.</li>



<li><strong>khả dụng</strong> : Ngay cả khi một phân đoạn bị hỏng, các phân đoạn khác vẫn tiếp tục hoạt động, tăng độ tin cậy của toàn bộ hệ thống.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Nhung_thach_thuc_va_can_nhac"></span>Những thách thức và cân nhắc<span class="ez-toc-section-end"></span></h4>



<p>Tuy nhiên, shending cũng đi kèm với những thách thức:</p>



<ul class="wp-block-list">
<li>Độ phức tạp của việc quản lý phân đoạn có thể tăng theo số lượng phân đoạn.</li>



<li>Các giao dịch yêu cầu thông tin trên các phân đoạn khác nhau sẽ phức tạp hơn để quản lý.</li>



<li>Tính nhất quán của dữ liệu có thể trở nên khó đảm bảo hơn khi số lượng phân đoạn tăng lên.</li>
</ul>



<p>Vì vậy, điều quan trọng là phải xem xét cẩn thận liệu sharding có phải là chiến lược phù hợp cho một ứng dụng nhất định hay không. Đôi khi các cách tiếp cận khác như phân vùng dọc, sao chép dữ liệu hoặc sử dụng cơ sở dữ liệu không quan hệ có thể phù hợp hơn.</p>



<h2 class="wp-block-heading"><span class="ez-toc-section" id="Du_lieu_duoc_phan_phoi_nhu_the_nao"></span>Dữ liệu được phân phối như thế nào?<span class="ez-toc-section-end"></span></h2>



<figure class="wp-block-image size-full"><img fetchpriority="high" decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png" alt="" class="wp-image-1070" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-1-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<p>Việc phân phối dữ liệu trong môi trường phân chia có thể được thực hiện theo các thuật toán khác nhau. Dưới đây là một số trong những phổ biến nhất:</p>



<ul class="wp-block-list">
<li><strong>Phân đoạn dựa trên phạm vi khóa:</strong> Dữ liệu được phân chia theo một khóa cụ thể, trong đó mỗi phân đoạn chịu trách nhiệm về một phạm vi giá trị.</li>



<li><strong>Phân đoạn dựa trên hàm băm:</strong> Hàm băm được sử dụng để xác định phân đoạn nào sẽ lưu trữ một bản ghi cụ thể, dựa trên khóa.</li>



<li><strong>Sharding dựa trên thư mục:</strong> Một thư mục duy trì ánh xạ giữa các bản ghi và phân đoạn nơi chúng được lưu trữ.</li>
</ul>



<p>Những phương pháp này cho phép phân phối dữ liệu tương đối cân bằng, giảm tắc nghẽn và cải thiện thời gian phản hồi.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Luu_tru_du_lieu_theo_phan_doan"></span>Lưu trữ dữ liệu theo phân đoạn<span class="ez-toc-section-end"></span></h4>



<p>Dữ liệu được lưu trữ trong mỗi phân đoạn độc lập với các phân đoạn khác. Điều này có nghĩa là mỗi phân đoạn hoạt động như một cơ sở dữ liệu độc lập, có các lược đồ và chỉ mục riêng. Tính nhất quán của dữ liệu trên các phân đoạn được duy trì một cách hợp lý thay vì vật lý, điều này đôi khi có thể gây ra sự phức tạp khi quản lý các giao dịch trải rộng trên nhiều phân đoạn.</p>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Nhuoc_diem_cua_Shending"></span>Nhược điểm của Shending<span class="ez-toc-section-end"></span></h4>



<p>Tuy nhiên, sharding cũng có những nhược điểm nhất định:</p>



<ul class="wp-block-list">
<li><strong>Độ phức tạp:</strong> Việc quản lý và duy trì nhiều phân đoạn có thể trở nên phức tạp, đặc biệt là đối với tính nhất quán của dữ liệu và quản lý giao dịch.</li>



<li><strong>Rủi ro phân phối kém:</strong> Việc phân phối dữ liệu không đồng đều có thể dẫn đến “điểm nóng”, trong đó một số phân đoạn bị quá tải.</li>



<li><strong>Chi phí:</strong> Nhu cầu vận hành và quản lý nhiều cơ sở hạ tầng hơn có thể làm tăng chi phí.</li>



<li></li>
</ul>



<figure class="wp-block-image size-full"><img decoding="async" width="1792" height="1024" src="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png" alt="" class="wp-image-1071" srcset="/images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2.png 1792w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-300x171.png 300w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1024x585.png 1024w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-150x86.png 150w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-768x439.png 768w, /images/blog/Quest-ce-que-le-Sharding-definition-et-avantages-de-cette-methode-de-distribution-des-donnees-2-1536x878.png 1536w" sizes="(max-width: 1792px) 100vw, 1792px" /></figure>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Nhung_thach_thuc_ky_thuat_cua_sharding"></span>Những thách thức kỹ thuật của sharding<span class="ez-toc-section-end"></span></h4>



<p>Việc triển khai sharding đặt ra một số câu hỏi kỹ thuật:</p>



<ul class="wp-block-list">
<li><strong>Độ phức tạp của thiết kế</strong> : Việc lập lịch trình phân chia khóa là rất quan trọng và cần được thực hiện cẩn thận vì thiết kế kém có thể dẫn đến mất cân bằng trong phân phối dữ liệu và làm ảnh hưởng đến hiệu quả của hệ thống.</li>



<li><strong>Truy vấn ngang</strong> : Việc thực hiện các truy vấn trên nhiều phân đoạn có thể phức tạp và cồng kềnh vì nó đòi hỏi cơ chế giao tiếp và tổng hợp giữa các phân đoạn.</li>



<li><strong>Giao dịch phân phối</strong> : Việc duy trì tính toàn vẹn của các giao dịch trên nhiều phân đoạn rất phức tạp và đòi hỏi các giao thức phối hợp và cơ chế khóa phức tạp.</li>



<li><strong>Chia tỷ lệ</strong> : Mặc dù phân đoạn cho phép khả năng mở rộng nhưng việc thêm hoặc xóa phân đoạn sau thực tế có thể phức tạp và thường yêu cầu phân phối lại dữ liệu.</li>
</ul>



<h4 class="wp-block-heading"><span class="ez-toc-section" id="Nhung_can_nhac_thuc_te_cho_viec_bao_ve"></span>Những cân nhắc thực tế cho việc bảo vệ<span class="ez-toc-section-end"></span></h4>



<p>Bên cạnh những thách thức về mặt kỹ thuật, còn có những cân nhắc thực tế cần tính đến:</p>



<ul class="wp-block-list">
<li><strong>Trị giá</strong> : Sự phức tạp của việc triển khai và duy trì sharding có thể dẫn đến chi phí đáng kể về phần cứng, phần mềm và nguồn nhân lực chuyên môn.</li>



<li><strong>Hiệu suất</strong> : Việc chọn chiến lược sharding không phù hợp có thể dẫn đến hiệu suất kém, đặc biệt nếu cân bằng tải không được quản lý tốt.</li>



<li><strong>Tính nhất quán của dữ liệu</strong> : Đảm bảo tính nhất quán của dữ liệu trên tất cả các phân đoạn là điều cần thiết nhưng khó đạt được, đặc biệt là trong môi trường phân tán cao.</li>



<li><strong>Chuyên môn kỹ thuật</strong> : Cần có chuyên môn kỹ thuật sâu để quản lý sự phức tạp của sharding và ứng phó với các vấn đề.</li>



<li><strong>Sao lưu và khôi phục</strong> : Việc quản lý sao lưu và khôi phục trở nên phức tạp hơn với phân đoạn vì các hoạt động này phải được phối hợp trên nhiều phân đoạn.</li>
</ul>



<p>Tóm lại, mặc dù sharding là một kỹ thuật mạnh mẽ dành cho cơ sở dữ liệu đòi hỏi mức hiệu suất và khả năng mở rộng cao, nhưng nó đặt ra một loạt thách thức và yêu cầu phải cân nhắc thực tế đáng kể để được triển khai một cách tối ưu. Bằng cách nhận thức được các vấn đề và chuẩn bị cẩn thận chiến lược sharding, các tổ chức có thể hưởng lợi đầy đủ từ lợi ích của nó đồng thời giảm thiểu rủi ro và chi phí liên quan.</p>



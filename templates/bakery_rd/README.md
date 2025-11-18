# Hệ thống Axiom Prompt cho R&D Bánh kẹo

Chào mừng bạn đến với hệ thống prompt được cá nhân hóa cho Nghiên cứu và Phát triển (R&D) trong ngành làm bánh. Hệ thống này được xây dựng dựa trên nền tảng của dự án Axiom Prompt Engineering (APE), nhằm cung cấp một bộ công cụ mạnh mẽ, linh hoạt và dựa trên khoa học để giải quyết các thách thức trong ngành.

## Tổng quan

Hệ thống này bao gồm một bộ các "Prompt Template" được thiết kế cho các tác vụ R&D cụ thể. Mỗi template hoạt động dựa trên một bộ "Axiom" (chân lý khoa học) cốt lõi được định nghĩa trong `/protocols/bakery_axioms.md`. Điều này đảm bảo rằng tất cả các kết quả đầu ra đều có tính chính xác và nhất quán về mặt khoa học.

## Các Prompt Template có sẵn

1.  **`recipe_generation.md`**: Dùng để tạo ra các công thức làm bánh mới từ ý tưởng ban đầu, với các ràng buộc cụ thể.
2.  **`troubleshooting.md`**: Dùng để chẩn đoán và tìm ra giải pháp cho các vấn đề kỹ thuật gặp phải trong quá trình sản xuất.
3.  **`research_analyzer.md`**: Dùng để tóm tắt, phân tích và tìm cảm hứng sáng tạo từ các tài liệu khoa học hoặc kỹ thuật.
4.  **`ingredient_comparison.md`**: Dùng để thực hiện các phân tích so sánh chi tiết giữa các loại nguyên liệu khác nhau.
5.  **`tech_doc_generator.md`**: Dùng để tự động hóa việc tạo các tài liệu kỹ thuật như Bảng thông số sản phẩm (Spec Sheet) hoặc Quy trình vận hành tiêu chuẩn (SOP).

## Chế độ Tối ưu hóa (Optimization Modes)

Đây là trái tim của hệ thống, cho phép bạn điều chỉnh phong cách và độ sâu của phản hồi để phù hợp với nhu-cầu-tại-thời-điểm. Bạn có thể chọn một trong ba chế độ sau:

### MODE: `Accurate`

-   **Mục tiêu:** Cung cấp thông tin chính xác, chi tiết, và sâu về mặt khoa học.
-   **Khi nào sử dụng:** Khi bạn cần câu trả lời dựa trên dữ liệu, bằng chứng khoa học rõ ràng, và cần hiểu rõ "tại sao" đằng sau mỗi hiện tượng. Rất lý tưởng cho việc xây dựng công thức nền tảng, phân tích nguyên nhân gốc rễ của sự cố, hoặc khi cần tạo tài liệu kỹ thuật chính thức.
-   **Kết quả mong đợi:** Các bảng so sánh chi tiết, công thức với tỷ lệ phần trăm của thợ làm bánh (baker's percentages), giải thích cặn kẽ về các cơ chế hóa học, và các quy trình có kiểm soát chặt chẽ.

### MODE: `Efficient`

-   **Mục tiêu:** Cung cấp câu trả lời nhanh chóng, đi thẳng vào vấn đề và có tính ứng dụng ngay lập tức.
-   **Khi nào sử dụng:** Khi bạn đang ở trong môi trường sản xuất, cần một giải pháp nhanh, hoặc muốn có một cái nhìn tổng quan mà không cần đi sâu vào chi tiết. Rất phù hợp để xử lý sự cố cấp bách, tạo SOP cô đọng, hoặc khi cần so sánh nhanh giữa các lựa chọn.
-   **Kết quả mong đợi:** Các checklist, gạch đầu dòng, hướng dẫn "If-Then", các quy tắc kinh nghiệm (rule of thumb), và các bản tóm tắt cho quản lý (executive summary).

### MODE: `Creative`

-   **Mục tiêu:** Khơi nguồn cảm hứng, thúc đẩy tư duy đột phá và khám phá những ý tưởng mới lạ.
-   **Khi nào sử dụng:** Khi bạn đang trong giai đoạn brainstorm, tìm kiếm sự đổi mới, hoặc muốn nhìn một vấn đề cũ theo một góc độ hoàn toàn mới. Lý tưởng cho việc phát triển sản phẩm mới, tìm kiếm ứng dụng không ngờ tới cho một nguyên liệu, hoặc biến một "lỗi" thành một "tính năng".
-   **Kết quả mong đợi:** Các câu hỏi "What if...?", các ý tưởng kết hợp liên ngành, các phép loại suy (analogy) để giải thích khái niệm phức tạp, và các gợi ý cho những thử nghiệm trong tương lai.

## Cách sử dụng

1.  **Chọn Template:** Dựa vào công việc bạn cần làm (ví dụ: tạo công thức mới -> `recipe_generation.md`).
2.  **Điền Tham số:** Mở tệp template và điền thông tin của bạn vào các trường trong dấu ngoặc vuông `[...]`, ví dụ: `[ProductName]`, `[Constraints]`.
3.  **Chọn Chế độ Tối ưu:** Quyết định mục tiêu của bạn là gì (chính xác, hiệu quả, hay sáng tạo?) và điền vào trường `[OptimizationMode]`.
4.  **Thực thi Prompt:** Sao chép toàn bộ nội dung đã điền vào một mô hình ngôn ngữ lớn (LLM).
5.  **Xem các ví dụ:** Tham khảo các tệp trong thư mục `/examples/bakery_rd/` để xem các kịch bản sử dụng thực tế.

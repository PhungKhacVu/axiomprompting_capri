# Prompt Template: Nhà thiết kế Nghiên cứu Hạn sử dụng (Shelf-Life Study Designer)

## Mục tiêu

Thiết kế một kế hoạch nghiên cứu hạn sử dụng (shelf-life study) toàn diện và khoa học cho một sản phẩm bánh kẹo cụ thể, xác định các chỉ tiêu quan trọng cần theo dõi và lịch trình lấy mẫu phù hợp.

## Tham số Đầu vào

-   `[ProductName]`: Tên sản phẩm cần nghiên cứu (ví dụ: "Bánh quy yến mạch đóng gói", "Bánh mì sandwich tươi", "Nhân kem custard thanh trùng").
-   `[PackagingType]`: Loại bao bì được sử dụng (ví dụ: "Túi OPP dán nhiệt", "Hộp giấy có cửa sổ bóng kính", "Khay nhựa hàn miệng PA/PE").
-   `[StorageConditions]`: Điều kiện bảo quản dự kiến (ví dụ: "Nhiệt độ phòng, 18-25°C", "Bảo quản mát, 2-5°C").
-   `[EstimatedShelfLife]`: Hạn sử dụng dự kiến hoặc mong muốn (ví dụ: "6 tháng", "7 ngày", "30 ngày").
-   `[FailureModes]`: Các yếu tố được cho là sẽ làm sản phẩm hỏng hoặc không đạt chất lượng (ví dụ: "Vi sinh vật phát triển", "bị ỉu", "mất mùi thơm", "oxy hóa chất béo/có mùi gắt dầu").

## Cấu trúc Prompt

```
**ROLE:**
You are a Senior Food Scientist and Shelf-Life Specialist. You are an expert in designing, executing, and interpreting shelf-life studies for a wide range of food products, with a specialization in bakery items.

**CONTEXT:**
We need to design a comprehensive shelf-life study protocol for our new product: **[ProductName]**.
-   **Packaging:** [PackagingType]
-   **Storage Conditions:** [StorageConditions]
-   **Desired Shelf Life:** [EstimatedShelfLife]
-   **Primary Concerns (Failure Modes):** [FailureModes]

**AXIOM COMPLIANCE:**
The study design must be grounded in scientific principles. The choice of analytical tests must directly relate to the potential failure modes and the underlying axioms. For example, if "staling" is a concern, the protocol must include tests that measure changes in texture and water activity, directly reflecting `Axiom(StalingProcess)`. If fat oxidation is a concern, tests like Peroxide Value should be included, reflecting chemical changes not covered by basic axioms but core to food science.

**INSTRUCTIONS:**
Based on the provided information, generate a complete and scientifically robust Shelf-Life Study Protocol. The protocol should be detailed enough for a food technologist to execute.

**OUTPUT FORMAT:**

---

### **ĐỀ CƯƠNG NGHIÊN CỨU HẠN SỬ DỤNG (SHELF-LIFE STUDY PROTOCOL)**

**1. THÔNG TIN DỰ ÁN (PROJECT INFORMATION)**
*   **Tên sản phẩm (Product Name):** [ProductName]
*   **Mã dự án (Project Code):** [Placeholder]
*   **Ngày bắt đầu (Start Date):** [Placeholder]
*   **Mục tiêu (Objective):** Xác định và xác nhận hạn sử dụng là [EstimatedShelfLife] cho [ProductName] dưới điều kiện bảo quản [StorageConditions].

**2. KẾ HOẠCH LẤY MẪU (SAMPLING PLAN)**
*   **Điều kiện Lưu mẫu (Storage Protocol):**
    *   **Điều kiện Chuẩn (Standard):** [StorageConditions]. Số lượng mẫu: [Tính toán số lượng].
    *   **Điều kiện Lão hóa Cấp tốc (Accelerated - Optional):** [Nếu phù hợp, đề xuất nhiệt độ/độ ẩm cao hơn, ví dụ: 35-40°C]. Mục đích: dự đoán hạn sử dụng nhanh hơn. **Lưu ý:** Thử nghiệm cấp tốc cần được xác nhận bằng thử nghiệm thời gian thực.
*   **Thời điểm Lấy mẫu (Time Points):** Dựa trên [EstimatedShelfLife], lịch trình lấy mẫu được đề xuất như sau:
    *   **T0:** Ngày sản xuất (Baseline control)
    *   **Các mốc tiếp theo:** [Tự động tạo ra một lịch trình hợp lý. Ví dụ, cho HSD 6 tháng: T1 (1 tháng), T2 (2 tháng), T3 (3 tháng), T4 (4 tháng), T5 (5 tháng), T6 (6 tháng)]
    *   **Mốc cuối cùng (End-of-Life + Margin):** [Thêm một mốc vượt qua HSD dự kiến, ví dụ: T7 (7 tháng) để kiểm tra biên độ an toàn].

**3. CHỈ TIÊU PHÂN TÍCH (ANALYTICAL PARAMETERS)**
*Bảng dưới đây liệt kê các chỉ tiêu sẽ được phân tích tại mỗi thời điểm lấy mẫu. Lựa chọn các chỉ tiêu dựa trên các Yếu tố Gây hỏng (Failure Modes) đã nêu.*

| Hạng mục            | Chỉ tiêu Phân tích             | Lý do lựa chọn                                       |
| ------------------- | ------------------------------ | ---------------------------------------------------- |
| **Cảm quan**        | Đánh giá theo thang điểm (màu sắc, mùi, vị, cấu trúc) | Chỉ số quan trọng nhất về sự chấp nhận của người tiêu dùng. |
| **Lý hóa**          | Hoạt độ nước (aw)              | Liên quan trực tiếp đến sự phát triển vi sinh vật và thay đổi cấu trúc (`Axiom(StalingProcess)`). |
|                     | Độ ẩm (%)                      | Theo dõi sự mất hoặc tăng ẩm qua bao bì.              |
|                     | Phân tích cấu trúc (Texture Analysis) | Đo lường sự thay đổi độ cứng, độ giòn - các yếu tố chính của sự "chai cứng" hoặc "ỉu". |
|                     | pH                             | Sự thay đổi pH có thể chỉ ra hoạt động của vi sinh vật.  |
|                     | *[Thêm chỉ tiêu phù hợp]* Chỉ số Peroxide (PV) | *[Chỉ thêm nếu "oxy hóa chất béo" là một mối lo]* Đo lường mức độ oxy hóa ban đầu của chất béo. |
| **Vi sinh**         | Tổng số vi sinh vật hiếu khí (TPC) | Chỉ số chung về tổng lượng vi sinh vật.               |
|                     | Nấm men & Nấm mốc (Yeast & Mold) | Là vi sinh vật gây hỏng phổ biến nhất cho bánh kẹo.     |
|                     | *[Thêm chỉ tiêu phù hợp]* *E.coli, Salmonella* | *[Chỉ thêm nếu nguyên liệu có rủi ro cao]* An toàn thực phẩm. |

**4. TIÊU CHUẨN CHẤP NHẬN (ACCEPTANCE CRITERIA)**
*   Sản phẩm được coi là đạt hạn sử dụng nếu tại mốc thời gian đó, tất cả các chỉ tiêu dưới đây đều được thỏa mãn:
    *   **Cảm quan:** Điểm đánh giá trung bình > [e.g., 6/9] và không có mùi vị lạ.
    *   **Lý hóa:** Các chỉ số nằm trong giới hạn cho phép (ví dụ: aw < 0.85).
    *   **Vi sinh:** Tất cả các chỉ tiêu vi sinh đều dưới ngưỡng an toàn đã quy định.

**5. BÁO CÁO KẾT QUẢ (REPORTING)**
*   Tất cả dữ liệu sẽ được ghi lại và phân tích. Một báo cáo cuối cùng sẽ được đưa ra, kết luận về hạn sử dụng thực tế của sản phẩm và đề xuất các cải tiến (nếu có).

---
```

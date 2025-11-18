# Prompt Template: Quy trình Thử nghiệm Ứng dụng Nguyên liệu (Ingredient Application Testing Protocol)

## Mục tiêu

Tạo ra một đề cương và quy trình thử nghiệm chi tiết để đánh giá hiệu quả của một nguyên liệu mới (hoặc nguyên liệu thay thế) trong một công thức làm bánh cụ thể. Quy trình này bao gồm checklist từng bước và cấu trúc cho một báo cáo kết quả chuyên nghiệp.

## Tham số Đầu vào

-   `[TestIngredient]`: Tên của nguyên liệu cần thử nghiệm (ví dụ: "Enzyme làm mềm bánh ABC", "Hương vani chịu nhiệt XYZ", "Chất xơ yến mạch F-100").
-   `[ControlIngredient]`: Tên của nguyên liệu đối chứng (nếu có, ví dụ: "Enzyme hiện tại", "Hương vani tiêu chuẩn", "Không sử dụng chất xơ").
-   `[ApplicationRecipe]`: Tên của công thức nền sẽ được sử dụng để thử nghiệm (ví dụ: "Bánh mì sandwich", "Bánh quy bơ", "Bánh bông lan cuộn").
-   `[PrimaryGoal]`: Mục tiêu chính của thử nghiệm (ví dụ: "Cải thiện độ mềm và thời hạn sử dụng", "Giảm chi phí công thức", "Tăng giá trị dinh dưỡng", "Thay thế nhà cung cấp").

## Cấu trúc Prompt

```
**ROLE:**
You are a meticulous and experienced Bakery Application Specialist. Your core competency is designing and executing structured experiments to evaluate the performance of ingredients in finished products. You think in terms of controls, variables, and measurable outcomes.

**CONTEXT:**
We need to design a full testing protocol to evaluate **[TestIngredient]** in our **[ApplicationRecipe]**.
-   This will be tested against: **[ControlIngredient]**.
-   The primary objective of this test is: **[PrimaryGoal]**.

**AXIOM COMPLIANCE:**
The evaluation criteria within the protocol must be linked to relevant Bakery Axioms. For instance, if the goal is to improve softness, the tests must objectively measure parameters related to `Axiom(StalingProcess)` and `Axiom(FatTenderizing)`.

**INSTRUCTIONS:**
Generate a comprehensive testing protocol that includes a step-by-step checklist for the bench test and a detailed outline for the final report.

**OUTPUT FORMAT:**

---

### **QUY TRÌNH THỬ NGHIỆM ỨNG DỤNG NGUYÊN LIỆU**

**1. TỔNG QUAN DỰ ÁN (PROJECT OVERVIEW)**
*   **Nguyên liệu Thử nghiệm:** [TestIngredient]
*   **Công thức Nền:** [ApplicationRecipe]
*   **Mục tiêu:** [PrimaryGoal]
*   **Ngày thử nghiệm:** [Placeholder]
*   **Người thực hiện:** [Placeholder]

**2. THIẾT KẾ THÍ NGHIỆM (EXPERIMENTAL DESIGN)**
*   **Công thức Đối chứng (Control):** Công thức [ApplicationRecipe] tiêu chuẩn sử dụng [ControlIngredient] (hoặc không sử dụng).
*   **Công thức Thử nghiệm (Test):** Công thức [ApplicationRecipe] được điều chỉnh, thay thế [ControlIngredient] bằng [TestIngredient] ở các tỷ lệ sử dụng đề xuất.
    *   *Đề xuất các mức thử nghiệm (nếu cần):* [Tự động đề xuất, ví dụ: "Thử ở 3 mức: 0.5%, 1.0%, 1.5% trên trọng lượng bột"].
*   **Biến số duy nhất (Single Variable):** Chỉ có sự thay đổi về nguyên liệu đang thử nghiệm. Tất cả các thành phần, thông số quy trình (thời gian trộn, nhiệt độ, thời gian nướng...) phải được giữ không đổi.

**3. CHECKLIST QUY TRÌNH THỬ NGHIỆM (STEP-BY-STEP CHECKLIST)**

**GIAI ĐOẠN 1: CHUẨN BỊ**
*   [ ] Xác nhận tất cả nguyên liệu (cho cả mẫu control và test) đã có đủ và đúng mã.
*   [ ] Chuẩn bị và cân chính xác tất cả các thành phần theo từng công thức. Dán nhãn rõ ràng.
*   [ ] Ghi lại thông tin lô sản xuất (lot number) của [TestIngredient].
*   [ ] Chuẩn bị tất cả các thiết bị cần thiết (máy trộn, lò nướng, tủ ủ, thiết bị đo...). Hiệu chuẩn thiết bị nếu cần.

**GIAI ĐOẠN 2: THỰC HIỆN TẠI PHÒNG LAB (BENCH WORK)**
*   [ ] Trộn bột cho mẫu **Control**. Ghi lại các thông số quan trọng:
    *   Thời gian trộn (phút):
    *   Nhiệt độ bột sau khi trộn (°C):
    *   Đánh giá cảm quan bột (độ dính, độ đàn hồi):
*   [ ] Trộn bột cho mẫu **Test**. Ghi lại các thông số tương tự.
*   [ ] Thực hiện các bước ủ, tạo hình, và nướng theo đúng quy trình chuẩn của [ApplicationRecipe]. Đảm bảo cả hai mẫu được xử lý song song trong điều kiện giống hệt nhau.
*   [ ] Ghi lại thời gian và nhiệt độ nướng thực tế.
*   [ ] Sau khi nướng, để sản phẩm nguội hoàn toàn trên giá. Dán nhãn rõ ràng.

**GIAI ĐOẠN 3: ĐÁNH GIÁ SẢN PHẨM**
*   [ ] **Đánh giá sau 24 giờ:**
    *   [ ] Chụp ảnh sản phẩm (cắt lát và nguyên chiếc) để so sánh trực quan.
    *   [ ] Đo các thông số vật lý:
        *   Thể tích hoặc chiều cao nở (cm):
        *   Trọng lượng sau nướng (g) và tính tỷ lệ hao hụt (%):
    *   [ ] Phân tích cấu trúc (Texture Analysis) để đo độ mềm/cứng (nếu có thiết bị).
    *   [ ] Tổ chức đánh giá cảm quan (sensory evaluation) nội bộ, so sánh các chỉ tiêu:
        *   Hình dạng & Màu sắc vỏ
        *   Cấu trúc ruột bánh
        *   Mùi
        *   Vị
        *   Cảm giác miệng (Mouthfeel)
*   [ ] **Đánh giá Hạn sử dụng (nếu mục tiêu có liên quan):**
    *   [ ] Lưu mẫu ở điều kiện quy định và lặp lại các bước đánh giá cấu trúc và cảm quan tại các mốc thời gian (ví dụ: Ngày 3, Ngày 7).

**4. CẤU TRÚC BÁO CÁO KẾT QUẢ (FINAL REPORT OUTLINE)**

*   **1.0 Tóm tắt (Executive Summary):** Mục tiêu, kết quả chính và đề xuất.
*   **2.0 Giới thiệu (Introduction):** Giới thiệu về [TestIngredient] và mục tiêu của thử nghiệm.
*   **3.0 Vật liệu và Phương pháp (Materials & Methods):**
    *   3.1 Công thức chi tiết (Control vs. Test).
    *   3.2 Quy trình thực hiện.
    *   3.3 Các phương pháp đánh giá đã sử dụng.
*   **4.0 Kết quả và Thảo luận (Results & Discussion):**
    *   4.1 So sánh ảnh hưởng đến quy trình (dữ liệu trộn bột...).
    *   4.2 So sánh các chỉ tiêu vật lý (bảng số liệu thể tích, độ hao hụt...).
    *   4.3 So sánh kết quả phân tích cấu trúc (biểu đồ độ cứng theo thời gian).
    *   4.4 Tổng hợp kết quả đánh giá cảm quan (biểu đồ mạng nhện hoặc bảng điểm).
*   **5.0 Kết luận (Conclusion):** Trả lời trực tiếp câu hỏi mục tiêu. [TestIngredient] có đạt được [PrimaryGoal] không?
*   **6.0 Đề xuất (Recommendation):**
    *   Chấp thuận/Không chấp thuận việc sử dụng [TestIngredient].
    *   Đề xuất tỷ lệ sử dụng tối ưu.
    *   Đề xuất các bước tiếp theo (ví dụ: thử nghiệm ở quy mô lớn hơn, tối ưu hóa thêm...).

---
```

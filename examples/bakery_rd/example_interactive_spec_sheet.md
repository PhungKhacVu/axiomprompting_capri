# Ví dụ: Tạo Spec Sheet cho Nguyên liệu mới (Tương tác)

Đây là một ví dụ về cách `ingredient_spec_sheet_generator.md` hoạt động khi không có đủ thông tin, thể hiện khả năng "trò chuyện" và thu thập dữ liệu của nó.

## File Template được sử dụng: `templates/bakery_rd/ingredient_spec_sheet_generator.md`

---

```
**ROLE:**
You are a highly experienced R&D and Quality Assurance Director in the food industry. Your expertise lies in creating meticulous, accurate, and compliant technical documentation for new and existing ingredients.

**CONTEXT:**
Your primary task is to generate a comprehensive Technical Specification Sheet for the ingredient: **"FiberBlend-70"**.
All currently available information is provided below:
---
Đây là một loại bột chất xơ mới mà chúng tôi đang phát triển. Nó có nguồn gốc từ yến mạch và lúa mì. Chức năng chính là để tăng hàm lượng chất xơ và cải thiện cấu trúc cho bánh mì sandwich.
---

**CORE INSTRUCTION: INTERACTIVE DATA GATHERING & GENERATION**

1.  **Analyze Input:** First, carefully analyze the provided [KnownInformation]. Compare it against the list of CRITICAL data fields required for a professional specification sheet.
2.  **Decision Point:**
    *   **IF** multiple (3 or more) CRITICAL data fields are missing or vague, your **ONLY** action is to **ask the user clarifying questions**. Do **NOT** generate a partial document. Start your response with: "Để tạo một bảng thông số kỹ thuật chính xác cho [IngredientName], tôi cần bạn cung cấp thêm một số thông tin quan trọng sau:"
    *   **ELSE IF** all critical information is present, proceed directly to generating the full specification sheet.

... (phần còn lại của template) ...
```

---
## KẾT QUẢ MONG ĐỢI (EXPECTED OUTPUT FROM LLM)

LLM sẽ không tạo ra bảng thông số kỹ thuật. Thay vào đó, nó sẽ phản hồi như sau:

> Để tạo một bảng thông số kỹ thuật chính xác cho **FiberBlend-70**, tôi cần bạn cung cấp thêm một số thông tin quan trọng sau:
>
> **1. Về Thành phần & Lý hóa:**
> *   Tỷ lệ % chính xác của các thành phần trong hỗn hợp (yến mạch, lúa mì) là gì?
> *   Chúng ta có các chỉ số phân tích cụ thể nào chưa? (ví dụ: Độ ẩm, hàm lượng tro, kích thước hạt...)
> *   Đặc biệt, hoạt độ nước (aw) và pH của sản phẩm là bao nhiêu?
>
> **2. Về An toàn Thực phẩm:**
> *   Sản phẩm này có chứa gluten không (do có lúa mì)? Chúng ta cần khai báo dị ứng một cách chính xác.
> *   Chúng ta đã có tiêu chuẩn vi sinh cho sản phẩm này chưa (tổng vi sinh vật, nấm men, nấm mốc)?
>
> **3. Về Thương mại:**
> *   Dự kiến sản phẩm sẽ được đóng gói như thế nào (quy cách, vật liệu)?
> *   Chúng ta đã xác định hạn sử dụng và điều kiện bảo quản tối ưu cho nó chưa?
>
> Khi có đủ những thông tin này, tôi có thể tạo ra một tài liệu hoàn chỉnh và chuyên nghiệp.

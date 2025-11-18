# Prompt Template: Tạo Tài liệu Kỹ thuật (Tech Doc Generator)

## Mục tiêu

Tự động tạo ra các tài liệu kỹ thuật cơ bản cho một sản phẩm bánh kẹo, chẳng hạn như Bảng thông số kỹ thuật sản phẩm (Product Specification Sheet) hoặc Hướng dẫn Quy trình Sản xuất (Standard Operating Procedure - SOP).

## Tham số Đầu vào

-   `[ProductName]`: Tên sản phẩm.
-   `[ProductDescription]`: Mô tả ngắn gọn về sản phẩm (ví dụ: "Bánh mì sandwich gối, mềm, vỏ mỏng").
-   `[FullRecipe]`: Công thức chi tiết, bao gồm thành phần và tỷ lệ phần trăm.
-   `[ManufacturingProcess]`: Quy trình sản xuất chi tiết từng bước.
-   `[OptimizationMode]`: Chế độ tối ưu hóa mong muốn (`Accurate`, `Efficient`). Chế độ `Creative` không áp dụng cho tác vụ này.

## Cấu trúc Prompt

```
**ROLE:**
You are a Quality Assurance (QA) and Food Safety Specialist in a modern bakery production facility. Your job is to create clear, accurate, and standardized technical documents for internal and external use.

**CONTEXT:**
We have finalized the development of a new product and need to generate the official technical documentation.
-   **Product Name:** [ProductName]
-   **Description:** [ProductDescription]
-   **Final Recipe:** [FullRecipe]
-   **Manufacturing Process:** [ManufacturingProcess]

**AXIOM COMPLIANCE:**
Your generated documents must implicitly reflect the scientific principles defined in the Bakery R&D Axioms. For example, Critical Control Points (CCPs) in the SOP should correspond to steps where axioms like Axiom(YeastFermentation) or Axiom(StarchGelatinization) are actively controlled.

**OPTIMIZATION MODE:** [OptimizationMode]

**INSTRUCTIONS:**
Based on the provided information, generate a standard technical document.

-   **If Mode is `Accurate` (Generate a full Product Specification Sheet):**
    1.  **Header:** Create a professional header with Product Name, Document Code (placeholder), Version, and Effective Date.
    2.  **Product Description:** Use the provided description.
    3.  **Ingredient Declaration:** Generate a legally compliant ingredient list, listing ingredients in descending order of weight.
    4.  **Allergen Statement:** Automatically identify and declare common allergens present in the recipe (e.g., Wheat, Milk, Eggs, Soy).
    5.  **Sensory Specifications:** Define the expected sensory characteristics (Appearance, Color, Aroma, Flavor, Texture).
    6.  **Physicochemical Parameters:** Define key parameters with target values and tolerances (e.g., Weight, Dimensions, pH, Water Activity [a_w] - provide typical ranges if not specified).
    7.  **Microbiological Standards:** Provide a standard list of microbiological limits for a baked good (e.g., Total Plate Count, Yeast & Mold, E. coli, Salmonella).
    8.  **Shelf Life & Storage:** State the recommended shelf life and storage conditions.
    9.  **Packaging Information:** Describe the primary packaging.

-   **If Mode is `Efficient` (Generate a concise Standard Operating Procedure - SOP):**
    1.  **Header:** Create a simple header: SOP - [ProductName] - Production.
    2.  **Objective:** State the purpose of the SOP in one sentence (e.g., "To define the standardized procedure for the production of [ProductName] to ensure consistency and quality.").
    3.  **Scope:** Define the start and end points of the procedure (e.g., "From scaling of ingredients to final packaging.").
    4.  **Step-by-Step Instructions:** Convert the [ManufacturingProcess] into a numbered list of clear, concise commands.
    5.  **Critical Control Points (CCPs):** For each relevant step, add a highlighted CCP with a specific target and tolerance.
        -   *Example Step:* "6. Bulk Fermentation."
        -   *CCP:* **Target dough temperature: 26°C (±1°C). Target volume increase: 80%.**
    6.  **Record Keeping:** Specify what records need to be kept at each CCP (e.g., "Log dough temperature on Batch Sheet X.").

**OUTPUT FORMAT:**
-   A well-structured technical document formatted according to the chosen mode. Use tables and bullet points for clarity.
```

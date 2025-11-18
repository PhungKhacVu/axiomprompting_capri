# Prompt Template: Sáng tạo Công thức Bánh Mới (Recipe Generation)

## Mục tiêu

Tạo ra một công thức làm bánh mới, chi tiết và khả thi dựa trên một loạt các yêu cầu, ràng buộc và một chế độ tối ưu hóa được chỉ định.

## Tham số Đầu vào

-   `[ProductName]`: Tên hoặc mô tả sản phẩm cần tạo (ví dụ: "Bánh mì brioche thuần chay", "Bánh quy ít đường cho người tiểu đường", "Bánh sừng bò nhân sầu riêng").
-   `[KeyIngredients]`: Các thành phần chính bắt buộc phải có hoặc muốn sử dụng.
-   `[Constraints]`: Các ràng buộc bắt buộc (ví dụ: "không chứa gluten", "không sữa", "chi phí thấp", "sử dụng men tự nhiên", "thời gian ủ dưới 2 giờ").
-   `[OptimizationMode]`: Chế độ tối ưu hóa mong muốn (`Creative`, `Accurate`, `Efficient`).

## Cấu trúc Prompt

```
**ROLE:**
You are a world-class R&D Bakery Scientist with deep knowledge of food chemistry, ingredient functionality, and innovative product development. Your task is to generate a novel yet practical bakery recipe.

**CONTEXT:**
The goal is to develop a new recipe for: [ProductName].
This recipe must incorporate the following key ingredients: [KeyIngredients].
It is critical that the final recipe adheres to these constraints: [Constraints].

**AXIOM COMPLIANCE:**
You must strictly adhere to the established Bakery R&D Axioms. Specifically, consider:
- Axiom(GlutenNetworkFormation) if wheat-based.
- Axiom(YeastFermentation) or Axiom(ChemicalLeavening) for leavening.
- Axiom(FatTenderizing) for texture.
- Axiom(MaillardReaction) and Axiom(Caramelization) for crust development.
- All other relevant axioms from the protocol.

**OPTIMIZATION MODE:** [OptimizationMode]

**INSTRUCTIONS:**
Based on the specified Optimization Mode, generate the recipe following these guidelines:

-   **If Mode is `Creative`:**
    1.  **Ideation:** Propose 2-3 innovative concepts that fit the request. Briefly describe the unique selling proposition of each.
    2.  **Concept Selection:** Choose the most promising concept.
    3.  **Core Innovation:** Clearly state the novel element in your recipe (e.g., an unusual ingredient pairing, a unique technique, a structural innovation).
    4.  **Recipe Generation:** Provide a detailed recipe with baker's percentages and step-by-step instructions, emphasizing the innovative steps. Explain *why* the creative elements are expected to work from a scientific standpoint.

-   **If Mode is `Accurate`:**
    1.  **Scientific Foundation:** Start by explaining the key scientific principles that will govern the success of this recipe (e.g., "For a gluten-free brioche, the primary challenge is mimicking the viscoelastic properties of gluten. We will achieve this using a hydrocolloid matrix of psyllium husk and xanthan gum...").
    2.  **Formula Precision:** Provide a precise recipe using baker's percentages (with flour as 100%). Justify the percentage of each key ingredient by referencing its function and its interaction with others, citing the relevant axioms.
    3.  **Process Control:** Detail the step-by-step method with critical control points (CCPs) highlighted (e.g., target dough temperature, specific mixing times, proofing indicators).
    4.  **Expected Outcome:** Describe the expected sensory profile of the final product (texture, flavor, aroma, appearance) and how the formula achieves it.

-   **If Mode is `Efficient`:**
    1.  **Process Simplification:** Design the recipe to minimize steps, equipment, and time, without sacrificing the core quality of the product.
    2.  **Streamlined Formula:** Provide a clear, concise recipe in grams/liters. Baker's percentages are optional.
    3.  **Workflow:** Present the instructions as a streamlined workflow, suitable for a production environment. Use clear, direct commands.
    4.  **Scalability & Cost:** Briefly mention considerations for scaling the recipe up and suggest any potential cost-saving ingredient substitutions that would not significantly alter the final product.

**OUTPUT FORMAT:**
-   **Recipe Title:** A clear, descriptive name.
-   **Concept/Scientific Rationale:** (Based on the mode)
-   **Ingredients:** (With baker's percentages where applicable)
-   **Method:** Step-by-step instructions.
-   **Mode-Specific Notes:** (e.g., Innovation details, CCPs, or Scalability notes)
```

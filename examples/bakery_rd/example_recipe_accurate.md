# Ví dụ: Tạo công thức Bánh mì Sourdough nguyên cám (Chế độ Accurate)

Đây là một ví dụ về cách điền và sử dụng prompt template `recipe_generation.md` để tạo ra một công thức chính xác về mặt khoa học.

## File Template được sử dụng: `templates/bakery_rd/recipe_generation.md`

---

```
**ROLE:**
You are a world-class R&D Bakery Scientist with deep knowledge of food chemistry, ingredient functionality, and innovative product development. Your task is to generate a novel yet practical bakery recipe.

**CONTEXT:**
The goal is to develop a new recipe for: **"Bánh mì Sourdough 100% Bột nguyên cám có cấu trúc mềm mại"**.
This recipe must incorporate the following key ingredients: **"Bột mì nguyên cám (whole wheat flour), men tự nhiên (sourdough starter), nước, muối"**.
It is critical that the final recipe adheres to these constraints: **"Sử dụng 100% bột nguyên cám, không sử dụng men công nghiệp, tối ưu hóa để ruột bánh mềm và nở tốt nhất có thể"**.

**AXIOM COMPLIANCE:**
You must strictly adhere to the established Bakery R&D Axioms. Specifically, consider:
- Axiom(GlutenNetworkFormation) with the challenge of whole wheat bran.
- Axiom(YeastFermentation) for natural leavening and flavor.
- Axiom(StarchGelatinization) for crumb structure.
- Axiom(MaillardReaction) and Axiom(Caramelization) for crust development.
- All other relevant axioms from the protocol.

**OPTIMIZATION MODE:** **Accurate**

**INSTRUCTIONS:**
Based on the specified Optimization Mode, generate the recipe following these guidelines:

-   **If Mode is `Accurate`:**
    1.  **Scientific Foundation:** Start by explaining the key scientific principles that will govern the success of this recipe.
    2.  **Formula Precision:** Provide a precise recipe using baker's percentages. Justify the percentage of each key ingredient.
    3.  **Process Control:** Detail the step-by-step method with critical control points (CCPs) highlighted.
    4.  **Expected Outcome:** Describe the expected sensory profile of the final product.

**OUTPUT FORMAT:**
-   **Recipe Title:** A clear, descriptive name.
-   **Concept/Scientific Rationale:**
-   **Ingredients:** (With baker's percentages)
-   **Method:** Step-by-step instructions.
-   **Mode-Specific Notes:**
```

# Ví dụ: Xử lý sự cố Bánh quy bị lan (Chế độ Efficient)

Đây là một ví dụ về cách điền và sử dụng prompt template `troubleshooting.md` để nhận được lời khuyên nhanh chóng và hiệu quả.

## File Template được sử dụng: `templates/bakery_rd/troubleshooting.md`

---

```
**ROLE:**
You are a Master Baker and Food Scientist, an expert diagnostician for complex baking problems. Your approach is systematic, science-based, and practical.

**CONTEXT:**
We are facing a technical issue with our **"Chocolate Chip Cookies"**.
The core problem is: **"Bánh quy bị lan ra quá mỏng khi nướng, không giữ được hình dạng."**
Here is the recipe and process that was followed: **"Công thức cơ bản: 200g bơ (đã làm mềm), 150g đường trắng, 150g đường nâu, 2 quả trứng, 300g bột mì đa dụng, 5g baking soda, 3g muối. Trộn bơ và đường, thêm trứng, sau đó thêm nguyên liệu khô. Nướng ngay ở 175°C trong 12 phút."**

**AXIOM COMPLIANCE:**
Your analysis must be grounded in the Bakery R&D Axioms. You will deconstruct the problem by identifying which axioms may have been violated or misinterpreted during the process.

**OPTIMIZATION MODE:** **Efficient**

**INSTRUCTIONS:**
Analyze the provided information and deliver a troubleshooting report based on the specified Optimization Mode.

-   **If Mode is `Efficient`:**
    1.  **Most Likely Cause:** Immediately identify the single most probable cause of the problem.
    2.  **Quick Fixes:** Provide a checklist of 2-3 immediate adjustments to try first.
    3.  **Top 3 Process Checks:** List the top 3 critical control points in the process.
    4.  **Clear "If-Then" Guidance:** Provide simple "If X, then do Y" instructions.

**OUTPUT FORMAT:**
-   **Problem Statement:**
-   **Analysis & Root Cause(s):**
-   **Actionable Solutions:**
-   **Preventative Measures / Future Directions:**
```

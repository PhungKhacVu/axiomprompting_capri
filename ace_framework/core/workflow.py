import os
from .agent import AceAgent

class AceWorkflow:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.template_dir = os.path.join(base_dir, "ace-templates")

        # Initialize Agents
        self.architect = AceAgent("Architect", os.path.join(self.template_dir, "system_design.md"))
        self.implementer = AceAgent("Implementer", os.path.join(self.template_dir, "code_generation.md"))
        self.reviewer = AceAgent("Reviewer", os.path.join(self.template_dir, "code_review.md"))
        self.documenter = AceAgent("Documenter", os.path.join(self.template_dir, "technical_writing.md"))

    def run_workflow(self, user_request: str, context: str = "") -> dict:
        results = {}

        # Step 1: Architect (Planning)
        print("\n[bold cyan]1. Architect is planning...[/bold cyan]")
        design_doc = self.architect.run({
            "user_request": user_request,
            "context": context
        })
        results["system_design"] = design_doc
        self._save_artifact("system_design.md", design_doc)

        # Step 2: Implementer (Execution)
        print("\n[bold green]2. Implementer is coding...[/bold green]")
        code_output = self.implementer.run({
            "design_document": design_doc
        })
        results["implementation_code"] = code_output
        self._save_artifact("implementation_output.md", code_output)

        # Step 3: Reviewer (Reflection)
        print("\n[bold magenta]3. Reviewer is reviewing...[/bold magenta]")
        review_report = self.reviewer.run({
            "design_document": design_doc,
            "implementation_code": code_output
        })
        results["review_report"] = review_report
        self._save_artifact("review_report.md", review_report)

        # Step 4: Documenter (Documentation)
        print("\n[bold yellow]4. Documenter is writing docs...[/bold yellow]")
        documentation = self.documenter.run({
            "design_document": design_doc,
            "implementation_code": code_output,
            "review_report": review_report
        })
        results["documentation"] = documentation
        self._save_artifact("documentation.md", documentation)

        return results

    def _save_artifact(self, filename: str, content: str):
        """Saves a workflow artifact to the output directory."""
        output_dir = os.path.join(self.base_dir, "output")
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  -> Saved {filename}")

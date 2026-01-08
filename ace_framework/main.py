import os
import sys
import argparse
from rich.console import Console
from rich.prompt import Confirm, Prompt
from rich.panel import Panel
from core.workflow import AceWorkflow
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

console = Console()

def print_header():
    console.print(Panel.fit(
        "[bold cyan]ACE Framework (Agentic Collaborative Entity)[/bold cyan]\n"
        "[italic]Architect -> Implementer -> Reviewer -> Documenter[/italic]",
        border_style="cyan"
    ))

def run_preflight_checklist(skip: bool = False) -> bool:
    console.print("\n[bold]ACE PRE-FLIGHT CHECKLIST[/bold]")

    if skip:
        console.print("[yellow]Skipping checklist (Auto-confirmed via flag)[/yellow]")
        return True

    checklist_items = [
        "Role definition clear and specific?",
        "Reference materials linked/available?",
        "Acceptance criteria defined?",
        "Lessons learned from similar tasks reviewed?",
        "Constraints clarified with stakeholders?"
    ]

    all_checked = True
    for item in checklist_items:
        if not Confirm.ask(f"[green]?[/green] {item}", default=True):
            all_checked = False
            console.print(f"[red]X Item '{item}' not confirmed.[/red]")

    if not all_checked:
        return Confirm.ask("[bold red]Not all checklist items were confirmed. Proceed anyway?[/bold red]")

    return True

def main():
    parser = argparse.ArgumentParser(description="ACE Framework CLI")
    parser.add_argument("--skip-checklist", action="store_true", help="Skip the pre-flight checklist")
    parser.add_argument("--prompt", type=str, help="The project request prompt")
    parser.add_argument("--context", type=str, default="", help="Additional context")
    args = parser.parse_args()

    print_header()

    if not run_preflight_checklist(skip=args.skip_checklist):
        console.print("[red]Aborting workflow due to failed checklist.[/red]")
        sys.exit(0)

    console.print("\n[bold green]Ready to launch ACE workflow[/bold green]")

    user_request = args.prompt
    if not user_request:
        # Fallback to interactive prompt if not provided via arg
        try:
            user_request = Prompt.ask("\n[bold]Enter your project request[/bold]")
        except EOFError:
            # Handle non-interactive environments gracefully
            console.print("[red]Error: No prompt provided and input is not interactive.[/red]")
            console.print("Usage: python main.py --prompt 'Your request'")
            sys.exit(1)

    if not user_request:
        console.print("[red]Request cannot be empty.[/red]")
        sys.exit(1)

    context = args.context
    if not context and not args.prompt: # Only ask for context if we are in interactive mode (inferred)
         try:
             context = Prompt.ask("[bold]Enter any additional context/constraints (optional)[/bold]", default="")
         except EOFError:
             pass

    # Initialize and run workflow
    base_dir = os.path.dirname(os.path.abspath(__file__))

    workflow = AceWorkflow(base_dir)
    workflow.run_workflow(user_request, context)

    console.print("\n[bold green]ACE Workflow Complete![/bold green]")
    console.print(f"Check the [bold]{os.path.join(base_dir, 'output')}[/bold] directory for results.")

if __name__ == "__main__":
    main()

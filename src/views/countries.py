from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from models.countries import Country
from .base import View


class CountriesView(View):
    def __init__(self, data: list[Country], page_size: int = 10) -> None:
        super().__init__(data)
        self.page_size = page_size
        self.page_number = 1

    @staticmethod
    def _create_table() -> Table:
        table = Table(
            title="Country Information",
            show_lines=True,
            show_edge=True,
            show_header=True
        )

        table.add_column("Name", justify="left", vertical="middle", style="cyan")
        table.add_column("Capital", justify="left", vertical="middle", style="magenta")
        table.add_column("Link to flag (PNG)", justify="left", vertical="middle", style="green")

        return table

    def _display_page(self) -> None:
        table = self._create_table()
        start_index = (self.page_number - 1) * self.page_size
        end_index = min(start_index + self.page_size, len(self.data))

        # Handle cases where the page might be out of range
        if start_index >= len(self.data):
            print("No more data to display.")
            return

        # Add rows to the table
        for country in self.data[start_index:end_index]:
            table.add_row(country.name, country.capital, country.flag_url)

        console = Console()
        console.print(table)

        # Show pagination controls
        total_pages = -(-len(self.data) // self.page_size)  # Ceiling division
        controls = self._generate_controls(total_pages)

        # Display pagination controls as a panel
        controls_panel = Panel("\n".join(controls), title="Navigation", style="magenta")
        console.print(controls_panel)

        # Get user input for navigation
        choice = Prompt.ask("Select an option (use the exact text in brackets)", default="").strip().lower()
        self._handle_navigation(choice, total_pages)

    def _generate_controls(self, total_pages: int) -> list[str]:
        controls = []
        if self.page_number > 1:
            controls.append("[<] Previous Page")

        if self.page_number < total_pages:
            controls.append("[>] Next Page")

        controls.append(f"Page {self.page_number} of {total_pages}")
        controls.append("[Q] Quit")
        return controls

    def _handle_navigation(self, choice: str, total_pages: int) -> None:
        if choice == "<" and self.page_number > 1:
            self.page_number -= 1
        elif choice == ">" and self.page_number < total_pages:
            self.page_number += 1
        elif choice == "q":
            print("Exiting...")
            return
        else:
            print("Invalid choice. Please use the exact text in brackets.")
            return

        self._display_page()

    def _display_data(self) -> None:
        self._display_page()

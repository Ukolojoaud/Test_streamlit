import calendar
from rich.console import Console
from rich.table import Table

def colorful_calendar(year):
    console = Console()
    calendar.setfirstweekday(calendar.SUNDAY)
    cal = calendar.Calendar()

    for month in range(1, 13):
        # Get weeks for the given month
        month_weeks = cal.monthdayscalendar(year, month)
        month_name = calendar.month_name[month]

        # Create a table for the month
        table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

        # Add weekday columns
        table.add_column("Sun", justify="center", style="red")
        table.add_column("Mon", justify="center", style="green")
        table.add_column("Tue", justify="center", style="green")
        table.add_column("Wed", justify="center", style="green")
        table.add_column("Thu", justify="center", style="green")
        table.add_column("Fri", justify="center", style="green")
        table.add_column("Sat", justify="center", style="red")

        # Add rows for each week
        for week in month_weeks:
            table.add_row(*[str(day) if day != 0 else "" for day in week])

        # Print the table for the month
        console.print(table)
        console.print("\n")  # Space between months

# Call the function
colorful_calendar(2025)

import os
import math
from pymenu import select_menu
from typing import Union
from pathlib import Path

SPACING = 7 # Amount of spacing between elements in .txt file

def load_data() -> list[dict]:
    root_dir: Path = Path(os.getcwd())
    data_file_path: Union[str, Path] = Path(root_dir / "coinCount.txt")
    if not data_file_path.is_file():
        with open(data_file_path, "w", encoding="utf-8") as f:
            f.write(f"Name{' '*SPACING}Bags Checked{' '*SPACING}Correct Bags{' '*SPACING}")


def check_bag() -> bool:
    pass

def view_total() -> None:
    pass

def list_volunteers() -> None:
    pass

def main() -> None:
    options: list[str] = ["Check Bag", "View Total", "List Volunteers"]
    selected_option: str = select_menu.create_select_menu(options, "Pick an option: ")
    
    if selected_option == options[0]:
        check_bag()
    elif selected_option == options[1]:
        view_total()
    elif selected_option == options[2]:
        list_volunteers()

main()
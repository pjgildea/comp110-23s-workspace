from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    return result


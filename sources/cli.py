import sys
from typing import Iterable

import lake
import build_static_site
import generate_report
import generate_report_12mies
import generate_summary_report
import drenaz_miesieczny
import recovery_after_drainage_stop


def _iter_lakes(lake_id: str | None) -> Iterable[str]:
    if lake_id is not None:
        if lake_id not in lake.LAKES:
            raise SystemExit(f"Dostępne jeziora: {', '.join(lake.LAKES)}")
        return [lake_id]
    return list(lake.LAKES.keys())


def refresh_models(lake_id: str | None = None, include_natural: bool = True) -> None:
    for lid in _iter_lakes(lake_id):
        lake.run_training_and_save(lid)
        if include_natural:
            lake.run_training_and_save(
                lid,
                variant="natural",
            )


def refresh_reports(lake_id: str | None = None) -> None:
    for lid in _iter_lakes(lake_id):
        if not lake.get_model_path(lid).exists():
            continue
        generate_report.run(lake_id=lid)
        generate_report_12mies.run_report_for_lake(lid)
        drenaz_miesieczny.run_lake(lid)
    results = generate_summary_report._collect_metrics()
    if results:
        generate_summary_report._write_summary_report(results)
    recovery_after_drainage_stop.main()


def refresh_www() -> None:
    build_static_site.build()


def refresh_all(lake_id: str | None = None) -> None:
    refresh_models(lake_id=lake_id)
    refresh_reports(lake_id=lake_id)
    refresh_www()


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Użycie: python sources/cli.py [refresh-models|refresh-reports|refresh-www|refresh-all] [lake_id]")
    cmd = sys.argv[1]
    lake_id = sys.argv[2] if len(sys.argv) > 2 else None
    if cmd == "refresh-models":
        refresh_models(lake_id=lake_id)
        return
    if cmd == "refresh-reports":
        refresh_reports(lake_id=lake_id)
        return
    if cmd == "refresh-www":
        refresh_www()
        return
    if cmd == "refresh-all":
        refresh_all(lake_id=lake_id)
        return
    raise SystemExit(f"Nieznane polecenie: {cmd}")


if __name__ == "__main__":
    main()


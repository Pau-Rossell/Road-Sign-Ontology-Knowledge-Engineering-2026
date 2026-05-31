from __future__ import annotations

from _common import fail_if_mtsd_missing


def main() -> None:
    fail_if_mtsd_missing()
    raise SystemExit(
        "MTSD source discovery succeeded, but the repository does not currently include "
        "the MTSD object graph needed to compute repository-wide percentages for CQ-22."
    )


if __name__ == "__main__":
    main()

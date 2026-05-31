from __future__ import annotations

from _common import fail_if_mtsd_missing


def main() -> None:
    fail_if_mtsd_missing()
    raise SystemExit(
        "MTSD source discovery succeeded, but the fully annotated MTSD image/object graph "
        "needed for CQ-25 is not present in this repository snapshot."
    )


if __name__ == "__main__":
    main()

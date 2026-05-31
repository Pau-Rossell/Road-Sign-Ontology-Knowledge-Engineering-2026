from __future__ import annotations

from _common import fail_if_mtsd_missing


def main() -> None:
    fail_if_mtsd_missing()
    raise SystemExit(
        "MTSD source discovery succeeded, but no dataset graph is present here with "
        "aligned image/sign objects for CQ-21."
    )


if __name__ == "__main__":
    main()

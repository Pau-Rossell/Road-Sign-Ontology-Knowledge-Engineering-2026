from __future__ import annotations

from _common import fail_if_mtsd_missing


def main() -> None:
    fail_if_mtsd_missing()
    raise SystemExit(
        "MTSD source discovery succeeded, but there is no available MTSD object/alignment "
        "graph here to answer CQ-23."
    )


if __name__ == "__main__":
    main()

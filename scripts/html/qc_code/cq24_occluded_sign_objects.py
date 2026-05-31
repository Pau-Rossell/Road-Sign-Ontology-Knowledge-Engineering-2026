from __future__ import annotations

from _common import fail_if_mtsd_missing


def main() -> None:
    fail_if_mtsd_missing()
    raise SystemExit(
        "MTSD source discovery succeeded, but this repository snapshot does not provide "
        "the MTSD occlusion annotations/alignment graph needed for CQ-24."
    )


if __name__ == "__main__":
    main()

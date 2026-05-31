from __future__ import annotations

from _common import fail_if_mtsd_missing


TARGET_SOURCE_FILE = "-7fWq6WjZM8L1eUSuvOEA.json"


def main() -> None:
    fail_if_mtsd_missing()
    raise SystemExit(
        "MTSD source discovery succeeded, but this repository snapshot does not include "
        "the expected MTSD graph/schema implementation needed for CQ-20."
    )


if __name__ == "__main__":
    main()

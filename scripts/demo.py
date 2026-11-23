import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from legal_ai_recursal.cli import main  # noqa: E402

if __name__ == "__main__":
    main()

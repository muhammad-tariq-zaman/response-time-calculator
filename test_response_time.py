import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, tempfile
from pathlib import Path
from response_time import avg_minutes, avg_from_csv
class T(unittest.TestCase):
    def test_avg(self):
        rows = [{"created_at": "2026-01-01 09:00", "resolved_at": "2026-01-01 10:00"},
                {"created_at": "2026-01-01 09:00", "resolved_at": "2026-01-01 09:30"}]
        self.assertEqual(avg_minutes(rows), 45.0)
    def test_csv(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"t.csv"; p.write_text("created_at,resolved_at\n2026-01-01 09:00,2026-01-01 10:00\n")
            self.assertEqual(avg_from_csv(str(p)), 60.0)
if __name__ == "__main__": unittest.main()

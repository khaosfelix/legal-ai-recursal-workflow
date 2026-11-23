import unittest
from src.engine import analyze_dict

def base():
    return {
        "case_id":"T","phase":"sentence","decision_result":"partially_granted",
        "notification_date":"2026-11-03","current_date":"2026-11-04",
        "moral_damages":0,"material_damages":0,"material_estimate_from_claim":0,
        "fee_percentage":0,"fixed_fees":0,"other_effective_amounts":0,"compensation":0,
        "appeal_criteria":[],"declaratory_motion_filed":False,"judgment_annulled":False,
        "defense_filed":True,"operative_obligation":None
    }

class EngineTests(unittest.TestCase):
    def test_gross_total_does_not_subtract_compensation(self):
        p=base()
        p.update(moral_damages=5000,material_damages=1200,fee_percentage=10,compensation=800)
        r=analyze_dict(p)
        self.assertEqual(r["fees"],620.0)
        self.assertEqual(r["gross_total"],6820.0)
        self.assertEqual(r["compensation"],800.0)

    def test_material_estimate(self):
        p=base()
        p.update(material_estimate_from_claim=1500)
        r=analyze_dict(p)
        self.assertEqual(r["material_value_used"],1500)
        self.assertTrue(r["warnings"])

    def test_overdue_ed_triggers_non_appeal(self):
        p=base()
        p.update(phase="appeal_judgment",decision_result="appeal_denied",
                 notification_date="2026-10-20",current_date="2026-11-03")
        r=analyze_dict(p)
        self.assertEqual(r["deadline_status"],"ULTRAPASSADO")
        self.assertEqual(r["route"],"NON_APPEAL_JUSTIFICATION")

    def test_annulled_judgment_clears_merits_exposure(self):
        p=base()
        p.update(phase="appeal_judgment",decision_result="annulled",
                 judgment_annulled=True,defense_filed=False,
                 moral_damages=5000,material_damages=2000,fee_percentage=10,
                 operative_obligation="Old obligation")
        r=analyze_dict(p)
        self.assertEqual(r["gross_total"],0.0)
        self.assertIsNone(r["obligation"])
        self.assertEqual(r["route"],"RETURN_TO_ORIGIN")
        self.assertIsNotNone(r["next_operational_deadline"])

if __name__ == "__main__":
    unittest.main()

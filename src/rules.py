from datetime import datetime, timedelta
from typing import Iterable, Optional

DECISION_LABELS = {
    "granted": "PROCEDENTE",
    "partially_granted": "PARCIALMENTE PROCEDENTE",
    "dismissed": "IMPROCEDENTE",
    "appeal_granted": "PROVIDO",
    "appeal_partially_granted": "PARCIALMENTE PROVIDO",
    "appeal_denied": "DESPROVIDO",
    "not_known": "NÃO CONHECIDO",
    "annulled": "PROVIDO",
}

DEMO_APPEAL_CRITERIA = {
    "compensation_issue",
    "prescription_issue",
    "double_refund_issue",
    "regulatory_reporting_issue",
    "high_damage_issue",
}

def parse_date(value: str):
    return datetime.strptime(value, "%Y-%m-%d").date()

def format_date(value):
    return value.strftime("%d/%m/%Y")

def add_business_days(start_date, business_days: int, holidays: Optional[Iterable] = None):
    holidays = set(holidays or [])
    current = start_date
    counted = 0
    while counted < business_days:
        current += timedelta(days=1)
        if current.weekday() < 5 and current not in holidays:
            counted += 1
    return current

def calculate_ed_deadline(notification_date: str):
    return add_business_days(parse_date(notification_date), 5)

def material_value(material_damages: float, material_estimate_from_claim: float):
    if material_damages > 0:
        return material_damages, False
    if material_estimate_from_claim > 0:
        return material_estimate_from_claim, True
    return 0.0, False

def calculate_fees(moral: float, material: float, fee_percentage: float, fixed_fees: float):
    if fixed_fees > 0:
        return fixed_fees
    return round((moral + material) * (fee_percentage / 100.0), 2)

def gross_exposure(moral: float, material: float, fees: float, other_effective_amounts: float):
    return round(moral + material + fees + other_effective_amounts, 2)

def route_case(phase: str, appeal_criteria, deadline_expired: bool,
               declaratory_motion_filed: bool, judgment_annulled: bool):
    if judgment_annulled:
        return "RETURN_TO_ORIGIN"
    if phase == "appeal_judgment" and deadline_expired and not declaratory_motion_filed:
        return "NON_APPEAL_JUSTIFICATION"
    if set(appeal_criteria) & DEMO_APPEAL_CRITERIA:
        return "APPEAL_REVIEW_RECOMMENDED"
    return "MANUAL_ECONOMIC_REVIEW"

def record_type(phase: str, route: str):
    if route == "NON_APPEAL_JUSTIFICATION":
        return "RECORD_NON_APPEAL_JUSTIFICATION"
    if route == "RETURN_TO_ORIGIN":
        return "RECORD_RETURN_TO_ORIGIN"
    if phase == "appeal_judgment":
        return "RECORD_APPEAL_JUDGMENT"
    if phase == "enforcement":
        return "RECORD_ENFORCEMENT_DECISION"
    return "RECORD_FIRST_INSTANCE_DECISION"

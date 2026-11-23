from dataclasses import asdict
from .models import AnalysisOutput, CaseInput
from .rules import (
    DECISION_LABELS, add_business_days, calculate_ed_deadline, calculate_fees,
    format_date, gross_exposure, material_value, parse_date, record_type, route_case,
)

def analyze_case(case: CaseInput) -> AnalysisOutput:
    warnings = []
    if case.phase not in {"sentence", "appeal_judgment", "enforcement"}:
        raise ValueError("Unsupported phase")
    label = DECISION_LABELS.get(case.decision_result)
    if not label:
        raise ValueError("Unsupported decision_result")

    ed_deadline = calculate_ed_deadline(case.notification_date)
    current = parse_date(case.current_date)
    expired = current > ed_deadline

    if expired and not case.declaratory_motion_filed:
        deadline_status = "ULTRAPASSADO"
    elif case.declaratory_motion_filed:
        deadline_status = "ED_APRESENTADO"
    else:
        deadline_status = "ABERTO"

    material, estimated = material_value(case.material_damages, case.material_estimate_from_claim)
    if estimated:
        warnings.append("Material damages estimated from the synthetic claim value.")

    fees = calculate_fees(case.moral_damages, material, case.fee_percentage, case.fixed_fees)
    total = gross_exposure(case.moral_damages, material, fees, case.other_effective_amounts)

    route = route_case(
        case.phase, case.appeal_criteria, expired,
        case.declaratory_motion_filed, case.judgment_annulled
    )

    next_deadline = None
    obligation = case.operative_obligation

    if case.judgment_annulled:
        transit_assumption = ed_deadline
        next_deadline = format_date(
            add_business_days(transit_assumption, 1 if case.defense_filed else 15)
        )
        warnings.append(
            "Return-to-origin deadline is a portfolio-demo rule, not an official procedural calculation."
        )
        total = 0.0
        material = 0.0
        fees = 0.0
        obligation = None

    return AnalysisOutput(
        case_id=case.case_id,
        decision_label=label,
        deadline_ed=format_date(ed_deadline),
        deadline_status=deadline_status,
        material_value_used=material,
        fees=fees,
        gross_total=total,
        compensation=case.compensation,
        route=route,
        record_type=record_type(case.phase, route),
        obligation=obligation,
        next_operational_deadline=next_deadline,
        warnings=warnings,
    )

def analyze_dict(payload: dict) -> dict:
    return asdict(analyze_case(CaseInput(**payload)))

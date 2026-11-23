from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CaseInput:
    case_id: str
    phase: str
    decision_result: str
    notification_date: str
    current_date: str
    moral_damages: float = 0.0
    material_damages: float = 0.0
    material_estimate_from_claim: float = 0.0
    fee_percentage: float = 0.0
    fixed_fees: float = 0.0
    other_effective_amounts: float = 0.0
    compensation: float = 0.0
    appeal_criteria: List[str] = field(default_factory=list)
    declaratory_motion_filed: bool = False
    judgment_annulled: bool = False
    defense_filed: bool = True
    operative_obligation: Optional[str] = None

@dataclass
class AnalysisOutput:
    case_id: str
    decision_label: str
    deadline_ed: str
    deadline_status: str
    material_value_used: float
    fees: float
    gross_total: float
    compensation: float
    route: str
    record_type: str
    obligation: Optional[str]
    next_operational_deadline: Optional[str]
    warnings: List[str] = field(default_factory=list)

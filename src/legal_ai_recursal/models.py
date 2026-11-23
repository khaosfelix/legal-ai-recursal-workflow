from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import Any

from .enums import (
    FaseProcessual,
    FonteValorMaterial,
    ResultadoDecisao,
    RotaAnalise,
    StatusPrazo,
    TipoRegistro,
)


ZERO = Decimal("0.00")


def _decimal(value: Any) -> Decimal:
    if value in (None, ""):
        return ZERO
    return Decimal(str(value))


def _date(value: str | None) -> date | None:
    return date.fromisoformat(value) if value else None


@dataclass(frozen=True)
class ObrigacaoEntrada:
    acao: str
    objeto: str
    identificador: str | None = None
    local: str | None = None

    @classmethod
    def from_dict(cls, payload: dict[str, Any] | None) -> "ObrigacaoEntrada | None":
        if not payload:
            return None
        return cls(
            acao=payload["acao"],
            objeto=payload["objeto"],
            identificador=payload.get("identificador"),
            local=payload.get("local"),
        )


@dataclass(frozen=True)
class CasoEntrada:
    id_caso: str
    fase: FaseProcessual
    resultado_decisao: ResultadoDecisao
    data_intimacao: date
    data_analise: date
    data_transito: date | None = None

    dano_moral: Decimal = ZERO
    dano_material_exato: Decimal = ZERO
    estimativa_material_inicial: Decimal = ZERO

    percentual_honorarios: Decimal = ZERO
    honorarios_fixos: Decimal = ZERO
    outras_verbas_efetivas: Decimal = ZERO
    compensacao: Decimal = ZERO

    criterios_recursais: tuple[str, ...] = ()
    ed_interposto: bool = False
    decisao_anulada: bool = False
    contestacao_apresentada: bool = True

    feriados: tuple[date, ...] = ()
    obrigacao: ObrigacaoEntrada | None = None

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "CasoEntrada":
        return cls(
            id_caso=payload["id_caso"],
            fase=FaseProcessual(payload["fase"]),
            resultado_decisao=ResultadoDecisao(payload["resultado_decisao"]),
            data_intimacao=_date(payload["data_intimacao"]),
            data_analise=_date(payload["data_analise"]),
            data_transito=_date(payload.get("data_transito")),
            dano_moral=_decimal(payload.get("dano_moral")),
            dano_material_exato=_decimal(payload.get("dano_material_exato")),
            estimativa_material_inicial=_decimal(payload.get("estimativa_material_inicial")),
            percentual_honorarios=_decimal(payload.get("percentual_honorarios")),
            honorarios_fixos=_decimal(payload.get("honorarios_fixos")),
            outras_verbas_efetivas=_decimal(payload.get("outras_verbas_efetivas")),
            compensacao=_decimal(payload.get("compensacao")),
            criterios_recursais=tuple(payload.get("criterios_recursais", [])),
            ed_interposto=bool(payload.get("ed_interposto", False)),
            decisao_anulada=bool(payload.get("decisao_anulada", False)),
            contestacao_apresentada=bool(payload.get("contestacao_apresentada", True)),
            feriados=tuple(_date(x) for x in payload.get("feriados", [])),
            obrigacao=ObrigacaoEntrada.from_dict(payload.get("obrigacao")),
        )


@dataclass(frozen=True)
class SaidaAnalise:
    id_caso: str
    versao_regras: str
    decisao: str

    prazo_ed: date
    status_prazo_ed: StatusPrazo

    dano_material_utilizado: Decimal
    fonte_dano_material: FonteValorMaterial
    honorarios: Decimal
    compensacao: Decimal
    exposicao_bruta: Decimal

    rota: RotaAnalise
    tipo_registro: TipoRegistro

    obrigacao_operacional: str | None = None
    proxima_providencia: str | None = None
    prazo_operacional: date | None = None

    alertas: tuple[str, ...] = ()
    trilha_auditoria: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        def money(v: Decimal) -> str:
            return f"{v:.2f}"

        return {
            "id_caso": self.id_caso,
            "versao_regras": self.versao_regras,
            "decisao": self.decisao,
            "prazo_ed": self.prazo_ed.isoformat(),
            "status_prazo_ed": self.status_prazo_ed.value,
            "dano_material_utilizado": money(self.dano_material_utilizado),
            "fonte_dano_material": self.fonte_dano_material.value,
            "honorarios": money(self.honorarios),
            "compensacao": money(self.compensacao),
            "exposicao_bruta": money(self.exposicao_bruta),
            "rota": self.rota.value,
            "tipo_registro": self.tipo_registro.value,
            "obrigacao_operacional": self.obrigacao_operacional,
            "proxima_providencia": self.proxima_providencia,
            "prazo_operacional": (
                self.prazo_operacional.isoformat() if self.prazo_operacional else None
            ),
            "alertas": list(self.alertas),
            "trilha_auditoria": list(self.trilha_auditoria),
        }

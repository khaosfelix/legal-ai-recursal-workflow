from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Any

from .enums import (
    FaseProcessual,
    FonteTransito,
    FonteValorMaterial,
    ResultadoDecisao,
    RotaAnalise,
    StatusPrazo,
    TipoDeposito,
)

ZERO = Decimal("0.00")


def as_decimal(value: Any) -> Decimal:
    if value in (None, ""):
        return ZERO
    return Decimal(str(value))


def as_date(value: str | None) -> date | None:
    return date.fromisoformat(value) if value else None


@dataclass(frozen=True)
class RecursoCandidato:
    nome: str
    prazo_dias_uteis: int
    interposto: bool = False
    data_base: date | None = None

    @classmethod
    def from_dict(cls, payload: dict[str, Any] | None) -> "RecursoCandidato | None":
        if not payload:
            return None
        return cls(
            nome=payload["nome"],
            prazo_dias_uteis=int(payload["prazo_dias_uteis"]),
            interposto=bool(payload.get("interposto", False)),
            data_base=as_date(payload.get("data_base")),
        )


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
class CumprimentoEntrada:
    valor_devido: Decimal = ZERO
    valor_pago_ou_garantido: Decimal = ZERO
    tipo_deposito: TipoDeposito = TipoDeposito.PAGAMENTO_DEFINITIVO

    @classmethod
    def from_dict(cls, payload: dict[str, Any] | None) -> "CumprimentoEntrada | None":
        if not payload:
            return None
        return cls(
            valor_devido=as_decimal(payload.get("valor_devido")),
            valor_pago_ou_garantido=as_decimal(payload.get("valor_pago_ou_garantido")),
            tipo_deposito=TipoDeposito(payload.get("tipo_deposito", "pagamento_definitivo")),
        )


@dataclass(frozen=True)
class CasoEntrada:
    id_caso: str
    fase: FaseProcessual
    resultado_decisao: ResultadoDecisao
    data_intimacao: date
    data_analise: date

    data_transito_certificada: date | None = None
    feriados: tuple[date, ...] = ()

    ed_interposto: bool = False
    ed_julgado: bool = False
    data_intimacao_pos_ed: date | None = None
    recurso_subsequente: RecursoCandidato | None = None

    rito: str = "DEMO"
    uf: str = "XX"
    identificador_processo: str = "DEMO"
    decisao_liquida: bool = True
    criterios_calculadora: tuple[str, ...] = ()

    dano_moral: Decimal = ZERO
    dano_material_exato: Decimal = ZERO
    estimativa_material: Decimal = ZERO
    percentual_honorarios: Decimal = ZERO
    honorarios_fixos: Decimal = ZERO
    outras_verbas: Decimal = ZERO
    compensacao: Decimal = ZERO

    teses_prioritarias: tuple[str, ...] = ()
    provas_relevantes: tuple[str, ...] = ()
    riscos_recursais: tuple[str, ...] = ()
    recomendar_recurso: bool = False

    decisao_anulada: bool = False
    contestacao_apresentada: bool = True

    obrigacao: ObrigacaoEntrada | None = None
    cumprimento: CumprimentoEntrada | None = None

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "CasoEntrada":
        return cls(
            id_caso=payload["id_caso"],
            fase=FaseProcessual(payload["fase"]),
            resultado_decisao=ResultadoDecisao(payload["resultado_decisao"]),
            data_intimacao=as_date(payload["data_intimacao"]),
            data_analise=as_date(payload["data_analise"]),
            data_transito_certificada=as_date(payload.get("data_transito_certificada")),
            feriados=tuple(as_date(x) for x in payload.get("feriados", [])),
            ed_interposto=bool(payload.get("ed_interposto", False)),
            ed_julgado=bool(payload.get("ed_julgado", False)),
            data_intimacao_pos_ed=as_date(payload.get("data_intimacao_pos_ed")),
            recurso_subsequente=RecursoCandidato.from_dict(payload.get("recurso_subsequente")),
            rito=payload.get("rito", "DEMO"),
            uf=payload.get("uf", "XX"),
            identificador_processo=payload.get("identificador_processo", "DEMO"),
            decisao_liquida=bool(payload.get("decisao_liquida", True)),
            criterios_calculadora=tuple(payload.get("criterios_calculadora", [])),
            dano_moral=as_decimal(payload.get("dano_moral")),
            dano_material_exato=as_decimal(payload.get("dano_material_exato")),
            estimativa_material=as_decimal(payload.get("estimativa_material")),
            percentual_honorarios=as_decimal(payload.get("percentual_honorarios")),
            honorarios_fixos=as_decimal(payload.get("honorarios_fixos")),
            outras_verbas=as_decimal(payload.get("outras_verbas")),
            compensacao=as_decimal(payload.get("compensacao")),
            teses_prioritarias=tuple(payload.get("teses_prioritarias", [])),
            provas_relevantes=tuple(payload.get("provas_relevantes", [])),
            riscos_recursais=tuple(payload.get("riscos_recursais", [])),
            recomendar_recurso=bool(payload.get("recomendar_recurso", False)),
            decisao_anulada=bool(payload.get("decisao_anulada", False)),
            contestacao_apresentada=bool(payload.get("contestacao_apresentada", True)),
            obrigacao=ObrigacaoEntrada.from_dict(payload.get("obrigacao")),
            cumprimento=CumprimentoEntrada.from_dict(payload.get("cumprimento")),
        )


@dataclass(frozen=True)
class AnalisePrazo:
    nome: str
    data_fatal: date | None
    status: StatusPrazo


@dataclass(frozen=True)
class AnaliseTransito:
    data: date | None
    fonte: FonteTransito
    observacao: str | None = None


@dataclass(frozen=True)
class AnaliseFinanceira:
    dano_material: Decimal
    fonte_material: FonteValorMaterial
    honorarios: Decimal
    exposicao_bruta: Decimal
    compensacao: Decimal


@dataclass(frozen=True)
class CamposCalculadoraExterna:
    rito: str
    liquidez: str
    uf: str
    identificador_processo: str
    criterios: tuple[str, ...]
    dano_moral: Decimal
    dano_material: Decimal
    total_moral_material: Decimal


@dataclass(frozen=True)
class AnaliseExecucao:
    complemento: Decimal
    tipo: str | None
    justificativa: str | None


@dataclass(frozen=True)
class SaidaAnalise:
    id_caso: str
    decisao: str
    prazo_ed: AnalisePrazo
    prazo_recurso_subsequente: AnalisePrazo | None
    transito: AnaliseTransito
    financeiro: AnaliseFinanceira
    rota: RotaAnalise
    posicionamento: str
    obrigacao_operacional: str | None
    calculadora_externa: CamposCalculadoraExterna | None
    execucao: AnaliseExecucao | None
    cadastro_operacional: dict[str, Any]
    referencia_docx: str | None
    proxima_providencia: str | None
    prazo_operacional: date | None
    alertas: tuple[str, ...]

from decimal import Decimal

from .enums import FaseProcessual, ResultadoDecisao
from .models import CasoEntrada


def validar(caso: CasoEntrada) -> None:
    if not caso.id_caso.strip():
        raise ValueError("id_caso é obrigatório.")

    if caso.data_analise < caso.data_intimacao:
        raise ValueError("data_analise não pode ser anterior à intimação.")

    monetarios = [
        caso.dano_moral,
        caso.dano_material_exato,
        caso.estimativa_material,
        caso.percentual_honorarios,
        caso.honorarios_fixos,
        caso.outras_verbas,
        caso.compensacao,
    ]
    if any(x < Decimal("0") for x in monetarios):
        raise ValueError("Valores monetários não podem ser negativos.")

    if caso.percentual_honorarios > Decimal("100"):
        raise ValueError("Percentual de honorários fora do limite do demo.")

    if caso.decisao_anulada and caso.resultado_decisao != ResultadoDecisao.ANULADO:
        raise ValueError("decisao_anulada exige resultado_decisao='anulado'.")

    if caso.resultado_decisao == ResultadoDecisao.ANULADO and caso.fase != FaseProcessual.ACORDAO:
        raise ValueError("O cenário anulado do demo é exclusivo de acórdão.")

    if caso.ed_interposto and caso.ed_julgado and not caso.data_intimacao_pos_ed:
        raise ValueError("ED julgado exige data_intimacao_pos_ed no demo.")

    if caso.recurso_subsequente and caso.recurso_subsequente.prazo_dias_uteis <= 0:
        raise ValueError("Prazo do recurso subsequente deve ser positivo.")

    if caso.cumprimento:
        if caso.cumprimento.valor_devido < Decimal("0") or caso.cumprimento.valor_pago_ou_garantido < Decimal("0"):
            raise ValueError("Valores de cumprimento não podem ser negativos.")

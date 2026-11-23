from .enums import FaseProcessual
from .models import AnaliseFinanceira, CamposCalculadoraExterna, CasoEntrada


def gerar_campos_calculadora(
    caso: CasoEntrada,
    financeiro: AnaliseFinanceira,
) -> CamposCalculadoraExterna | None:
    """Prepara campos para uma ferramenta externa. Não implementa a calculadora."""
    if caso.fase != FaseProcessual.SENTENCA:
        return None

    return CamposCalculadoraExterna(
        rito=caso.rito,
        liquidez="LÍQUIDA" if caso.decisao_liquida else "ILÍQUIDA",
        uf=caso.uf,
        identificador_processo=caso.identificador_processo,
        criterios=caso.criterios_calculadora,
        dano_moral=caso.dano_moral,
        dano_material=financeiro.dano_material,
        total_moral_material=caso.dano_moral + financeiro.dano_material,
    )

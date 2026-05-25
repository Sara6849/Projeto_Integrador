# ============================================================
#  PROJETO INTEGRADOR — IGUALDADE DE GÊNERO NO AMBIENTE ACADÊMICO
#  UniCEUB Taguatinga
#  Gráficos com dados oficiais (Gov.br / Senado Federal / TCU / IPEA)
# ============================================================

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Configuração global de estilo
plt.rcParams.update({
    'font.family': 'sans-serif',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': '#FAFAFA',
    'axes.facecolor': '#FAFAFA',
})

ROXO       = '#6A1B9A'
ROXO_CLARO = '#CE93D8'
PINK       = '#AD1457'
PINK_CLARO = '#F48FB1'
VERDE      = '#00695C'
VERDE_CL   = '#80CBC4'
AMARELO    = '#F57F17'
CINZA      = '#BDBDBD'

fig = plt.figure(figsize=(18, 22))
fig.patch.set_facecolor('#F3E5F5')

# Título geral
fig.suptitle(
    'Igualdade de Gênero no Ambiente Acadêmico\nDados Oficiais — Gov.br | Senado Federal | TCU | IPEA',
    fontsize=18, fontweight='bold', color='#4A148C', y=0.98
)

# ── GRÁFICO 1 ──────────────────────────────────────────────
# Situação das Universidades Federais (TCU, 2024)
ax1 = fig.add_subplot(3, 2, 1)

categorias = [
    'Sem política\ninstitucionalizada',
    'Sem programas\nde capacitação',
    'Sem protocolos\nde acolhimento',
    'Com políticas\n(com lacunas)',
]
valores = [60, 72, 74, 28]
cores   = [PINK, ROXO, ROXO_CLARO, VERDE]

barras = ax1.barh(categorias, valores, color=cores, edgecolor='white', height=0.55)
ax1.set_xlim(0, 100)
ax1.set_xlabel('% das 69 Universidades Federais', fontsize=9, color='#333')
ax1.set_title('Universidades Federais — Combate ao Assédio\n(TCU, 2024)', fontsize=11, fontweight='bold', color='#4A148C')
ax1.tick_params(axis='y', labelsize=9)
ax1.tick_params(axis='x', labelsize=9)

for barra, val in zip(barras, valores):
    ax1.text(val + 1, barra.get_y() + barra.get_height()/2,
             f'{val}%', va='center', fontsize=10, fontweight='bold', color='#333')

ax1.text(0.98, -0.14, 'Fonte: portal.tcu.gov.br',
         transform=ax1.transAxes, fontsize=7.5, color='gray', ha='right', style='italic')

# ── GRÁFICO 2 ──────────────────────────────────────────────
# Denúncias Ligue 180: anônimas x identificadas (Gov.br, 2024)
ax2 = fig.add_subplot(3, 2, 2)

labels  = ['Anônimas\n86.105', 'Pela própria\nvítima\n38.470', 'Por terceiros\n7.509']
tamanhos = [86105, 38470, 7509]
explode  = (0.05, 0, 0)
cores2   = [ROXO, PINK_CLARO, CINZA]

wedges, texts, autotexts = ax2.pie(
    tamanhos, labels=labels, autopct='%1.1f%%',
    startangle=140, colors=cores2, explode=explode,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2},
    textprops={'fontsize': 9}
)
for at in autotexts:
    at.set_fontsize(10)
    at.set_fontweight('bold')
    at.set_color('white')

ax2.set_title('Denúncias ao Ligue 180 por Tipo\n(Gov.br — Balanço 2024)', fontsize=11, fontweight='bold', color='#4A148C')
ax2.text(0.5, -0.12, 'Total: 132.084 denúncias | Fonte: gov.br',
         transform=ax2.transAxes, fontsize=7.5, color='gray', ha='center', style='italic')

# ── GRÁFICO 3 ──────────────────────────────────────────────
# Crescimento denúncias Ligue 180 no DF (Gov.br)
ax3 = fig.add_subplot(3, 2, 3)

anos    = ['2023', '2024']
valores3 = [2723, 2923]
atendimentos = [16875, 23148]

x = np.arange(len(anos))
width = 0.35

b1 = ax3.bar(x - width/2, valores3,    width, label='Denúncias',    color=ROXO,  edgecolor='white')
b2 = ax3.bar(x + width/2, atendimentos, width, label='Atendimentos', color=PINK,  edgecolor='white')

ax3.set_xticks(x)
ax3.set_xticklabels(anos, fontsize=10)
ax3.set_title('Ligue 180 no Distrito Federal — Evolução\n(Gov.br, 2024)', fontsize=11, fontweight='bold', color='#4A148C')
ax3.legend(fontsize=9)
ax3.set_ylabel('Quantidade', fontsize=9)

for barra in b1:
    ax3.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 150,
             f'{int(barra.get_height()):,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
for barra in b2:
    ax3.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 150,
             f'{int(barra.get_height()):,}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax3.annotate('+37,1%\nnos atendimentos', xy=(0.68, 23148), xytext=(0.3, 21000),
             fontsize=8.5, color=VERDE, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=VERDE, lw=1.5))

ax3.text(0.98, -0.14, 'Fonte: gov.br — Secretaria de Comunicação Social',
         transform=ax3.transAxes, fontsize=7.5, color='gray', ha='right', style='italic')

# ── GRÁFICO 4 ──────────────────────────────────────────────
# Por que as mulheres NÃO denunciam (DataSenado, 2025)
ax4 = fig.add_subplot(3, 2, 4)

motivos = [
    'Preocupação\ncom os filhos',
    'Descrença na\npunição',
    'Acharam que\nnão ia acontecer\nde novo',
    'Medo de\nrepresálias',
    'Vergonha /\nconstrangimento',
]
percentuais = [17, 14, 13, 11, 9]
cores4 = [PINK, ROXO, ROXO_CLARO, AMARELO, CINZA]

barras4 = ax4.bar(motivos, percentuais, color=cores4, edgecolor='white', width=0.6)
ax4.set_ylabel('% das mulheres que não denunciaram', fontsize=8.5)
ax4.set_title('Por Que as Mulheres NÃO Denunciam\n(DataSenado, 2025)', fontsize=11, fontweight='bold', color='#4A148C')
ax4.tick_params(axis='x', labelsize=7.5)
ax4.tick_params(axis='y', labelsize=9)
ax4.set_ylim(0, 22)

for b, v in zip(barras4, percentuais):
    ax4.text(b.get_x() + b.get_width()/2, v + 0.3, f'{v}%',
             ha='center', va='bottom', fontsize=10, fontweight='bold', color='#333')

ax4.text(0.98, -0.22, 'Fonte: senado.leg.br — DataSenado',
         transform=ax4.transAxes, fontsize=7.5, color='gray', ha='right', style='italic')

# ── GRÁFICO 5 ──────────────────────────────────────────────
# Subnotificação: casos reais x registrados (IPEA / TCU)
ax5 = fig.add_subplot(3, 2, 5)

categorias5  = ['Estupros\n(IPEA/IBGE)', 'Assédio nas\nuniversidades\n(TCU)']
registrados  = [6, 10]
nao_registrados = [94, 90]

x5 = np.arange(len(categorias5))
w5 = 0.5

ax5.bar(x5, nao_registrados, w5, label='NÃO registrados / silenciados', color=PINK,    bottom=registrados, edgecolor='white')
ax5.bar(x5, registrados,     w5, label='Registrados oficialmente',       color=VERDE,   edgecolor='white')

ax5.set_xticks(x5)
ax5.set_xticklabels(categorias5, fontsize=10)
ax5.set_ylim(0, 115)
ax5.set_ylabel('Percentual (%)', fontsize=9)
ax5.set_title('Subnotificação — Casos Reais x Registrados\n(IPEA / TCU)', fontsize=11, fontweight='bold', color='#4A148C')
ax5.legend(fontsize=8.5, loc='upper right')

for xi, (r, nr) in enumerate(zip(registrados, nao_registrados)):
    ax5.text(xi, r/2,         f'{r}%',  ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    ax5.text(xi, r + nr/2,    f'{nr}%', ha='center', va='center', fontsize=11, fontweight='bold', color='white')

ax5.text(0.98, -0.14, 'Fonte: ipea.gov.br / portal.tcu.gov.br',
         transform=ax5.transAxes, fontsize=7.5, color='gray', ha='right', style='italic')

# ── GRÁFICO 6 ──────────────────────────────────────────────
# Percepção das brasileiras (DataSenado, 2025)
ax6 = fig.add_subplot(3, 2, 6)

percepcoes = [
    '79% acreditam que\na violência aumentou',
    '71% consideram o\nBrasil muito machista',
    '87,5% usariam\no aplicativo*',
    '61% não\nregistram B.O.',
]
vals6 = [79, 71, 87.5, 61]
cores6 = [PINK, ROXO, VERDE, AMARELO]

barras6 = ax6.barh(percepcoes, vals6, color=cores6, edgecolor='white', height=0.5)
ax6.set_xlim(0, 110)
ax6.set_xlabel('% das entrevistadas', fontsize=9)
ax6.set_title('Percepção das Brasileiras\n(DataSenado 2025 + pesquisa de campo*)', fontsize=11, fontweight='bold', color='#4A148C')
ax6.tick_params(axis='y', labelsize=8.5)

for barra, val in zip(barras6, vals6):
    ax6.text(val + 1, barra.get_y() + barra.get_height()/2,
             f'{val}%', va='center', fontsize=10, fontweight='bold', color='#333')

ax6.text(0, -0.18, '*87,5% é dado da pesquisa de campo do próprio projeto',
         transform=ax6.transAxes, fontsize=7.5, color='gray', style='italic')
ax6.text(0.98, -0.24, 'Fonte: senado.leg.br — DataSenado (2025)',
         transform=ax6.transAxes, fontsize=7.5, color='gray', ha='right', style='italic')

# ── AJUSTES FINAIS ──────────────────────────────────────────
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.subplots_adjust(hspace=0.55, wspace=0.35)

# Salva a imagem
plt.savefig('graficos_genero.png', dpi=150, bbox_inches='tight', facecolor='#F3E5F5')
print("✅ Gráfico salvo como 'graficos_genero.png' na mesma pasta do script!")

# Exibe na tela
plt.show()

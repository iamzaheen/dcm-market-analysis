"""
dcm_analysis.py — European DCM Market Analysis Tool
=====================================================
Analyses European Debt Capital Market (DCM) trends with focus on:
  - Corporate bond credit spreads (IG and HY)
  - Corporate hybrid bond market dynamics
  - Yield curve analysis
  - Refinancing risk assessment

Relevant to: Debt Capital Markets, Corporate Hybrid Bond Structuring,
             Liability Management — HypoVereinsbank / UniCredit DCM desk

Data sources: Simulated from published market data (ECB, Amundi, OECD)
              In production: Bloomberg / Refinitiv API

Author: Syed Mohammad Zaheen
MSc Quantitative Finance, University of Kiel
GitHub: github.com/iamzaheen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────
# COLOURS
# ─────────────────────────────────────────────────────────
NAVY   = '#1B3A6B'
BLUE   = '#2E6DB4'
ORANGE = '#E87722'
GREEN  = '#2E8B57'
RED    = '#C0392B'
LGRAY  = '#CCCCCC'

# ─────────────────────────────────────────────────────────
# 1. MARKET DATA
# ─────────────────────────────────────────────────────────
# Based on: Amundi (Dec 2025), ECB Bulletin May 2025,
#           OECD Global Debt Report 2026
# In production: Bloomberg / Refinitiv API

np.random.seed(42)
dates = pd.date_range('2020-01-01', '2025-12-31', freq='ME')
n     = len(dates)

ig_base = np.array([
    95, 180, 120, 100, 90, 85, 80, 95, 88, 85, 82, 80,
    78,  82,  85,  90, 88, 85, 84, 82, 80, 78, 76, 75,
   110, 130, 125, 120,115,110,108,105,102,100, 98, 95,
    92,  90,  88,  86, 84, 82, 80, 78, 76, 75, 74, 73,
    75,  78,  80,  82, 84, 86, 88, 90, 88, 86, 84, 82,
    80,  78,  76,  74, 72, 70, 68, 66, 65, 64, 63, 62])

ig_spreads     = pd.Series(ig_base + np.random.normal(0,  3, n), index=dates, name='IG Spreads (bps)')
hy_spreads     = pd.Series(ig_base * 3.8 + np.random.normal(0, 15, n), index=dates, name='HY Spreads (bps)')
hybrid_spreads = pd.Series(ig_base * 2.1 + np.random.normal(0,  8, n), index=dates, name='Hybrid Spreads (bps)')

bund_yield = pd.Series([
    -0.5,-0.4,-0.3,-0.2,-0.1, 0.0, 0.1, 0.0,-0.1,-0.2,-0.3,-0.4,
    -0.3,-0.2,-0.1, 0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2, 1.8, 2.2,
     2.3, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8, 1.7, 1.8, 1.9, 2.0,
     2.1, 2.2, 2.3, 2.4, 2.5, 2.4, 2.3, 2.2, 2.1, 2.0, 1.9, 1.8,
     1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.5, 2.4, 2.3, 2.2,
     2.1, 2.0, 1.9, 1.8, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4],
    index=dates, name='Bund 10Y (%)')

# ─────────────────────────────────────────────────────────
# 2. DCM ISSUANCE DATA
# ─────────────────────────────────────────────────────────
years         = ['2020','2021','2022','2023','2024','2025']
ig_issuance   = [380, 420, 310, 340, 390, 450]
hy_issuance   = [ 85,  95,  55,  70,  88,  95]
hyb_issuance  = [ 35,  42,  28,  38,  45,  52]

# ─────────────────────────────────────────────────────────
# 3. HYBRID BOND SECTOR BREAKDOWN
# ─────────────────────────────────────────────────────────
sectors = ['Utilities','Oil & Gas','Telecoms','Industrials','Other']
shares  = [34, 31, 18, 10, 7]

# ─────────────────────────────────────────────────────────
# 4. REFINANCING WALL
# ─────────────────────────────────────────────────────────
mat_years = ['2026','2027','2028','2029','2030']
ig_mat    = [185, 210, 195, 165, 140]
hy_mat    = [ 55,  70,  65,  50,  45]
hyb_mat   = [ 18,  22,  20,  16,  14]

# ─────────────────────────────────────────────────────────
# 5. DASHBOARD
# ─────────────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 14))
fig.patch.set_facecolor('#FAFAFA')

fig.text(0.5, 0.985, 'European Debt Capital Markets — Quantitative Analysis Dashboard',
         ha='center', va='top', fontsize=14, fontweight='bold', color=NAVY)
fig.text(0.5, 0.965, 'Syed Mohammad Zaheen  |  MSc Quantitative Finance, University of Kiel',
         ha='center', va='top', fontsize=11, color='gray')

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35, top=0.935)

# ── Panel 1: Credit Spread Evolution ────────────────────
ax1 = fig.add_subplot(gs[0, :2])
ax1.plot(dates, ig_spreads,     color=NAVY,   lw=1.8, label='Euro IG Spreads')
ax1.plot(dates, hybrid_spreads, color=ORANGE, lw=1.8, label='Corporate Hybrid Spreads')
ax1.plot(dates, hy_spreads,     color=RED,    lw=1.5, linestyle='--', alpha=0.7, label='Euro HY Spreads')
ax1.fill_between(dates, ig_spreads, alpha=0.1, color=NAVY)
ax1.set_title('European Corporate Credit Spreads (2020–2025)', fontsize=12, fontweight='bold', color=NAVY)
ax1.set_ylabel('Spread over Bund (bps)')
ax1.legend(fontsize=9, loc='upper right')
ax1.grid(True, alpha=0.25)
ax1.set_facecolor('#F8F9FA')

# ── Panel 2: Key Metrics ─────────────────────────────────
ax2 = fig.add_subplot(gs[0, 2])
ax2.axis('off')
metrics = [
    ('Euro IG Yield',    '3.2%',   NAVY),
    ('Euro HY Yield',   '5.1%',   RED),
    ('IG Spread',        '62 bps', BLUE),
    ('HY Spread',       '285 bps',ORANGE),
    ('IG Issuance 2025','€450bn', GREEN),
    ('HY Default Rate', '2–3%',   NAVY),
]
ax2.text(0.5, 0.97, 'Market Snapshot\nDec 2025', ha='center', va='top',
         fontsize=11, fontweight='bold', color=NAVY, transform=ax2.transAxes)
for i, (label, val, color) in enumerate(metrics):
    y = 0.82 - i * 0.13
    ax2.text(0.05, y, label, fontsize=9,  color='gray',  transform=ax2.transAxes)
    ax2.text(0.95, y, val,   fontsize=10, fontweight='bold', color=color,
             ha='right', transform=ax2.transAxes)
ax2.set_title('Key Metrics', fontsize=11, fontweight='bold', color=NAVY, pad=8)

# ── Panel 3: Issuance Volume ─────────────────────────────
ax3 = fig.add_subplot(gs[1, :2])
x = np.arange(len(years)); w = 0.25
ax3.bar(x - w, ig_issuance,  width=w, color=NAVY,   label='IG Corporate',    alpha=0.85)
ax3.bar(x,     hy_issuance,  width=w, color=RED,    label='High Yield',      alpha=0.85)
ax3.bar(x + w, hyb_issuance, width=w, color=ORANGE, label='Corporate Hybrid',alpha=0.85)
ax3.set_xticks(x); ax3.set_xticklabels(years)
ax3.set_title('European DCM Primary Issuance Volume (EUR bn)', fontsize=12, fontweight='bold', color=NAVY)
ax3.set_ylabel('Issuance (EUR bn)')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.25, axis='y')
ax3.set_facecolor('#F8F9FA')
ax3.annotate('Record\nissuance', xy=(5 - w, 450), xytext=(4.2, 420),
             arrowprops=dict(arrowstyle='->', color=NAVY), fontsize=8, color=NAVY)

# ── Panel 4: Hybrid Sector Pie ───────────────────────────
ax4 = fig.add_subplot(gs[1, 2])
colors_pie = [NAVY, BLUE, ORANGE, GREEN, LGRAY]
ax4.pie(shares, labels=sectors, autopct='%1.0f%%', colors=colors_pie,
        startangle=90, textprops={'fontsize': 8},
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
ax4.set_title('Hybrid Bond Issuers\nby Sector', fontsize=11, fontweight='bold', color=NAVY)

# ── Panel 5: Refinancing Wall ────────────────────────────
ax5 = fig.add_subplot(gs[2, :2])
x2 = np.arange(len(mat_years))
ax5.bar(x2 - w, ig_mat,  width=w, color=NAVY,   label='IG Corporate',    alpha=0.85)
ax5.bar(x2,     hy_mat,  width=w, color=RED,    label='High Yield',      alpha=0.85)
ax5.bar(x2 + w, hyb_mat, width=w, color=ORANGE, label='Corporate Hybrid',alpha=0.85)
ax5.set_xticks(x2); ax5.set_xticklabels(mat_years)
ax5.set_title('European Corporate Refinancing Wall 2026–2030 (EUR bn)',
              fontsize=12, fontweight='bold', color=NAVY)
ax5.set_ylabel('Debt Maturing (EUR bn)')
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.25, axis='y')
ax5.set_facecolor('#F8F9FA')
ax5.text(0.02, 0.92,
         '65% of IG debt maturing has coupon ≤ 4%\nvs current IG yield 3.2% → refinancing incentive',
         transform=ax5.transAxes, fontsize=8, color=NAVY,
         bbox=dict(boxstyle='round,pad=0.3', facecolor='#EEF2FA', edgecolor=NAVY, alpha=0.8))

# ── Panel 6: Yield Decomposition ─────────────────────────
ax6 = fig.add_subplot(gs[2, 2])
ig_yield = bund_yield + ig_spreads / 100
ax6.plot(dates, bund_yield, color=LGRAY, lw=1.5, label='Bund 10Y')
ax6.plot(dates, ig_yield,   color=NAVY,  lw=1.8, label='Euro IG Yield')
ax6.fill_between(dates, bund_yield, ig_yield, alpha=0.2, color=NAVY, label='IG Credit Spread')
ax6.set_title('Bund Yield vs\nEuro IG Total Yield', fontsize=11, fontweight='bold', color=NAVY)
ax6.set_ylabel('Yield (%)')
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.25)
ax6.set_facecolor('#F8F9FA')

plt.savefig('dcm_dashboard.png', dpi=150, bbox_inches='tight', facecolor='#FAFAFA')
plt.show()
print("Saved: dcm_dashboard.png")

# ─────────────────────────────────────────────────────────
# 6. SUMMARY REPORT
# ─────────────────────────────────────────────────────────
print("\n" + "="*65)
print("  EUROPEAN DCM MARKET ANALYSIS — KEY FINDINGS")
print("="*65)
print(f"\n  CREDIT SPREADS (Dec 2025):")
print(f"  Euro IG spread     : {ig_spreads.iloc[-1]:.0f} bps  (yield ~3.2%)")
print(f"  Corporate Hybrid   : {hybrid_spreads.iloc[-1]:.0f} bps  (yield ~4.5%)")
print(f"  Euro HY spread     : {hy_spreads.iloc[-1]:.0f} bps  (yield ~5.1%)")
print(f"  Bund 10Y yield     : {bund_yield.iloc[-1]:.1f}%")
print(f"\n  DCM ISSUANCE (2025 — record year):")
for cat, val in zip(['IG','HY','Hybrid'], [ig_issuance[-1], hy_issuance[-1], hyb_issuance[-1]]):
    print(f"  {cat:8} issuance  : EUR {val}bn")
print(f"\n  HYBRID BOND MARKET:")
print(f"  Largest issuers    : Utilities (34%) and Oil & Gas (31%)")
print(f"  Green hybrids      : 17% of outstanding volume")
print(f"  Hybrid vs HY yield : comparable to senior BB-rated bonds")
print(f"\n  REFINANCING RISK (2026–2028):")
print(f"  IG debt maturing   : 24% of outstanding (~EUR 590bn)")
print(f"  HY debt maturing   : 31% of outstanding (~EUR 190bn)")
print(f"  Key insight        : 65% of maturing IG debt has coupon <= 4%")
print(f"  vs current IG yield: 3.2% => favourable refinancing conditions")
print(f"  Implication        : strong pipeline for LM exercises and new issuance")
print(f"\n  INVESTMENT CONCLUSION:")
print(f"  2025: third consecutive year of strong Euro credit performance.")
print(f"  Record IG and HY issuance driven by robust investor demand.")
print(f"  Corporate hybrids: IG credit quality, HY-like yields.")
print(f"  2026 outlook: strong IG pipeline, tech sector dominant theme.")
print("="*65)

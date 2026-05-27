# European DCM Market Analysis Tool

A Python-based quantitative analysis of European Debt Capital Markets (DCM), with focus on corporate bond credit spreads, corporate hybrid bonds, primary issuance trends, and refinancing risk — the core analytical work of a DCM desk.

**Relevant to:** Debt Capital Markets · Corporate Hybrid Bond Structuring · Liability Management Exercises

---

## What this project covers

| Analysis | Description |
|---|---|
| Credit spread evolution | Euro IG, HY, and Corporate Hybrid spreads (2020–2025) |
| Primary issuance trends | Record EUR 450bn IG issuance in 2025 |
| Hybrid bond market | Sector breakdown, yield comparison vs HY |
| Refinancing wall | EUR ~590bn IG debt maturing 2026–2028 |
| Yield analysis | Bund 10Y vs Euro IG total yield decomposition |

---

## Key findings (Dec 2025)

- **Record issuance:** 2025 marked the third consecutive year of strong Euro credit performance, with record IG (€450bn) and HY (€95bn) issuance driven by robust investor demand
- **Corporate hybrids:** Utilities (34%) and Oil & Gas (31%) dominate; hybrid yields comparable to senior BB bonds — attractive for IG issuers seeking subordinated capital
- **Refinancing opportunity:** 65% of IG debt maturing 2026–2028 carries coupon ≤ 4% vs current IG yield of 3.2% → strong pipeline for liability management exercises and new issuance
- **Credit spreads:** Euro IG at ~62bps, HY at ~285bps, hybrids at ~130bps over Bund

---

## Usage

```bash
pip install numpy pandas matplotlib
python dcm_analysis.py
```

Generates `dcm_dashboard.png` — a 6-panel quantitative DCM dashboard.

In production, data would be pulled via Bloomberg API (`pdblp`) or Refinitiv (`refinitiv-data`).

---

## Dashboard panels

1. **Credit spread evolution** — IG, Hybrid, HY spreads over Bund 2020–2025
2. **Market snapshot** — key yield and spread metrics as of Dec 2025
3. **Primary issuance volume** — annual DCM issuance by segment 2020–2025
4. **Hybrid bond sector breakdown** — pie chart by issuer sector
5. **Refinancing wall** — corporate debt maturities 2026–2030
6. **Yield decomposition** — Bund 10Y vs Euro IG total yield with spread fill

---

## Data sources

- Amundi Euro Credit Market Views, December 2025
- OECD Global Debt Report 2026
- ECB Economic Bulletin, May 2025
- Bloomberg Global Aggregate indices (reference data)

*Note: Data is simulated from published market reports for portfolio demonstration purposes. Production version connects to Bloomberg / Refinitiv API.*

---

## Author

Syed Mohammad Zaheen
MSc Quantitative Finance, University of Kiel
GitHub: [iamzaheen](https://github.com/iamzaheen)

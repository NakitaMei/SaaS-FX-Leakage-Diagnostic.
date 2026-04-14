# SaaS-FX-Leakage-Diagnostic.
Automated MRR and FX leakage diagnostic pipeline engineered for GDPR and GoBD compliance.

# SaaS Revenue Leakage Diagnostic: Strategy & DAX Architecture

🌐 **[Launch Live Diagnostic Application](https://your-streamlit-url-here.streamlit.app/)** *Note: Replace the link above with your actual Streamlit deployment URL.*

---

## 🇬🇧 ENGLISH: Strategic Blueprint

### 1. The Mathematical Logic
Scaling SaaS companies face hidden capital burn when crossing borders and scaling infrastructure. This Python diagnostic engine isolates two primary leakage nodes:

* **FX Spread Leakage:** Un-optimized cross-border transactions incur hidden bank or payment gateway spreads (typically 2-3%). 
    * `Annual_FX_Leakage = (MRR * Cross_Border_%) * FX_Spread * 12`
* **API & Infrastructure Drag:** Orphaned API calls from disconnected tech stacks result in unbilled server load.
    * `Annual_API_Leakage = Monthly_API_Cost * Orphaned_% * 12`

### 2. Integration with Standard DAX Data Models
Traditional Power BI / DAX architectures handle multi-currency conversions poorly when relying on static Excel lookups. A standard DAX measure like:
`CALCULATE(SUM(Transactions[Amount]) * RELATED(FX_Rates[Rate]))` 
often fails to account for intraday spread volatility, leading to month-end reconciliation errors.

**The FinOps Solution:** This architecture utilizes Python for pre-processing. By executing the multi-currency consolidation and calculating the exact FX spread loss *before* the data hits the Power BI visualization layer, we ensure the DAX model remains lightweight, accurate, and scalable.

### 3. Compliance & Risk Mitigation
* **GDPR (DSGVO):** The application runs entirely in-memory using Streamlit. Zero server-side data retention. No database storage.
* **GoBD:** The script generates a timestamped SHA-256 hash of the processed logic, establishing an immutable audit trail for processing integrity.

---

## 🇩🇪 DEUTSCH: Strategie & DAX-Architektur

### 1. Die mathematische Logik
Wachsende SaaS-Unternehmen verzeichnen oft versteckte Kapitalverluste bei grenzüberschreitenden Transaktionen und skalierender Infrastruktur. Dieses Python-Diagnosetool isoliert zwei primäre Verlustquellen:

* **Wechselkursverluste (FX Spread):** Nicht optimierte grenzüberschreitende Transaktionen verursachen versteckte Gebühren bei Banken oder Zahlungsanbietern (typischerweise 2-3%).
    * `Jährlicher_FX_Verlust = (MRR * Cross_Border_%) * FX_Spread * 12`
* **API- & Infrastruktur-Verluste:** Verwaiste API-Aufrufe aus nicht synchronisierten Tech-Stacks führen zu unberechneten Serverkosten.
    * `Jährlicher_API_Verlust = Monatliche_API_Kosten * Orphaned_% * 12`

### 2. Integration mit Standard-DAX-Datenmodellen
Traditionelle Power BI / DAX-Architekturen verarbeiten Multi-Währungs-Umrechnungen oft ineffizient, wenn sie auf statischen Excel-Tabellen basieren. Eine Standard-DAX-Formel wie:
`CALCULATE(SUM(Transactions[Amount]) * RELATED(FX_Rates[Rate]))`
berücksichtigt häufig nicht die Volatilität der untertägigen Spreads, was zu Fehlern beim Monatsabschluss führt.

**Die FinOps-Lösung:** Diese Architektur nutzt Python für die Vorverarbeitung. Indem wir die Multi-Währungs-Konsolidierung durchführen und den genauen Spread-Verlust berechnen, *bevor* die Daten in Power BI visualisiert werden, bleibt das DAX-Modell schlank, fehlerfrei und skalierbar.

### 3. Compliance & Risikomanagement
* **DSGVO (GDPR):** Die Anwendung wird vollständig In-Memory über Streamlit ausgeführt. Keine serverseitige Datenspeicherung. Keine Datenbank-Nutzung.
* **GoBD:** Das Skript generiert einen mit Zeitstempel versehenen SHA-256-Hash der verarbeiteten Logik. Dies schafft einen unveränderlichen Prüfpfad (Audit Trail) und garantiert die Verarbeitungsintegrität nach deutschen Compliance-Standards.

---
*Built by Nakita Meiring | Fractional CFO & FinOps Data Architect*

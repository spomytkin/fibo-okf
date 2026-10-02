---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: quoted ex dividend
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether or not the price is quoted ex-dividend. When a bond is said to trade ex-dividend it means that there is
      a period of time prior to each coupon payment during which a bond purchaser does not receive custody of the next coupon.
      That payment is made to the previous bond holder and accrued interest is therefore negative during the ex-dividend period.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/quotedExDividend
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: quoted ex dividend
type: Ontology Property
---

# quoted ex dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/quotedExDividend>

## Definition

Whether or not the price is quoted ex-dividend. When a bond is said to trade ex-dividend it means that there is a period of time prior to each coupon payment during which a bond purchaser does not receive custody of the next coupon. That payment is made to the previous bond holder and accrued interest is therefore negative during the ex-dividend period.

## Relationships

- **Domain**: [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): quoted ex dividend
- **definition** (en): Whether or not the price is quoted ex-dividend. When a bond is said to trade ex-dividend it means that there is a period of time prior to each coupon payment during which a bond purchaser does not receive custody of the next coupon. That payment is made to the previous bond holder and accrued interest is therefore negative during the ex-dividend period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

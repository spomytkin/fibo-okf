---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: price quoted ex dividend
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether or not the yield is based on a price which is quoted ex-dividend. When a bond is said to trade ex-dividend
      it means that there is a period of time prior to each coupon payment during which a bond purchaser does not receive
      custody of the next coupon. That payment is made to the previous bond holder and accrued interest is therefore negative
      during the ex-dividend period.
  domain:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/priceQuotedExDividend
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: price quoted ex dividend
type: Ontology Property
---

# price quoted ex dividend

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/priceQuotedExDividend>

## Definition

Whether or not the yield is based on a price which is quoted ex-dividend. When a bond is said to trade ex-dividend it means that there is a period of time prior to each coupon payment during which a bond purchaser does not receive custody of the next coupon. That payment is made to the previous bond holder and accrued interest is therefore negative during the ex-dividend period.

## Relationships

- **Domain**: [DebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtInstrumentYield.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): price quoted ex dividend
- **definition** (en): Whether or not the yield is based on a price which is quoted ex-dividend. When a bond is said to trade ex-dividend it means that there is a period of time prior to each coupon payment during which a bond purchaser does not receive custody of the next coupon. That payment is made to the previous bond holder and accrued interest is therefore negative during the ex-dividend period.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

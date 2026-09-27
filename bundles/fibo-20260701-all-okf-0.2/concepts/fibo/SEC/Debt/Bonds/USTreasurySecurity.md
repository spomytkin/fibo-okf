---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.S. Treasury security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument issued by the United States Department of the Treasury that carries a full faith and credit guarantee
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/USTreasurySecurity
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: U.S. Treasury security
type: Ontology Class
---

# U.S. Treasury security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/USTreasurySecurity>

## Definition

debt instrument issued by the United States Department of the Treasury that carries a full faith and credit guarantee

## Relationships

- **Subclass of**: [SovereignDebtInstrument](/concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md)

## Constraints

- **[isDenominatedIn](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/isDenominatedIn.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/ISO4217-CurrencyCodes/USDollar`

## Annotations

- **label**: U.S. Treasury security
- **definition**: debt instrument issued by the United States Department of the Treasury that carries a full faith and credit guarantee

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: variable debt principal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: principal that is defined in relation to some variable and so varies over time, as principal
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Not the same as principal paydown. This is when the principal itself varies over time, usually as a result of being
      defined in relation to some index such as an inflation index. Forms the debt principal in instruments such as inflation
      bonds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasMonetaryAmount
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/PubliclyIssuedDebt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/PubliclyIssuedDebt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableDebtPrincipal
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: variable debt principal
type: Ontology Class
---

# variable debt principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/VariableDebtPrincipal>

## Definition

principal that is defined in relation to some variable and so varies over time, as principal

## Relationships

- **Subclass of**: [PubliclyIssuedDebt](/concepts/fibo/SEC/Debt/DebtInstruments/PubliclyIssuedDebt.md)

## Constraints

- **[hasMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/hasMonetaryAmount.md)**: some values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label**: variable debt principal
- **definition**: principal that is defined in relation to some variable and so varies over time, as principal
- **explanatoryNote** (en): Not the same as principal paydown. This is when the principal itself varies over time, usually as a result of being defined in relation to some index such as an inflation index. Forms the debt principal in instruments such as inflation bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

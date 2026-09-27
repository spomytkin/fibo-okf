---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: partial amortization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: amortization in which the very last payment the last payment due may be a large balloon payment of all remaining
      principal and interest
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Amortization.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Amortization
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PartialAmortization
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: partial amortization
type: Ontology Class
---

# partial amortization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/PartialAmortization>

## Definition

amortization in which the very last payment the last payment due may be a large balloon payment of all remaining principal and interest

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Amortization](/concepts/fibo/FBC/DebtAndEquities/Debt/Amortization.md)

## Annotations

- **label**: partial amortization
- **definition**: amortization in which the very last payment the last payment due may be a large balloon payment of all remaining principal and interest

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

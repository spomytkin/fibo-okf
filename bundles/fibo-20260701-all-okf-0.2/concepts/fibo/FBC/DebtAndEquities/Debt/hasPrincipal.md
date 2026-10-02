---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has principal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the face value of an obligation, such as a bond or loan, that must be repaid at maturity, i.e., the base
      amount raised by a mortgage or other debt instrument
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Principal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipal
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: has principal
type: Ontology Property
---

# has principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasPrincipal>

## Definition

indicates the face value of an obligation, such as a bond or loan, that must be repaid at maturity, i.e., the base amount raised by a mortgage or other debt instrument

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Range**: [Principal](/concepts/fibo/FBC/DebtAndEquities/Debt/Principal.md)

## Annotations

- **label**: has principal
- **definition**: indicates the face value of an obligation, such as a bond or loan, that must be repaid at maturity, i.e., the base amount raised by a mortgage or other debt instrument

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

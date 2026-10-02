---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is owed to
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a debt to the party to which it is payable
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isOwedTo
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: is owed to
type: Ontology Property
---

# is owed to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isOwedTo>

## Definition

links a debt to the party to which it is payable

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Domain**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)
- **Range**: [Creditor](/concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md)

## Annotations

- **label**: is owed to
- **definition**: links a debt to the party to which it is payable

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

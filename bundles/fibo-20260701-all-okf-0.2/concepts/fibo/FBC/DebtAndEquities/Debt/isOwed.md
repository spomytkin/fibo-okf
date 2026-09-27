---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is owed
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links a creditor to a debt that is outstanding and payable to them
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Creditor
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isOwed
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: is owed
type: Ontology Property
---

# is owed

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isOwed>

## Definition

links a creditor to a debt that is outstanding and payable to them

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Domain**: [Creditor](/concepts/fibo/FBC/DebtAndEquities/Debt/Creditor.md)
- **Range**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)

## Annotations

- **label**: is owed
- **definition**: links a creditor to a debt that is outstanding and payable to them

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

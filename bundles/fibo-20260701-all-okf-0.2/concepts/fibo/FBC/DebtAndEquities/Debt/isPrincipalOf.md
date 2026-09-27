---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is principal of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: links the value of a debt, excluding any interest or other costs of using credit, to the debt that it applies to
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Principal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isPrincipalOf
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: is principal of
type: Ontology Property
---

# is principal of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isPrincipalOf>

## Definition

links the value of a debt, excluding any interest or other costs of using credit, to the debt that it applies to

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Domain**: [Principal](/concepts/fibo/FBC/DebtAndEquities/Debt/Principal.md)

## Annotations

- **label**: is principal of
- **definition**: links the value of a debt, excluding any interest or other costs of using credit, to the debt that it applies to

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

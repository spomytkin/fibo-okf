---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debtor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a party that owes a debt or other obligation to another party
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/owes
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Obligor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Obligor
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debtor
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: debtor
type: Ontology Class
---

# debtor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debtor>

## Definition

a party that owes a debt or other obligation to another party

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Obligor](/concepts/fibo/FND/Agreements/Agreements/Obligor.md)

## Constraints

- **[owes](/concepts/fibo/FBC/DebtAndEquities/Debt/owes.md)**: min qualified cardinality 0 of type [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: all values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Annotations

- **label**: debtor
- **definition**: a party that owes a debt or other obligation to another party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

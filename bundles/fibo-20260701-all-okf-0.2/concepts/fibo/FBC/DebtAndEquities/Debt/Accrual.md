---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: accrual
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the process of accumulating interest or other income that has been earned but not paid
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: There are legal contractual terms for the accrual of interest, as distinct from the payment of interest.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Interest
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/Role
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Accrual
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: accrual
type: Ontology Class
---

# accrual

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Accrual>

## Definition

the process of accumulating interest or other income that has been earned but not paid

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Subclass of**: [Role](<https://www.omg.org/spec/Commons/RolesAndCompositions/Role>)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: min qualified cardinality 0 of type [Interest](/concepts/fibo/FBC/DebtAndEquities/Debt/Interest.md)

## Annotations

- **label**: accrual
- **definition**: the process of accumulating interest or other income that has been earned but not paid
- **explanatoryNote**: There are legal contractual terms for the accrual of interest, as distinct from the payment of interest.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

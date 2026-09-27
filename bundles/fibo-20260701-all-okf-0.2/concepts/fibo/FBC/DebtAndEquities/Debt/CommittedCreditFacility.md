---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: committed credit facility
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit facility that is a confirmed source of financing for the borrower, as long as the borrower meets the conditions
      of the agreement
  disjoint_with:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/UncommittedCreditFacility.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/UncommittedCreditFacility
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedSubFacility
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedCreditFacility
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: committed credit facility
type: Ontology Class
---

# committed credit facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedCreditFacility>

## Definition

credit facility that is a confirmed source of financing for the borrower, as long as the borrower meets the conditions of the agreement

## Relationships

- **Subclass of**: [CreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md)

## Constraints

- **Disjoint with**: [UncommittedCreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/UncommittedCreditFacility.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: min qualified cardinality 0 of type [CommittedSubFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CommittedSubFacility.md)

## Annotations

- **label** (en): committed credit facility
- **definition** (en): credit facility that is a confirmed source of financing for the borrower, as long as the borrower meets the conditions of the agreement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

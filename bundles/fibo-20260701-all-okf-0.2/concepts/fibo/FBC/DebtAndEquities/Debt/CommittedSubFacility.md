---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: committed sub-facility
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contractually committed portion of a credit facility that is available to the borrower and may be associated with
      some specific collateral
  disjoint_with:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/UncommittedSubFacility.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/UncommittedSubFacility
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedCreditFacility
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isConstituentOf
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/SubFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/SubFacility
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedSubFacility
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: committed sub-facility
type: Ontology Class
---

# committed sub-facility

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CommittedSubFacility>

## Definition

contractually committed portion of a credit facility that is available to the borrower and may be associated with some specific collateral

## Relationships

- **Subclass of**: [SubFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/SubFacility.md)

## Constraints

- **Disjoint with**: [UncommittedSubFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/UncommittedSubFacility.md)
- **[isConstituentOf](<https://www.omg.org/spec/Commons/Collections/isConstituentOf>)**: some values from of type [CommittedCreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CommittedCreditFacility.md)

## Annotations

- **label** (en): committed sub-facility
- **definition** (en): contractually committed portion of a credit facility that is available to the borrower and may be associated with some specific collateral

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

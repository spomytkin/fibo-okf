---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: borrower disclosure requirement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRight
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/governs
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/BorrowerDisclosureRequirement
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
title: borrower disclosure requirement
type: Ontology Class
---

# borrower disclosure requirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/BorrowerDisclosureRequirement>

## Relationships

- **Subclass of**: [DisclosureRequirement](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/DisclosureRequirement.md)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: some values from of type [ProductDisclosureRight](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/ProductDisclosureRight.md)
- **[governs](<https://www.omg.org/spec/Commons/RegulatoryAgencies/governs>)**: some values from of type [BorrowerAssessment](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/BorrowerAssessment.md)

## Annotations

- **label** (en): borrower disclosure requirement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

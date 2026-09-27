---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has application phase
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The phase within the application lifecycle, that this Loan Application is at,
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplication
  range:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplicationPhase.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/LoanApplicationPhase
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Lifecycles/hasStage
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasApplicationPhase
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: has application phase
type: Ontology Property
---

# has application phase

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/hasApplicationPhase>

## Definition

The phase within the application lifecycle, that this Loan Application is at,

## Relationships

- **Domain**: [LoanApplication](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplication.md)
- **Range**: [LoanApplicationPhase](/concepts/fibo/LOAN/LoansGeneral/LoanApplications/LoanApplicationPhase.md)
- **Subproperty of**: [hasStage](/concepts/fibo/FND/Arrangements/Lifecycles/hasStage.md)

## Annotations

- **label** (en): has application phase
- **definition** (en): The phase within the application lifecycle, that this Loan Application is at,

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

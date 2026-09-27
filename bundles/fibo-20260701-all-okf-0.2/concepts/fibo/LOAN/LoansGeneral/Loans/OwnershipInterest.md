---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ownership interest
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier indicating the nature of the applicant's or borrower's ownership or leasehold interest in an asset used
      as collateral for the loan
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that there are a number of variations for ownership interest that represent 'corner cases', including jurisdiction-specific
      variants, which can be added as needed for specific applications.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OwnershipInterest
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: ownership interest
type: Ontology Class
---

# ownership interest

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OwnershipInterest>

## Definition

classifier indicating the nature of the applicant's or borrower's ownership or leasehold interest in an asset used as collateral for the loan

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)

## Annotations

- **label**: ownership interest
- **definition**: classifier indicating the nature of the applicant's or borrower's ownership or leasehold interest in an asset used as collateral for the loan
- **usageNote**: Note that there are a number of variations for ownership interest that represent 'corner cases', including jurisdiction-specific variants, which can be added as needed for specific applications.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

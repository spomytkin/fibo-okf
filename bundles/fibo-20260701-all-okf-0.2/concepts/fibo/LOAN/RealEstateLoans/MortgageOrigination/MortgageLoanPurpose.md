---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage loan purpose
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the purpose for which mortgage loan proceeds will be used, such as real property purchase, dwelling construction,
      or loan refinancing
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanPurpose.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/LoanPurpose
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageLoanPurpose
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: mortgage loan purpose
type: Ontology Class
---

# mortgage loan purpose

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageLoanPurpose>

## Definition

the purpose for which mortgage loan proceeds will be used, such as real property purchase, dwelling construction, or loan refinancing

## Relationships

- **Subclass of**: [LoanPurpose](/concepts/fibo/LOAN/LoansSpecific/LoanProducts/LoanPurpose.md)
- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: mortgage loan purpose
- **definition**: the purpose for which mortgage loan proceeds will be used, such as real property purchase, dwelling construction, or loan refinancing

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

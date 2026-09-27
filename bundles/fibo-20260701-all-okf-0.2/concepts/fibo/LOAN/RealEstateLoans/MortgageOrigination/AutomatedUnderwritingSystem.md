---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: automated underwriting system
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: software system that collects the information necessary to approve a loan application and supports a mortgage lender's
      analysis of a new loan application
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, automated underwriting systems review the applicant's credit history and ability to repay
      the loan, and determine whether the price the applicant is offering to pay is supported by the property value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/AutomatedSystem.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AutomatedSystem
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AutomatedUnderwritingSystem
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: automated underwriting system
type: Ontology Class
---

# automated underwriting system

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/AutomatedUnderwritingSystem>

## Definition

software system that collects the information necessary to approve a loan application and supports a mortgage lender's analysis of a new loan application

## Relationships

- **Subclass of**: [AutomatedSystem](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/AutomatedSystem.md)

## Annotations

- **label**: automated underwriting system
- **definition**: software system that collects the information necessary to approve a loan application and supports a mortgage lender's analysis of a new loan application
- **explanatoryNote**: In the United States, automated underwriting systems review the applicant's credit history and ability to repay the loan, and determine whether the price the applicant is offering to pay is supported by the property value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

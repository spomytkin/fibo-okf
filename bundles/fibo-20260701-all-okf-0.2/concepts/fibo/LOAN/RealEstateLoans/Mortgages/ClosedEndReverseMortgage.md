---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: Instructions for the Preparation of Consolidated Reports of Condition and Income, FFIEC 031 and FFIEC 041, Updated
      March 2023, clause A-91
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: closed-end reverse mortgage
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: reverse mortgage that provides a lump sum payment to the borrower at closing, with no ability for the borrower
      to receive additional funds under the mortgage at a later date
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Normally, closed-end reverse mortgages are first liens.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/ClosedEndMortgageLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ClosedEndMortgageLoan
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ClosedEndReverseMortgage
sources:
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: closed-end reverse mortgage
type: Ontology Class
---

# closed-end reverse mortgage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ClosedEndReverseMortgage>

## Definition

reverse mortgage that provides a lump sum payment to the borrower at closing, with no ability for the borrower to receive additional funds under the mortgage at a later date

## Relationships

- **Subclass of**: [ClosedEndMortgageLoan](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/ClosedEndMortgageLoan.md)
- **Subclass of**: [ReverseMortgageLoan](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan.md)

## Annotations

- **source**: Instructions for the Preparation of Consolidated Reports of Condition and Income, FFIEC 031 and FFIEC 041, Updated March 2023, clause A-91
- **label**: closed-end reverse mortgage
- **definition**: reverse mortgage that provides a lump sum payment to the borrower at closing, with no ability for the borrower to receive additional funds under the mortgage at a later date
- **explanatoryNote**: Normally, closed-end reverse mortgages are first liens.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

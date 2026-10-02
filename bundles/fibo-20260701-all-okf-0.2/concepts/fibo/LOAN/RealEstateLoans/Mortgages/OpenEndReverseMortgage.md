---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: Instructions for the Preparation of Consolidated Reports of Condition and Income, FFIEC 031 and FFIEC 041, Updated
      March 2023, clause A-91
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: open-end reverse mortgage
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: reverse mortgage structured like a home equity line of credit in that it provides the borrower with additional
      funds after closing (either as fixed monthly payments, under a line of credit, or both)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Normally, open-end reverse mortgages are first liens. These include combinations of both a lump sum payment to
      the borrower at closing and payments after the closing of the loan.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/OpenEndReverseMortgage
sources:
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: open-end reverse mortgage
type: Ontology Class
---

# open-end reverse mortgage

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/OpenEndReverseMortgage>

## Definition

reverse mortgage structured like a home equity line of credit in that it provides the borrower with additional funds after closing (either as fixed monthly payments, under a line of credit, or both)

## Relationships

- **Subclass of**: [OpenEndMortgageLoan](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan.md)
- **Subclass of**: [ReverseMortgageLoan](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/ReverseMortgageLoan.md)

## Annotations

- **source**: Instructions for the Preparation of Consolidated Reports of Condition and Income, FFIEC 031 and FFIEC 041, Updated March 2023, clause A-91
- **label**: open-end reverse mortgage
- **definition**: reverse mortgage structured like a home equity line of credit in that it provides the borrower with additional funds after closing (either as fixed monthly payments, under a line of credit, or both)
- **explanatoryNote**: Normally, open-end reverse mortgages are first liens. These include combinations of both a lump sum payment to the borrower at closing and payments after the closing of the loan.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

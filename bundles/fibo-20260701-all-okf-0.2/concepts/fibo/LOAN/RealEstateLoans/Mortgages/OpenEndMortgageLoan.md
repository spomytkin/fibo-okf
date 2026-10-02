---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: open-end mortgage loan
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan secured by real estate with a provision that the outstanding loan amount may be increased upon mutual agreement
      of the lender and the borrower
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: MISMO Business Glossary, available at https://www.mismo.org/standards-resources/business-glossary/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/OpenEndCredit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/OpenEndCredit
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan
sources:
- id: fibo-source-69fec2eeb0
  resource: references/fibo/LOAN/RealEstateLoans/Mortgages.rdf
  sha256: 69fec2eeb0f7fc099e11c13a9ed3e6b5a1902c2f2a2af30a81282d1f4a6bdfa5
  title: FIBO source LOAN/RealEstateLoans/Mortgages.rdf
title: open-end mortgage loan
type: Ontology Class
---

# open-end mortgage loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/OpenEndMortgageLoan>

## Definition

loan secured by real estate with a provision that the outstanding loan amount may be increased upon mutual agreement of the lender and the borrower

## Relationships

- **Subclass of**: [OpenEndCredit](/concepts/fibo/LOAN/LoansGeneral/Loans/OpenEndCredit.md)
- **Subclass of**: [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Annotations

- **label**: open-end mortgage loan
- **definition**: loan secured by real estate with a provision that the outstanding loan amount may be increased upon mutual agreement of the lender and the borrower
- **adaptedFrom**: MISMO Business Glossary, available at https://www.mismo.org/standards-resources/business-glossary/

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

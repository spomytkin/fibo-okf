---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: home equity line of credit
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: line of credit granted to a homeowner secured by the equity value in a borrower's home or other property
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/acronym
    value: HELOC
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Home equity loans allow the borrower to borrow against the difference between the fair market value of the property,
      as determined by an appraisal, and the amount of any outstanding debt on that property, which is typically a first mortgage.
      Common practice is to set the maximum amount that can be borrowed of up to 80 percent of the fair market value less
      any outstanding debt.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Usually, the term of a HELOC can vary from 5 to up to 25 years, with an initial draw period during which the borrower
      can access the line of credit, followed by a repayment period during which monthly payments on principal and interest
      are due until the loan is paid in full. Note that there are restrictions in the US on the nature of the property that
      may be used as collateral for a HELOC - it must be classified as a 1-4 family dwelling. That determination is independent
      from the use of proceeds.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit
  - concept: /concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit
sources:
- id: fibo-source-7c7642cd54
  resource: references/fibo/LOAN/LoansSpecific/ConsumerLoans.rdf
  sha256: 7c7642cd546c2c1de619d2ea9b384b314886dedf7c8601dab9a46870d0e591d7
  title: FIBO source LOAN/LoansSpecific/ConsumerLoans.rdf
title: home equity line of credit
type: Ontology Class
---

# home equity line of credit

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/HomeEquityLineOfCredit>

## Definition

line of credit granted to a homeowner secured by the equity value in a borrower's home or other property

## Relationships

- **Subclass of**: [RevolvingLineOfCredit](/concepts/fibo/FBC/DebtAndEquities/Debt/RevolvingLineOfCredit.md)
- **Subclass of**: [SecuredConsumerLoan](/concepts/fibo/LOAN/LoansSpecific/ConsumerLoans/SecuredConsumerLoan.md)
- **Subclass of**: [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Annotations

- **label** (en): home equity line of credit
- **definition** (en): line of credit granted to a homeowner secured by the equity value in a borrower's home or other property
- **acronym** (en): HELOC
- **explanatoryNote** (en): Home equity loans allow the borrower to borrow against the difference between the fair market value of the property, as determined by an appraisal, and the amount of any outstanding debt on that property, which is typically a first mortgage. Common practice is to set the maximum amount that can be borrowed of up to 80 percent of the fair market value less any outstanding debt.
- **explanatoryNote** (en): Usually, the term of a HELOC can vary from 5 to up to 25 years, with an initial draw period during which the borrower can access the line of credit, followed by a repayment period during which monthly payments on principal and interest are due until the loan is paid in full. Note that there are restrictions in the US on the nature of the property that may be used as collateral for a HELOC - it must be classified as a 1-4 family dwelling. That determination is independent from the use of proceeds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

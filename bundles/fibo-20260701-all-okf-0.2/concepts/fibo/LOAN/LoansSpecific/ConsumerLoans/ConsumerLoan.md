---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consumer loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan to one or more individuals for household, family, or other personal expenditures, excluding mortgages and
      student loans
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Other secured consumer loans may include loans against insurance policies, against securities held in a retirement
      account, loans secured with collateral other than for the loan's stated purpose, lines of credit other than credit card
      agreements, and so forth.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 12 CFR § 228.12, https://www.law.cornell.edu/cfr/text/12/228.12
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United Kingdom and per the Bank of England, lending to individuals (excluding student loans) consists of
      sterling lending secured on dwellings (i.e. mortgages) and sterling consumer credit to UK-resident individuals. See
      https://www.bankofengland.co.uk/statistics/details/further-details-about-total-lending-to-individuals-data. This definition
      is broader than the definition used in the US, however.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'In the United States, consumer loans do not include a home mortgage, small business, or small farm loans. They
      are defined by law to include the following: (1) Motor vehicle loan, which is a consumer loan extended for the purchase
      of and secured by a motor vehicle; (2) Credit card loan, which is a line of credit for household, family, or other personal
      expenditures that is accessed by a borrower''s use of a ''credit card,'' as this term is defined in § 1026.2 of 12 CFR
      § 228.12; (3) Other secured consumer loan, which is a secured consumer loan that is not included in one of the other
      categories of consumer loans; and (4) Other unsecured consumer loan, which is an unsecured consumer loan that is not
      included in one of the other categories of consumer loans.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasBorrower
    value: N498790302ca74ef3ad5633d32951c883
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/Loan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan
sources:
- id: fibo-source-7c7642cd54
  resource: references/fibo/LOAN/LoansSpecific/ConsumerLoans.rdf
  sha256: 7c7642cd546c2c1de619d2ea9b384b314886dedf7c8601dab9a46870d0e591d7
  title: FIBO source LOAN/LoansSpecific/ConsumerLoans.rdf
title: consumer loan
type: Ontology Class
---

# consumer loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/ConsumerLoan>

## Definition

loan to one or more individuals for household, family, or other personal expenditures, excluding mortgages and student loans

## Relationships

- **Subclass of**: [Loan](/concepts/fibo/LOAN/LoansGeneral/Loans/Loan.md)

## Constraints

- **[hasBorrower](/concepts/fibo/FBC/DebtAndEquities/Debt/hasBorrower.md)**: some values from value `N498790302ca74ef3ad5633d32951c883`

## Annotations

- **label** (en): consumer loan
- **definition** (en): loan to one or more individuals for household, family, or other personal expenditures, excluding mortgages and student loans
- **example** (en): Other secured consumer loans may include loans against insurance policies, against securities held in a retirement account, loans secured with collateral other than for the loan's stated purpose, lines of credit other than credit card agreements, and so forth.
- **adaptedFrom** (en): 12 CFR § 228.12, https://www.law.cornell.edu/cfr/text/12/228.12
- **explanatoryNote** (en): In the United Kingdom and per the Bank of England, lending to individuals (excluding student loans) consists of sterling lending secured on dwellings (i.e. mortgages) and sterling consumer credit to UK-resident individuals. See https://www.bankofengland.co.uk/statistics/details/further-details-about-total-lending-to-individuals-data. This definition is broader than the definition used in the US, however.
- **explanatoryNote** (en): In the United States, consumer loans do not include a home mortgage, small business, or small farm loans. They are defined by law to include the following: (1) Motor vehicle loan, which is a consumer loan extended for the purchase of and secured by a motor vehicle; (2) Credit card loan, which is a line of credit for household, family, or other personal expenditures that is accessed by a borrower's use of a 'credit card,' as this term is defined in § 1026.2 of 12 CFR § 228.12; (3) Other secured consumer loan, which is a secured consumer loan that is not included in one of the other categories of consumer loans; and (4) Other unsecured consumer loan, which is an unsecured consumer loan that is not included in one of the other categories of consumer loans.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

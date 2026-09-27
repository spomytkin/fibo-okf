---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: HMDA covered loan contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under
      US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: the Revised HMDA regulatory text.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HowSubmitted
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract
sources:
- id: fibo-source-c6feed0cf8
  resource: references/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
  sha256: c6feed0cf8f9c31063c105e293abb9e2add43152d3993dd5c4e7722d89df3473
  title: FIBO source LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
title: HMDA covered loan contract
type: Ontology Class
---

# HMDA covered loan contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HMDA-CoveredLoanContract>

## Definition

a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015

## Relationships

- **Subclass of**: [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [HowSubmitted](/concepts/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/HowSubmitted.md)

## Annotations

- **label**: HMDA covered loan contract
- **definition**: a closed-end mortgage loan or open-end line of credit that is not an excluded transaction for HMDA reporting under US section 1003.3(c) of the Revised Home Mortgage Disclosure Act of 2015
- **adaptedFrom**: the Revised HMDA regulatory text.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

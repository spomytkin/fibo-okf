---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: universal loan identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unique identifier given to unequivocally identify a specific loan secured by real estate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the US, the structure of this identifier is defined in the 2015 revision to the Home Mortgage Disclosure Act.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/LegalEntityIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/UniversalLoanIdentifier
sources:
- id: fibo-source-c6feed0cf8
  resource: references/fibo/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
  sha256: c6feed0cf8f9c31063c105e293abb9e2add43152d3993dd5c4e7722d89df3473
  title: FIBO source LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages.rdf
title: universal loan identifier
type: Ontology Class
---

# universal loan identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/HomeMortgageDisclosureActCoveredMortgages/UniversalLoanIdentifier>

## Definition

unique identifier given to unequivocally identify a specific loan secured by real estate

## Relationships

- **Subclass of**: [FinancialInstrumentIdentifier](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrumentIdentifier.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [LegalEntityIdentifier](/concepts/fibo/BE/LegalEntities/LEIEntities/LegalEntityIdentifier.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Annotations

- **label**: universal loan identifier
- **definition**: unique identifier given to unequivocally identify a specific loan secured by real estate
- **explanatoryNote**: In the US, the structure of this identifier is defined in the 2015 revision to the Home Mortgage Disclosure Act.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

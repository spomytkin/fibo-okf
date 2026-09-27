---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan-to-value ratio
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ratio, expressed as a percentage, between the principal amount of the loan and the appraised value of the asset
      securing the financing
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LTV
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/Appraisal
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/AppraisedValue
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanToValueRatio
sources:
- id: fibo-source-3a6fded17e
  resource: references/fibo/LOAN/LoansGeneral/Loans.rdf
  sha256: 3a6fded17e53b09613c8738a0ed77662a436d03a066ae0ddf7952214fb5d7280
  title: FIBO source LOAN/LoansGeneral/Loans.rdf
title: loan-to-value ratio
type: Ontology Class
---

# loan-to-value ratio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/LoanToValueRatio>

## Definition

ratio, expressed as a percentage, between the principal amount of the loan and the appraised value of the asset securing the financing

## Relationships

- **Subclass of**: [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [Appraisal](/concepts/fibo/FND/Arrangements/Assessments/Appraisal.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [Principal](/concepts/fibo/FBC/DebtAndEquities/Debt/Principal.md)
- **[hasArgument](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/hasArgument>)**: some values from of type [AppraisedValue](/concepts/fibo/FND/Arrangements/Assessments/AppraisedValue.md)

## Annotations

- **label**: loan-to-value ratio
- **definition**: ratio, expressed as a percentage, between the principal amount of the loan and the appraised value of the asset securing the financing
- **abbreviation**: LTV

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

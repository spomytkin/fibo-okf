---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contract leg 1 interest payment terms IY7VKEUR45886
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: interest payment terms for contract IY7VKEUR45886 swap leg 1 that is a fixed interest rate leg
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
  related_to:
  - concept: /concepts/fibo/EXMP/Securities/IRSwapExamples/ContractLeg1-IY7VKEUR45886-InterestRate.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestRate
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/ContractLeg1-IY7VKEUR45886-InterestRate
  - concept: /concepts/fibo/EXMP/Securities/IRSwapExamples/EuropeanCentralBankBBusinessDayAdjustment.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/BusinessDates/hasBusinessDayConvention
    resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/EuropeanCentralBankBBusinessDayAdjustment
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/DayCountConvention-30E360.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasAccrualBasis
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/DayCountConvention-30E360
  - concept: /concepts/fibo/IND/InterestRates/InterestRates/OneYear.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/hasInterestPaymentFrequency
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/OneYear
resource: https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/ContractLeg1-IY7VKEUR45886-InterestPaymentTerms
sources:
- id: fibo-source-dbb6868e12
  resource: references/fibo/EXMP/Securities/IRSwapExamples.rdf
  sha256: dbb6868e124bba0f62a80f6387c9e212e8d2931ed572f2e411e31534e2edcfc5
  title: FIBO source EXMP/Securities/IRSwapExamples.rdf
title: contract leg 1 interest payment terms IY7VKEUR45886
type: Ontology Individual
---

# contract leg 1 interest payment terms IY7VKEUR45886

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/EXMP/Securities/IRSwapExamples/ContractLeg1-IY7VKEUR45886-InterestPaymentTerms>

## Definition

interest payment terms for contract IY7VKEUR45886 swap leg 1 that is a fixed interest rate leg

## Relationships

- **Related to**: [DayCountConvention-30E360](/concepts/fibo/FBC/DebtAndEquities/Debt/DayCountConvention-30E360.md)
- **Related to**: [OneYear](/concepts/fibo/IND/InterestRates/InterestRates/OneYear.md)
- **Related to**: [ContractLeg1-IY7VKEUR45886-InterestRate](/concepts/fibo/EXMP/Securities/IRSwapExamples/ContractLeg1-IY7VKEUR45886-InterestRate.md)
- **Related to**: [EuropeanCentralBankBBusinessDayAdjustment](/concepts/fibo/EXMP/Securities/IRSwapExamples/EuropeanCentralBankBBusinessDayAdjustment.md)

## Annotations

- **label**: contract leg 1 interest payment terms IY7VKEUR45886
- **definition**: interest payment terms for contract IY7VKEUR45886 swap leg 1 that is a fixed interest rate leg

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is Employee Retirement Income Security Act conformant
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether the security conforms to the Employee Retirement Income Security Act (ERISA) of 1974, a federal
      outline for regulating employee benefit plans, including healthcare plans sponsored and/or insured by an employer
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Code Title 29, Chapter 18, Subchapter I, Section 1002 provides definitions related to employee benefit plans.
      Specifically, this section outlines the terms used in ERISA, including definitions for various types of plans such as
      employee welfare benefit plans, employee pension benefit plans, and others. See https://www.law.cornell.edu/uscode/text/29/1002.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Employee Retirement Income Security Act (ERISA) is a federal law that establishes standards for certain employer-sponsored
      retirement and health plans. It has undergone several changes since its initial enactment in 1974. ERISA aims to protect
      individuals participating in these plans by prohibiting fiduciaries from misusing funds and setting standards for participation,
      benefit accrual, vesting, and funding of retirement plans
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/isEmployeeRetirementIncomeSecurityActConformant
sources:
- id: fibo-source-91c51c4810
  resource: references/fibo/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
  sha256: 91c51c4810cfe6c5acc0aaf99de529357298d47f01cfe4f5eee4962f40f5be33
  title: FIBO source SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions.rdf
title: is Employee Retirement Income Security Act conformant
type: Ontology Property
---

# is Employee Retirement Income Security Act conformant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/isEmployeeRetirementIncomeSecurityActConformant>

## Definition

indicates whether the security conforms to the Employee Retirement Income Security Act (ERISA) of 1974, a federal outline for regulating employee benefit plans, including healthcare plans sponsored and/or insured by an employer

## Relationships

- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is Employee Retirement Income Security Act conformant
- **definition**: indicates whether the security conforms to the Employee Retirement Income Security Act (ERISA) of 1974, a federal outline for regulating employee benefit plans, including healthcare plans sponsored and/or insured by an employer
- **adaptedFrom**: U.S. Code Title 29, Chapter 18, Subchapter I, Section 1002 provides definitions related to employee benefit plans. Specifically, this section outlines the terms used in ERISA, including definitions for various types of plans such as employee welfare benefit plans, employee pension benefit plans, and others. See https://www.law.cornell.edu/uscode/text/29/1002.
- **explanatoryNote**: The Employee Retirement Income Security Act (ERISA) is a federal law that establishes standards for certain employer-sponsored retirement and health plans. It has undergone several changes since its initial enactment in 1974. ERISA aims to protect individuals participating in these plans by prohibiting fiduciaries from misusing funds and setting standards for participation, benefit accrual, vesting, and funding of retirement plans

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

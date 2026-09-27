---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: absolute prepayment rate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: measure of the monthly rate of loan prepayments as a percentage of the original pool balance
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ABS
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: ABS is defined by the following formula where SMM refers to Single Monthly Mortality, which measures the percentage
      of dollars prepaid in a given month expressed as a percentage of the scheduled loan balance. ABS = (100 * SMM)/100 +
      (SMM X (Age - 1).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The ABS measurement differs from conditional prepayment rate (CPR) used in the mortgage industry, which measures
      prepayment as an annualized percentage of the current pool balance.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AbsolutePrepaymentRate
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: absolute prepayment rate
type: Ontology Class
---

# absolute prepayment rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/AbsolutePrepaymentRate>

## Definition

measure of the monthly rate of loan prepayments as a percentage of the original pool balance

## Relationships

- **Subclass of**: [DebtPoolStatisticalMeasure](/concepts/fibo/SEC/Debt/PoolBackedSecurities/DebtPoolStatisticalMeasure.md)

## Annotations

- **label** (en): absolute prepayment rate
- **definition** (en): measure of the monthly rate of loan prepayments as a percentage of the original pool balance
- **abbreviation** (en): ABS
- **explanatoryNote** (en): ABS is defined by the following formula where SMM refers to Single Monthly Mortality, which measures the percentage of dollars prepaid in a given month expressed as a percentage of the scheduled loan balance. ABS = (100 * SMM)/100 + (SMM X (Age - 1).
- **explanatoryNote** (en): The ABS measurement differs from conditional prepayment rate (CPR) used in the mortgage industry, which measures prepayment as an annualized percentage of the current pool balance.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest obligation in light of default
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: obligation in respect of default(s) in the performance of any payment obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Prior to the occurrence or effective designation of an early termination date in respect of the relevant transaction,
      a party that defaults in the performance of any payment obligation will, to the extent permitted by law (and in the
      case of an ISDA Master Agreement is subject to Section 6(c)), be required to pay interest (before as well as after judgment)
      on the overdue amount to the other party on demand in the same currency as such overdue amount, for the period from
      (and including) the original due date for payment to (but excluding) the date of actual payment, at the default rate.
      Such interest will be calculated on the basis of daily compounding and the actual number of days elapsed.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/hasDefaultInterestCompoundingBasis
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#boolean
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/isDefaultInterestApplicable
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isMandatedBy
    value: Nd49bfbdd38bf414592677d6e7d0890fc
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContractualObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualObligation
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault
sources:
- id: fibo-source-bc069e913f
  resource: references/fibo/FBC/DebtAndEquities/CreditEvents.rdf
  sha256: bc069e913f78f120d461cf77899be0452acda5d5786c9cd342e37931a2b141c6
  title: FIBO source FBC/DebtAndEquities/CreditEvents.rdf
title: interest obligation in light of default
type: Ontology Class
---

# interest obligation in light of default

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/InterestObligationInLightOfDefault>

## Definition

obligation in respect of default(s) in the performance of any payment obligation

## Relationships

- **Subclass of**: [ContingentObligation](/concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md)
- **Subclass of**: [ContractualObligation](/concepts/fibo/FND/Law/LegalCapacity/ContractualObligation.md)

## Constraints

- **[hasDefaultInterestCompoundingBasis](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/hasDefaultInterestCompoundingBasis.md)**: max qualified cardinality 1 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[isDefaultInterestApplicable](/concepts/fibo/FBC/DebtAndEquities/CreditEvents/isDefaultInterestApplicable.md)**: max qualified cardinality 1 of type [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)
- **[isMandatedBy](/concepts/fibo/FND/Relations/Relations/isMandatedBy.md)**: some values from value `Nd49bfbdd38bf414592677d6e7d0890fc`

## Annotations

- **label** (en): interest obligation in light of default
- **definition** (en): obligation in respect of default(s) in the performance of any payment obligation
- **example** (en): Prior to the occurrence or effective designation of an early termination date in respect of the relevant transaction, a party that defaults in the performance of any payment obligation will, to the extent permitted by law (and in the case of an ISDA Master Agreement is subject to Section 6(c)), be required to pay interest (before as well as after judgment) on the overdue amount to the other party on demand in the same currency as such overdue amount, for the period from (and including) the original due date for payment to (but excluding) the date of actual payment, at the default rate. Such interest will be calculated on the basis of daily compounding and the actual number of days elapsed.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

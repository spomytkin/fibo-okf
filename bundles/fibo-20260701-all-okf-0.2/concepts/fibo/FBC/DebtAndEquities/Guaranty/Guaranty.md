---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: guaranty
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commitment whereby something is formally assured if a party with primary liability fails to perform
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The commitment may cover a debt, cash flows on a debt instrument (such as interest payments), or performance of
      some obligation.
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuaranteedAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/PriorityLevel
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasPriorityLevel
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/isGuaranteedBy
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasExpirationDate
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/holdsDuring
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Agreements/Commitment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Agreements/Commitment
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: guaranty
type: Ontology Class
---

# guaranty

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guaranty>

## Definition

commitment whereby something is formally assured if a party with primary liability fails to perform

## Relationships

- **Defined by**: [Guaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty.md)
- **Subclass of**: [Commitment](/concepts/fibo/FND/Agreements/Agreements/Commitment.md)

## Constraints

- **[hasGuaranteedAmount](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasGuaranteedAmount.md)**: all values from of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[hasPriorityLevel](/concepts/fibo/FBC/DebtAndEquities/Guaranty/hasPriorityLevel.md)**: all values from of type [PriorityLevel](/concepts/fibo/FBC/DebtAndEquities/Guaranty/PriorityLevel.md)
- **[isGuaranteedBy](/concepts/fibo/FBC/DebtAndEquities/Guaranty/isGuaranteedBy.md)**: all values from of type [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- **[hasExpirationDate](/concepts/fibo/FND/Arrangements/Documents/hasExpirationDate.md)**: all values from of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[holdsDuring](<https://www.omg.org/spec/Commons/PartiesAndSituations/holdsDuring>)**: all values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: guaranty
- **definition**: commitment whereby something is formally assured if a party with primary liability fails to perform
- **adaptedFrom**: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
- **explanatoryNote**: The commitment may cover a debt, cash flows on a debt instrument (such as interest payments), or performance of some obligation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: long-term equity anticipation security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: equity option that allows the holder to buy or sell shares of stock with expiration dates that are longer than
      one year, and typically up to three years from issue
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LEAP
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: By providing opportunities to control and manage risk or even to speculate, LEAPS are virtually identical to regular
      options. Expiration dates on LEAPs can range from nine months to three years, which is longer than the holding period
      for a traditional call or put option. Although they are not available on all stocks, LEAPS are available on most widely
      held issues.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/Duration
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractDuration
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/Options/EquityOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/EquityOption
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/LongTermEquityAnticipationSecurity
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: long-term equity anticipation security
type: Ontology Class
---

# long-term equity anticipation security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/LongTermEquityAnticipationSecurity>

## Definition

equity option that allows the holder to buy or sell shares of stock with expiration dates that are longer than one year, and typically up to three years from issue

## Relationships

- **Subclass of**: [EquityOption](/concepts/fibo/DER/DerivativesContracts/Options/EquityOption.md)

## Constraints

- **[hasContractDuration](/concepts/fibo/FND/Agreements/Contracts/hasContractDuration.md)**: some values from of type [Duration](<https://www.omg.org/spec/Commons/DatesAndTimes/Duration>)

## Annotations

- **label** (en): long-term equity anticipation security
- **definition** (en): equity option that allows the holder to buy or sell shares of stock with expiration dates that are longer than one year, and typically up to three years from issue
- **abbreviation** (en): LEAP
- **explanatoryNote** (en): By providing opportunities to control and manage risk or even to speculate, LEAPS are virtually identical to regular options. Expiration dates on LEAPs can range from nine months to three years, which is longer than the holding period for a traditional call or put option. Although they are not available on all stocks, LEAPS are available on most widely held issues.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has dated date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specifies the date on which interest begins to accrue on a fixed-income security
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Investors who purchase a fixed-income security between interest payment dates must also pay the seller or issuer
      any interest that has accrued from the dated date to the purchase date, or settlement date, in addition to the face
      value.
  domain:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/InterestPaymentTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasDatedDate
sources:
- id: fibo-source-c925727a93
  resource: references/fibo/SEC/Debt/DebtInstruments.rdf
  sha256: c925727a93c23f915b4b066177d4aaad43b8ca620e9ced28bc7a9b1cb316a54c
  title: FIBO source SEC/Debt/DebtInstruments.rdf
title: has dated date
type: Ontology Property
---

# has dated date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasDatedDate>

## Definition

specifies the date on which interest begins to accrue on a fixed-income security

## Relationships

- **Domain**: [InterestPaymentTerms](/concepts/fibo/FBC/DebtAndEquities/Debt/InterestPaymentTerms.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasExplicitDate>)

## Annotations

- **label**: has dated date
- **definition**: specifies the date on which interest begins to accrue on a fixed-income security
- **explanatoryNote** (en): Investors who purchase a fixed-income security between interest payment dates must also pay the seller or issuer any interest that has accrued from the dated date to the purchase date, or settlement date, in addition to the face value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

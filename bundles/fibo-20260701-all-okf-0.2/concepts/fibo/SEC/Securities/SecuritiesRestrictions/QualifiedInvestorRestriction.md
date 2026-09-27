---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: qualified investor restriction
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal holding restriction that defines the concept of a qualified investor for a given purpose and specifies that
      only such qualified investors may hold the security
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If a holding period is not defined, then the period for which the restriction applies is indefinite.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasHoldingPeriod
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesRestrictions/LegalHoldingRestriction.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/LegalHoldingRestriction
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/QualifiedInvestorRestriction
sources:
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: qualified investor restriction
type: Ontology Class
---

# qualified investor restriction

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/QualifiedInvestorRestriction>

## Definition

legal holding restriction that defines the concept of a qualified investor for a given purpose and specifies that only such qualified investors may hold the security

## Relationships

- **Subclass of**: [LegalHoldingRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/LegalHoldingRestriction.md)

## Constraints

- **[hasHoldingPeriod](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/hasHoldingPeriod.md)**: all values from of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: qualified investor restriction
- **definition**: legal holding restriction that defines the concept of a qualified investor for a given purpose and specifies that only such qualified investors may hold the security
- **explanatoryNote**: If a holding period is not defined, then the period for which the restriction applies is indefinite.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has announcement date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the first day the public will receive information regarding a new security issue
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An announcement date may also refer to the release of a corporate event or new financial news, such as interest
      rate changes or earnings reports.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/Date
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/hasDate
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasAnnouncementDate
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: has announcement date
type: Ontology Property
---

# has announcement date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/hasAnnouncementDate>

## Definition

indicates the first day the public will receive information regarding a new security issue

## Relationships

- **Range**: [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **Subproperty of**: [hasDate](<https://www.omg.org/spec/Commons/DatesAndTimes/hasDate>)

## Annotations

- **label**: has announcement date
- **definition**: indicates the first day the public will receive information regarding a new security issue
- **explanatoryNote**: An announcement date may also refer to the release of a corporate event or new financial news, such as interest rate changes or earnings reports.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

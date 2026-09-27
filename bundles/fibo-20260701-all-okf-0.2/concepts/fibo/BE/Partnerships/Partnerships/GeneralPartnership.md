---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: general partnership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: partnership that has at least two general partners that agree to share in all assets, profits, and financial and
      legal liabilities of the business
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: General partnerships are the most basic and common form of partnership world-wide.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasGeneralPartner
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: Nd28daaad5fe040de8357c10b4a3a0fc3
  subclass_of:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartnership
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: general partnership
type: Ontology Class
---

# general partnership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartnership>

## Definition

partnership that has at least two general partners that agree to share in all assets, profits, and financial and legal liabilities of the business

## Relationships

- **Subclass of**: [Partnership](/concepts/fibo/BE/Partnerships/Partnerships/Partnership.md)

## Constraints

- **[hasGeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/hasGeneralPartner.md)**: some values from of type [GeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `Nd28daaad5fe040de8357c10b4a3a0fc3`

## Annotations

- **label**: general partnership
- **definition**: partnership that has at least two general partners that agree to share in all assets, profits, and financial and legal liabilities of the business
- **abbreviation**: GP
- **explanatoryNote**: General partnerships are the most basic and common form of partnership world-wide.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

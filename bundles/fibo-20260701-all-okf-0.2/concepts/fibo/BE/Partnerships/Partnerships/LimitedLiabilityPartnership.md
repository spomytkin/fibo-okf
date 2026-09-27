---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited liability partnership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: partnership that has general partners but provides its individual partners some level of protection against personal
      liability for certain partnership liabilities
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Law firms, accountancies, wealth managers, professional medical groups, and other professional consultancies often
      take the form of a limited liability partnership.
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: One example of a limited liability partnership is that of an incorporated limited partnership (ILP) in Australia.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LLP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: LLPs are a flexible legal and tax entity that allows partners to benefit from economies of scale by working together
      while also reducing their liability for the actions of other partners.
  disjoint_with:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/LimitedPartnership.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartnership
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasGeneralPartner
  subclass_of:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedLiabilityPartnership
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: limited liability partnership
type: Ontology Class
---

# limited liability partnership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedLiabilityPartnership>

## Definition

partnership that has general partners but provides its individual partners some level of protection against personal liability for certain partnership liabilities

## Relationships

- **Subclass of**: [Partnership](/concepts/fibo/BE/Partnerships/Partnerships/Partnership.md)

## Constraints

- **Disjoint with**: [LimitedPartnership](/concepts/fibo/BE/Partnerships/Partnerships/LimitedPartnership.md)
- **[hasGeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/hasGeneralPartner.md)**: some values from of type [GeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md)

## Annotations

- **label**: limited liability partnership
- **definition**: partnership that has general partners but provides its individual partners some level of protection against personal liability for certain partnership liabilities
- **example**: Law firms, accountancies, wealth managers, professional medical groups, and other professional consultancies often take the form of a limited liability partnership.
- **example**: One example of a limited liability partnership is that of an incorporated limited partnership (ILP) in Australia.
- **abbreviation**: LLP
- **explanatoryNote**: LLPs are a flexible legal and tax entity that allows partners to benefit from economies of scale by working together while also reducing their liability for the actions of other partners.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

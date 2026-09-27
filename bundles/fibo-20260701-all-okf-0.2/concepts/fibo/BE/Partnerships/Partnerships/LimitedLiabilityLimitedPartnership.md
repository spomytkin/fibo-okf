---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited liability limited partnership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: limited partnership that consists of one or more general partners who are liable for the obligations of the entity
      as well as one or more protected limited liability partners
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LLLP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The primary difference between an LLLP and more traditional limited partnership is that an LLLP allows liability
      transfer from the general partner's (to external insurer) for debts and obligations of the limited partnership. Typically,
      general partners manage the LLLP, while the limited partners' interest is primarily for investment purposes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/LimitedPartnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartnership
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedLiabilityLimitedPartnership
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: limited liability limited partnership
type: Ontology Class
---

# limited liability limited partnership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedLiabilityLimitedPartnership>

## Definition

limited partnership that consists of one or more general partners who are liable for the obligations of the entity as well as one or more protected limited liability partners

## Relationships

- **Subclass of**: [LimitedPartnership](/concepts/fibo/BE/Partnerships/Partnerships/LimitedPartnership.md)

## Annotations

- **label**: limited liability limited partnership
- **definition**: limited partnership that consists of one or more general partners who are liable for the obligations of the entity as well as one or more protected limited liability partners
- **abbreviation**: LLLP
- **explanatoryNote**: The primary difference between an LLLP and more traditional limited partnership is that an LLLP allows liability transfer from the general partner's (to external insurer) for debts and obligations of the limited partnership. Typically, general partners manage the LLLP, while the limited partners' interest is primarily for investment purposes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

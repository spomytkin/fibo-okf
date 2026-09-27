---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited partnership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: partnership that has at least one general partner and at least one limited partner
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: In the United States, film production companies, real estate investment firms, and private equity firms are typically
      formed as limited partnerships. In the United Kingdom, limited partnerships are governed by the Limited Partnerships
      Act 1907 and, on matters on which that Act is silent, also by the Partnership Act 1890.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: LP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Limited partnerships are distinct from limited liability partnerships, in which all partners have limited liability.
      Similar to a general partnership, the general partners have management control, share the right to use partnership property,
      share the profits of the firm in predefined proportions, and have joint and several liability for the debts of the partnership.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasGeneralPartner
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartner
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasLimitedPartner
  subclass_of:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartnership
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: limited partnership
type: Ontology Class
---

# limited partnership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartnership>

## Definition

partnership that has at least one general partner and at least one limited partner

## Relationships

- **Subclass of**: [Partnership](/concepts/fibo/BE/Partnerships/Partnerships/Partnership.md)

## Constraints

- **[hasGeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/hasGeneralPartner.md)**: some values from of type [GeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md)
- **[hasLimitedPartner](/concepts/fibo/BE/Partnerships/Partnerships/hasLimitedPartner.md)**: some values from of type [LimitedPartner](/concepts/fibo/BE/Partnerships/Partnerships/LimitedPartner.md)

## Annotations

- **label**: limited partnership
- **definition**: partnership that has at least one general partner and at least one limited partner
- **example**: In the United States, film production companies, real estate investment firms, and private equity firms are typically formed as limited partnerships. In the United Kingdom, limited partnerships are governed by the Limited Partnerships Act 1907 and, on matters on which that Act is silent, also by the Partnership Act 1890.
- **abbreviation**: LP
- **explanatoryNote**: Limited partnerships are distinct from limited liability partnerships, in which all partners have limited liability. Similar to a general partnership, the general partners have management control, share the right to use partnership property, share the profits of the firm in predefined proportions, and have joint and several liability for the debts of the partnership.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: limited partner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: partner whose liabilities are limited to the extent of their investment or guarantees and that has no involvement
      in the day to day operations of the partnership
  disjoint_with:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartner
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: limited partner
type: Ontology Class
---

# limited partner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartner>

## Definition

partner whose liabilities are limited to the extent of their investment or guarantees and that has no involvement in the day to day operations of the partnership

## Relationships

- **Subclass of**: [Partner](/concepts/fibo/BE/Partnerships/Partnerships/Partner.md)

## Constraints

- **Disjoint with**: [GeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md)

## Annotations

- **label**: limited partner
- **definition**: partner whose liabilities are limited to the extent of their investment or guarantees and that has no involvement in the day to day operations of the partnership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

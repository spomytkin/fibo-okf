---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has limited partner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates an actor that may have some measure of influence over the partnership
  domain:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
  range:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/LimitedPartner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/LimitedPartner
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasLimitedPartner
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: has limited partner
type: Ontology Property
---

# has limited partner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasLimitedPartner>

## Definition

indicates an actor that may have some measure of influence over the partnership

## Relationships

- **Domain**: [Partnership](/concepts/fibo/BE/Partnerships/Partnerships/Partnership.md)
- **Range**: [LimitedPartner](/concepts/fibo/BE/Partnerships/Partnerships/LimitedPartner.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: has limited partner
- **definition**: indicates an actor that may have some measure of influence over the partnership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

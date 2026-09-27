---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has general partner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates an actor that has some measure of control over the partnership
  domain:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
  range:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasGeneralPartner
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: has general partner
type: Ontology Property
---

# has general partner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasGeneralPartner>

## Definition

indicates an actor that has some measure of control over the partnership

## Relationships

- **Domain**: [Partnership](/concepts/fibo/BE/Partnerships/Partnerships/Partnership.md)
- **Range**: [GeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md)
- **Subproperty of**: [isAffectedBy](<https://www.omg.org/spec/Commons/PartiesAndSituations/isAffectedBy>)

## Annotations

- **label**: has general partner
- **definition**: indicates an actor that has some measure of control over the partnership

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

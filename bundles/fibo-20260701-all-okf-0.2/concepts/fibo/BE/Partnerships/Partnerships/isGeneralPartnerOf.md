---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is general partner of
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the organization that the general partner manages
  domain:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
  inverse_of:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/hasGeneralPartner.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/hasGeneralPartner
  range:
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partnership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partnership
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/isGeneralPartnerOf
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: is general partner of
type: Ontology Property
---

# is general partner of

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/isGeneralPartnerOf>

## Definition

indicates the organization that the general partner manages

## Relationships

- **Domain**: [GeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/GeneralPartner.md)
- **Inverse of**: [hasGeneralPartner](/concepts/fibo/BE/Partnerships/Partnerships/hasGeneralPartner.md)
- **Range**: [Partnership](/concepts/fibo/BE/Partnerships/Partnerships/Partnership.md)
- **Subproperty of**: [actsOn](<https://www.omg.org/spec/Commons/PartiesAndSituations/actsOn>)

## Annotations

- **label**: is general partner of
- **definition**: indicates the organization that the general partner manages

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

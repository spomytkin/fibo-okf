---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: general partner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: partner and part-owner that is responsible for managing the day to day operations of the partnership and that may
      be jointly and severally liable for the obligations of the partnership
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that although typically a general partner is a person, in the context of certain funds, such as private equity,
      a general partner may be a firm that manages the fund.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: Nfd63d0b9d34d4a0da4a644435dd95420
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty
  - concept: /concepts/fibo/BE/Partnerships/Partnerships/Partner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/Partner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner
sources:
- id: fibo-source-d8e7bd00bc
  resource: references/fibo/BE/Partnerships/Partnerships.rdf
  sha256: d8e7bd00bcec02116a8ba944082e7c83bd17338e42c9b9925e2ef483b7e1cacf
  title: FIBO source BE/Partnerships/Partnerships.rdf
title: general partner
type: Ontology Class
---

# general partner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Partnerships/Partnerships/GeneralPartner>

## Definition

partner and part-owner that is responsible for managing the day to day operations of the partnership and that may be jointly and severally liable for the obligations of the partnership

## Relationships

- **Subclass of**: [DeJureControllingInterestParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/DeJureControllingInterestParty.md)
- **Subclass of**: [Partner](/concepts/fibo/BE/Partnerships/Partnerships/Partner.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `Nfd63d0b9d34d4a0da4a644435dd95420`

## Annotations

- **label**: general partner
- **definition**: partner and part-owner that is responsible for managing the day to day operations of the partnership and that may be jointly and severally liable for the obligations of the partnership
- **explanatoryNote**: Note that although typically a general partner is a person, in the context of certain funds, such as private equity, a general partner may be a firm that manages the fund.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

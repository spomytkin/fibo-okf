---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: corporate bylaws
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written rules for conduct of a corporation, adopted by the board of directors
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Corporate bylaws may contain any provision, not inconsistent with law or with the certificate of incorporation,
      relating to the business of the corporation, the conduct of its affairs, and its rights or powers or the rights or powers
      of its stockholders, directors, officers or employees. Changes to the bylaws of a corporation require a board-level
      resolution and may require a vote of the shareholders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/hasSharesAuthorized
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Bylaws.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Bylaws
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateBylaws
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: corporate bylaws
type: Ontology Class
---

# corporate bylaws

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateBylaws>

## Definition

written rules for conduct of a corporation, adopted by the board of directors

## Relationships

- **Subclass of**: [Bylaws](/concepts/fibo/BE/OwnershipAndControl/Executives/Bylaws.md)

## Constraints

- **[hasSharesAuthorized](/concepts/fibo/BE/LegalEntities/CorporateBodies/hasSharesAuthorized.md)**: some values from of type [nonNegativeInteger](<http://www.w3.org/2001/XMLSchema#nonNegativeInteger>)

## Annotations

- **label**: corporate bylaws
- **definition**: written rules for conduct of a corporation, adopted by the board of directors
- **explanatoryNote**: Corporate bylaws may contain any provision, not inconsistent with law or with the certificate of incorporation, relating to the business of the corporation, the conduct of its affairs, and its rights or powers or the rights or powers of its stockholders, directors, officers or employees. Changes to the bylaws of a corporation require a board-level resolution and may require a vote of the shareholders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

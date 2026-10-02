---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: constitutional owner
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entity owner that holds an equity stake in said entity, in the form of shareholders' equity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Typically this would be share ownership or the holding of partnership equity. Ownership in this 'constitutional'
      sense means that the owner is in some way a member of the organization, such as an employee or director, as distinct
      from some outside investor.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/ShareholdersEquity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: constitutional owner
type: Ontology Class
---

# constitutional owner

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/ConstitutionalOwner>

## Definition

entity owner that holds an equity stake in said entity, in the form of shareholders' equity

## Relationships

- **Subclass of**: [EntityOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [ShareholdersEquity](/concepts/fibo/FND/OwnershipAndControl/Ownership/ShareholdersEquity.md)

## Annotations

- **label**: constitutional owner
- **definition**: entity owner that holds an equity stake in said entity, in the form of shareholders' equity
- **explanatoryNote**: Typically this would be share ownership or the holding of partnership equity. Ownership in this 'constitutional' sense means that the owner is in some way a member of the organization, such as an employee or director, as distinct from some outside investor.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

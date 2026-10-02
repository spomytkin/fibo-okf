---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: de facto controlling interest party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that exercises some control over an entity other than via explicit, legal means
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: a silent partner, i.e. where someone has made a large investment, which is bilateral (not part of the constitutional
      framework of the company)
  - predicate: http://www.w3.org/2004/02/skos/core#scopeNote
    value: divides further into financial leverage via loans; non fiscal types of leverage (influence)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A control owner (i.e., control person, per SEC regulations) may have some means or right that allows them to exercise
      control over board composition, other than through proxy assignment or vote. Not all control persons have this facility,
      as it is not inherent to having a significant (for example, 20 percent or more) ownership stake.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/BoardMember
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/nominates
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/DeFactoControl
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/isControllingPartyIn
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/ControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty
sources:
- id: fibo-source-81ee03cff7
  resource: references/fibo/BE/OwnershipAndControl/ControlParties.rdf
  sha256: 81ee03cff7bfd7e2f6e748c95bd2b9fc331c79b25135024086bfb943a8031ba1
  title: FIBO source BE/OwnershipAndControl/ControlParties.rdf
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: de facto controlling interest party
type: Ontology Class
---

# de facto controlling interest party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/DeFactoControllingInterestParty>

## Definition

party that exercises some control over an entity other than via explicit, legal means

## Relationships

- **Subclass of**: [ControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/ControllingParty.md)

## Constraints

- **[nominates](/concepts/fibo/BE/OwnershipAndControl/Executives/nominates.md)**: min qualified cardinality 0 of type [BoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/BoardMember.md)
- **[isControllingPartyIn](/concepts/fibo/FND/OwnershipAndControl/Control/isControllingPartyIn.md)**: some values from of type [DeFactoControl](/concepts/fibo/FND/OwnershipAndControl/Control/DeFactoControl.md)

## Annotations

- **label**: de facto controlling interest party
- **definition**: party that exercises some control over an entity other than via explicit, legal means
- **example**: a silent partner, i.e. where someone has made a large investment, which is bilateral (not part of the constitutional framework of the company)
- **scopeNote**: divides further into financial leverage via loans; non fiscal types of leverage (influence)
- **explanatoryNote**: A control owner (i.e., control person, per SEC regulations) may have some means or right that allows them to exercise control over board composition, other than through proxy assignment or vote. Not all control persons have this facility, as it is not inherent to having a significant (for example, 20 percent or more) ownership stake.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

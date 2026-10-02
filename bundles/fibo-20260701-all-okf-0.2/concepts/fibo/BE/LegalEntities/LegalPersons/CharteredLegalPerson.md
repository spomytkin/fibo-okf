---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: chartered legal person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a legal person created by a royal charter or decree
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Anything with 'Royal Institute' in the name. Also universities are generally set up by royal charter in a monarchy
      or principality, (often pre-dating any Privy Council i.e. directly be the monarch in the case of older universities).
      The Bank of England and the British Broadcasting Council (BBC) are also incorporated through Royal Charter.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In a monarchy or principality, the monarch typically vests the power to create such bodies, in an entity called
      (for example) the Privy Council.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/CharteredLegalPerson
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: chartered legal person
type: Ontology Class
---

# chartered legal person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/CharteredLegalPerson>

## Definition

a legal person created by a royal charter or decree

## Relationships

- **Subclass of**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)

## Annotations

- **label**: chartered legal person
- **definition**: a legal person created by a royal charter or decree
- **example**: Anything with 'Royal Institute' in the name. Also universities are generally set up by royal charter in a monarchy or principality, (often pre-dating any Privy Council i.e. directly be the monarch in the case of older universities). The Bank of England and the British Broadcasting Council (BBC) are also incorporated through Royal Charter.
- **explanatoryNote**: In a monarchy or principality, the monarch typically vests the power to create such bodies, in an entity called (for example) the Privy Council.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

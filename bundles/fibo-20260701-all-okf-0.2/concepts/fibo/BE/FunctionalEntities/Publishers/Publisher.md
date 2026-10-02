---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: publisher
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: role of person(s) or organization(s) responsible for the printing or distribution of an item, whether in digital
      or print (physical) form
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 'ISO 10161-1:2014(en), Information and documentation - Open Systems Interconnection - Interlibrary Loan Application
      Protocol Specification - Part 1: Protocol specification'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Publishers may also include banks, government agencies and the like.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/Party
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher
sources:
- id: fibo-source-c08bba6665
  resource: references/fibo/BE/FunctionalEntities/Publishers.rdf
  sha256: c08bba6665f5e8fa0f777c7625413d35aa10a63353e739c085127bbbe73c5d28
  title: FIBO source BE/FunctionalEntities/Publishers.rdf
title: publisher
type: Ontology Class
---

# publisher

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/Publishers/Publisher>

## Definition

role of person(s) or organization(s) responsible for the printing or distribution of an item, whether in digital or print (physical) form

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: min qualified cardinality 0 of type [Party](<https://www.omg.org/spec/Commons/PartiesAndSituations/Party>)

## Annotations

- **label**: publisher
- **definition**: role of person(s) or organization(s) responsible for the printing or distribution of an item, whether in digital or print (physical) form
- **adaptedFrom**: ISO 10161-1:2014(en), Information and documentation - Open Systems Interconnection - Interlibrary Loan Application Protocol Specification - Part 1: Protocol specification
- **explanatoryNote**: Publishers may also include banks, government agencies and the like.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: birth certificate identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier associated with a vital record documenting the birth of a child
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: birth certificate number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificate
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentifier
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: birth certificate identifier
type: Ontology Class
---

# birth certificate identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentifier>

## Definition

identifier associated with a vital record documenting the birth of a child

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [BirthCertificateIdentificationScheme](/concepts/fibo/FND/AgentsAndPeople/People/BirthCertificateIdentificationScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [BirthCertificate](/concepts/fibo/FND/AgentsAndPeople/People/BirthCertificate.md)

## Annotations

- **label**: birth certificate identifier
- **definition**: identifier associated with a vital record documenting the birth of a child
- **synonym**: birth certificate number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

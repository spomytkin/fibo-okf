---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has legal address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the legal address for the entity, in the jurisdiction in which the entity is established, used for registration
      purposes with respect to obtaining an LEI
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  domain:
  - predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://www.omg.org/spec/Commons/Organizations/LegalEntity
  range:
  - concept: /concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: has legal address
type: Ontology Property
---

# has legal address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalAddress>

## Definition

indicates the legal address for the entity, in the jurisdiction in which the entity is established, used for registration purposes with respect to obtaining an LEI

## Relationships

- **Domain**: [LegalEntity](<https://www.omg.org/spec/Commons/Organizations/LegalEntity>)
- **Range**: [ConventionalStreetAddress](/concepts/fibo/FND/Places/Addresses/ConventionalStreetAddress.md)
- **Subproperty of**: [hasRegisteredAddress](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/hasRegisteredAddress.md)

## Annotations

- **label**: has legal address
- **definition**: indicates the legal address for the entity, in the jurisdiction in which the entity is established, used for registration purposes with respect to obtaining an LEI
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: business license
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: license that allows the holder to conduct business or carry out a specific profession within some jurisdiction
      for some period of time
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isRecognizedIn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/License.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessLicense
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: business license
type: Ontology Class
---

# business license

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessLicense>

## Definition

license that allows the holder to conduct business or carry out a specific profession within some jurisdiction for some period of time

## Relationships

- **Subclass of**: [License](/concepts/fibo/FND/Law/LegalCapacity/License.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: exact qualified cardinality 1 of type [BusinessEntity](/concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- **[isRecognizedIn](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isRecognizedIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: business license
- **definition**: license that allows the holder to conduct business or carry out a specific profession within some jurisdiction for some period of time

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

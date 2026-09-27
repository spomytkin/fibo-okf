---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: relationship record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a record describing relationships between legal entities
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/isQuantifiedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipQualifier
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isQualifiedBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Documents/records
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Collections/Constituent
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipRecord
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: relationship record
type: Ontology Class
---

# relationship record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipRecord>

## Definition

a record describing relationships between legal entities

## Relationships

- **Subclass of**: [Constituent](<https://www.omg.org/spec/Commons/Collections/Constituent>)

## Constraints

- **[isQuantifiedBy](/concepts/fibo/BE/LegalEntities/LEIEntities/isQuantifiedBy.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[isQualifiedBy](/concepts/fibo/FND/Agreements/Contracts/isQualifiedBy.md)**: min qualified cardinality 0 of type [RelationshipQualifier](/concepts/fibo/BE/LegalEntities/LEIEntities/RelationshipQualifier.md)
- **[records](<https://www.omg.org/spec/Commons/Documents/records>)**: exact qualified cardinality 1 of type [EntityOwnership](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwnership.md)

## Annotations

- **label**: relationship record
- **definition**: a record describing relationships between legal entities
- **adaptedFrom**: GLEIF Level 2 Relationship Record (RR) Common Data Format (CDF), see https://www.gleif.org/en/about-lei/common-data-file-format/relationship-record-cdf-format#

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

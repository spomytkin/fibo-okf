---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity ownership
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: ownership by some party of an interest in some non-governmental formal organization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasOwnershipPercentage
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity
    value: Nc4476581fc5b41aaaf1f70040df2786f
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipQualifier
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isQualifiedBy
  - cardinality: 0
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/RelationshipStatus
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Ownership
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership
sources:
- id: fibo-source-2b91fda366
  resource: references/fibo/BE/OwnershipAndControl/OwnershipParties.rdf
  sha256: 2b91fda366d3f3c717a0ba0367d0a26920e3e046b78d354a395c83e1fd36ba52
  title: FIBO source BE/OwnershipAndControl/OwnershipParties.rdf
title: entity ownership
type: Ontology Class
---

# entity ownership

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwnership>

## Definition

ownership by some party of an interest in some non-governmental formal organization

## Relationships

- **Subclass of**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership/Ownership.md)

## Constraints

- **[hasOwnershipPercentage](/concepts/fibo/BE/LegalEntities/LEIEntities/hasOwnershipPercentage.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasOwnedEntity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasOwnedEntity.md)**: some values from value `Nc4476581fc5b41aaaf1f70040df2786f`
- **[hasOwningEntity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasOwningEntity.md)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **[isQualifiedBy](/concepts/fibo/FND/Agreements/Contracts/isQualifiedBy.md)**: min qualified cardinality 0 of type [RelationshipQualifier](/concepts/fibo/BE/LegalEntities/LEIEntities/RelationshipQualifier.md)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: min qualified cardinality 0
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: exact qualified cardinality 1 of type [RelationshipStatus](/concepts/fibo/BE/LegalEntities/LEIEntities/RelationshipStatus.md)

## Annotations

- **label**: entity ownership
- **definition**: ownership by some party of an interest in some non-governmental formal organization

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

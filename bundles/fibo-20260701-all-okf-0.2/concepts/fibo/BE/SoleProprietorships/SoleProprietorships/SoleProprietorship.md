---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sole proprietorship
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: unincorporated business owned by a single person
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LiabilityCapacity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasCapacity
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/BusinessEntity
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/LegalPerson
resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship
sources:
- id: fibo-source-84f58ed741
  resource: references/fibo/BE/SoleProprietorships/SoleProprietorships.rdf
  sha256: 84f58ed7419a3ea2c8e26947f96d11a0b14f06c5725024cf16ab63a68ce3c4ac
  title: FIBO source BE/SoleProprietorships/SoleProprietorships.rdf
title: sole proprietorship
type: Ontology Class
---

# sole proprietorship

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship>

## Definition

unincorporated business owned by a single person

## Relationships

- **Subclass of**: [BusinessEntity](/concepts/fibo/BE/LegalEntities/LegalPersons/BusinessEntity.md)
- **Subclass of**: [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Constraints

- **[hasCapacity](/concepts/fibo/FND/Law/LegalCapacity/hasCapacity.md)**: some values from of type [LiabilityCapacity](/concepts/fibo/FND/Law/LegalCapacity/LiabilityCapacity.md)
- **[isOwnedAndControlledBy](/concepts/fibo/FND/OwnershipAndControl/OwnershipAndControl/isOwnedAndControlledBy.md)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: sole proprietorship
- **definition**: unincorporated business owned by a single person

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

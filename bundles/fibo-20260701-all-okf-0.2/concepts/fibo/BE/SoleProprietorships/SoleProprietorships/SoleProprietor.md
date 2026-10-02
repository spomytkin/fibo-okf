---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sole proprietor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns a business, has the rights to all profits from that business and is considered a single entity
      (unincorporated) together with that business for tax and liability purposes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A sole proprietor has unlimited liability with respect to any business debts.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: sole owner
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: sole trader
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/hasInvestmentEntity
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N8bd3c89c949c4b3db43e5a1a43a416c9
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/EntityOwner
resource: https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietor
sources:
- id: fibo-source-84f58ed741
  resource: references/fibo/BE/SoleProprietorships/SoleProprietorships.rdf
  sha256: 84f58ed7419a3ea2c8e26947f96d11a0b14f06c5725024cf16ab63a68ce3c4ac
  title: FIBO source BE/SoleProprietorships/SoleProprietorships.rdf
title: sole proprietor
type: Ontology Class
---

# sole proprietor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/SoleProprietorships/SoleProprietorships/SoleProprietor>

## Definition

party that owns a business, has the rights to all profits from that business and is considered a single entity (unincorporated) together with that business for tax and liability purposes

## Relationships

- **Subclass of**: [EntityOwner](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/EntityOwner.md)

## Constraints

- **[hasInvestmentEntity](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/hasInvestmentEntity.md)**: some values from of type [SoleProprietorship](/concepts/fibo/BE/SoleProprietorships/SoleProprietorships/SoleProprietorship.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: exact qualified cardinality 1 of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N8bd3c89c949c4b3db43e5a1a43a416c9`

## Annotations

- **label**: sole proprietor
- **definition**: party that owns a business, has the rights to all profits from that business and is considered a single entity (unincorporated) together with that business for tax and liability purposes
- **explanatoryNote**: A sole proprietor has unlimited liability with respect to any business debts.
- **synonym**: sole owner
- **synonym**: sole trader

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

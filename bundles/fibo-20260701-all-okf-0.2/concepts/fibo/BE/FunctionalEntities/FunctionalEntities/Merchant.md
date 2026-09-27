---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: merchant
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party engaged in the purchase and sales of goods produced by others for profit
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantIdentifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Merchant
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: merchant
type: Ontology Class
---

# merchant

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/Merchant>

## Definition

party engaged in the purchase and sales of goods produced by others for profit

## Relationships

- **Subclass of**: [FunctionalBusinessEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [MerchantCategoryCode](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: some values from of type [MerchantIdentifier](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/MerchantIdentifier.md)

## Annotations

- **label**: merchant
- **definition**: party engaged in the purchase and sales of goods produced by others for profit

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

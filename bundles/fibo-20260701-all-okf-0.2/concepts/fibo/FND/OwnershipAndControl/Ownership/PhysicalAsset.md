---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: physical asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: tangible asset that has a material form, such as property, equipment, and inventory
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Physical (tangible) assets are real items of value that are used to generate revenue for a company.
  disjoint_with:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/TangibleAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/TangibleAsset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/PhysicalAsset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: physical asset
type: Ontology Class
---

# physical asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/PhysicalAsset>

## Definition

tangible asset that has a material form, such as property, equipment, and inventory

## Relationships

- **Subclass of**: [TangibleAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/TangibleAsset.md)

## Constraints

- **Disjoint with**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Annotations

- **label**: physical asset
- **definition**: tangible asset that has a material form, such as property, equipment, and inventory
- **explanatoryNote**: Physical (tangible) assets are real items of value that are used to generate revenue for a company.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

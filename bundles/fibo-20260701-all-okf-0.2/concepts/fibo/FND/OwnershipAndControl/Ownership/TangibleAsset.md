---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tangible asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: asset that is a physical, measurable resource, i.e., one that takes a physical form
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Tangible assets include cash, cash equivalents and accounts receivables (AR), inventory, equipment, buildings and
      real estate, crops, and investments. Tangible assets such as art, furniture, stamps, gold, wine, toys and books of significant
      value may be included in an individual or organization's asset portfolio.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/TangibleAsset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: tangible asset
type: Ontology Class
---

# tangible asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/TangibleAsset>

## Definition

asset that is a physical, measurable resource, i.e., one that takes a physical form

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Annotations

- **label**: tangible asset
- **definition**: asset that is a physical, measurable resource, i.e., one that takes a physical form
- **explanatoryNote**: Tangible assets include cash, cash equivalents and accounts receivables (AR), inventory, equipment, buildings and real estate, crops, and investments. Tangible assets such as art, furniture, stamps, gold, wine, toys and books of significant value may be included in an individual or organization's asset portfolio.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

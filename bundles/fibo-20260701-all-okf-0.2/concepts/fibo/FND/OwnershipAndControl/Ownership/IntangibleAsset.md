---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: intangible asset
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifiable, non-monetary asset that lacks physical substance
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Intangible assets may include intellectual property, patents, copyrights, trademarks, rights-of-way (easements),
      brands, organizational abilities (know-how), and data.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Intangible assets include assets that may involve a legal claim to some future benefit, typically a claim to future
      cash. Intangible assets have become an increasingly larger component of the valuation for all companies, from newer
      social media companies to even the most established and iconic manufacturers.
  disjoint_with:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/TangibleAsset.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/TangibleAsset
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/IntangibleAsset
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: intangible asset
type: Ontology Class
---

# intangible asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/IntangibleAsset>

## Definition

identifiable, non-monetary asset that lacks physical substance

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Constraints

- **Disjoint with**: [TangibleAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/TangibleAsset.md)

## Annotations

- **label**: intangible asset
- **definition**: identifiable, non-monetary asset that lacks physical substance
- **example**: Intangible assets may include intellectual property, patents, copyrights, trademarks, rights-of-way (easements), brands, organizational abilities (know-how), and data.
- **explanatoryNote**: Intangible assets include assets that may involve a legal claim to some future benefit, typically a claim to future cash. Intangible assets have become an increasingly larger component of the valuation for all companies, from newer social media companies to even the most established and iconic manufacturers.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

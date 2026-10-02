---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: holding
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: owned financial interest consisting of legal or beneficial ownership of an asset or security that confers economic
      rights on its owner
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that there is no common, broadly accepted definition of the term holding across regulators, either within
      a single country such as the US, or across national jurisdictions. Typically, a holding may refer to a single asset,
      such as a piece of real estate, a portfolio of assets, multiple portfolios, and so forth, and may be aggregated over
      multiple assets.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/hasFractionalInterest
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Asset
resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Holding
sources:
- id: fibo-source-de57f166a6
  resource: references/fibo/FND/OwnershipAndControl/Ownership.rdf
  sha256: de57f166a681de4546904cb9a49d26917586e61cebb91ca017cc3bda8df3a305
  title: FIBO source FND/OwnershipAndControl/Ownership.rdf
title: holding
type: Ontology Class
---

# holding

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/Holding>

## Definition

owned financial interest consisting of legal or beneficial ownership of an asset or security that confers economic rights on its owner

## Relationships

- **Subclass of**: [Asset](/concepts/fibo/FND/OwnershipAndControl/Ownership/Asset.md)

## Constraints

- **[hasFractionalInterest](/concepts/fibo/FND/Law/LegalCapacity/hasFractionalInterest.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: holding
- **definition**: owned financial interest consisting of legal or beneficial ownership of an asset or security that confers economic rights on its owner
- **explanatoryNote**: Note that there is no common, broadly accepted definition of the term holding across regulators, either within a single country such as the US, or across national jurisdictions. Typically, a holding may refer to a single asset, such as a piece of real estate, a portfolio of assets, multiple portfolios, and so forth, and may be aggregated over multiple assets.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

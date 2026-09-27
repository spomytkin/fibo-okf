---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has merchant category description
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: provides a text description of the sector to which the code applies
  domain:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/hasMerchantCategoryDescription
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: has merchant category description
type: Ontology Property
---

# has merchant category description

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/hasMerchantCategoryDescription>

## Definition

provides a text description of the sector to which the code applies

## Relationships

- **Domain**: [MerchantCategoryCode](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: has merchant category description
- **definition**: provides a text description of the sector to which the code applies

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

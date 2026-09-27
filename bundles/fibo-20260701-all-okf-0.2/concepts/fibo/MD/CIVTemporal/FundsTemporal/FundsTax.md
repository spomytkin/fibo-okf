---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: funds tax
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/FundsTax
sources:
- id: fibo-source-6355d85024
  resource: references/fibo/MD/CIVTemporal/FundsTemporal.rdf
  sha256: 6355d85024e646fcee8b117a329d3c2307126ca0c3e3721b62ec12813bf12817
  title: FIBO source MD/CIVTemporal/FundsTemporal.rdf
title: funds tax
type: Ontology Class
---

# funds tax

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/FundsTax>

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)

## Annotations

- **label** (en): funds tax

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

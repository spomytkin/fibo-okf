---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: incurs tax
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/OwnershipParties/Investor
  range:
  - concept: /concepts/fibo/MD/CIVTemporal/FundsTemporal/FundsTax.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/FundsTax
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/incursTax
sources:
- id: fibo-source-6355d85024
  resource: references/fibo/MD/CIVTemporal/FundsTemporal.rdf
  sha256: 6355d85024e646fcee8b117a329d3c2307126ca0c3e3721b62ec12813bf12817
  title: FIBO source MD/CIVTemporal/FundsTemporal.rdf
title: incurs tax
type: Ontology Property
---

# incurs tax

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/FundsTemporal/incursTax>

## Relationships

- **Domain**: [Investor](/concepts/fibo/BE/OwnershipAndControl/OwnershipParties/Investor.md)
- **Range**: [FundsTax](/concepts/fibo/MD/CIVTemporal/FundsTemporal/FundsTax.md)

## Annotations

- **label** (en): incurs tax

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sale method
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Sale Method of the security.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/MuniDebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/MuniDebtOffering
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#string
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/saleMethod
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: sale method
type: Ontology Property
---

# sale method

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/saleMethod>

## Definition

Sale Method of the security.

## Relationships

- **Domain**: [MuniDebtOffering](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/MuniDebtOffering.md)
- **Range**: [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label** (en): sale method
- **definition** (en): Sale Method of the security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: over allotment available
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Whether an over-allotment option is available for the security.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/overAllotmentAvailable
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: over allotment available
type: Ontology Property
---

# over allotment available

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/overAllotmentAvailable>

## Definition

Whether an over-allotment option is available for the security.

## Relationships

- **Domain**: [IssueOverAllotmentTerms](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): over allotment available
- **definition** (en): Whether an over-allotment option is available for the security.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

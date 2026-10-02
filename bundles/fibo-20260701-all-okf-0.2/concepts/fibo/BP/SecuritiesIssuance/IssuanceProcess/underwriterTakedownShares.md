---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: underwriter takedown shares
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Takedown quantity of the security handled by the underwriter (that will be brought into DTC).
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#integer
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/underwriterTakedownShares
sources:
- id: fibo-source-fa20b53ed2
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceProcess.rdf
  sha256: fa20b53ed283631237b4ff106a6a421d47c8e9bcb760277569287fb0cabdce1f
  title: FIBO source BP/SecuritiesIssuance/IssuanceProcess.rdf
title: underwriter takedown shares
type: Ontology Property
---

# underwriter takedown shares

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/underwriterTakedownShares>

## Definition

Takedown quantity of the security handled by the underwriter (that will be brought into DTC).

## Relationships

- **Domain**: [UnderwriterTakedown](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/UnderwriterTakedown.md)
- **Range**: [integer](<http://www.w3.org/2001/XMLSchema#integer>)

## Annotations

- **label** (en): underwriter takedown shares
- **definition** (en): Takedown quantity of the security handled by the underwriter (that will be brought into DTC).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

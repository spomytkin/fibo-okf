---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: issuance closing
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The process of crediting the DTC participant account on settlement date with the position for the new issue. The
      overall closing process includes the exchange of funds that happens outside of DTC.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuanceClosing
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: issuance closing
type: Ontology Class
---

# issuance closing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssuanceClosing>

## Definition

The process of crediting the DTC participant account on settlement date with the position for the new issue. The overall closing process includes the exchange of funds that happens outside of DTC.

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/IssuanceProcessActivity.md)

## Annotations

- **label** (en): issuance closing
- **definition** (en): The process of crediting the DTC participant account on settlement date with the position for the new issue. The overall closing process includes the exchange of funds that happens outside of DTC.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

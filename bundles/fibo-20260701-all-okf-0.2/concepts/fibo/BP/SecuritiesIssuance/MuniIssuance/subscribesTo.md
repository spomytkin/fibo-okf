---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: subscribes to
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Subscriber responds to marketing / draft propspectus, indicates interest and is allocated shares / debt units based
      on interest.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/Subscriber
  range:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/subscribesTo
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: subscribes to
type: Ontology Property
---

# subscribes to

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/subscribesTo>

## Definition

Subscriber responds to marketing / draft propspectus, indicates interest and is allocated shares / debt units based on interest.

## Relationships

- **Domain**: [Subscriber](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/Subscriber.md)
- **Range**: [SecuritiesUnderwritingIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)

## Annotations

- **label** (en): subscribes to
- **definition** (en): Subscriber responds to marketing / draft propspectus, indicates interest and is allocated shares / debt units based on interest.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

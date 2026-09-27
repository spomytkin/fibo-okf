---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: numbering agency
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The agency which will provide the primary securitiy identifier for the security. Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/AllocatePrimaryIdentifier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/AgencyMBSIssuance/allocatesIdentifier
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AllocatePrimaryIdentifier
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/allocatesIdentifier
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/NumberingAgency
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: numbering agency
type: Ontology Class
---

# numbering agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/NumberingAgency>

## Definition

The agency which will provide the primary securitiy identifier for the security. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [SecuritiesIssuanceProcessActor](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcessActor.md)

## Constraints

- **[allocatesIdentifier](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/allocatesIdentifier.md)**: some values from of type [AllocatePrimaryIdentifier](/concepts/fibo/BP/SecuritiesIssuance/AgencyMBSIssuance/AllocatePrimaryIdentifier.md)
- **[allocatesIdentifier](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/allocatesIdentifier.md)**: some values from of type [AllocatePrimaryIdentifier](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/AllocatePrimaryIdentifier.md)

## Annotations

- **label** (en): numbering agency
- **definition** (en): The agency which will provide the primary securitiy identifier for the security. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

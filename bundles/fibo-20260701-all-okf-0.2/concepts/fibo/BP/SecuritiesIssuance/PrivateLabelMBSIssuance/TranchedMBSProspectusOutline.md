---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranched m b s prospectus outline
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An outline of the tranched prospectus, provind an intial representation of the possible tranches and their features.
      Term origin:MBS PoC Reviews
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/DraftTrancheTermsheet
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasContent.1
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSProspectusOutline
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: tranched m b s prospectus outline
type: Ontology Class
---

# tranched m b s prospectus outline

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSProspectusOutline>

## Definition

An outline of the tranched prospectus, provind an intial representation of the possible tranches and their features. Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [PreliminaryProspectus](/concepts/fibo/BP/SecuritiesIssuance/IssuanceDocuments/PreliminaryProspectus.md)

## Constraints

- **[hasContent.1](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/hasContent.1.md)**: some values from of type [DraftTrancheTermsheet](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/DraftTrancheTermsheet.md)

## Annotations

- **label** (en): tranched m b s prospectus outline
- **definition** (en): An outline of the tranched prospectus, provind an intial representation of the possible tranches and their features. Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: identify underwriter
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PotentialTranchedIssueUnderwriter
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/resultsIn
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IdentifyUnderwriter
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: identify underwriter
type: Ontology Class
---

# identify underwriter

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/IdentifyUnderwriter>

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)

## Constraints

- **[resultsIn](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/resultsIn.md)**: some values from of type [PotentialTranchedIssueUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/PotentialTranchedIssueUnderwriter.md)

## Annotations

- **label** (en): identify underwriter

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

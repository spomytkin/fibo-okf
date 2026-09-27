---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dissemination underwriter
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/Dissemination
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/makesDecisionOn
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DisseminationUnderwriter
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: dissemination underwriter
type: Ontology Class
---

# dissemination underwriter

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DisseminationUnderwriter>

## Relationships

- **Subclass of**: [PotentialMuniUnderwriter](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/PotentialMuniUnderwriter.md)

## Constraints

- **[makesDecisionOn](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/makesDecisionOn.md)**: some values from of type [Dissemination](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/Dissemination.md)

## Annotations

- **label** (en): dissemination underwriter

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

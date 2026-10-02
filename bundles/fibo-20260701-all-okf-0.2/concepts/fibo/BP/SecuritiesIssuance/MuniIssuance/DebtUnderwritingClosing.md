---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt underwriting closing
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/UnderwriterTakedownForDebt
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/refersTo
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceClosing.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceClosing
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DebtUnderwritingClosing
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: debt underwriting closing
type: Ontology Class
---

# debt underwriting closing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DebtUnderwritingClosing>

## Relationships

- **Subclass of**: [UnderwritingIssuanceClosing](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/UnderwritingIssuanceClosing.md)

## Constraints

- **[refersTo](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/refersTo.md)**: some values from of type [UnderwriterTakedownForDebt](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/UnderwriterTakedownForDebt.md)

## Annotations

- **label** (en): debt underwriting closing

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

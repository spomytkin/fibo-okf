---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: asset pool creation process
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtSecuritizationProcess
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/DatesAndTimes/precedes
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: asset pool creation process
type: Ontology Class
---

# asset pool creation process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/AssetPoolCreationProcess>

## Constraints

- **[precedes](<https://www.omg.org/spec/Commons/DatesAndTimes/precedes>)**: some values from of type [DebtSecuritizationProcess](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/DebtSecuritizationProcess.md)

## Annotations

- **label** (en): asset pool creation process

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

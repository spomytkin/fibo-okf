---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt issuance process information
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: information specific to the issuance of a debt security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtIssuancePurpose
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/hasDebtIssuancePurpose
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtIssuanceProcessInformation
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: debt issuance process information
type: Ontology Class
---

# debt issuance process information

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtIssuanceProcessInformation>

## Definition

information specific to the issuance of a debt security

## Relationships

- **Subclass of**: [TradedInstrumentIssuanceProcessInformation](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/TradedInstrumentIssuanceProcessInformation.md)

## Constraints

- **[hasDebtIssuancePurpose](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/hasDebtIssuancePurpose.md)**: some values from of type [DebtIssuancePurpose](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/DebtIssuancePurpose.md)

## Annotations

- **label** (en): debt issuance process information
- **definition** (en): information specific to the issuance of a debt security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

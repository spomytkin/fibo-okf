---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: securities underwriting issuance
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Underwriting, as a method of Securities Issuance.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesIssuanceContext.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesIssuanceContext
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuance
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: securities underwriting issuance
type: Ontology Class
---

# securities underwriting issuance

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuance>

## Definition

Underwriting, as a method of Securities Issuance.

## Relationships

- **Subclass of**: [SecuritiesIssuanceContext](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesIssuanceContext.md)

## Constraints

- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label** (en): securities underwriting issuance
- **definition** (en): Underwriting, as a method of Securities Issuance.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

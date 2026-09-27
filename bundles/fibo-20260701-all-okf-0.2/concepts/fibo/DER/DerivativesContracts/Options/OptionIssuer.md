---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: option issuer
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: issuer granting the rights defined in the option in exchange for some consideration
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N1956c9f13e3d493ab160c717ea1a6687
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Issuer
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionIssuer
sources:
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: option issuer
type: Ontology Class
---

# option issuer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Options/OptionIssuer>

## Definition

issuer granting the rights defined in the option in exchange for some consideration

## Relationships

- **Subclass of**: [Issuer](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Issuer.md)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N1956c9f13e3d493ab160c717ea1a6687`

## Annotations

- **label** (en): option issuer
- **definition** (en): issuer granting the rights defined in the option in exchange for some consideration

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

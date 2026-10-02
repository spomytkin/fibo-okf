---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt securities market maker
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An actor which has the role of Market Maker in a given market.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/determinesMarketPriceForDebt
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: debt securities market maker
type: Ontology Class
---

# debt securities market maker

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtSecuritiesMarketMaker>

## Definition

An actor which has the role of Market Maker in a given market.

## Relationships

- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Constraints

- **[determinesMarketPriceForDebt](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/determinesMarketPriceForDebt.md)**: some values from of type [OTCBondMarketPrice](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/OTCBondMarketPrice.md)

## Annotations

- **label** (en): debt securities market maker
- **definition** (en): An actor which has the role of Market Maker in a given market.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

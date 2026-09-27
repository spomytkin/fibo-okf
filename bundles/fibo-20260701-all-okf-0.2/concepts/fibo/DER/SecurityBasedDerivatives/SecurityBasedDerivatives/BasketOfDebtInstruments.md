---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket of debt instruments
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of securities whose constituents are debt instruments
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: Nd25cb6c3297a43a381556013956257e7
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Baskets/BasketOfSecurities.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Baskets/BasketOfSecurities
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: basket of debt instruments
type: Ontology Class
---

# basket of debt instruments

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments>

## Definition

basket of securities whose constituents are debt instruments

## Relationships

- **Subclass of**: [BasketOfSecurities](/concepts/fibo/SEC/Securities/Baskets/BasketOfSecurities.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `Nd25cb6c3297a43a381556013956257e7`

## Annotations

- **label** (en): basket of debt instruments
- **definition** (en): basket of securities whose constituents are debt instruments

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

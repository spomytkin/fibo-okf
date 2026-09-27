---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: local lines of credit debt basket
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: basket of debt instruments that may be relevant for companies with international operations, often permitting debt
      to be incurred by a non-guarantor restricted subsidiary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
    value: N32a2a53161734a629a98239bcdc971d4
  subclass_of:
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments
resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/LocalLinesOfCreditDebtBasket
sources:
- id: fibo-source-e409c614fa
  resource: references/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
  sha256: e409c614fa05cf3a92ef2ffb652008525612be13fc2347acd6b082fe0f4dc330
  title: FIBO source DER/SecurityBasedDerivatives/SecurityBasedDerivatives.rdf
title: local lines of credit debt basket
type: Ontology Class
---

# local lines of credit debt basket

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/LocalLinesOfCreditDebtBasket>

## Definition

basket of debt instruments that may be relevant for companies with international operations, often permitting debt to be incurred by a non-guarantor restricted subsidiary

## Relationships

- **Subclass of**: [BasketOfDebtInstruments](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/BasketOfDebtInstruments.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from value `N32a2a53161734a629a98239bcdc971d4`

## Annotations

- **label** (en): local lines of credit debt basket
- **definition** (en): basket of debt instruments that may be relevant for companies with international operations, often permitting debt to be incurred by a non-guarantor restricted subsidiary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

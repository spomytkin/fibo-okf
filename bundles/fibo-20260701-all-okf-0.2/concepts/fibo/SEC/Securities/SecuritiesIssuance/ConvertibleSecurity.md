---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: convertible security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security that can be converted into another security
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Convertible securities may be convertible bonds or preferred stocks that pay regular interest and can be converted
      into shares of common stock (sometimes conditioned on the stock price appreciating to a predetermined level).
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Warrants are equity convertible securities. They give the owner the option to buy newly issued shares at a determined
      exercise price and date.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConversionTerms
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasContractualElement
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: convertible security
type: Ontology Class
---

# convertible security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/ConvertibleSecurity>

## Definition

security that can be converted into another security

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Constraints

- **[hasContractualElement](/concepts/fibo/FND/Agreements/Contracts/hasContractualElement.md)**: some values from of type [ConversionTerms](/concepts/fibo/SEC/Securities/SecuritiesIssuance/ConversionTerms.md)

## Annotations

- **label**: convertible security
- **definition**: security that can be converted into another security
- **example**: Convertible securities may be convertible bonds or preferred stocks that pay regular interest and can be converted into shares of common stock (sometimes conditioned on the stock price appreciating to a predetermined level).
- **example**: Warrants are equity convertible securities. They give the owner the option to buy newly issued shares at a determined exercise price and date.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

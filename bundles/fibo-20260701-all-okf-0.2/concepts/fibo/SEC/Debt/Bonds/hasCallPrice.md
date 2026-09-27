---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has call price
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the amount of the call on the specified call date, typically the sum of par value and the call premium,
      as specified in the contract
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This is the price a bond issuer or preferred stock issuer must pay investors to buy back, or call, all or part
      of an issue before the maturity date.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: has redemption price
  domain:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/CallFeature
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryPrice
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasPrice
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasCallPrice
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: has call price
type: Ontology Property
---

# has call price

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/hasCallPrice>

## Definition

indicates the amount of the call on the specified call date, typically the sum of par value and the call premium, as specified in the contract

## Relationships

- **Domain**: [CallFeature](/concepts/fibo/SEC/Debt/DebtInstruments/CallFeature.md)
- **Range**: [MonetaryPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryPrice.md)
- **Subproperty of**: [hasPrice](/concepts/fibo/FND/Accounting/CurrencyAmount/hasPrice.md)

## Annotations

- **label**: has call price
- **definition**: indicates the amount of the call on the specified call date, typically the sum of par value and the call premium, as specified in the contract
- **explanatoryNote**: This is the price a bond issuer or preferred stock issuer must pay investors to buy back, or call, all or part of an issue before the maturity date.
- **synonym**: has redemption price

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

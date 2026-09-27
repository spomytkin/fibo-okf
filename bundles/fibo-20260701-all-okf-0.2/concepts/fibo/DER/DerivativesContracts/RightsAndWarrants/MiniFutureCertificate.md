---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mini-future certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making
      leverage available without a term restriction, and whose payoff depends on whether or not the underlying asset has reached
      or exceeded a predetermined price
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The price of a mini-future always corresponds to its intrinsic value, i.e. the capital outlay, plus the bid-ask
      spread. The financing costs associated with building up the leverage effect are offset against the capital outlay on
      a daily basis, thereby eliminating the need for a premium. Investors have to pay only financing costs they actually
      utilize. In contrast to options, factors like volatility have no influence at all on the price of mini-futures.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/ExoticOptions/BarrierOption
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Entitlement
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/MiniFutureCertificate
sources:
- id: fibo-source-a0aea9b36b
  resource: references/fibo/DER/DerivativesContracts/RightsAndWarrants.rdf
  sha256: a0aea9b36bb60a086c8893ea282e5892663626e9fa136bc320592582d9e598d5
  title: FIBO source DER/DerivativesContracts/RightsAndWarrants.rdf
title: mini-future certificate
type: Ontology Class
---

# mini-future certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/RightsAndWarrants/MiniFutureCertificate>

## Definition

entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making leverage available without a term restriction, and whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price

## Relationships

- **Subclass of**: [BarrierOption](/concepts/fibo/DER/DerivativesContracts/ExoticOptions/BarrierOption.md)
- **Subclass of**: [SecurityBasedDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md)
- **Subclass of**: [Entitlement](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Entitlement.md)

## Annotations

- **label** (en): mini-future certificate
- **definition** (en): entitlement that combines the structure of an open-end certificate with a leverage option with no fixed term, making leverage available without a term restriction, and whose payoff depends on whether or not the underlying asset has reached or exceeded a predetermined price
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): The price of a mini-future always corresponds to its intrinsic value, i.e. the capital outlay, plus the bid-ask spread. The financing costs associated with building up the leverage effect are offset against the capital outlay on a daily basis, thereby eliminating the need for a premium. Investors have to pay only financing costs they actually utilize. In contrast to options, factors like volatility have no influence at all on the price of mini-futures.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: forward
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: derivative instrument that is privately negotiated between parties to buy the underlier at a specified future date
      at the price specified in the contract
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth
      Edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Certain contracts labeled 'forwards', such as London Metal Exchange (LME) Forwards, are actually futures and are
      exchange-traded. Some power and gas markets, such as Nord Pool, trade electricity forwards with clearinghouse support.
      Per the ontology, both would be classified as futures by definition, but naming blurs the lines.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Since forward contracts are not exchange traded, there is no mark-to-market requirement, which allows a buyer to
      avoid almost all capital outflow initially (though some counterparties might set collateral requirements). The forward
      price makes the forward contract have no value when the contract is written. However, if the value of the underlying
      commodity changes, the value of the forward contract becomes positive or negative, depending on the position held. Forwards
      are priced in a manner similar to futures. Like in the case of a futures contract, the first step in pricing a forward
      is to add the spot price to the cost of carry (interest forgone, convenience yield, storage costs and interest/dividend
      received on the underlying). Unlike a futures contract though, the price may also include a premium for counterparty
      credit risk, and the fact that there is not daily marking to market process to minimize default risk. If there is no
      allowance for these credit risks, then the forward price will equal the futures price.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The primary distinctions between futures and forwards are (1) forwards are bilateral and privately negotiated,
      (2) forwards are over-the-counter instruments rather than exchange traded, (3) forwards are fully customizable whereas
      futures are typically standardized, (4) the risk associated with a forward is assumed by the counterparties whereas
      it is mitigated via central clearing for futures, and (5) there is typically no margin requirement for a forward whereas
      futures require margin posting.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: forward contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward
sources:
- id: fibo-source-4932191e9c
  resource: references/fibo/DER/DerivativesContracts/FuturesAndForwards.rdf
  sha256: 4932191e9cdfb6ce62af4c9077f0e5e184cf60c8a969d4a7166b65bf658bce7f
  title: FIBO source DER/DerivativesContracts/FuturesAndForwards.rdf
title: forward
type: Ontology Class
---

# forward

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/FuturesAndForwards/Forward>

## Definition

derivative instrument that is privately negotiated between parties to buy the underlier at a specified future date at the price specified in the contract

## Relationships

- **Subclass of**: [OverTheCounterDerivativeInstrument](/concepts/fibo/DER/DerivativesContracts/DerivativesBasics/OverTheCounterDerivativeInstrument.md)
- **Subclass of**: [DerivativeInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DerivativeInstrument.md)

## Annotations

- **label** (en): forward
- **definition** (en): derivative instrument that is privately negotiated between parties to buy the underlier at a specified future date at the price specified in the contract
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth Edition, October 2019
- **explanatoryNote** (en): Certain contracts labeled 'forwards', such as London Metal Exchange (LME) Forwards, are actually futures and are exchange-traded. Some power and gas markets, such as Nord Pool, trade electricity forwards with clearinghouse support. Per the ontology, both would be classified as futures by definition, but naming blurs the lines.
- **explanatoryNote** (en): Since forward contracts are not exchange traded, there is no mark-to-market requirement, which allows a buyer to avoid almost all capital outflow initially (though some counterparties might set collateral requirements). The forward price makes the forward contract have no value when the contract is written. However, if the value of the underlying commodity changes, the value of the forward contract becomes positive or negative, depending on the position held. Forwards are priced in a manner similar to futures. Like in the case of a futures contract, the first step in pricing a forward is to add the spot price to the cost of carry (interest forgone, convenience yield, storage costs and interest/dividend received on the underlying). Unlike a futures contract though, the price may also include a premium for counterparty credit risk, and the fact that there is not daily marking to market process to minimize default risk. If there is no allowance for these credit risks, then the forward price will equal the futures price.
- **explanatoryNote** (en): The primary distinctions between futures and forwards are (1) forwards are bilateral and privately negotiated, (2) forwards are over-the-counter instruments rather than exchange traded, (3) forwards are fully customizable whereas futures are typically standardized, (4) the risk associated with a forward is assumed by the counterparties whereas it is mitigated via central clearing for futures, and (5) there is typically no margin requirement for a forward whereas futures require margin posting.
- **synonym** (en): forward contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

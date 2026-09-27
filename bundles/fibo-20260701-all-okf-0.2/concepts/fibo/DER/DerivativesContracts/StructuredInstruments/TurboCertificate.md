---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: turbo certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate that acts as a leveraged security, whose price tracks an underlying financial asset's price one for
      one, and that can be used to go long or short
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: As risk management each turbo trade has a built-in knock-out level and will terminate if this is hit.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'There are two types of turbos: long turbos, sometimes known as bull turbos, and short turbos, also known as bear
      turbos. You''d buy a long turbo if you thought the price of the underlying asset was set to rise. With a long turbo,
      the knock-out level will be below the underlying asset''s current market price to protect you against downward movements.
      Alternatively, you''d buy a short turbo if you thought the price of the underlying asset might fall. A short turbo will
      have a knock-out level which is above the underlying asset''s current market price to protect you against upward movements.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Turbos are traded on venue rather than over the counter (OTC), and have fully visible order books that you can
      view to gauge sentiment and plan your strategy. Turbo trading works by buying a transferrable security whose value is
      based on an underlying asset's. So, you effectively take a position on that asset's price either rising or falling.
      For each trade, you choose a knock-out level – the point where you'd like to exit if the market turns against you. This
      then helps to determine the purchase price for the turbo, which will be your maximum possible loss. You'll pay this
      outlay in full upfront.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: turbo
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: turbo warrant
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TurboCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: turbo certificate
type: Ontology Class
---

# turbo certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TurboCertificate>

## Definition

certificate that acts as a leveraged security, whose price tracks an underlying financial asset's price one for one, and that can be used to go long or short

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): turbo certificate
- **definition** (en): certificate that acts as a leveraged security, whose price tracks an underlying financial asset's price one for one, and that can be used to go long or short
- **explanatoryNote** (en): As risk management each turbo trade has a built-in knock-out level and will terminate if this is hit.
- **explanatoryNote** (en): There are two types of turbos: long turbos, sometimes known as bull turbos, and short turbos, also known as bear turbos. You'd buy a long turbo if you thought the price of the underlying asset was set to rise. With a long turbo, the knock-out level will be below the underlying asset's current market price to protect you against downward movements. Alternatively, you'd buy a short turbo if you thought the price of the underlying asset might fall. A short turbo will have a knock-out level which is above the underlying asset's current market price to protect you against upward movements.
- **explanatoryNote** (en): Turbos are traded on venue rather than over the counter (OTC), and have fully visible order books that you can view to gauge sentiment and plan your strategy. Turbo trading works by buying a transferrable security whose value is based on an underlying asset's. So, you effectively take a position on that asset's price either rising or falling. For each trade, you choose a knock-out level – the point where you'd like to exit if the market turns against you. This then helps to determine the purchase price for the turbo, which will be your maximum possible loss. You'll pay this outlay in full upfront.
- **synonym** (en): turbo
- **synonym** (en): turbo warrant

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

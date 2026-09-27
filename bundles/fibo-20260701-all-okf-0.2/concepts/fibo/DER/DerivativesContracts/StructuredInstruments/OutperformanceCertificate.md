---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: outperformance certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate that allows disproportionate participation (outperformance) in positive performance above the strike,
      reflecting underlying price moves 1:1 (adjusted by the conversion ratio and any related fees), and whose risk is comparable
      to direct investment in the underlying asset(s)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'For example: You buy an outperformance certificate based on a stock. The certificate’s strike price is 100 Euros
      and its participation factor is 150 percent. If the price of the underlying stock surpasses the strike price of 100
      Euros, you are rewarded with a 150 percent return, instead of just 100 percent. If the price of the stock climbs to
      110 Euros, for example, the value of the certificate would be 115 Euros.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.2.8
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: outperformance certificate
type: Ontology Class
---

# outperformance certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate>

## Definition

certificate that allows disproportionate participation (outperformance) in positive performance above the strike, reflecting underlying price moves 1:1 (adjusted by the conversion ratio and any related fees), and whose risk is comparable to direct investment in the underlying asset(s)

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): outperformance certificate
- **definition** (en): certificate that allows disproportionate participation (outperformance) in positive performance above the strike, reflecting underlying price moves 1:1 (adjusted by the conversion ratio and any related fees), and whose risk is comparable to direct investment in the underlying asset(s)
- **example** (en): For example: You buy an outperformance certificate based on a stock. The certificate’s strike price is 100 Euros and its participation factor is 150 percent. If the price of the underlying stock surpasses the strike price of 100 Euros, you are rewarded with a 150 percent return, instead of just 100 percent. If the price of the stock climbs to 110 Euros, for example, the value of the certificate would be 115 Euros.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.2.8

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

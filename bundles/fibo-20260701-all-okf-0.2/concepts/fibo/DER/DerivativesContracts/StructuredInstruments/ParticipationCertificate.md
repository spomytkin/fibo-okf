---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: participation certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: participation product that provides the possibility to participate in the gains or losses in the price of an asset,
      subject to counterparty risk
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'In many cases, certificates do not give the investor the right to receive dividend distributions from the underlying
      stocks or other assets. For example: You buy a bonus certificate issued by your bank which is based on a stock that
      pays annual dividends. During the certificate''s term, the bank holds the underlying stock and receives the dividends.
      At the end of the term, the bank pays the predefined bonus, even though the actual price of the stock is lower (but
      not below the protection threshold).Depending on the type of certificate, the exact terms and conditions, and the contract''s
      expiry date, it is possible that the investor may receive the underlying asset instead of money at the end of the investment
      term. That is often the case with discount certificates based on stocks, for example, when their price sits below the
      predetermined cap. If the certificate''s issuer becomes insolvent, the assets which underly the certificate are considered
      part of the issuer''s liquid assets. This is in contrast to owning actual securities or shares in investment funds,
      as these are segregated assets which remain the property of the investor if the broker or custodian bank fails.'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: bearer debt note
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: certificate
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: participation certificate
type: Ontology Class
---

# participation certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate>

## Definition

participation product that provides the possibility to participate in the gains or losses in the price of an asset, subject to counterparty risk

## Relationships

- **Subclass of**: [ParticipationInstrument](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument.md)
- **Subclass of**: [StructuredFinanceInstrument](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceInstrument.md)

## Annotations

- **label** (en): participation certificate
- **definition** (en): participation product that provides the possibility to participate in the gains or losses in the price of an asset, subject to counterparty risk
- **explanatoryNote** (en): In many cases, certificates do not give the investor the right to receive dividend distributions from the underlying stocks or other assets. For example: You buy a bonus certificate issued by your bank which is based on a stock that pays annual dividends. During the certificate's term, the bank holds the underlying stock and receives the dividends. At the end of the term, the bank pays the predefined bonus, even though the actual price of the stock is lower (but not below the protection threshold).Depending on the type of certificate, the exact terms and conditions, and the contract's expiry date, it is possible that the investor may receive the underlying asset instead of money at the end of the investment term. That is often the case with discount certificates based on stocks, for example, when their price sits below the predetermined cap. If the certificate's issuer becomes insolvent, the assets which underly the certificate are considered part of the issuer's liquid assets. This is in contrast to owning actual securities or shares in investment funds, as these are segregated assets which remain the property of the investor if the broker or custodian bank fails.
- **synonym** (en): bearer debt note
- **synonym** (en): certificate

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

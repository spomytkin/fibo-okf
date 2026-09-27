---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: barrier reverse convertible certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'participation certificate whose payout is conditional: should the barrier never be breached, the nominal price
      plus coupon is paid at redemption; if the barrier is breached the product changes into a reverse convertible'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: Due to the barrier, the probability of maximum redemption is higher; the coupon, however, is smaller than for a
      reverse convertible. It has reduced risk compared to a direct investment into the underlying asset(s). With higher risk
      levels, multiple underlying assets (worst-of) allow for higher coupons or lower barriers; limited profit potential (Cap).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.4.8
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierReverseConvertibleCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: barrier reverse convertible certificate
type: Ontology Class
---

# barrier reverse convertible certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierReverseConvertibleCertificate>

## Definition

participation certificate whose payout is conditional: should the barrier never be breached, the nominal price plus coupon is paid at redemption; if the barrier is breached the product changes into a reverse convertible

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- **Subclass of**: [StructuredFinanceWithoutPrincipalProtection](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)

## Annotations

- **label** (en): barrier reverse convertible certificate
- **definition** (en): participation certificate whose payout is conditional: should the barrier never be breached, the nominal price plus coupon is paid at redemption; if the barrier is breached the product changes into a reverse convertible
- **note** (en): Due to the barrier, the probability of maximum redemption is higher; the coupon, however, is smaller than for a reverse convertible. It has reduced risk compared to a direct investment into the underlying asset(s). With higher risk levels, multiple underlying assets (worst-of) allow for higher coupons or lower barriers; limited profit potential (Cap).
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.4.8

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: barrier discount certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: participation certificate that enables the investor to acquire the underlying asset at a lower price in return
      for a limited payout, and for which the maximum redemption amount (Cap) is paid out if the barrier is never breached
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: Due to the barrier, the probability of maximum redemption is higher; the discount, however, is smaller than for
      a discount certificate. If the barrier is breached the product changes into a discount certificate. Barrier discount
      certificates have reduced risk compared to direct investment in the underlying assets, with limited profit potential
      (Cap). With higher risk levels multiple underlying assets (worst-of) allow for higher discounts or a lower barrier.
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
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierDiscountCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: barrier discount certificate
type: Ontology Class
---

# barrier discount certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BarrierDiscountCertificate>

## Definition

participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the maximum redemption amount (Cap) is paid out if the barrier is never breached

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- **Subclass of**: [StructuredFinanceWithoutPrincipalProtection](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)

## Annotations

- **label** (en): barrier discount certificate
- **definition** (en): participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the maximum redemption amount (Cap) is paid out if the barrier is never breached
- **note** (en): Due to the barrier, the probability of maximum redemption is higher; the discount, however, is smaller than for a discount certificate. If the barrier is breached the product changes into a discount certificate. Barrier discount certificates have reduced risk compared to direct investment in the underlying assets, with limited profit potential (Cap). With higher risk levels multiple underlying assets (worst-of) allow for higher discounts or a lower barrier.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.4.8

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: discount certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: participation certificate that enables the investor to acquire the underlying asset at a lower price in return
      for a limited payout, and for which the underlying asset(s) and/or a cash amount is redeemed should the underlying asset
      close below the strike on expiry, for which, in return, the potential profit is capped
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: Discount certificates correspond to a buy-write-strategy; they have reduced risk compared to a direct investment
      in the underlying asset; with higher risk levels multiple underlying assets (worst-of) allow for higher discounts; limited
      profit opportunity (Cap).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.4.8
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: At the end of the certificate's maturity, a cash disbursement occurs. If the price of the underlying when the maturity
      is up is higher than the maximal payout or identical to it, the issuer pays the maximum amount. If the price of the
      underlying is less than the cap, the issuer pays either the current price of the certificate in cash or he gives the
      investor the underlying, for example a share, at its current price. The issuer can choose. The cash payout is obligatory
      in the case of discount certificates on indices, currencies or interest.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Discount certificates are ideal for conservative investors that want to guard against market fluctuations and who
      expect in the medium term sideways-moving prices. Because the buyer of a discount certificate does not profit from price
      gains that are higher than the cap, this form of investment is best suited for a medium-term oriented engagement. If
      the certificate reaches its cap before the maturity, the investor should take the profits.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The maximum profit that an investor can reach with a discount certificate is calculated by taking the difference
      between the purchase price and the cap on the underlying. Losses, in contrast, are lessened by the discount. The investor
      suffers a loss only when the price of the underlying at the end of the maturity has fallen so far that the discount
      is depleted. The discount thus works as a buffer against risk.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
  - concept: /concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/DiscountCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: discount certificate
type: Ontology Class
---

# discount certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/DiscountCertificate>

## Definition

participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the underlying asset(s) and/or a cash amount is redeemed should the underlying asset close below the strike on expiry, for which, in return, the potential profit is capped

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)
- **Subclass of**: [StructuredFinanceWithoutPrincipalProtection](/concepts/fibo/SEC/Debt/PoolBackedSecurities/StructuredFinanceWithoutPrincipalProtection.md)

## Annotations

- **label** (en): discount certificate
- **definition** (en): participation certificate that enables the investor to acquire the underlying asset at a lower price in return for a limited payout, and for which the underlying asset(s) and/or a cash amount is redeemed should the underlying asset close below the strike on expiry, for which, in return, the potential profit is capped
- **note** (en): Discount certificates correspond to a buy-write-strategy; they have reduced risk compared to a direct investment in the underlying asset; with higher risk levels multiple underlying assets (worst-of) allow for higher discounts; limited profit opportunity (Cap).
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.4.8
- **explanatoryNote** (en): At the end of the certificate's maturity, a cash disbursement occurs. If the price of the underlying when the maturity is up is higher than the maximal payout or identical to it, the issuer pays the maximum amount. If the price of the underlying is less than the cap, the issuer pays either the current price of the certificate in cash or he gives the investor the underlying, for example a share, at its current price. The issuer can choose. The cash payout is obligatory in the case of discount certificates on indices, currencies or interest.
- **explanatoryNote** (en): Discount certificates are ideal for conservative investors that want to guard against market fluctuations and who expect in the medium term sideways-moving prices. Because the buyer of a discount certificate does not profit from price gains that are higher than the cap, this form of investment is best suited for a medium-term oriented engagement. If the certificate reaches its cap before the maturity, the investor should take the profits.
- **explanatoryNote** (en): The maximum profit that an investor can reach with a discount certificate is calculated by taking the difference between the purchase price and the cap on the underlying. Losses, in contrast, are lessened by the discount. The investor suffers a loss only when the price of the underlying at the end of the maturity has fallen so far that the discount is depleted. The discount thus works as a buffer against risk.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

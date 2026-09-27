---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bonus certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate whose minimum redemption is equal to the nominal value provided the barrier has not been breached,
      with a greater risk in relation to multiple underlying asset(s) (worst-of), allowing for a higher bonus level or lower
      barrier, and with a reduced risk compared to a direct investment into the underlying asset(s)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'For example: You buy a bonus certificate based on a stock. The price of the stock at the time that you get the
      certificate is 100 Euros. The bonus level is 120 Euros, and the protection threshold is 80 Euros. Over the two-year
      term, the price of the stock fluctuates between 90 and 110 Euros. When the certificate matures at the end of the term,
      you receive the bonus price of 120 Euros.'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: If the barrier is breached the product becomes a tracker certificate.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.2.8
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: "Bonus certificates have a risk buffer for price losses in the underlying; the bonus guarantees a minimum return\
      \ above the risk level. A bonus certificate represents an alternative to a direct investment in a share or an index.\
      \ Investors primarily use them if they believe that despite rising prices setbacks are still likely to occur.\n\t\t\n\
      A bonus certificate is furnished with a bonus amount and an upper and lower price level. If the certificate expires\
      \ with the price of the underlying ranging between these two levels, owners are paid out their bonuses. If the underlying\
      \ was at or below the risk level during the certificate's lifetime, its price is that of the current value of the certificate\
      \ at expiry. If the underlying is above the upper level at expiry, the investor fully participates in the price gains.\
      \ Some bonus certificates have a profit cap. This is where the certificate stops participating in the price gains of\
      \ the underlying.\n\nA bonus certificate is issued at the current price of the underlying. The upper level is derived\
      \ from adding the bonus to the issue price. The lower level is determined at issuance and usually expressed in percent."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BonusCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: bonus certificate
type: Ontology Class
---

# bonus certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BonusCertificate>

## Definition

certificate whose minimum redemption is equal to the nominal value provided the barrier has not been breached, with a greater risk in relation to multiple underlying asset(s) (worst-of), allowing for a higher bonus level or lower barrier, and with a reduced risk compared to a direct investment into the underlying asset(s)

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): bonus certificate
- **definition** (en): certificate whose minimum redemption is equal to the nominal value provided the barrier has not been breached, with a greater risk in relation to multiple underlying asset(s) (worst-of), allowing for a higher bonus level or lower barrier, and with a reduced risk compared to a direct investment into the underlying asset(s)
- **example** (en): For example: You buy a bonus certificate based on a stock. The price of the stock at the time that you get the certificate is 100 Euros. The bonus level is 120 Euros, and the protection threshold is 80 Euros. Over the two-year term, the price of the stock fluctuates between 90 and 110 Euros. When the certificate matures at the end of the term, you receive the bonus price of 120 Euros.
- **note** (en): If the barrier is breached the product becomes a tracker certificate.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.2.8
- **explanatoryNote** (en): Bonus certificates have a risk buffer for price losses in the underlying; the bonus guarantees a minimum return above the risk level. A bonus certificate represents an alternative to a direct investment in a share or an index. Investors primarily use them if they believe that despite rising prices setbacks are still likely to occur. 		 A bonus certificate is furnished with a bonus amount and an upper and lower price level. If the certificate expires with the price of the underlying ranging between these two levels, owners are paid out their bonuses. If the underlying was at or below the risk level during the certificate's lifetime, its price is that of the current value of the certificate at expiry. If the underlying is above the upper level at expiry, the investor fully participates in the price gains. Some bonus certificates have a profit cap. This is where the certificate stops participating in the price gains of the underlying.  A bonus certificate is issued at the current price of the underlying. The upper level is derived from adding the bonus to the issue price. The lower level is determined at issuance and usually expressed in percent.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: outperformance bonus certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate that allows disproportionate participation (outperformance) in positive performance above the strike,
      in which the minimum redemption is equal to the nominal value provided the barrier has not been breached, with greater
      risk multiple underlying asset(s) (worst-of) allow for a higher bonus level or lower barrier, and reduced risk compared
      to a direct investment into the underlying asset(s)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: If the barrier is breached the product changes into an outperformance certificate.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.2.8
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The outperformance bonus certificate combines the strengths of both outperformance and normal bonus certificates.
      This means that you’re protected on the downside by a bonus level (i.e., a feature of bonus certificates) but nevertheless
      have the opportunity to participate disproportionately in upside gains in the underlying instrument (the ''outperformance
      certificate'' dimension). If you compare all three structured product types with each other, you’ll see that outperformance
      bonus certificates come up a bit short in terms of the characteristics of the other two forms. In other words, the disproportionate
      participation rate (outperformance) is usually somewhat lower than with a ''plain vanilla'' outperformance certificate.
      This is because additional bonus protection has to be bought in order to structure the product properly. The same applies
      to the bonus dimension: because such a certificate still affords disproportionate participation, its downside protection
      level is more modest.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/BonusCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BonusCertificate
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceBonusCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: outperformance bonus certificate
type: Ontology Class
---

# outperformance bonus certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/OutperformanceBonusCertificate>

## Definition

certificate that allows disproportionate participation (outperformance) in positive performance above the strike, in which the minimum redemption is equal to the nominal value provided the barrier has not been breached, with greater risk multiple underlying asset(s) (worst-of) allow for a higher bonus level or lower barrier, and reduced risk compared to a direct investment into the underlying asset(s)

## Relationships

- **Subclass of**: [BonusCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/BonusCertificate.md)
- **Subclass of**: [OutperformanceCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/OutperformanceCertificate.md)

## Annotations

- **label** (en): outperformance bonus certificate
- **definition** (en): certificate that allows disproportionate participation (outperformance) in positive performance above the strike, in which the minimum redemption is equal to the nominal value provided the barrier has not been breached, with greater risk multiple underlying asset(s) (worst-of) allow for a higher bonus level or lower barrier, and reduced risk compared to a direct investment into the underlying asset(s)
- **note** (en): If the barrier is breached the product changes into an outperformance certificate.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.2.8
- **explanatoryNote** (en): The outperformance bonus certificate combines the strengths of both outperformance and normal bonus certificates. This means that you’re protected on the downside by a bonus level (i.e., a feature of bonus certificates) but nevertheless have the opportunity to participate disproportionately in upside gains in the underlying instrument (the 'outperformance certificate' dimension). If you compare all three structured product types with each other, you’ll see that outperformance bonus certificates come up a bit short in terms of the characteristics of the other two forms. In other words, the disproportionate participation rate (outperformance) is usually somewhat lower than with a 'plain vanilla' outperformance certificate. This is because additional bonus protection has to be bought in order to structure the product properly. The same applies to the bonus dimension: because such a certificate still affords disproportionate participation, its downside protection level is more modest.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: twin-win certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate that makes profits possible with rising and falling underlying asset values, in which a falling underlying
      asset price converts into profit up to the barrier, and whose minimum redemption is equal to the nominal value provided
      the barrier has not been breached
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#note
    value: If the barrier is breached the product changes into a tracker certificate. With higher risk levels, multiple underlying
      asset(s) (worst-of) allow for a higher bonus level or lower barrier. Twin-win certificates have reduced risk compared
      to a direct investment into the underlying asset(s).
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.2.8
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Twin-win certificates are suited to investors who are convinced that the underlying instrument has a good chance
      of going up. If it in fact does, the built-in leverage of the product enables you to participate not just 1:1 in that
      upside move (as would be the case with a normal tracker certificate), but instead at a disproportionate rate and with
      no price limitation.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With a twin-win certificate, you can actually have it both ways. In other words, this type of structured product
      generates a profit for you not only when the price of the underlying instrument goes up, but also if it declines to
      a certain extent. And this with a specially built-in safety mechanism. The unique structure of these products makes
      it possible to turn a modest loss in the underlying instrument into a modest gain.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TwinWinCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: twin-win certificate
type: Ontology Class
---

# twin-win certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TwinWinCertificate>

## Definition

certificate that makes profits possible with rising and falling underlying asset values, in which a falling underlying asset price converts into profit up to the barrier, and whose minimum redemption is equal to the nominal value provided the barrier has not been breached

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): twin-win certificate
- **definition** (en): certificate that makes profits possible with rising and falling underlying asset values, in which a falling underlying asset price converts into profit up to the barrier, and whose minimum redemption is equal to the nominal value provided the barrier has not been breached
- **note** (en): If the barrier is breached the product changes into a tracker certificate. With higher risk levels, multiple underlying asset(s) (worst-of) allow for a higher bonus level or lower barrier. Twin-win certificates have reduced risk compared to a direct investment into the underlying asset(s).
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.2.8
- **explanatoryNote** (en): Twin-win certificates are suited to investors who are convinced that the underlying instrument has a good chance of going up. If it in fact does, the built-in leverage of the product enables you to participate not just 1:1 in that upside move (as would be the case with a normal tracker certificate), but instead at a disproportionate rate and with no price limitation.
- **explanatoryNote** (en): With a twin-win certificate, you can actually have it both ways. In other words, this type of structured product generates a profit for you not only when the price of the underlying instrument goes up, but also if it declines to a certain extent. And this with a specially built-in safety mechanism. The unique structure of these products makes it possible to turn a modest loss in the underlying instrument into a modest gain.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

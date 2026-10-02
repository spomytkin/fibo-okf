---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: index certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate whose underlying asset is an index
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If the underlying share increases in value, the value of the certificate increases in analog to the gain; with
      every setback, the certificate value declines accordingly.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Investors should think about currency risks when investing in index certificates that track a share index outside
      of the euro zone. And they should pay attention to whether the underlying index is a performance or price index. With
      a performance index, all dividends and profits from subscription rights flow into the index value. In contrast to that,
      price indices show the pure development of the shares and thus the price declines that usually accompany dividend payouts.
      Index certificates are particularly interesting to investors that want to profit from positive capital-market developments,
      but who don’t want to deal with the daily price developments of several individual shares.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: With Index certificates investors can participate one-to-one in the development of an exchange index – without
      actually buying the underlying shares in that comprise that index. Every index certificate has a subscription rate (e.g.,
      1:10 or 1:100) that defines the value of the certificate in relation to the index listing. The investor invests broadly
      diversified and transparently with minimal effort and smaller amounts.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/IndexCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: index certificate
type: Ontology Class
---

# index certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/IndexCertificate>

## Definition

certificate whose underlying asset is an index

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): index certificate
- **definition** (en): certificate whose underlying asset is an index
- **explanatoryNote** (en): If the underlying share increases in value, the value of the certificate increases in analog to the gain; with every setback, the certificate value declines accordingly.
- **explanatoryNote** (en): Investors should think about currency risks when investing in index certificates that track a share index outside of the euro zone. And they should pay attention to whether the underlying index is a performance or price index. With a performance index, all dividends and profits from subscription rights flow into the index value. In contrast to that, price indices show the pure development of the shares and thus the price declines that usually accompany dividend payouts. Index certificates are particularly interesting to investors that want to profit from positive capital-market developments, but who don’t want to deal with the daily price developments of several individual shares.
- **explanatoryNote** (en): With Index certificates investors can participate one-to-one in the development of an exchange index – without actually buying the underlying shares in that comprise that index. Every index certificate has a subscription rate (e.g., 1:10 or 1:100) that defines the value of the certificate in relation to the index listing. The investor invests broadly diversified and transparently with minimal effort and smaller amounts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

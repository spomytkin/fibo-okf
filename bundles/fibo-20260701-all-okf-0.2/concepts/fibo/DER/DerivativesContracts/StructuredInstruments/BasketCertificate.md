---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: basket certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate whose underlying asset represents a fraction of a basket of securities that corresponds to the subscription
      ratio
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Basket certificates make sense if an investor is convinced of the potential in a particular sector or region, but
      shies away from the risk of investing in individual securities. Because the certificate is expected to achieve higher
      profits than the benchmark index, the share basket usually contains fewer titles than the benchmark index. That increases
      the potential for profits; but the risk of loss increases compared to the index. Unlike shares, basket certificates
      are not eligible for dividend payouts. The limited maturity should also be taken into account.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The issuer determines the basket's compilation before quoting the certificate. Fundamentally, all securities with
      regular, at least daily, price determinations are suited for the portfolio. The selection criteria for the shares or
      securities in the basket are known and remain unchanged during the life of the certificate. Note, however, that the
      composition of the share basket can change over time. If the issuer follows a specific strategy with the certificate,
      the basket has to be adjusted at specific end-of-period dates, provided the market leaders change. In such a case, the
      basket is called an active basket. If, in contrast, the composition of a share basket remains clearly defined, as is
      the case for an index certificate, it is called a passive basket.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The success of a basket certificate is measured on whether it can outperform a comparison index or fund, a so-called
      benchmark. Basket certificates can be roughly divided into three categories based on the criteria for selecting securities:
      Sector certificates; country or region certificates; and strategy and thematic certificates.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BasketCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: basket certificate
type: Ontology Class
---

# basket certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/BasketCertificate>

## Definition

certificate whose underlying asset represents a fraction of a basket of securities that corresponds to the subscription ratio

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): basket certificate
- **definition** (en): certificate whose underlying asset represents a fraction of a basket of securities that corresponds to the subscription ratio
- **explanatoryNote** (en): Basket certificates make sense if an investor is convinced of the potential in a particular sector or region, but shies away from the risk of investing in individual securities. Because the certificate is expected to achieve higher profits than the benchmark index, the share basket usually contains fewer titles than the benchmark index. That increases the potential for profits; but the risk of loss increases compared to the index. Unlike shares, basket certificates are not eligible for dividend payouts. The limited maturity should also be taken into account.
- **explanatoryNote** (en): The issuer determines the basket's compilation before quoting the certificate. Fundamentally, all securities with regular, at least daily, price determinations are suited for the portfolio. The selection criteria for the shares or securities in the basket are known and remain unchanged during the life of the certificate. Note, however, that the composition of the share basket can change over time. If the issuer follows a specific strategy with the certificate, the basket has to be adjusted at specific end-of-period dates, provided the market leaders change. In such a case, the basket is called an active basket. If, in contrast, the composition of a share basket remains clearly defined, as is the case for an index certificate, it is called a passive basket.
- **explanatoryNote** (en): The success of a basket certificate is measured on whether it can outperform a comparison index or fund, a so-called benchmark. Basket certificates can be roughly divided into three categories based on the criteria for selecting securities: Sector certificates; country or region certificates; and strategy and thematic certificates.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

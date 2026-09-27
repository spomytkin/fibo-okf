---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tracker certificate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: certificate that reflects underlying price moves 1:1 (adjusted by conversion ratio and any related fees), in which
      the associated risk is comparable to direct investment in the underlying asset(s)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Tracker certificates can be purchased on stock exchanges which they are listed on. Many of these certificates
      track underlying assets at a ratio of 1:100. That means that an investor can invest just a fraction of the amount which
      would be required to buy the actual underlying asset. For example: You invest in a tracker certificate which is based
      on a stock basket with a value of 10,000 Euros. Because the tracker certificate uses a ratio of 1:100, you only need
      to pay 100 Euros for the certificate. If the price of the underlying stocks goes up by 10 percent (to 11,000 Euros),
      the value of the certificate will also go up by 10 percent (to 110 Euros).'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Trackers can be used to invest in the performance of multiple stocks, for example. A tracker certificate is a structured
      instrument that allows the investor to invest in an underlying asset without actually owning the asset. From an investor
      perspective, tracker certificates work much like investment funds. The tracker follows the price of an underlying asset
      (one or more stocks, for example). The investor buys a certificate based on the tracker. If the value of the underlying
      asset goes up, the value of the certificate goes up with it. If the underlying asset loses value, the certificate loses
      value.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15, clause 6.2.8
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Some tracker certificates have an expiry date. That means they only track an underlying asset for a predetermined
      length of time (one year, for example). The certificate matures at the end of that period, at which point you as the
      investor are paid out its going value at the time of expiry.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Tracker certificates can also be used to profit off negative price developments. This is the case with so-called
      bear tracker certificates which take a short position on the underlying asset. Note that tracker certificates do not
      normally pay out dividends. If one holds a certificate which tracks the stock of a company which pay dividends, they
      will not receive them. However, they may receive some form of compensation from the certificate’s issuer in some cases.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Unlike investment funds – which are divided into shares and owned by investors – tracker certificates are simply
      debt claims against the issuer (the bank which offers them, for example). That means the underlying asset which you
      are investing in does not belong to you, but to the issuer. Shares of investment funds, on the other hand, are classified
      as segregated assets in some jurisdictions, such as Switzerland, and are owned by you as the shareholder rather than
      by the fund managers. In practice, investors are not likely to notice the difference. But whether you hold tracker certificates
      or fund shares makes a big difference when an investment company becomes insolvent. Tracker certificates are not protected
      against issuer bankruptcy, and fall into the pool of general debt claims against the bankrupt party. If the issuer of
      a tracker certificate goes bankrupt, you may very likely lose all or part of the money which you invested in the tracker
      certificate. This danger is known as counterparty risk. By investing in tracker certificates, you agree to carry the
      counterparty risk.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TrackerCertificate
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: tracker certificate
type: Ontology Class
---

# tracker certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/TrackerCertificate>

## Definition

certificate that reflects underlying price moves 1:1 (adjusted by conversion ratio and any related fees), in which the associated risk is comparable to direct investment in the underlying asset(s)

## Relationships

- **Subclass of**: [ParticipationCertificate](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/ParticipationCertificate.md)

## Annotations

- **label** (en): tracker certificate
- **definition** (en): certificate that reflects underlying price moves 1:1 (adjusted by conversion ratio and any related fees), in which the associated risk is comparable to direct investment in the underlying asset(s)
- **example** (en): Tracker certificates can be purchased on stock exchanges which they are listed on. Many of these certificates track underlying assets at a ratio of 1:100. That means that an investor can invest just a fraction of the amount which would be required to buy the actual underlying asset. For example: You invest in a tracker certificate which is based on a stock basket with a value of 10,000 Euros. Because the tracker certificate uses a ratio of 1:100, you only need to pay 100 Euros for the certificate. If the price of the underlying stocks goes up by 10 percent (to 11,000 Euros), the value of the certificate will also go up by 10 percent (to 110 Euros).
- **example** (en): Trackers can be used to invest in the performance of multiple stocks, for example. A tracker certificate is a structured instrument that allows the investor to invest in an underlying asset without actually owning the asset. From an investor perspective, tracker certificates work much like investment funds. The tracker follows the price of an underlying asset (one or more stocks, for example). The investor buys a certificate based on the tracker. If the value of the underlying asset goes up, the value of the certificate goes up with it. If the underlying asset loses value, the certificate loses value.
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15, clause 6.2.8
- **explanatoryNote** (en): Some tracker certificates have an expiry date. That means they only track an underlying asset for a predetermined length of time (one year, for example). The certificate matures at the end of that period, at which point you as the investor are paid out its going value at the time of expiry.
- **explanatoryNote** (en): Tracker certificates can also be used to profit off negative price developments. This is the case with so-called bear tracker certificates which take a short position on the underlying asset. Note that tracker certificates do not normally pay out dividends. If one holds a certificate which tracks the stock of a company which pay dividends, they will not receive them. However, they may receive some form of compensation from the certificate’s issuer in some cases.
- **explanatoryNote** (en): Unlike investment funds – which are divided into shares and owned by investors – tracker certificates are simply debt claims against the issuer (the bank which offers them, for example). That means the underlying asset which you are investing in does not belong to you, but to the issuer. Shares of investment funds, on the other hand, are classified as segregated assets in some jurisdictions, such as Switzerland, and are owned by you as the shareholder rather than by the fund managers. In practice, investors are not likely to notice the difference. But whether you hold tracker certificates or fund shares makes a big difference when an investment company becomes insolvent. Tracker certificates are not protected against issuer bankruptcy, and fall into the pool of general debt claims against the bankrupt party. If the issuer of a tracker certificate goes bankrupt, you may very likely lose all or part of the money which you invested in the tracker certificate. This danger is known as counterparty risk. By investing in tracker certificates, you agree to carry the counterparty risk.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

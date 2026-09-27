---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred, restricted voting, redeemable exchangeable, cumulative, registered share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share that confers less than one vote per share, may be exchanged for securities of another issuer, may
      be redeemed at the option of the issuer and/or of the shareholder, provides a periodic stated income and dividends not
      paid in any year accumulate, and is registered
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/CumulativePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CumulativePreferredShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/ExchangeablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ExchangeablePreferredShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/NonParticipatingPreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NonParticipatingPreferredShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/RestrictedVotingShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/RestrictedVotingShare
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/PreferredRestrictedVotingRedeemableExchangeableCumulativeRegisteredShare
sources:
- id: fibo-source-e698ab6eab
  resource: references/fibo/SEC/Equities/EquityCFIClassificationIndividuals.rdf
  sha256: e698ab6eabe9528750ce3dbc76f03090e26eac1f69c2fa7f62cb5d52ba93d10e
  title: FIBO source SEC/Equities/EquityCFIClassificationIndividuals.rdf
title: preferred, restricted voting, redeemable exchangeable, cumulative, registered share
type: Ontology Class
---

# preferred, restricted voting, redeemable exchangeable, cumulative, registered share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/PreferredRestrictedVotingRedeemableExchangeableCumulativeRegisteredShare>

## Definition

preferred share that confers less than one vote per share, may be exchanged for securities of another issuer, may be redeemed at the option of the issuer and/or of the shareholder, provides a periodic stated income and dividends not paid in any year accumulate, and is registered

## Relationships

- **Subclass of**: [CumulativePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/CumulativePreferredShare.md)
- **Subclass of**: [ExchangeablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/ExchangeablePreferredShare.md)
- **Subclass of**: [NonParticipatingPreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/NonParticipatingPreferredShare.md)
- **Subclass of**: [PreferredShareWithFixedRateDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithFixedRateDividend.md)
- **Subclass of**: [RestrictedVotingShare](/concepts/fibo/SEC/Equities/EquityInstruments/RestrictedVotingShare.md)
- **Subclass of**: [RegisteredSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)

## Annotations

- **label** (en-US): preferred, restricted voting, redeemable exchangeable, cumulative, registered share
- **definition**: preferred share that confers less than one vote per share, may be exchanged for securities of another issuer, may be redeemed at the option of the issuer and/or of the shareholder, provides a periodic stated income and dividends not paid in any year accumulate, and is registered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

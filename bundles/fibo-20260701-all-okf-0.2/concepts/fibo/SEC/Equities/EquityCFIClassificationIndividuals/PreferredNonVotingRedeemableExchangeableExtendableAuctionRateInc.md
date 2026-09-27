---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred, non-voting, redeemable/exchangeable/extendable, auction rate income, registered share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share that confers zero votes per share, may be exchanged for securities of another issuer, whose issuer
      and/or shareholders have the option to extend the maturity date, that provides a periodic income whose dividend rate
      is adjusted through an auction, and is registered
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/ExchangeablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ExchangeablePreferredShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/ExtendablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ExtendablePreferredShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/NonVotingShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NonVotingShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/PreferredNonVotingRedeemableExchangeableExtendableAuctionRateIncomeRegisteredShare
sources:
- id: fibo-source-e698ab6eab
  resource: references/fibo/SEC/Equities/EquityCFIClassificationIndividuals.rdf
  sha256: e698ab6eabe9528750ce3dbc76f03090e26eac1f69c2fa7f62cb5d52ba93d10e
  title: FIBO source SEC/Equities/EquityCFIClassificationIndividuals.rdf
title: preferred, non-voting, redeemable/exchangeable/extendable, auction rate income, registered share
type: Ontology Class
---

# preferred, non-voting, redeemable/exchangeable/extendable, auction rate income, registered share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/PreferredNonVotingRedeemableExchangeableExtendableAuctionRateIncomeRegisteredShare>

## Definition

preferred share that confers zero votes per share, may be exchanged for securities of another issuer, whose issuer and/or shareholders have the option to extend the maturity date, that provides a periodic income whose dividend rate is adjusted through an auction, and is registered

## Relationships

- **Subclass of**: [ExchangeablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/ExchangeablePreferredShare.md)
- **Subclass of**: [ExtendablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/ExtendablePreferredShare.md)
- **Subclass of**: [NonVotingShare](/concepts/fibo/SEC/Equities/EquityInstruments/NonVotingShare.md)
- **Subclass of**: [PreferredShareWithAuctionRateDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend.md)
- **Subclass of**: [RegisteredSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)

## Annotations

- **label** (en-US): preferred, non-voting, redeemable/exchangeable/extendable, auction rate income, registered share
- **definition**: preferred share that confers zero votes per share, may be exchanged for securities of another issuer, whose issuer and/or shareholders have the option to extend the maturity date, that provides a periodic income whose dividend rate is adjusted through an auction, and is registered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

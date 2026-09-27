---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: preferred, enhanced voting, extendable, auction rate income, registered share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: preferred share that confers multiple votes per share, may be redeemed at the option of the issuer and/or of the
      shareholder with an extendable redemption date, provides a periodic income whose dividend rate is adjusted through an
      auction, and is registered
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/EnhancedVotingShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/EnhancedVotingShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/ExtendablePreferredShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/ExtendablePreferredShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/PreferredEnhancedVotingExtendableAuctionRateIncomeRegisteredShare
sources:
- id: fibo-source-e698ab6eab
  resource: references/fibo/SEC/Equities/EquityCFIClassificationIndividuals.rdf
  sha256: e698ab6eabe9528750ce3dbc76f03090e26eac1f69c2fa7f62cb5d52ba93d10e
  title: FIBO source SEC/Equities/EquityCFIClassificationIndividuals.rdf
title: preferred, enhanced voting, extendable, auction rate income, registered share
type: Ontology Class
---

# preferred, enhanced voting, extendable, auction rate income, registered share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/PreferredEnhancedVotingExtendableAuctionRateIncomeRegisteredShare>

## Definition

preferred share that confers multiple votes per share, may be redeemed at the option of the issuer and/or of the shareholder with an extendable redemption date, provides a periodic income whose dividend rate is adjusted through an auction, and is registered

## Relationships

- **Subclass of**: [EnhancedVotingShare](/concepts/fibo/SEC/Equities/EquityInstruments/EnhancedVotingShare.md)
- **Subclass of**: [ExtendablePreferredShare](/concepts/fibo/SEC/Equities/EquityInstruments/ExtendablePreferredShare.md)
- **Subclass of**: [PreferredShareWithAuctionRateDividend](/concepts/fibo/SEC/Equities/EquityInstruments/PreferredShareWithAuctionRateDividend.md)
- **Subclass of**: [RegisteredSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)

## Annotations

- **label** (en-US): preferred, enhanced voting, extendable, auction rate income, registered share
- **definition**: preferred share that confers multiple votes per share, may be redeemed at the option of the issuer and/or of the shareholder with an extendable redemption date, provides a periodic income whose dividend rate is adjusted through an auction, and is registered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

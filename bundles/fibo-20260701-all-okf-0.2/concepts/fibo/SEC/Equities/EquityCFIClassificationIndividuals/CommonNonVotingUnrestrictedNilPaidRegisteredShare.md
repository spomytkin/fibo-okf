---
owl:
  annotations:
  - language: en-US
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common, non-voting, unrestricted, nil paid, registered share
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: common share that confers exactly 0 votes per share, is unrestricted from a sales perspective, is nil paid and
      is registered
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/ESNUOR
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/CommonShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/CommonShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/NilPaidShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NilPaidShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/NonVotingShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/NonVotingShare
  - concept: /concepts/fibo/SEC/Equities/EquityInstruments/UnrestrictedShare.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/UnrestrictedShare
  - concept: /concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/CommonNonVotingUnrestrictedNilPaidRegisteredShare
sources:
- id: fibo-source-e698ab6eab
  resource: references/fibo/SEC/Equities/EquityCFIClassificationIndividuals.rdf
  sha256: e698ab6eabe9528750ce3dbc76f03090e26eac1f69c2fa7f62cb5d52ba93d10e
  title: FIBO source SEC/Equities/EquityCFIClassificationIndividuals.rdf
title: common, non-voting, unrestricted, nil paid, registered share
type: Ontology Class
---

# common, non-voting, unrestricted, nil paid, registered share

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/CommonNonVotingUnrestrictedNilPaidRegisteredShare>

## Definition

common share that confers exactly 0 votes per share, is unrestricted from a sales perspective, is nil paid and is registered

## Relationships

- **Subclass of**: [CommonShare](/concepts/fibo/SEC/Equities/EquityInstruments/CommonShare.md)
- **Subclass of**: [NilPaidShare](/concepts/fibo/SEC/Equities/EquityInstruments/NilPaidShare.md)
- **Subclass of**: [NonVotingShare](/concepts/fibo/SEC/Equities/EquityInstruments/NonVotingShare.md)
- **Subclass of**: [UnrestrictedShare](/concepts/fibo/SEC/Equities/EquityInstruments/UnrestrictedShare.md)
- **Subclass of**: [RegisteredSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/RegisteredSecurity.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityCFIClassificationIndividuals/ESNUOR`

## Annotations

- **label** (en-US): common, non-voting, unrestricted, nil paid, registered share
- **definition**: common share that confers exactly 0 votes per share, is unrestricted from a sales perspective, is nil paid and is registered

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: registered security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security that is registered with some registration authority
  disjoint_with:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/ExemptSecurity.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/ExemptSecurity
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
    value: Na8663081327d430f9e3385005ccf3c6b
  - filler: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isRegisteredWith
  - filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity
sources:
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
title: registered security
type: Ontology Class
---

# registered security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/RegisteredSecurity>

## Definition

security that is registered with some registration authority

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Constraints

- **Disjoint with**: [ExemptSecurity](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/ExemptSecurity.md)
- **[isIssuedInForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isIssuedInForm.md)**: some values from value `Na8663081327d430f9e3385005ccf3c6b`
- **[isRegisteredWith](/concepts/fibo/SEC/Securities/SecuritiesIssuance/isRegisteredWith.md)**: some values from of type [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)
- **[hasRegistrationDate](<https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate>)**: some values from of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)

## Annotations

- **label**: registered security
- **definition**: security that is registered with some registration authority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

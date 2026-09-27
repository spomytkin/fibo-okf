---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is registered
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the registration authority for a given security, i.e., in the name of the owner on the books of the issuer,
      with the issuer's registrar, with a third-party transfer agent, with a broker-dealer, or other competent party
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isRegisteredWith
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: is registered
type: Ontology Property
---

# is registered

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isRegisteredWith>

## Definition

indicates the registration authority for a given security, i.e., in the name of the owner on the books of the issuer, with the issuer's registrar, with a third-party transfer agent, with a broker-dealer, or other competent party

## Relationships

- **Domain**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **Range**: [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)
- **Subproperty of**: [isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)

## Annotations

- **label**: is registered
- **definition**: indicates the registration authority for a given security, i.e., in the name of the owner on the books of the issuer, with the issuer's registrar, with a third-party transfer agent, with a broker-dealer, or other competent party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

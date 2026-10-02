---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: trust fund manager
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party empowered to act on behalf of the trustee to manage the assets of the trust
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N880ac3b5682e4b8db98d8c3e611a4168
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustFundManager
sources:
- id: fibo-source-2a4049b46d
  resource: references/fibo/BE/Trusts/Trusts.rdf
  sha256: 2a4049b46d7d8daeb24877203142458caefea7a26ad56d16d6dd69523f6a04f1
  title: FIBO source BE/Trusts/Trusts.rdf
title: trust fund manager
type: Ontology Class
---

# trust fund manager

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/TrustFundManager>

## Definition

party empowered to act on behalf of the trustee to manage the assets of the trust

## Relationships

- **Subclass of**: [LegallyDelegatedAuthority](<https://www.omg.org/spec/Commons/BusinessAuthorizations/LegallyDelegatedAuthority>)

## Constraints

- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N880ac3b5682e4b8db98d8c3e611a4168`

## Annotations

- **label**: trust fund manager
- **definition**: party empowered to act on behalf of the trustee to manage the assets of the trust

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

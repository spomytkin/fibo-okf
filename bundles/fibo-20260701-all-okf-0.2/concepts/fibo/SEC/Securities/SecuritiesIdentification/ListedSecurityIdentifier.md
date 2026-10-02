---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: listed security identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security identifier issued in the public domain and referred to in listings and other relevant publications
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/ListedSecurity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/Exchange
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: listed security identifier
type: Ontology Class
---

# listed security identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier>

## Definition

security identifier issued in the public domain and referred to in listings and other relevant publications

## Relationships

- **Subclass of**: [SecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [SecurityIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentificationScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [ListedSecurity](/concepts/fibo/SEC/Securities/SecuritiesListings/ListedSecurity.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from of type [Exchange](/concepts/fibo/FBC/FunctionalEntities/Markets/Exchange.md)
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: some values from of type [SecurityRegistry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistry.md)

## Annotations

- **label**: listed security identifier
- **definition**: security identifier issued in the public domain and referred to in listings and other relevant publications

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

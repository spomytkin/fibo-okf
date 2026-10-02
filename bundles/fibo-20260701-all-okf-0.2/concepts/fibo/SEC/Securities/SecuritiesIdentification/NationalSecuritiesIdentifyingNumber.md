---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: National Securities Identifying Number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: generic, nine-digit alpha numeric code which identifies a fungible security, assigned by a national numbering agency
      under the ISO 6166 standard
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: NSIN
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: National Securities Identifying Number
type: Ontology Class
---

# National Securities Identifying Number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber>

## Definition

generic, nine-digit alpha numeric code which identifies a fungible security, assigned by a national numbering agency under the ISO 6166 standard

## Relationships

- **Subclass of**: [SecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [NationalSecurityIdentificationScheme](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecurityIdentificationScheme.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: some values from of type [NationalNumberingAgency](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency.md)

## Annotations

- **label**: National Securities Identifying Number
- **definition**: generic, nine-digit alpha numeric code which identifies a fungible security, assigned by a national numbering agency under the ISO 6166 standard
- **abbreviation**: NSIN

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

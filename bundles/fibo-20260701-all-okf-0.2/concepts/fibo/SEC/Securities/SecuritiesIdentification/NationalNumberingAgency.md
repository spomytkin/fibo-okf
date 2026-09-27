---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: national numbering agency
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registration authority responsible for issuing and managing National Securities Identifying Numbers for securities
      in accordance with the ISO 6166 standard in some jurisdiction (typically that of a country)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: NNA
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  - filler: https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Locations/hasCoverageArea
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/registers
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: national numbering agency
type: Ontology Class
---

# national numbering agency

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalNumberingAgency>

## Definition

registration authority responsible for issuing and managing National Securities Identifying Numbers for securities in accordance with the ISO 6166 standard in some jurisdiction (typically that of a country)

## Relationships

- **Subclass of**: [RegistrationAuthority](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistrationAuthority>)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from of type [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- **[hasCoverageArea](<https://www.omg.org/spec/Commons/Locations/hasCoverageArea>)**: some values from of type [GeopoliticalEntity](<https://www.omg.org/spec/Commons/Locations/GeopoliticalEntity>)
- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [NationalSecuritiesIdentifyingNumberRegistry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumberRegistry.md)
- **[registers](<https://www.omg.org/spec/Commons/RegistrationAuthorities/registers>)**: some values from of type [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)

## Annotations

- **label**: national numbering agency
- **definition**: registration authority responsible for issuing and managing National Securities Identifying Numbers for securities in accordance with the ISO 6166 standard in some jurisdiction (typically that of a country)
- **abbreviation**: NNA

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

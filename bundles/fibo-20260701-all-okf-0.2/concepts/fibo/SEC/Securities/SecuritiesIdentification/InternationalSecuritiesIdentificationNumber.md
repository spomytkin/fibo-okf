---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: international securities identification number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security identifier that is defined as specified in ISO 6166, Securities and related financial instruments -- International
      securities identification numbering system (ISIN)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: ISIN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: ISINs consist of two alphabetic characters, which are the ISO 3166-1 alpha-2 code for the issuing country, nine
      alpha-numeric characters (the National Securities Identifying Number, or NSIN, which identifies the security, padded
      as necessary with leading zeros), and one numerical check digit. The ISIN is specified as a class of identifiers because
      although there is a scheme associated with the structure of an ISIN, there are many country-specific variations issued
      by national numbering agencies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://www.omg.org/spec/LCC/Countries/CountryRepresentation/Alpha2Code
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.iso.org/iso/catalogue_detail?csnumber=44811
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumber
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
title: international securities identification number
type: Ontology Class
---

# international securities identification number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/InternationalSecuritiesIdentificationNumber>

## Definition

security identifier that is defined as specified in ISO 6166, Securities and related financial instruments -- International securities identification numbering system (ISIN)

## Relationships

- **See also**: [catalogue_detail](<http://www.iso.org/iso/catalogue_detail?csnumber=44811>)
- **Subclass of**: [SecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityIdentifier.md)
- **Subclass of**: [StructuredIdentifier](<https://www.omg.org/spec/Commons/ContextualIdentifiers/StructuredIdentifier>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [Alpha2Code](<https://www.omg.org/spec/LCC/Countries/CountryRepresentation/Alpha2Code>)

## Annotations

- **label**: international securities identification number
- **definition**: security identifier that is defined as specified in ISO 6166, Securities and related financial instruments -- International securities identification numbering system (ISIN)
- **abbreviation**: ISIN
- **explanatoryNote**: ISINs consist of two alphabetic characters, which are the ISO 3166-1 alpha-2 code for the issuing country, nine alpha-numeric characters (the National Securities Identifying Number, or NSIN, which identifies the security, padded as necessary with leading zeros), and one numerical check digit. The ISIN is specified as a class of identifiers because although there is a scheme associated with the structure of an ISIN, there are many country-specific variations issued by national numbering agencies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

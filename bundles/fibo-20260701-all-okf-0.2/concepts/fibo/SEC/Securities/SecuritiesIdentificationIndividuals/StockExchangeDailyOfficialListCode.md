---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Stock Exchange Daily Official List (SEDOL) code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: seven-character security identifier, issued by the London Stock Exchange, that is the National Securities Identifying
      Number (NSIN) for securities issued in the United Kingdom, which is also part of the ISIN for the security it identifies
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SEDOL code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListScheme
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.isin.net/sedol/
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListCode
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Stock Exchange Daily Official List (SEDOL) code
type: Ontology Class
---

# Stock Exchange Daily Official List (SEDOL) code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListCode>

## Definition

seven-character security identifier, issued by the London Stock Exchange, that is the National Securities Identifying Number (NSIN) for securities issued in the United Kingdom, which is also part of the ISIN for the security it identifies

## Relationships

- **See also**: [sedol](<https://www.isin.net/sedol/>)
- **Subclass of**: [ListedSecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md)
- **Subclass of**: [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- **Subclass of**: [ProprietarySecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/StockExchangeDailyOfficialListScheme`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/LondonStockExchange`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/SEDOLMasterFile`

## Annotations

- **label**: Stock Exchange Daily Official List (SEDOL) code
- **definition**: seven-character security identifier, issued by the London Stock Exchange, that is the National Securities Identifying Number (NSIN) for securities issued in the United Kingdom, which is also part of the ISIN for the security it identifies
- **abbreviation**: SEDOL code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Committee on Uniform Securities Identification Procedures (CUSIP) number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: nine-character alphanumeric number that identifies all North American stocks and registered bonds for the purposes
      of facilitating clearing and settlement of trades, issued by CUSIP Global Services on behalf of the American Bankers'
      Association, which is a part of Standard and Poor's Capital IQ, that is the National Numbering Agency Identifier for
      securities issued in North America, which is also part of the ISIN for the security it identifies
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CUSIP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: CUSIP number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresScheme
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.cusip.com/cusip/about-cgs-identifiers.htm
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresNumber
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Committee on Uniform Securities Identification Procedures (CUSIP) number
type: Ontology Class
---

# Committee on Uniform Securities Identification Procedures (CUSIP) number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresNumber>

## Definition

nine-character alphanumeric number that identifies all North American stocks and registered bonds for the purposes of facilitating clearing and settlement of trades, issued by CUSIP Global Services on behalf of the American Bankers' Association, which is a part of Standard and Poor's Capital IQ, that is the National Numbering Agency Identifier for securities issued in North America, which is also part of the ISIN for the security it identifies

## Relationships

- **See also**: [about-cgs-identifiers.htm](<https://www.cusip.com/cusip/about-cgs-identifiers.htm>)
- **Subclass of**: [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- **Subclass of**: [ProprietarySecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommitteeOnUniformSecuritiesIdentificationProceduresScheme`
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CUSIPGlobalServices`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CGSCUSIPAccessRepository`

## Annotations

- **label**: Committee on Uniform Securities Identification Procedures (CUSIP) number
- **definition**: nine-character alphanumeric number that identifies all North American stocks and registered bonds for the purposes of facilitating clearing and settlement of trades, issued by CUSIP Global Services on behalf of the American Bankers' Association, which is a part of Standard and Poor's Capital IQ, that is the National Numbering Agency Identifier for securities issued in North America, which is also part of the ISIN for the security it identifies
- **abbreviation**: CUSIP
- **synonym**: CUSIP number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

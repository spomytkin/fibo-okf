---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Valoren
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identification number assigned to financial instruments in Switzerland, Liechtenstein and Belgium, issued by SIX
      Financial Information, that is the National Securities Identifying Number (NSIN) for securities issued in those countries
      and is also part of the ISIN for the security it identifies
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.isin.net/valoren/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A VALOR code is between six and nine characters in length and like other securities identification codes (like
      ISIN, CUSIPs etc). A VALOR is utilized for identification purposes as well as clearing and settlement, similar to an
      ISIN code, and identifies debt and equity securities.
  - language: de
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Valor
  - language: de
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Valor Nummer
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Valor
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Valor Code
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Valoren Code
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Valoren Number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/ValorenScheme
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.six-group.com/en/products-services/financial-information.html
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
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/Valoren
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Valoren
type: Ontology Class
---

# Valoren

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/Valoren>

## Definition

identification number assigned to financial instruments in Switzerland, Liechtenstein and Belgium, issued by SIX Financial Information, that is the National Securities Identifying Number (NSIN) for securities issued in those countries and is also part of the ISIN for the security it identifies

## Relationships

- **See also**: [financial-information.html](<https://www.six-group.com/en/products-services/financial-information.html>)
- **Subclass of**: [ListedSecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ListedSecurityIdentifier.md)
- **Subclass of**: [NationalSecuritiesIdentifyingNumber](/concepts/fibo/SEC/Securities/SecuritiesIdentification/NationalSecuritiesIdentifyingNumber.md)
- **Subclass of**: [ProprietarySecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/ValorenScheme`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation`

## Annotations

- **label**: Valoren
- **definition**: identification number assigned to financial instruments in Switzerland, Liechtenstein and Belgium, issued by SIX Financial Information, that is the National Securities Identifying Number (NSIN) for securities issued in those countries and is also part of the ISIN for the security it identifies
- **adaptedFrom**: https://www.isin.net/valoren/
- **explanatoryNote**: A VALOR code is between six and nine characters in length and like other securities identification codes (like ISIN, CUSIPs etc). A VALOR is utilized for identification purposes as well as clearing and settlement, similar to an ISIN code, and identifies debt and equity securities.
- **synonym** (de): Valor
- **synonym** (de): Valor Nummer
- **synonym** (en): Valor
- **synonym** (en): Valor Code
- **synonym** (en): Valoren Code
- **synonym** (en): Valoren Number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Euroclear Clearstream common code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: nine-character alphanumeric securities identifier, issued in Luxembourg, jointly by Euroclear and Clearstream
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.isin.net/common-code-isin/
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: common code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: Nbce2d030e87b4bf2947b9c48b44bdda7
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCodeScheme
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  - kind: all_values_from
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: N9f319bf6f69d407090369d284ee76a27
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCode
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Euroclear Clearstream common code
type: Ontology Class
---

# Euroclear Clearstream common code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCode>

## Definition

nine-character alphanumeric securities identifier, issued in Luxembourg, jointly by Euroclear and Clearstream

## Relationships

- **Subclass of**: [ProprietarySecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)
- **Subclass of**: [RegisteredIdentifier](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegisteredIdentifier>)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: all values from value `Nbce2d030e87b4bf2947b9c48b44bdda7`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/EuroclearClearstreamCommonCodeScheme`
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: all values from value `N9f319bf6f69d407090369d284ee76a27`
- **[isRegisteredIn](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/CommonCodeRepository`

## Annotations

- **label**: Euroclear Clearstream common code
- **definition**: nine-character alphanumeric securities identifier, issued in Luxembourg, jointly by Euroclear and Clearstream
- **adaptedFrom**: http://www.isin.net/common-code-isin/
- **synonym**: common code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

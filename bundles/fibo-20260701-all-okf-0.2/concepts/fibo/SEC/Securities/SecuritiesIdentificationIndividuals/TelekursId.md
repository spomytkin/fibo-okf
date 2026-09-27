---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Telekurs Id
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier used to identify financial instruments owned, managed, and distributed by SIX Financial Information
      (formerly Telekurs AG and subsequently SIX Telekurs Ltd.)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Telekurs Id was phased out in favor of the Valoren (Valor Nummer in Swiss German) in 2013.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursSecurityIdentifierScheme
  - kind: has_value
    property: https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursId
sources:
- id: fibo-source-be76358ba2
  resource: references/fibo/SEC/Securities/SecuritiesIdentificationIndividuals.rdf
  sha256: be76358ba2a858eedd6bae77ca133882b7a1e2862cc351839d6b047eb2b024fa
  title: FIBO source SEC/Securities/SecuritiesIdentificationIndividuals.rdf
title: Telekurs Id
type: Ontology Class
---

# Telekurs Id

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursId>

## Definition

identifier used to identify financial instruments owned, managed, and distributed by SIX Financial Information (formerly Telekurs AG and subsequently SIX Telekurs Ltd.)

## Relationships

- **Subclass of**: [ProprietarySecurityIdentifier](/concepts/fibo/SEC/Securities/SecuritiesIdentification/ProprietarySecurityIdentifier.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation`
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentificationIndividuals/TelekursSecurityIdentifierScheme`
- **[isRegisteredBy](<https://www.omg.org/spec/Commons/RegistrationAuthorities/isRegisteredBy>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/CommercialRegistrationAuthorities/SIXFinancialInformation`

## Annotations

- **label**: Telekurs Id
- **definition**: identifier used to identify financial instruments owned, managed, and distributed by SIX Financial Information (formerly Telekurs AG and subsequently SIX Telekurs Ltd.)
- **explanatoryNote**: The Telekurs Id was phased out in favor of the Valoren (Valor Nummer in Swiss German) in 2013.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

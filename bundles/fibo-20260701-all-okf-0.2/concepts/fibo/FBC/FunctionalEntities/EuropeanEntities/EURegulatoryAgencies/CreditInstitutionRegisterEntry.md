---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Credit Institution Register entry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: entry in the Credit Institution Register, a repository of credit institutions collected by the European Banking
      Authority (EBA) as provided by the various national banking authorities for those institutions that qualify
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.eba.europa.eu/risk-analysis-and-data/credit-institutions-register
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isIncludedIn
    value: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegister
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegisterEntry
sources:
- id: fibo-source-ae4bf1d843
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
  sha256: ae4bf1d8430cf5c1d1d6e3b5004b20bc4d4e330a4cc094c02e2880e7bd06fd6f
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
title: Credit Institution Register entry
type: Ontology Class
---

# Credit Institution Register entry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegisterEntry>

## Definition

entry in the Credit Institution Register, a repository of credit institutions collected by the European Banking Authority (EBA) as provided by the various national banking authorities for those institutions that qualify

## Relationships

- **Subclass of**: [RegistryEntry](<https://www.omg.org/spec/Commons/RegistrationAuthorities/RegistryEntry>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [CreditInstitution](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md)
- **[isIncludedIn](<https://www.omg.org/spec/Commons/Collections/isIncludedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/CreditInstitutionRegister`
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: all values from of type [CreditInstitution](/concepts/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/CreditInstitution.md)

## Annotations

- **label**: Credit Institution Register entry
- **definition**: entry in the Credit Institution Register, a repository of credit institutions collected by the European Banking Authority (EBA) as provided by the various national banking authorities for those institutions that qualify
- **adaptedFrom**: http://www.eba.europa.eu/risk-analysis-and-data/credit-institutions-register

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

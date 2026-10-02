---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European Central Bank headquarters and legal address
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: headquarters and legal address for the European Central Bank
  - language: de
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddressLine1
    value: Sonnemannstrasse 20
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasPostalCode
    value: '60314'
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/ConventionalStreetAddress
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md
    predicate: https://www.omg.org/spec/Commons/Locations/hasMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt
  - predicate: https://www.omg.org/spec/Commons/Locations/hasCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanCentralBankHeadquartersAndLegalAddress
sources:
- id: fibo-source-ae4bf1d843
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
  sha256: ae4bf1d8430cf5c1d1d6e3b5004b20bc4d4e330a4cc094c02e2880e7bd06fd6f
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies.rdf
title: European Central Bank headquarters and legal address
type: Ontology Individual
---

# European Central Bank headquarters and legal address

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EURegulatoryAgencies/EuropeanCentralBankHeadquartersAndLegalAddress>

## Definition

headquarters and legal address for the European Central Bank

## Relationships

- **Related to**: [Germany](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Germany>)
- **Related to**: [Frankfurt](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Frankfurt.md)

## Annotations

- **label**: European Central Bank headquarters and legal address
- **definition**: headquarters and legal address for the European Central Bank
- **hasAddressLine1** (de): Sonnemannstrasse 20
- **hasPostalCode**: 60314

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

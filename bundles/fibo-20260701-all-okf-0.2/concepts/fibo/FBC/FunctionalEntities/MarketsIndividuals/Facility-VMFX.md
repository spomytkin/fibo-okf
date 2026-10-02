---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: THE FAROESE SECURITIES MARKET
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: THE FAROESE SECURITIES MARKET (VMF) IS THE STOCK EXCHANGE OF THE FAROE ISLANDS.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: THE FAROESE SECURITIES MARKET
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.vmf.fo
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Torshavn.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Torshavn
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-THEFAROESESECURITIESMARKET.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-THEFAROESESECURITIESMARKET
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/FaroeIslands
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-VMFX
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: THE FAROESE SECURITIES MARKET
type: Ontology Individual
---

# THE FAROESE SECURITIES MARKET

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-VMFX>

## Relationships

- **Related to**: [FaroeIslands](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/FaroeIslands>)
- **Related to**: [Torshavn](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Torshavn.md)
- **Related to**: [ServiceProvider-THEFAROESESECURITIESMARKET](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-THEFAROESESECURITIESMARKET.md)

## Annotations

- **label**: THE FAROESE SECURITIES MARKET
- **note**: THE FAROESE SECURITIES MARKET (VMF) IS THE STOCK EXCHANGE OF THE FAROE ISLANDS.
- **hasFormalName**: THE FAROESE SECURITIES MARKET
- **hasWebsite**: http://www.vmf.fo

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

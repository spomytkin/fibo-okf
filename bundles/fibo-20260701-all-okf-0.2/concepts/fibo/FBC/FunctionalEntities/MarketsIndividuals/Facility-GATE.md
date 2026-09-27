---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: GATE
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: GATE
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.gate.com/en-eu
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://www.omg.org/spec/Commons/SitesAndFacilities/Facility
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/L-imsida.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/L-imsida
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-984500D6A0F945BB5A15.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-984500D6A0F945BB5A15
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Malta
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GATE
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: GATE
type: Ontology Individual
---

# GATE

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-GATE>

## Relationships

- **Related to**: [Malta](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Malta>)
- **Related to**: [L-imsida](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/L-imsida.md)
- **Related to**: [ServiceProvider-L-984500D6A0F945BB5A15](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-984500D6A0F945BB5A15.md)

## Annotations

- **label**: GATE
- **hasFormalName**: GATE
- **hasWebsite**: http://www.gate.com/en-eu

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: VP BANK AG
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: SYSTEMATIC INTERNALISER. REGISTERED MARKET FOR FX OTC DERIVATIVES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: VP BANK AG
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.vpbank.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/SystematicInternaliser
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Vaduz.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Vaduz
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-MI3TLH1I0D58ORE24Q14.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-MI3TLH1I0D58ORE24Q14
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Liechtenstein
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XVPB
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: VP BANK AG
type: Ontology Individual
---

# VP BANK AG

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XVPB>

## Relationships

- **Related to**: [Liechtenstein](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Liechtenstein>)
- **Related to**: [Vaduz](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Vaduz.md)
- **Related to**: [ServiceProvider-L-MI3TLH1I0D58ORE24Q14](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-MI3TLH1I0D58ORE24Q14.md)

## Annotations

- **label**: VP BANK AG
- **note**: SYSTEMATIC INTERNALISER. REGISTERED MARKET FOR FX OTC DERIVATIVES.
- **hasFormalName**: VP BANK AG
- **hasWebsite**: http://www.vpbank.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

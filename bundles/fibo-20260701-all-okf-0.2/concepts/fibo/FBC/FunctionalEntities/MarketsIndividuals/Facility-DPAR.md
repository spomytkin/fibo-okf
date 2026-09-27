---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: EURONEXT PARIS - DARK BOOK FACILITY
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: MIC TO IDENTIFY DARK MIDPOINT PEGGED TRANSACTIONS. NOT TO BE USED FOR REGULATORY REPORTING PURPOSES.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: EURONEXT PARIS - DARK BOOK FACILITY
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.euronext.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/DarkPool
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPAR.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPAR
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-969500HMVSZ0TCV65D58.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-969500HMVSZ0TCV65D58
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/France
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DPAR
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: EURONEXT PARIS - DARK BOOK FACILITY
type: Ontology Individual
---

# EURONEXT PARIS - DARK BOOK FACILITY

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DPAR>

## Relationships

- **Related to**: [France](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/France>)
- **Related to**: [Paris](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Paris.md)
- **Related to**: [Facility-XPAR](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-XPAR.md)
- **Related to**: [ServiceProvider-L-969500HMVSZ0TCV65D58](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-969500HMVSZ0TCV65D58.md)

## Annotations

- **label**: EURONEXT PARIS - DARK BOOK FACILITY
- **note**: MIC TO IDENTIFY DARK MIDPOINT PEGGED TRANSACTIONS. NOT TO BE USED FOR REGULATORY REPORTING PURPOSES.
- **hasFormalName**: EURONEXT PARIS - DARK BOOK FACILITY
- **hasWebsite**: http://www.euronext.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

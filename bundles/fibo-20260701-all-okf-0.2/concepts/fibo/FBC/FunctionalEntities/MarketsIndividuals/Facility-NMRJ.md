---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: NOMURA SECURITIES CO LTD
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: NOMURA JAPAN EQUITY TRADING.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: NSC
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: NOMURA SECURITIES CO LTD
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: http://www.nomura.com
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OperatingLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-XPSKD1VTEQPKCHBEKQ95.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-XPSKD1VTEQPKCHBEKQ95
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NMRJ
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: NOMURA SECURITIES CO LTD
type: Ontology Individual
---

# NOMURA SECURITIES CO LTD

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-NMRJ>

## Relationships

- **Related to**: [Japan](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/Japan>)
- **Related to**: [Tokyo](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/Tokyo.md)
- **Related to**: [ServiceProvider-L-XPSKD1VTEQPKCHBEKQ95](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-L-XPSKD1VTEQPKCHBEKQ95.md)

## Annotations

- **label**: NOMURA SECURITIES CO LTD
- **note**: NOMURA JAPAN EQUITY TRADING.
- **hasFacilityAcronym**: NSC
- **hasFormalName**: NOMURA SECURITIES CO LTD
- **hasWebsite**: http://www.nomura.com

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: DEUTSCHE BANK - CENTRAL RISK BOOK
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: DEUTSCHE BANK AG MARKET SEGMENT MARKET CODE FOR THE CENTRAL RISK BOOK AS PER MMT2 STANDARD DEFINITION PROPOSED
      BY FIXPROTOCOL.ORG AND SUPPORTED BY EUROPEAN TDM'S(HTTP://WWW.BATSTRADING.CO.UK/BXTR/)
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/hasFacilityAcronym
    value: CENTRAL RISK BOOK
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/hasFormalName
    value: DEUTSCHE BANK - CENTRAL RISK BOOK
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/Organizations/hasWebsite
    value: https://autobahn.db.com/microsite/html/equity.html
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketSegmentLevelMarket
  related_to:
  - concept: /concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInMunicipality
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessCentersIndividuals/London
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBIX.md
    predicate: https://www.omg.org/spec/Commons/Collections/isPartOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBIX
  - concept: /concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DEUTSCHEBANK-CENTRALRISKBOOK.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DEUTSCHEBANK-CENTRALRISKBOOK
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/operatesInCountry
    resource: https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBCR
sources:
- id: fibo-source-09daeb6fa0
  resource: references/fibo/FBC/FunctionalEntities/MarketsIndividuals.rdf
  sha256: 09daeb6fa0d1d7053970baed4bb58f7b0ef2d718a1cc5c800e2db6a88e94fb00
  title: FIBO source FBC/FunctionalEntities/MarketsIndividuals.rdf
title: DEUTSCHE BANK - CENTRAL RISK BOOK
type: Ontology Individual
---

# DEUTSCHE BANK - CENTRAL RISK BOOK

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBCR>

## Relationships

- **Related to**: [UnitedKingdomOfGreatBritainAndNorthernIreland](<https://www.omg.org/spec/LCC/Countries/ISO3166-1-CountryCodes/UnitedKingdomOfGreatBritainAndNorthernIreland>)
- **Related to**: [London](/concepts/fibo/FBC/FunctionalEntities/BusinessCentersIndividuals/London.md)
- **Related to**: [Facility-DBIX](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/Facility-DBIX.md)
- **Related to**: [ServiceProvider-DEUTSCHEBANK-CENTRALRISKBOOK](/concepts/fibo/FBC/FunctionalEntities/MarketsIndividuals/ServiceProvider-DEUTSCHEBANK-CENTRALRISKBOOK.md)

## Annotations

- **label**: DEUTSCHE BANK - CENTRAL RISK BOOK
- **note**: DEUTSCHE BANK AG MARKET SEGMENT MARKET CODE FOR THE CENTRAL RISK BOOK AS PER MMT2 STANDARD DEFINITION PROPOSED BY FIXPROTOCOL.ORG AND SUPPORTED BY EUROPEAN TDM'S(HTTP://WWW.BATSTRADING.CO.UK/BXTR/)
- **hasFacilityAcronym**: CENTRAL RISK BOOK
- **hasFormalName**: DEUTSCHE BANK - CENTRAL RISK BOOK
- **hasWebsite**: https://autobahn.db.com/microsite/html/equity.html

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
